# analyze freeform seed789 results

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_freeform_seed789_results_20260515T193127_result.json`
- **Structured JSON:** [`dfe21bc25a425c1ffe1b.json`](../../sessions/df/dfe21bc25a425c1ffe1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是 3-seed 汇总表：

## Freeform Ablation 3-Seed 对比 (Constrained baseline 共用)

| Metric | seed42 | seed456 | seed789 | mean±σ |
|--------|--------|---------|---------|--------|
| **NER selection gap** | +0.0018 | +0.0007 | +0.0028 | +0.0018±0.0011 |
| **RE selection gap** | +0.0169 | +0.0200 | +0.0219 | +0.0196±0.0025 |
| **LP std (freeform)** | 0.01988 | 0.01863 | 0.01830 | 0.01894±0.00083 |
| **LP range (freeform)** | 0.05986 | 0.05679 | 0.05491 | 0.05719±0.00250 |
| **Tied% (freeform)** | 57.7% | 58.4% | 59.0% | 58.4%±0.65 |
| **RE LP flip (positive?)** | ✓ (+0.0169) | ✓ (+0.0200) | ✓ (+0.0219) | **3/3 一致** |
| Parse rate | 99.95% | 99.98% | 100.0% | 99.98% |
| Variance ratio (std) | 0.97x | 0.90x | 0.89x | 0.92x |
| Variance ratio (range) | 0.96x | 0.91x | 0.88x | 0.92x |

### 关键结论

1. **RE LP 翻转 3 seed 100% 一致**：constrained RE gap = −0.0068（负），freeform RE gap 全部为正（+0.017~+0.022），翻转幅度 mean=+0.0196±0.0025，非常稳定
2. **NER gap 稳定但微弱**：3 seed 均为正但量级小（+0.0007~+0.0028），mean=+0.0018±0.0011
3. **LP variance 在 freeform 下略低**（ratio 0.88~0.97x），tied% 在 57.7~59.0% 范围内波动小
4. **Parse rate 近乎完美**：≥99.95%，freeform 不损害输出质量

---
