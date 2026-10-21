# ssh diagnose exp b1 scd conll control

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose-exp_b1_scd_conll_control_20260520T121546_result.json`
- **Structured JSON:** [`379b1d19457af5597599.json`](../../sessions/37/379b1d19457af5597599.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论：假阳性告警，实验已正常完成。**

- `exp_b1_scd_conll_control` 在 ~23 分钟内完成了 2 epochs / 690 steps 训练，train_loss=0.0359, eval_loss=0.0362，checkpoints 和结果文件均已写入 `checkpoints/qwen3-8b-conll-scd-lora/`
- cron 误判原因：配置了 `report_to: none` 且无 sentinel 文件，进程正常退出后被识别为"死亡"
- 其他 3 个 SCD 实验（fewnerd_standard / fewnerd_curriculum_q / threshold_ablation）全部健康运行中，分别占用 GPU 0/1/3
- 服务器资源充足：磁盘剩余 148G，GPU 2 空闲

报告已写入 `artifacts/diagnose_exp_b1_scd_conll_control.md`。

---
