# code qwen epoch eval script

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen_epoch_eval_script_20260515T144628_result.json`
- **Structured JSON:** [`1da60e12f900e5b31369.json`](../../sessions/1d/1da60e12f900e5b31369.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并通过语法检查：`/root/trace-verdict-study/scripts/eval_qwen_epochs.sh`

运行方式：
```bash
bash scripts/eval_qwen_epochs.sh           # 默认 GPU 0
bash scripts/eval_qwen_epochs.sh --gpu 1   # 指定 GPU
```

6 个 checkpoint（3 conditions × 2 epochs）会依次 eval，每个结束后打印 accuracy/lift/n 摘要。

---
