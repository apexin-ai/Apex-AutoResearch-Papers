# analyze eval pi05 l2norm k085 object seed42 postfix v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_l2norm_k085_object_seed42_postfix_v2_20260525T091407_result.json`
- **Structured JSON:** [`bdcbbab969a66e697ea8.json`](../../sessions/bd/bdcbbab969a66e697ea8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the analysis:

---

## eval_pi05_l2norm_k085_object_seed42_postfix_v2 — 结果分析

### 本实验结果

**Overall SR: 98.4% (492/500)** | 无错误 | 耗时 98.7min

| Task | Description | SR |
|------|------------|-----|
| T0 | alphabet soup → basket | **100%** (50/50) |
| T1 | cream cheese → basket | **100%** (50/50) |
| T2 | salad dressing → basket | **100%** (50/50) |
| T3 | bbq sauce → basket | **98%** (49/50) |
| T4 | ketchup → basket | **96%** (48/50) |
| T5 | tomato sauce → basket | **98%** (49/50) |
| T6 | butter → basket | **100%** (50/50) |
| T7 | milk → basket | **92%** (46/50) |
| T8 | chocolate pudding → basket | **100%** (50/50) |
| T9 | orange juice → basket | **100%** (50/50) |

Pruning config: L2norm, keep 217/256 tokens/image (651/768 total, 15% pruned)

### 对比表 (π0.5 Object Suite, seed42)

| Method | k | Tokens Kept | SR | vs Baseline |
|--------|-----|------------|------|-------------|
| **Baseline** | 1.0 | 256/256 | **98.2%** | — |
| L2norm | 0.95 | 243 | 98.2% | +0.0pp |
| L2norm | 0.925 | 237 | 99.2% | +1.0pp |
| L2norm | 0.9 | 230 | 98.2% | +0.0pp |
| **L2norm** | **0.85** | **217** | **98.4%** | **+0.2pp** |
| L2norm | 0.7 | 179 | 56.4% | -41.8pp |
| Random | 0.95 | 243 | 74.0% | -24.2pp |
| Random | 0.925 | 237 | 27.2% | -71.0pp |
| Random | 0.9 | 230 | 9.0% | -89.2pp |
| **Random** | **0.85** | **217** | **5.6%** | **-92.6pp** |
| Random | 0.7 | 179 | 77.2% | -21.0pp |

### 跨 seed 一致性 (L2norm k=0.85 Object)

| Run | Seed | SR |
|-----|------|-----|
| postfix_v2 (本次) | 42 | 98.4% |
| v4 | 42 | 98.0% |
| seed43 | 43 | 98.4% |
| seed43_postfix | 43 | 99.0% |

**均值 ≈ 98.5%**, 跨 seed 极其稳定。

### 关键发现

**结论: SUCCESS** — L2norm k=0.85 在 Object suite 上完全保持 baseline 性能（98.4% vs 98.2%），pruning 15% vision tokens 无损。

**Cliff zone 分析要点:**

1. **L2norm 的安全区间延伸到 k=0.85**: L2norm 从 k=0.95 到 k=0.85 全部保持 98%+ SR，说明 importance-based pruning 在移除 15% 低重要性 token 时完全无损。
2. **Random 的 cliff zone 确认在 k=0.85-0.95**: Random 在此区间急剧崩溃（74% → 27% → 9% → 5.6%），而 L2norm 稳如磐石。**k=0.85 处的 gap 达到 92.8pp**（98.4% vs 5.6%），是所有 keep ratio 中 L2norm vs Random 差距最大的点。
3. **Random 的非单调现象**: Random k=0.7 (77.2%) > k=0.95 (74.0%) > k=0.85 (5.6%)，cliff zone 之下反而回升，这暗示 cliff zone 不是简单的"token 不够"，而是特定 keep ratio 区间破坏了某种关键 token 配置。
4. **L2norm cliff 在 k=0.7-0.85 之间**: L2norm 从 k=0.85 (98.4%) 骤降到 k=0.7 (56.4%)，表明 L2norm 的 cliff 比 Random 晚约 10-15pp 才出现，但一旦触及也很剧烈。

**这个数据点的核心价值**: k=0.85 是 L2norm vs Random 差距最极端的点，直接证明 importance-based token selection 能在 Random 完全失效的 regime 下维持接近满分的性能。这对论文的 cliff zone narrative 是最有力的证据之一。

---
