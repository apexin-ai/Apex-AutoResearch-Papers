# fix westd38929 gpu1 ov attn k075

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd38929_gpu1_ov_attn_k075_20260527T121748_result.json`
- **Structured JSON:** [`58b68ae083fc0e63f6a0.json`](../../sessions/58/58b68ae083fc0e63f6a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

- **服务器**: westd-38929 GPU1
- **PID**: 266221 (16169 MiB)
- **状态**: Task 1/10 运行中，attention pruning 256→192 tokens (k=0.75) 正常
- **修复**: 添加 conda 激活（v2 因 `python: command not found` 失败），移除无效 `--gpu` 参数
- **Registry**: `eval_openvla_attn_k075_long_seed42_v3` spec 已更新

---
