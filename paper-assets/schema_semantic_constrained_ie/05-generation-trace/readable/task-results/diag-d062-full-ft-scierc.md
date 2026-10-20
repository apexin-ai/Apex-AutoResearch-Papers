# diag d062 full ft scierc

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_d062_full_ft_scierc_20260519T045139_result.json`
- **Structured JSON:** [`273d107d37e25034e97e.json`](../../sessions/27/273d107d37e25034e97e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**一句话总结**: 训练成功完成 (3 epochs, eval accuracy 97.6%)，但 checkpoint 保存时 `/dev/md0` 数据盘 (250GB) 空间不足导致 safetensors 序列化失败 (`os error 28: No space left on device`)。

**当前状态**: checkpoint 已被手动恢复保存，constrained inference (full_s1) 正在 tmux 中运行 (176/551 samples)。**不需要重新训练或重试。**

**两个需要关注的点**:
1. 数据盘 250GB 已用 65% (models 83GB + checkpoints 77GB)，建议清理旧 checkpoints
2. `WANDB_DISABLED=true` 是脚本里显式设置的，所以 cron 监控看不到 W&B 指标是预期行为，不是异常

报告已写入 `artifacts/d062_full_ft_scierc/diagnosis.md`。

---
