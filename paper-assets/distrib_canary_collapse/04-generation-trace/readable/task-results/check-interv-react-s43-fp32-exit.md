# check interv react s43 fp32 exit

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_interv_react_s43_fp32_exit_20260519T180441_result.json`
- **Structured JSON:** [`962c6ab4c90d317304ee.json`](../../sessions/96/962c6ab4c90d317304ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论：interv_react_s43_fp32 实验成功完成。**

| 项目 | 值 |
|------|-----|
| EXIT_CODE | 0 |
| Generations | gen_0 – gen_10 全部完整 |
| 干预触发 | Gen 2（distinct_1: 0.0983 → 0.0827，跌幅 15.8%） |
| 干预效果 | perplexity 从 158.2 (Gen 2) 恢复到 ~21.4 (Gen 3+) |
| 干预持续 | Gen 3-10 全程 α=0.0（未自动恢复到 α=1.0） |
| 与 s42 一致性 | Gen 2 触发干预，与 s42 一致 |

Registry 已更新为 DONE/success，cron 监控已删除。

---
