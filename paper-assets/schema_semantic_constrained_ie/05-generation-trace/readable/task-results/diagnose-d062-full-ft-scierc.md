# diagnose d062 full ft scierc

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_d062_full_ft_scierc_20260519T051152_result.json`
- **Structured JSON:** [`19f54345bc3ecab3fd9d.json`](../../sessions/19/19f54345bc3ecab3fd9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**d062_full_ft_scierc 实验全流程已成功完成，cron 是误报。**

关键事实：
- 训练 333/333 steps 完成，eval_loss=0.0946，token accuracy=97.61%
- 中间因磁盘空间不足导致首次 checkpoint 保存失败，但后续恢复保存成功（16.3GB model.safetensors）
- 推理完成 551/551 samples（unconstrained + constrained 两个模式）
- Constrained decoding 将 domain-range violation rate 从 2.74% 降至 0.0%
- Entity F1=0.6478，Relation F1=0.3789

Cron 误报原因：脚本禁用了 W&B (`WANDB_DISABLED=true`) 且无 sentinel 文件，监控系统无法探测到进程存活。建议后续脚本加入 sentinel 文件写入。

---
