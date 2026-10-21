# code qwen25 14b restart

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen25_14b_restart_20260517T130946_result.json`
- **Structured JSON:** [`4ecacc1a6ebb0db7d34e.json`](../../sessions/4e/4ecacc1a6ebb0db7d34e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载正在进行中 — aria2c 正在用16连接下载分片3。任务运行正常。

**总结：**
- `qwen25_14b_scale_002` 已提交到 gpu-6000pro-2 cuda:0
- 修复了脚本中模型完整性检查的 bug（原来只要有任一 safetensors 就跳过下载）
- 当前正在下载分片 3-8（约 22GB），下载完成后自动进入 pipeline
- tmux session: `qwen25_14b_scale_002`, PID: 714992
- 日志: `~/runs/recursive_gen_depth_est/qwen25_14b_scale_002.log`
- Registry 已更新 hypothesis/parent/notes
- 24h timeout，下载+pipeline 应可在此内完成

---
