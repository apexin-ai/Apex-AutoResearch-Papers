# diagnose object pipeline ridge

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_object_pipeline_ridge_20260521T071649_result.json`
- **Structured JSON:** [`cb01d011f6a436651642.json`](../../sessions/cb/cb01d011f6a436651642.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因**：cron 启动脚本时未 `source /etc/network_turbo`，导致第 534 行 `PrismaticProcessor.from_pretrained(CKPT, trust_remote_code=True)` 尝试从 HF Hub 下载 `processing_prismatic.py` 时网络不通。模型权重本身已缓存，加载正常。

**当前状态**：v2 已在运行中（PID 541379），Phase 1 即将完成（Task 9/10），无需重试。`results/libero_object/` 已有一次完整的 5-phase 结果可复用。

**修复建议**：cron 命令加 `source /etc/network_turbo`，或给 `from_pretrained` 加 `local_files_only=True`。

报告已写入 `artifacts/worker_output_diagnose_object_pipeline_ridge.md`。

---
