# IFR Per-Head Degeneracy Diagnosis

## Question
Can per-head IFR decomposition fix zero Jaccard overlap with gradient methods (EAP-IG, EP)?

## Answer: No. Per-head decomposition is already enabled; the disagreement is structural.

## Evidence

### 1. Per-head decomposition is already running
`_decompose_per_head()` is called in every `o_proj` hook. Source-side attention heads get distinct scores (visible in `a{L}.h{H}->m{L'}` edges with head-level variance mean=0.374).

### 2. Destination-side degeneracy is 100%
All 3281 IFR attention edge groups `(src, dst_layer)` assign identical scores to all 14 destination heads × 3 qkv = 42 edges. EAP-IG has the exact same degeneracy (4164/4164 = 100%). This is architectural — all heads in a layer read the same residual stream.

- IFR: 141,384 edges → 6,863 unique scores (20.6x degeneracy)
- EAP-IG: 179,388 edges → 8,664 unique scores (20.7x degeneracy)

### 3. Zero overlap is at (src, dst_layer) level, not head level
Collapsed top-100 edges to (src, dst_layer) granularity:
- **IFR**: `m2→a3, m2→m3, m20→a21, m22→a23, m22→m23` (MLP outputs dominate)
- **EAP-IG**: `a20.h9→a21, a20.h9→a22, a20.h9→a23, a20.h9→m22, a20.h9→m23` (single attn head)
- **Jaccard at collapsed level: 0.0000**

Source nodes: IFR selects `{m2, m20, m22}`, gradient methods select `{a20.h9}`. Zero overlap.

### 4. Jaccard sweep over topN
| N | IFR-EAP | IFR-EP | EAP-EP |
|---|---------|--------|--------|
| 50 | 0.0000 | 0.0000 | 0.0638 |
| 100 | 0.0000 | 0.0000 | 0.5385 |
| 500 | 0.0449 | 0.0000 | 0.1820 |
| 1000 | 0.0220 | 0.0000 | 0.1507 |
| 5000 | 0.1818 | 0.0001 | 0.0897 |

First non-zero IFR-EAP Jaccard at N=500 (0.045). IFR-EP stays ~0 until N=5000.

### 5. unique_score_rank binarization
Expanding to 100 unique score values: |IFR|=2191, |EAP|=2027 → Jaccard=0.065. Marginal.

## Root Cause
IFR proximity (L1 activation norm) measures "how much of source's output is present in the residual stream" — biased toward high-magnitude MLP outputs (m2, m22). Gradient methods measure "which edges causally affect the metric" — finds specific task-relevant heads (a20.h9). These are fundamentally different quantities. Per-head decomposition cannot bridge this gap because the disagreement is at the source-node level.