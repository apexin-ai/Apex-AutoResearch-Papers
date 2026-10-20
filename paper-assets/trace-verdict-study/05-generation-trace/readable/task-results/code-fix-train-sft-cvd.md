# code fix train sft cvd

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_train_sft_cvd_20260515T130134_result.json`
- **Structured JSON:** [`224c4f91bd6f631295e9.json`](../../sessions/22/224c4f91bd6f631295e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两处均已修复：

- `train/train_sft.py` 第 89-90 行：`if "CUDA_VISIBLE_DEVICES" not in os.environ:` 守护
- `eval/evaluate.py` 第 126-127 行：同样的守护

现在外层设置的 CVD 不会被 `--gpu` 参数覆盖。

---
