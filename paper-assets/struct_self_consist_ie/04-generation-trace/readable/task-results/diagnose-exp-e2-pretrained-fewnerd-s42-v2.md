# diagnose exp e2 pretrained fewnerd s42 v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_e2_pretrained_fewnerd_s42_v2_20260521T232627_result.json`
- **Structured JSON:** [`142e378b2d34307585dc.json`](../../sessions/14/142e378b2d34307585dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验实际已成功完成，cron 误判为失败。**

日志显示完整执行流程：37648/37648 instances 全部处理完毕，生成了 report.json，verdict 为 **PASS**，vLLM engine 正常 shutdown。关键指标：Greedy F1=0.5116, Oracle F1=0.6169, Structural > Surface=YES。

失败标记是 cron 监控的误报——进程正常退出后 cron 检测到 "process dead" 但未找到预期的 sentinel/W&B 标记，累计 5 次检测后自动标记为 failed。

**结论：无需重跑。** 实验结果完整，且原始 3-seed set 也已全部成功。

---
