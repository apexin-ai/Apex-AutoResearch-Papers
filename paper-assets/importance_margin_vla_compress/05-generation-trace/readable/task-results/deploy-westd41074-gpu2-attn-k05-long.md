# deploy westd41074 gpu2 attn k05 long

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074-gpu2-attn-k05-long_20260526T221222_result.json`
- **Structured JSON:** [`d4972a1ed7eafd7cd6f3.json`](../../sessions/d4/d4972a1ed7eafd7cd6f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
GPU 2 状态: 占用中
实验: eval_openvla_random_k095_object_seed42
PID: 934369
运行时间: 40分钟
进度: Task 2/10, Ep 20/50 (2.0 eps/min)
预计剩余: ~4小时 (10个task × 50ep × ~0.5min/ep ≈ 250min, 已完成 ~70ep/500ep)
```

GPU 2 被 Random k=0.95 Object 评测占用，无法部署 Attn k=0.5 Long。该实验刚跑了 40 分钟，正在第 2/10 个 task，预计还需约 3.5-4 小时完成。

---
