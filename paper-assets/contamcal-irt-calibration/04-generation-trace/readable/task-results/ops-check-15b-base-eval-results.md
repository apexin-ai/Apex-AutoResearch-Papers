# ops check 15B base eval results

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-15B-base-eval-results_20260515T115602_result.json`
- **Structured JSON:** [`cb3b64383f2d884c42b9.json`](../../sessions/cb/cb3b64383f2d884c42b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

```
CONCLUSION: success
METRICS: mmlu=0.2303 (3234/14042), gsm8k=0.0053 (7/1319), arc_challenge=0.2304 (270/1172), humaneval=0.2317 (38/164)
GPU_4_STATUS: free (0%, 0 MiB / 24564 MiB)
```

MMLU/ARC 约 23% 接近 4 选 1 随机水平，GSM8K 接近零——base pretrained 模型不遵循指令格式，符合预期。这为 3-regime 对比（base → SFT → Instruct）提供了底线数据点。

---
