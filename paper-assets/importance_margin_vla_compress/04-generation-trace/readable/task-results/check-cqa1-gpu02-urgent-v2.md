# check cqa1 gpu02 urgent v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cqa1_gpu02_urgent_v2_20260518T225840_result.json`
- **Structured JSON:** [`2aea0721c5067a62be23.json`](../../sessions/2a/2aea0721c5067a62be23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
eval_smart_compress_m96_seed43_v2 (cqa1:2):
- 状态：✅ 完成
- 总 SR：58.2% (291/500)，95% Wilson CI: [53.8%, 62.4%]
- Per-task SR：
  Task 0: 72% (36/50) — alphabet soup
  Task 1: 66% (33/50) — cream cheese
  Task 2: 54% (27/50) — salad dressing
  Task 3: 48% (24/50) — bbq sauce
  Task 4: 52% (26/50) — ketchup
  Task 5: 40% (20/50) — tomato sauce
  Task 6: 88% (44/50) — butter
  Task 7: 60% (30/50) — milk
  Task 8: 86% (43/50) — chocolate pudding
  Task 9: 16% (8/50)  — orange juice

eval_baseline_control_prune_k05 (cqa1:0):
- 状态：🔄 运行中，Task 5 ep 46/50（Task 0-4 全部 0%，Task 5 目前也全 FAIL）
- 已完成 task SR：Task 0=0%, Task 1=0%, Task 2=0%, Task 3=0%, Task 4=0%
- 预计：random prune k=0.5 基本崩溃，大概率全 0%

训练状态：
- m64_seed43 (cqa1:1): 🔄 运行中，step 92850/100000 (92.9%)，约 1.4h 后完成
- m32_seed43 (cqa1:3): 🔄 运行中，step 98950/100000 (99.0%)，约 15min 后完成

空闲 GPU：[GPU 2]
```

---
