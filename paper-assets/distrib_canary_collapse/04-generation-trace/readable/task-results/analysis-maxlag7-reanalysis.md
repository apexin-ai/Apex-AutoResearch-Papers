# analysis maxlag7 reanalysis

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_maxlag7-reanalysis_20260514T185905_result.json`
- **Structured JSON:** [`84f354ffe209991ebd59.json`](../../sessions/84/84f354ffe209991ebd59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**max_lag=7 重分析结论：无截断伪影。**

- 所有 20 个 canary→downstream pair 的 lag 值在 max_lag=5 和 max_lag=7 下**完全一致**
- **token_entropy→perplexity: lag=-5 是真实信号**，4/4 seed 一致（std=0），但 p-value borderline (0.058–0.12)，瓶颈是统计功效（仅 10 代数据），不是截断
- 6 个 SIGNIFICANT LEAD pair 的 lag 均为 -1 或 -2，远小于 max_lag，不受影响
- Verdict 不变：**STRONG PASS**

报告已保存至：
- 服务器：`results/mvp/analysis/ccf_maxlag7.json`
- 本地 artifacts：`ccf_maxlag7_report.md`
- memory.md 已更新（narrative 约束段落新增 max_lag=7 验证结论）

---
