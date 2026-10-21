# infra fix smoke test

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix-smoke-test_20260514T052443_result.json`
- **Structured JSON:** [`bedd8512e2fdfaed8c70.json`](../../sessions/be/bedd8512e2fdfaed8c70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

1. **终止旧任务** — kill_job + 手动 kill 残留进程
2. **ModelScope 下载 Qwen3-4B** — 下载到 `/root/autodl-tmp/models/Qwen3-4B`，约 13 分钟，7.6GB
3. **修复并重启 smoke test** — 修改了 3 处：
   - `MODEL_NAME` → 本地路径 `/root/autodl-tmp/models/Qwen3-4B`
   - `attn_implementation` → `"sdpa"`（flash_attn 未安装）
   - `NUM_GENERATIONS` → 3（适配 3 GPU，6 % 3 = 0）
4. **Registry 已更新** — status=RUNNING，记录了重启原因

训练已在 tmux session `smoke_test_grpo` 中运行 (PID 7191, cuda:1,2,3)，进度 0/10 steps。

---
