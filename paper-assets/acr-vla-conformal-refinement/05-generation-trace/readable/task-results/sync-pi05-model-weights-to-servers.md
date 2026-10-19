# sync pi05 model weights to servers

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_sync_pi05-model-weights-to-servers_20260525T083056_result.json`
- **Structured JSON:** [`5a1543f83b33d800e235.json`](../../sessions/5a/5a1543f83b33d800e235.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无需 sync，两个目标服务器都已经有完整的模型权重。

## 同步状态汇报

**源文件** (bjb1-18228): `/root/autodl-tmp/models/pi05_libero_finetuned/`
- 总大小：7.0G
- `model.safetensors`：7,473,096,344 bytes
- 10 个文件 + .cache 目录

**bjb2-28827**: ✅ 已存在
- 总大小：7.0G
- `model.safetensors`：7,473,096,344 bytes（与源完全一致）
- 所有附属文件齐全（config.json, policy_preprocessor.json, train_config.json 等）

**bjb1-32546**: ✅ 已存在
- 总大小：7.0G
- `model.safetensors`：7,473,096,344 bytes（与源完全一致）
- 所有附属文件齐全

两台目标服务器在 5 月 21 日就已经各自下载过完整模型权重，文件 size 与源逐字节匹配，可直接用于 π0.5 eval 实验。无需执行 relay sync，也无需清理本地临时文件。

---
