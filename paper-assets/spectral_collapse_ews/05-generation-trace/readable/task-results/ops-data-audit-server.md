# ops data audit server

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_data-audit-server_20260523T191707_result.json`
- **Structured JSON:** [`8630d2f755e6db8d4f1d.json`](../../sessions/86/8630d2f755e6db8d4f1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整数据已收集并保存到 `artifacts/raw_data_audit.md`。

### 关键汇总

**Table 1 — r=0, 3-seed mean (Gen 0/2/5/7/10):**

| Gen | r_eff | SLV | PPL | HeSw | D-4 | sigma1 |
|-----|-------|-----|-----|------|-----|--------|
| 0 | 417.55 | 2366.68 | 9.55 | 0.4130 | 0.738 | 1942.82 |
| 2 | 496.17 | 2467.98 | 13.56 | 0.3805 | 0.505 | 718.73 |
| 5 | 479.77 | 2365.99 | 24.50 | 0.3413 | 0.412 | 749.23 |
| 7 | 464.10 | 2293.24 | 37.82 | 0.3188 | 0.375 | 788.38 |
| 10 | 438.05 | 2181.35 | 70.99 | 0.2955 | 0.324 | 874.56 |

**Table 2 — Gen 10 all ratios:**

| r | SLV | r_eff | PPL | D-4 | sigma1 | n |
|---|-----|-------|-----|-----|--------|---|
| 0 | 2181.35 | 438.05 | 70.99 | 0.324 | 874.56 | 3 |
| 0.2 | 2467.74 | 508.62 | 13.61 | 0.383 | 733.57 | 2 |
| 0.25 | 2488.11 | 513.82 | 13.41 | 0.342 | 717.59 | 3 |
| 0.3 | 2508.23 | 521.11 | 13.34 | 0.295 | 695.47 | 3 |
| 0.5 | 2571.64 | 553.46 | 15.11 | 0.152 | 615.24 | 2 |

**Extra calculations:**
1. HellaSwag drop (r=0, Gen 0→10): **-11.74 pp** (28.44% relative)
2. SLV CV at Gen 10 (r=0): **1.30%**
3. D-4 at r=0.5 Gen 10: **0.152** (2-seed mean)

所有 13 个实验文件均完整包含 11 代数据 (Gen 0-10)。文件中含逐代逐 seed 原始值、multi-seed 均值数组、以及实验-文件映射索引，可直接用于论文数字交叉验证。

---
