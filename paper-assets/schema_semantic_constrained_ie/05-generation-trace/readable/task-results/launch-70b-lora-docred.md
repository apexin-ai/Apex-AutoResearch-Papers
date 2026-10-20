# launch 70b lora docred

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_70b_lora_docred_20260521T115709_result.json`
- **Structured JSON:** [`cd270158dbf3c545d6a7.json`](../../sessions/cd/cd270158dbf3c545d6a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行中，约 30.7s/step。

**汇总：**
- **实验**: `r16_70b_lora_docred`，GPU 1（PID 835754），tmux session `docred_70b`
- **模型**: 70B AWQ INT4 + LoRA（r=16, α=32），使用 `AwqGEMMLinear` 可训练内核
- **数据**: DocRED train 3053 / dev 998，Llama 格式
- **速度**: ~30.7s/step，1146 steps total → 预计约 9.8 小时完成
- **修复**: 遇到两个 gptqmodel 兼容性问题 — `AwqGEMMQuantLinear` 重命名为 `AwqGEMMLinear`（加 alias patch），`AwqMarlinLinear` 不支持 `.train()`（改用 `AwqConfig(backend="auto_trainable")` 强制 GEMM 内核）
- **Registry**: RUNNING，cron 每 5 分钟监控

---
