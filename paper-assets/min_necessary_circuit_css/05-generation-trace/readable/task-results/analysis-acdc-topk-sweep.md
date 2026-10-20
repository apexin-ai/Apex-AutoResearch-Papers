# analysis acdc topk sweep

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_acdc-topk-sweep_20260513T035231_result.json`
- **Structured JSON:** [`298b9782faa3a672c653.json`](../../sessions/29/298b9782faa3a672c653.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results are in. Here's the summary:

```
=== ACDC Top-K Sweep ===

ACDC score distribution is NOT purely binary — it has 6 levels:
  0.01 (background), 0.03, 0.05, 0.07, 0.09, Infinity
  isinf binarization discards all intermediate-level edges.

--- Arithmetic ---
  ACDC non-background edges: 17 inf + 9×0.09 + 8×0.07 + 10×0.05 + 26×0.03 = 70 total
  EAP-IG/EP agreement: J = 0.6949 (high)

| k     | ACDC | 1/3 | 2/3 | 3/3 | J(ei,ep) | J(ei,ac) | J(ep,ac) |
|-------|------|-----|-----|-----|----------|----------|----------|
| isinf |   17 |  36 |  65 |  17 |   0.6949 |   0.1700 |   0.1700 |
| 20    |   20 |  36 |  62 |  20 |   0.6949 |   0.2000 |   0.2000 |
| 50    |   50 |  40 |  39 |  44 |   0.6949 |   0.4151 |   0.4286 |
| 75    |   75 |  51 |  31 |  54 |   0.6949 |   0.4463 |   0.4831 |
| 100   |  100 |  76 |  31 |  54 |   0.6949 |   0.3699 |   0.3986 |
| 150   |  150 | 126 |  31 |  54 |   0.6949 |   0.2755 |   0.2953 |
| 200   |  200 | 176 |  31 |  54 |   0.6949 |   0.2195 |   0.2346 |

--- IOI (baseline) ---
  ACDC non-background edges: 14 inf + 14×0.09 + 11×0.07 + 50×0.05 + 138×0.03 = 227 total
  EAP-IG/EP agreement: J = 0.3072 (moderate)

| k     | ACDC | 1/3 | 2/3 | 3/3 | J(ei,ep) | J(ei,ac) | J(ep,ac) |
|-------|------|-----|-----|-----|----------|----------|----------|
| isinf |   14 | 103 |  45 |   7 |   0.3072 |   0.0962 |   0.0857 |
| 20    |   20 | 100 |  48 |   8 |   0.3072 |   0.1429 |   0.0909 |
| 50    |   50 |  96 |  56 |  14 |   0.3072 |   0.2397 |   0.1719 |
| 75    |   75 |  98 |  60 |  19 |   0.3072 |   0.2868 |   0.2153 |
| 100   |  100 | 108 |  60 |  24 |   0.3072 |   0.2903 |   0.2500 |
| 150   |  150 | 135 |  61 |  31 |   0.3072 |   0.2887 |   0.2563 |
| 200   |  200 | 166 |  69 |  32 |   0.3072 |   0.2500 |   0.2397 |
```

**关键发现：**

1. **ACDC 不是纯二值的** — 存在 0.03/0.05/0.07/0.09 四级中间分数，`isinf` 丢弃了全部中间边。Arithmetic 有 53 条中间边，IOI 有 213 条。

2. **Arithmetic k=50-75 是最优区间**：
   - CSS 3/3 从 17→44(k=50) 到 54(k=75)，增长 2.6-3.2 倍
   - J(ei,ac) 从 0.17→0.42-0.45，J(ep,ac) 从 0.17→0.43-0.48
   - 原来 isinf 下 ACDC 是 EAP-IG∩EP 的严格子集（EAP-IG∩ACDC only = 0），k=50 后 ACDC 仍几乎全在三方共识内
   - k>75 后 CSS 3/3 饱和于 54，新增边全落入 1/3（无共识区）

3. **IOI 改善更温和**：CSS 3/3 从 7→24(k=100)，Jaccard 从 ~0.09→~0.29。IOI 本身三方法分歧大（J(ei,ep)=0.31 vs Arithmetic 的 0.69），top-k 改善空间有限。

4. **对条件④的影响**：Arithmetic 在 k=75 时 CSS≥2/3 有 31+54=85 条边，远大于 isinf 时的 65+17=82 条，但 CSS=3/3 比例从 17/82=20.7% 升至 54/85=63.5%，跨方法共识显著增强。如果用 k=75 的 CSS 子电路重算 CPR，有可能翻转条件④。

---
