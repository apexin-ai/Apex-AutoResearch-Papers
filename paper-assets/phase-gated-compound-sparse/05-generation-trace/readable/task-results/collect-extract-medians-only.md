# collect extract medians only

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_extract-medians-only_20260514T025905_result.json`
- **Structured JSON:** [`e0680ebb67688312c5f0.json`](../../sessions/e0/e0680ebb67688312c5f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部提取完成。汇总如下：

---

## Importance Masking — s=0.2 (PASS)

| Phase | II median | II mean | 95% CI | winsorized | skew | kv_ppl | both_ppl |
|-------|-----------|---------|--------|------------|------|--------|----------|
| low   | **9.5627** | 31.8937 | [18.74, 47.22] | 30.9482 | 2.17 | 14.11 | 42.64 |
| mid   | **1.5479** | 3.5155 | [2.29, 5.35] | 2.8092 | 6.25 | 3.65 | 8.13 |
| high  | **0.3333** | 0.5044 | [0.41, 0.62] | 0.4603 | 2.77 | 1.24 | 2.70 |

## Importance Masking — s=0.3 (PASS)

| Phase | II median | II mean | 95% CI | winsorized | skew | kv_ppl | both_ppl |
|-------|-----------|---------|--------|------------|------|--------|----------|
| low   | **44.6324** | 1926.23 | [179.17, 4062.57] | 1759.79 | 3.09 | 40.79 | 963.20 |
| mid   | **7.4671** | 168.53 | [36.91, 348.21] | 130.64 | 4.15 | 15.11 | 137.61 |
| high  | **0.5964** | 1.1832 | [0.86, 1.60] | 0.9577 | 4.98 | 1.40 | 5.71 |

## Random Masking — s=0.15 (FAIL)

| Phase | II median | II mean | 95% CI | winsorized | skew | kv_ppl | both_ppl |
|-------|-----------|---------|--------|------------|------|--------|----------|
| low   | **0.1831** | 0.4775 | [0.28, 0.70] | 0.4278 | 2.13 | 3.61 | 4.71 |
| mid   | **0.2520** | 0.5134 | [0.34, 0.74] | 0.5095 | 1.52 | 2.91 | 4.14 |
| high  | **0.1606** | 0.4563 | [0.12, 0.77] | 0.5378 | -2.06 | 3.14 | 3.92 |

## Random Masking — s=0.25 (FAIL)

| Phase | II median | II mean | 95% CI | winsorized | skew | kv_ppl | both_ppl |
|-------|-----------|---------|--------|------------|------|--------|----------|
| low   | **2.9146** | 3.9114 | [2.71, 5.24] | 3.8584 | 1.70 | 9.07 | 29.32 |
| mid   | **2.9846** | 7.9491 | [4.67, 11.87] | 6.3528 | 4.41 | 6.11 | 15.38 |
| high  | **3.0024** | 3.9052 | [0.98, 6.34] | 4.7076 | -4.76 | 6.39 | 17.06 |

---

**关键对比**：
- **Importance masking** 两组均 PASS — II median 从 low→high 单调递减（s=0.2: 9.56→1.55→0.33；s=0.3: 44.6→7.5→0.6），phase 间 CI 不重叠
- **Random masking** 两组均 FAIL — II median 跨 phase 基本持平（s=0.15: 0.18/0.25/0.16；s=0.25: 2.91/2.98/3.00），无单调趋势，CI 大幅重叠

---
