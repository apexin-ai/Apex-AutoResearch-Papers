# infra fix batchsize16 script

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix_batchsize16_script_20260516T025116_result.json`
- **Structured JSON:** [`98a88021ac3caf1da56c.json`](../../sessions/98/98a88021ac3caf1da56c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。变更内容：

1. **添加 `--gradient_checkpointing`** — 在 `--gradient_accumulation_steps 1` 之后
2. **添加 `export WANDB_MODE=disabled`** — 统一标准

参数验证：
| 参数 | 值 | 状态 |
|------|-----|------|
| batch_size | 16 | ✓ |
| gradient_accumulation_steps | 1 | ✓ |
| gradient_checkpointing | 已添加 | ✓ |
| n_min | 2 | ✓ |
| seed | 42 | ✓ |
| weighting_method | adaptive | ✓ |
| data_path | scored_data.jsonl | ✓ |
| contamination_ratio | 0.4 | ✓ |
| tau | 0.8 | ✓ |
| WANDB_MODE | disabled | ✓ |

脚本路径：`/root/provenance_weight_training/scripts/run_batchsize16.sh`

---
