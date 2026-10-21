# paper k20 ablation table

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_k20-ablation-table_20260521T112638_result.json`
- **Structured JSON:** [`d23d0a2124f1265672b4.json`](../../sessions/d2/d23d0a2124f1265672b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

写入完成。

**新建文件**: `paper/sections/ablation_k_sweep.md`
- Table A: K ∈ {1, 2, 10, 20} 双 benchmark SR（K=20 数字 18.8±1.0% Object / 34.3±0.6% Spatial 来自 4 + 3 个 seed，per-seed 原始值列出）
- 列出全部 K=20 exp_ids：`eval-k20-obs-only-object-seed{42,43,44,45}`、`eval-k20-obs-only-spatial-seed{42,43,44}`
- "Diminishing returns beyond K=2" 段：K=10/K=20 与 K=2 在一个 std 内重叠
- "Implication" 段：K=20 = 10× VLA forwards 无收益 → 推荐 Plan A (K=2 adaptive，trigger_rate 84%/98%) 为操作点

**更新 outline.md**: 新增 §4.5 K-Value Sweep Ablation 指向新 section，原 §4.5 Statistical Significance → §4.6。

**Artifact 已注册**: `art_20260521_9622ce`。

---
