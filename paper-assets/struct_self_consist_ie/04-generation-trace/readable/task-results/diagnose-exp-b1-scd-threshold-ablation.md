# diagnose exp b1 scd threshold ablation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_b1_scd_threshold_ablation_20260520T200210_result.json`
- **Structured JSON:** [`db8679c955c211ee22bb.json`](../../sessions/db/db8679c955c211ee22bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结果：训练成功完成，是监控误判。**

根因：配置文件中 `report_to: none` 导致无 W&B 指标上报，加上无 sentinel file，Cron 监控将正常完成的训练误判为反复崩溃。

实际状态：
- 9412/9412 steps 全部完成，train_loss=0.0201，eval_loss=0.0306
- 日志中零错误/异常
- checkpoint-9412（final）和所有结果文件均完好
- LoRA adapter 可直接使用

报告已写入 `artifacts/diagnose_exp_b1_scd_threshold_ablation.md`。

---
