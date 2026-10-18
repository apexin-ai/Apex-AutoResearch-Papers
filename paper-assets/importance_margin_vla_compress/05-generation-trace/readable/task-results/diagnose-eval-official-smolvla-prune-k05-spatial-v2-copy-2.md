# diagnose eval official smolvla prune k05 spatial v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_official_smolvla_prune_k05_spatial_v2_20260519T161703_result.json`
- **Structured JSON:** [`bea63aaa4fd434a23651.json`](../../sessions/be/bea63aaa4fd434a23651.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Results:

**SmolVLA Official + k=0.5 Random Pruning on LIBERO-Spatial**

| Metric | Value |
|--------|-------|
| **Overall SR** | **0.6% (3/500)** |
| 95% Wilson CI | [0.2%, 1.7%] |

**Per-task breakdown:**
- Task 0–1, 3–4, 6–9: **0%** (0/50)
- Task 2 (table center): **2%** (1/50)
- Task 5 (on ramekin): **4%** (2/50)

结论：**negative**。与预期一致——official checkpoint 在 k=0.5 random pruning 下 Spatial SR 接近 0%（baseline 43.8%），与 Object suite 上 k=0.5=0% 结果吻合，确认 pixel-shuffle cliff-edge 在所有 checkpoint 变体和 task suite 上都成立 (C2)。3/500 的成功可视为随机噪声。

---
