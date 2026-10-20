# code prepare random50 multiseed

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_random50_multiseed_20260513T160412_result.json`
- **Structured JSON:** [`ba06419c9c8b7517f75f.json`](../../sessions/ba/ba06419c9c8b7517f75f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法检查通过，Python import 正常。

与原脚本差异：去掉了 `TRANSFORMERS_OFFLINE=1`，seed 和 output_dir 分别改为 123/456 对应路径，其余超参数完全一致。

提交命令：

```
SEED123_CMD: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /root/div_cal_verify/env.sh && cd /root/div_cal_verify && bash run_random50_seed123.sh 0

SEED456_CMD: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /root/div_cal_verify/env.sh && cd /root/div_cal_verify && bash run_random50_seed456.sh 1
```

两个脚本 GPU 参数化（`$1`），默认 GPU 0。如果双卡并行，seed123 用 GPU 0，seed456 用 GPU 1。

---
