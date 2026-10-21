# code 4way eval script

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_4way_eval_script_20260519T104053_result.json`
- **Structured JSON:** [`23d7e0c35cbdf1215966.json`](../../sessions/23/23d7e0c35cbdf1215966.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本创建完成。

**确认的 CLI 参数**：
- `--gate-type {threadgate,uniform,none}`（必选）
- `--checkpoint-dir`（可选，Base 不需要）
- `--conversations-path`
- `--output-dir`
- `--gar-variant {ours,dongre}`
- `--gate-profile`（flag）
- `--model`（默认从 config.py 的 `MODEL_NAME` 读取，无需显式指定）

**确认的 checkpoint 路径**：
| 条件 | 路径 | lora/ | gate_params.pt |
|------|------|-------|----------------|
| TG v7 | `runs/phase2_tg_s42_v7` | ✓ | ✓ |
| UG | `runs/phase2_ug_s42` | ✓ | ✓ |
| LoRA-only | `runs/phase2_lora_only_s42` | 训练中，仅 epoch_0/lora/ | 无（符合预期） |

**脚本**：`/root/turn_residual_gating/scripts/run_4way_eval.sh`，8 个 eval（4 条件 × 2 GAR variant），输出到 `runs/4way_eval/{base,tg_v7,ug,lora_only}_{ours,dongre}/`。

**语法验证**：`bash -n` 通过。

---
