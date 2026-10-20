# analysis appendix b precise gx

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_appendix_b_precise_gx_20260515T175728_result.json`
- **Structured JSON:** [`2074412b4af92cef9f01.json`](../../sessions/20/2074412b4af92cef9f01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**不需要重跑 profiling**——利用已有 n=500 per-problem additive II + aggregate PPL 修正项计算。

**Precise G_× (importance masking, n=500):**

| Model | s015 | s020 | s025 | s030 |
|-------|------|------|------|------|
| DeepSeek | 21.1× | 28.6× | 36.5× | 36.2× |
| Qwen | 43.9× | 53.4× | 62.2× | 64.0× |

**Combined range: 21–64×**（论文当前声称 58–241×，需更新）

关键文件：
- 计算脚本：`/root/autodl-tmp/pacs/compute_gx_final.py`
- 输出 JSON：`/root/autodl-tmp/pacs/analysis_output/appendix_b_precise_gx.json`
- 报告：`artifacts/appendix_b_precise_gx/report.md`

---
