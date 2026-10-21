# diagnose 26k ckpt format

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_26k_ckpt_format_20260527T050655_result.json`
- **Structured JSON:** [`19a16bd1b67d04b745d9.json`](../../sessions/19/19a16bd1b67d04b745d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 根因：26K eval 漏传 `--pi05` 参数

checkpoint 格式没有变化——24K 和 26K 的 key 结构 **完全相同**（1316 keys，zero diff，文件大小均为 7,540,115,784 bytes）。

问题出在 eval 调用方式：

| | 24K eval | 26K eval |
|---|---|---|
| `--pi05` | ✅ 传了 | ❌ 没传 |
| 模型架构 | Pi0.5（`time_mlp_in/out` + AdaLN `layernorm.dense.*`） | 标准 Pi0（`action_time_mlp_in/out` + `layernorm.weight`） |
| 结果 | keys 匹配，加载成功 | keys 不匹配，RuntimeError |

**证据**：24K 日志中有 `pi05_libero` 资源路径引用，26K 日志完全没有。

### 机制

`eval_safelibero.py` 的 `_load_policy_lora_baseline()` (line 764) 检查 `getattr(args, "pi05", False)`：
- `True` → `Pi0Config(pi05=True, ...)` → 模型含 `time_mlp_in/out` + AdaLN layernorm → 匹配 checkpoint
- `False` → `Pi0Config(paligemma_variant="gemma_2b", ...)` → 模型含 `action_time_mlp_in/out` + 标准 layernorm → 不匹配

### 30K eval 是否受影响

**不受影响，前提是 eval 命令加上 `--pi05`。** 30K checkpoint 来自同一个训练进程（PID 271266，仍在运行），key 结构不会变。

### 修复

26K 和 30K eval 命令都需要加 `--pi05`：

```bash
python scripts/eval_safelibero.py --model_type lora_baseline --pi05 \
    --checkpoint /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l1/26000 \
    ... (其他参数)
```

### 训练进度

当前 ~26947/30000（90%），预计 ~4h 后完成。

---
