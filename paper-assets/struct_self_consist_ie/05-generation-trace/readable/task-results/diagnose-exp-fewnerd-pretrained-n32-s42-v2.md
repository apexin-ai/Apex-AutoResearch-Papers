# diagnose exp fewnerd pretrained n32 s42 v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_fewnerd_pretrained_n32_s42_v2_20260523T113901_result.json`
- **Structured JSON:** [`e77b66e39f14e39fedfb.json`](../../sessions/e7/e77b66e39f14e39fedfb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告已保存到 `artifacts/diagnose_exp_fewnerd_pretrained_n32_s42_v2.md`。

**核心结论：实验没有失败，是 cron 监控误判。**

实验于 00:15 启动，19:28 完成，耗时约 19 小时，37648/37648 实例全部处理完毕。三个输出文件（samples.jsonl 7.2GB、report.json、n32_analysis.json）均完整生成，verdict = **PASS**。

误判原因：cron 检查 sentinel 文件和 W&B 记录，但该实验两者均未配置，导致 5 次检查都认为进程"无产出"。

关键指标：MV 比 greedy 提升 +3.85pp（F1 0.5390→0.5775），结构化一致性信号(SJ)优于表面信号(FK)，ρ 优势 +0.0515。

需注意：磁盘已用 96%（剩 13GB），后续实验前应清理。

---
