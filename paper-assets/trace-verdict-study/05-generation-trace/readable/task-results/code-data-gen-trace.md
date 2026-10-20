# code data gen trace

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_data-gen-trace_20260514T163506_result.json`
- **Structured JSON:** [`66138c5b2e8744a9acb3.json`](../../sessions/66/66138c5b2e8744a9acb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据生成完成。详细统计：

**HumanEval** (164题 × 10 samples = 1,640):
- Pass: 1,011 (62%), SyntaxError: 289, Other: 340, Timeout: 0
- 平均 trace: 135 行, 有 trace 的样本: 1,352

**MBPP** (427题 × 10 samples = 4,270):
- Pass: 2,947 (69%), SyntaxError: 0, Other: 1,311, Timeout: 12
- 平均 trace: 81 行, 有 trace 的样本: 4,258

**输出文件**: `/root/autodl-tmp/trace-verdict-study-data/raw_traces.jsonl` (139 MB, 5,910 行)
**Checkpoint**: `/root/autodl-tmp/trace-verdict-study-data/solutions_checkpoint.json`

---
