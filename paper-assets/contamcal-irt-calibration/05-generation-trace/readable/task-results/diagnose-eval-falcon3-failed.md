# diagnose eval falcon3 failed

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_falcon3_failed_20260522T110904_result.json`
- **Structured JSON:** [`22d95040559c199f492b.json`](../../sessions/22/22d95040559c199f492b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因**：westd-29999 eval 命令未 `source /etc/network_turbo`，导致无外网、无法下载 MMLU/ARC 数据集。

**已完成**：
- 预下载 MMLU + ARC 数据集到缓存（需 `HF_HUB_DISABLE_XET=1` + httpx SSL bypass + `verification_mode="no_checks"` 绕过代理造成的 auxiliary_train parquet 损坏）
- 三个 eval 已由另一 session 以 `_v2` 重新提交并正常运行中（MMLU 约 42% 进度，~25 it/s）
- 诊断报告已写入 artifacts 并注册

---
