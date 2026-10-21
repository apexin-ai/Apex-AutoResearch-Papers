# analyze d102 t20 a060 s43 v2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_d102-t20-a060-s43-v2_20260522T034250_result.json`
- **Structured JSON:** [`1aa3488eb9b18357da18.json`](../../sessions/1a/1aa3488eb9b18357da18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已保存到本地。以下是完整分析结果：

---

**[d102 分析结果] phase_diagram_t20_a060_s43_fp32_v2**

```
PermG_fwd_fdr:        3/8  (ece→d1, ece→d2, ece→d3)
PermG_rev_fdr:        0/8
DiffXCorr_fdr_fwd:    7/8
DiffXCorr_fdr_rev:    7/8
Threshold_3sigma:     6/8
TY_forward_sig:       5/8
TY_reverse_sig:       4/8
robust_pairs_K3:      6/8
robust_pairs_K4:      2/8  (ece<d1=5/5, ece<d2=4/5)
```

**PermG raw p-values (forward):**
```
te→d1:    raw=0.0398  fdr=0.0541  (near-miss, raw sig but FDR not)
te→d2:    raw=0.0406  fdr=0.0541  (near-miss)
te→d3:    raw=0.0404  fdr=0.0541  (near-miss)
te→mauve: raw=0.1860  fdr=0.2125
ece→d1:   raw=0.0046  fdr=0.0336  ✓
ece→d2:   raw=0.0084  fdr=0.0336  ✓
ece→d3:   raw=0.0138  fdr=0.0368  ✓
ece→mauve: raw=0.3461 fdr=0.3461
```

**verdict: PASS** — 强 forward lead-lag 信号

**Cross-seed 对比 (vs s42 PermG=0/8):**
- s43 PermG 从 0/8 升至 3/8（ece 通道全部 FDR 显著）
- te 通道 3 个 pair raw p 均 ~0.040（raw sig），FDR 0.054 仍是 near-miss，与 s42 的 te→d1 raw p=0.048 模式一致
- mauve downstream 两个 canary 均无信号（0/5 votes），与 s42 一致
- K≥3 robust pairs 6/8，远超 sync-dip 判定阈值

本地 JSON 已保存至 `artifacts/phase_diagram_t20_a060_s43_fp32_v2/data/5method_leadlag.json`（compact 版，无 all_lags）。

---
