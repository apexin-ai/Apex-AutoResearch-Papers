# code fix qlora lr

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-qlora-lr_20260513T101058_result.json`
- **Structured JSON:** [`349133136b76565f3320.json`](../../sessions/34/349133136b76565f3320.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改完成，无残留 5e-7：

| 文件 | 修改 |
|------|------|
| `src/train_dpo.py:472` | `default=5e-7` → `default=2e-5` |
| `configs/dpo_etadn.yaml:16` | `learning_rate: 5.0e-7` → `2.0e-5` |
| `configs/dpo_single_gamma.yaml:14` | `learning_rate: 5.0e-7` → `2.0e-5` |
| `scripts/run_training.sh` | 8 处 `python src/train_dpo.py` 调用均添加了 `--learning_rate 2e-5` |

---
