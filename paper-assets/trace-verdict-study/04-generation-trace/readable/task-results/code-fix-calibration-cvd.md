# code fix calibration cvd

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_calibration_cvd_20260515T130642_result.json`
- **Structured JSON:** [`f9bbae0d417438a210c4.json`](../../sessions/f9/f9bbae0d417438a210c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有赋值行现在都缩进了一级（在 `if` guard 内部），无残留的无条件覆盖。

**calibration.py** — 278、345 两处已加 `if "CUDA_VISIBLE_DEVICES" not in os.environ:` guard。

**额外修复的 6 个文件**（同样的问题）：
| 文件 | 原行号 |
|---|---|
| `train/train_sft.py` | 90 |
| `eval/evaluate.py` | 127 |
| `eval/bootstrap_compare.py` | 335 |
| `eval/eval_label_only_bootstrap.py` | 10 |
| `eval/bootstrap_loop_only.py` | 61 |
| `eval/bootstrap_ae_only.py` | 79 |

当前正在跑的 calibration 进程不受影响，下次启动时新逻辑生效。

---
