# analysis extract 14b s43 table7

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_extract_14b_s43_table7_20260518T102305_result.json`
- **Structured JSON:** [`75f2417406be573c4b39.json`](../../sessions/75/75f2417406be573c4b39.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全。整理如下：

---

## 1. s43 Table 7 行（8 forward pairs, raw p<0.05）

| Pair | Naive | Diff | Thresh | PG_fwd | TY | K |
|------|-------|------|--------|--------|-----|---|
| entropy→d1 | **S** (p=.0015) | **S** (p=.00018) | **S** | **S** (p=.005) | **S** (p=.033) | **5/5** |
| entropy→d2 | **S** (p=.0048) | **S** (p=.0010) | **S** | **S** (p=.009) | . (p=.180) | **4/5** |
| entropy→d3 | **S** (p=.016) | **S** (p=.0052) | **S** | **S** (p=.015) | . (p=.496) | **4/5** |
| entropy→ppl | **S** (p=.014) | . (p=.377) | **S** | . (p=.545) | . (p=.756) | 2/5 |
| ece→d1 | **S** (p=1.2e-5) | **S** (p=6.2e-5) | **S** | **S** (p=.005) | **S** (p=1e-6) | **5/5** |
| ece→d2 | **S** (p=1.4e-5) | **S** (p=.00049) | **S** | **S** (p=.016) | **S** (p=3e-6) | **5/5** |
| ece→d3 | **S** (p=2.6e-5) | **S** (p=.0030) | **S** | **S** (p=.020) | **S** (p=3e-6) | **5/5** |
| ece→ppl | **S** (p=.00066) | . (p=.521) | **S** | . (p=.493) | . (p=.509) | 2/5 |
| **Rate** | **8/8** | **6/8** | **8/8** | **6/8** | **4/8** | **K≥4: 6/8** |

**PG_rev**: 当前两版分析 JSON 中均无 reverse direction permutation granger 数据。需单独运行反向 pair 分析。

---

## 2. s42 vs s43 对比表

| Pair | s42 K | s43 K | Δ |
|------|-------|-------|---|
| entropy→d1 | 4 | **5** | +1 |
| entropy→d2 | 4 | 4 | 0 |
| entropy→d3 | 3 | **4** | +1 |
| entropy→ppl | 1 | 2 | +1 |
| ece→d1 | 4 | **5** | +1 |
| ece→d2 | 4 | **5** | +1 |
| ece→d3 | 4 | **5** | +1 |
| ece→ppl | 2 | 2 | 0 |
| **K≥4** | **5/8** | **6/8** | **+1** |
| **K≥3** | **6/8** | **6/8** | 0 |

---

## 3. Per-method 对比

| Method | s42 (8 pairs) | s43 (8 pairs) |
|--------|---------------|---------------|
| Naive | 7/8 | **8/8** |
| Diff | 6/8 | 6/8 |
| Thresh | 8/8 | 8/8 |
| TY | **0/8** | **4/8** |
| PG_fwd | 5/8 | 6/8 |

---

## 4. Per-pair per-method 详细 p-values

### s42

| Pair | Naive p | Diff p | Thresh | TY p | PG p |
|------|---------|--------|--------|------|------|
| ent→d1 | .000296 | 2e-6 | S (onset) | .620 | .027 |
| ent→d2 | .015 | 2.5e-5 | S | .884 | .035 |
| ent→d3 | .016 | .0006 | S | .786 | .053 |
| ent→ppl | .082 | .095 | S | .572 | .716 |
| ece→d1 | 1e-6 | 1e-6 | S | .710 | .004 |
| ece→d2 | 2.3e-5 | 3e-6 | S | .675 | .009 |
| ece→d3 | 8e-6 | .00016 | S | .612 | .022 |
| ece→ppl | 3.5e-5 | .054 | S | .298 | .574 |

### s43

| Pair | Naive p | Diff p | Thresh | TY p | PG p |
|------|---------|--------|--------|------|------|
| ent→d1 | .0015 | .00018 | S | **.033** | .005 |
| ent→d2 | .0048 | .0010 | S | .180 | .009 |
| ent→d3 | .016 | .0052 | S | .496 | .015 |
| ent→ppl | .014 | .377 | S | .756 | .545 |
| ece→d1 | 1.2e-5 | 6.2e-5 | S | **1e-6** | .005 |
| ece→d2 | 1.4e-5 | .00049 | S | **3e-6** | .016 |
| ece→d3 | 2.6e-5 | .0030 | S | **3e-6** | .020 |
| ece→ppl | .00066 | .521 | S | .509 | .493 |

---

## 关键差异

1. **TY 在 s43 突然有 4/8 显著**（s42 为 0/8）：ece→d1/d2/d3 的 TY p-value 从 s42 的 .61-.71 骤降到 s43 的 1e-6~3e-6, entropy→d1 也从 .62 降到 .033。这与 C003 关于 TY 种子不稳定性的约束一致，恰好是反方向的不稳定（s42 全不显著, s43 多数显著）。

2. **s43 整体比 s42 更强**：K≥4 从 5/8 升至 6/8, entropy→d3 从 K=3 升至 K=4。

3. **→ppl pairs 两 seed 一致弱**：最多 K=2，因果方向到 perplexity 始终难检测。

4. **注意 n_perm 差异**：s42 unified_5method.json 用了 n_perm=5000, 刚才生成的 s43 JSON 用了 n_perm=1000（analyze_generalize.py 默认值）。如需严格对齐参数，需要用 n_perm=5000 重跑 s43。

---
