# analysis mvp2 eval rsft s43 r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp2_eval_rsft_s43_r2_20260515T132104_result.json`
- **Structured JSON:** [`33c2d8facd8a3791a43e.json`](../../sessions/33/33c2d8facd8a3791a43e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## RSFT s43 Full Dev Eval 结果

| 指标 | s43 | r1 (s42) | s44 | SFT baseline |
|------|-----|----------|-----|--------------|
| **rel_f1** | **0.4683** | 0.4449 | 0.4655 | 0.4057 |
| **evi_f1** | **0.8156** | 0.8187 | 0.8087 | 0.7979 |
| **EDCR** | **0.6388** | 0.6565 | — | 0.7118 |
| pred_count | 14970 | — | — | — |
| truncated | 171/985 | — | — | — |
| format_ok | 985/985 | — | — | — |

### 三 seed 汇总（方差估计）

| 指标 | mean | std | min | max |
|------|------|-----|-----|-----|
| rel_f1 | **0.4596** | 0.0129 | 0.4449 | 0.4683 |
| evi_f1 | **0.8143** | 0.0051 | 0.8087 | 0.8187 |

s43 是三个 seed 中 rel_f1 最高的（0.4683），比 r1 高 +2.3pp。evi_f1 居中。EDCR 0.6388 是三个 seed 中最低的（r1=0.6565），说明 s43 的 distractor citation 比例更低。

### 路径
- Checkpoint: `/root/autodl-tmp/rsft_output_s43`
- Eval 输出: `/root/autodl-tmp/eval_results/rsft_s43/`
- Metrics: `/root/autodl-tmp/eval_results/rsft_s43/metrics.json`

---
