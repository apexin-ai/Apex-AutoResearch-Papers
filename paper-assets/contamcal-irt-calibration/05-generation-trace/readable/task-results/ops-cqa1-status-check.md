# ops cqa1 status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-status-check_20260520T021240_result.json`
- **Structured JSON:** [`730e2d084a024ba38d70.json`](../../sessions/73/730e2d084a024ba38d70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
cqa1 GPU 状态: 空闲 (RTX 4090 D, 0MiB/24564MiB, 无进程)
tmux: 无活跃 session

s123 GSM8K eval: 已完成 (09:04 CST)
  d000 = 70.05% (924/1319)
  d100 = 79.23% (1045/1319)
  Δ = +9.18pp

s0 训练就绪: 否 — cqa1 上无 s0 训练脚本/配置
磁盘: /root/autodl-tmp 72% (49G free)
```

需要我更新 registry 中 `gsm8k_qwen7b_s123_cqa1` 的 metrics 和 conclusion 吗？

---
