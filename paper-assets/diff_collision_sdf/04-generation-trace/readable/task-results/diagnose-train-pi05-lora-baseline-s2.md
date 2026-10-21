# diagnose train pi05 lora baseline s2

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_train_pi05_lora_baseline_s2_20260527T024030_result.json`
- **Structured JSON:** [`f42b5ade2a059ed372f5.json`](../../sessions/f4/f42b5ade2a059ed372f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全了，汇总报告如下：

---

## 诊断报告：train_pi05_lora_baseline_s2

### 训练进度
- **停止步数**：22364 / 30000（74.5%）
- **最后 loss**：~0.0090–0.0165（正常范围，无异常）
- **最后 lr**：6.14e-06
- **grad_norm**：0.10（正常，无 OOM / 梯度爆炸迹象）

### Checkpoint 情况
路径：`/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed2/`

| Checkpoint | 说明 |
|-----------|------|
| `20000/` | 中间 checkpoint |
| `22000/` | 最后一个保存的 checkpoint |
| `best/` | best loss = 0.00963 @ step 18000 |

checkpoint 包含完整文件（model.safetensors, optimizer.pt, metadata.pt），**可用于恢复训练**。

### 失败根因
**纯粹是 timeout 不够，训练本身无任何异常。**

- Phase 1（前 5000 步，LoRA 冻结）：~1.2s/step → 约 1.7 小时
- Phase 2（5001-30000 步，LoRA 解冻）：~4.60s/step → 约 31.9 小时
- **30K 步总需约 33.6 小时**，24h timeout 只够跑到 ~22K 步

s0 和 s1 都成功完成了 30K 步（checkpoint 目录有 `30000/`），s0 的 30K checkpoint 时间戳 `2026-05-26 09:32`，说明它们也跑了类似时长，应该是通过 tmux 或更长 timeout 提交的（它们的日志几乎为空，只有 EXIT_CODE=0）。

三个 seed 的 Phase 2 训练速度一致（~4.60s/it），s2 没有变慢。

### 建议
**从 step 22000 checkpoint 恢复继续训练**，只需跑剩余 8000 步（约 10.2 小时）。必须用 tmux 启动（符合 C002 约束），不要再用 submit_training_job 的 24h timeout。

---
