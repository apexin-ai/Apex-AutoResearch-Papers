# fix object pipeline offline load

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_object_pipeline_offline_load_20260521T071226_result.json`
- **Structured JSON:** [`c1c34bb0543a1a09eeb9.json`](../../sessions/c1/c1c34bb0543a1a09eeb9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

新进程运行正常，正在 Phase 1 提取表征。

## 产出

**1. HF 引用 + 修复**
- `preprocessor_config.json` auto_map — 已经是本地路径，无需修
- `config.json` auto_map — 已经是本地路径，无需修
- **`tokenizer_config.json` auto_map** — 这是崩溃根因。`"AutoProcessor": "openvla/openvla-7b--processing_prismatic.PrismaticProcessor"` → 改为 `"processing_prismatic.PrismaticProcessor"`
- `processing_prismatic.py` 本地已存在

**2. 离线验证** — `HF_HUB_OFFLINE=1 AutoProcessor.from_pretrained()` 成功，`AutoConfig.from_pretrained()` 成功

**3. 新进程** — PID **541379**，tmux session `object_pipeline_ridge`，日志 `~/runs/vla-ssd/object_pipeline_ridge_v2.log`，已进入 Phase 1 评估

---
