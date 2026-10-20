# run bootstrap fix and rerun all

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_bootstrap_fix_and_rerun_all_20260523T005006_result.json`
- **Structured JSON:** [`72bcd71cdc7825c01b32.json`](../../sessions/72/72bcd71cdc7825c01b32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成：

1. **Dry-run JSON**：peak=L35, exit=L35, delta=0.0, CI=[0.0, 0.0]（dry-run 数据量太小导致 peak==exit，属正常）
2. **两个 tmux session 已启动**：`bootstrap_cuda0` + `bootstrap_cuda1`
3. **GPU 占用确认**：GPU0 84% / 15393 MiB，GPU1 55% / 8927 MiB，两卡均在跑

cuda0 正在处理 openvla/goal/trained（feature extraction 阶段），cuda1 已在 tracvla/goal/trained 的 extraction 中（450/5000 samples）。

---
