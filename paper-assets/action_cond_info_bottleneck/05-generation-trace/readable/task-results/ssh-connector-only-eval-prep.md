# ssh connector only eval prep

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_connector-only-eval-prep_20260517T171028_result.json`
- **Structured JSON:** [`035af15d33c354ba379c.json`](../../sessions/03/035af15d33c354ba379c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报：

## 1. 兼容性状态

| 模式 | eval_acib.py（修改前） | cross_task_probe.py（修改前） |
|------|----------------------|----------------------------|
| **connector_only** | 功能正确但低效（scorer 仍执行，alpha=0.0 使其无效） | N/A（probe 测试 scorer，connector_only 无 scorer 意义） |
| **connector_lora** | **broken** — LoRA 权重被 `strict=False` 静默丢弃 | **broken** — 同理 |

根因：两脚本构造 `ACIBConfig` 时未传 `freeze_mode`/`lora_rank`/`lora_scale`，默认 `"legacy"`，导致 `_apply_lora_to_connector` 永远不被调用。

## 2. 代码修改

- **`/root/acib/scripts/eval_acib.py`** (line 129-131): `ACIBConfig` 构造增加 `freeze_mode`, `lora_rank`, `lora_scale`（从 checkpoint config 读取）
- **`/root/acib/scripts/cross_task_probe.py`** (line 163-165): 同上

修改后：
- `connector_only`: hook 直接 `return output`（跳过 scorer），更高效
- `connector_lora`: `_setup_freeze` 正确调用 `_apply_lora_to_connector`，`load_state_dict` 可正确匹配 LoRA 权重

## 3. 创建的脚本

| 脚本 | 用途 |
|------|------|
| `run_connector_only_eval.sh` | connector_only ablation, alpha=0.0, 4 suites |
| `run_v73_eval_probe_a.sh` | cross-task probe for v7.3 connector_lora |
| `run_v73_eval_alpha00_spatial.sh` | v7.3 alpha=0.0 spatial-only sanity check |
| `run_v73_eval_alpha10.sh` | v7.3 alpha=1.0 full 4-suite eval |

## 4. 剩余注意事项

- `cross_task_probe.py` 对 `connector_only` 模式无实际意义（scorer 永远不被调用，hook 短路返回），不建议对 connector_only checkpoint 跑 probe
- `cross_task_probe.py` 的 `--checkpoint_dir` 期望的是 `checkpoint-STEP/` 子目录路径（非训练 output_dir），probe 脚本已按此格式配置

---
