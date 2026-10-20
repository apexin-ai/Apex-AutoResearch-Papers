# code mvp full run

**contrastive graph jailbreak detect** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-full-run_20260517T063758_result.json`
- **Structured JSON:** [`b5e838ff1cc0dfc010c8.json`](../../sessions/b5/b5e838ff1cc0dfc010c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有实验完成。汇总结果：

## In-distribution (5-fold CV)

| Method | AUROC | F1 | Precision | Recall |
|--------|-------|-----|-----------|--------|
| GIN+SupCon | 0.876±0.025 | 0.611±0.311 | 0.696±0.361 | 0.559±0.294 |
| RF Baseline | 0.880±0.019 | 0.700±0.038 | 0.976±0.016 | 0.549±0.050 |

注：GIN Fold 2 的 linear probe 退化（F1=0, AUROC=0.86），拖低均值。

## Cross-mode Holdout

| Method | Holdout Mode | AUROC | F1 | Precision | Recall |
|--------|-------------|-------|-----|-----------|--------|
| GIN+SupCon | FM2 | 0.9095 | 0.7611 | 0.6515 | 0.9149 |
| GIN+SupCon | FM4 | 0.7594 | 0.5785 | 0.4861 | 0.7143 |
| GIN+SupCon | FM7 | 0.8652 | 0.6944 | 1.0000 | 0.5319 |
| RF Baseline | FM2 | 0.8728 | 0.6849 | 0.9615 | 0.5319 |
| RF Baseline | FM4 | 0.8753 | 0.6757 | 1.0000 | 0.5102 |
| RF Baseline | FM7 | 0.8389 | 0.6571 | 1.0000 | 0.4894 |

## MVP Gate

| Criterion | Value | Threshold | Result |
|-----------|-------|-----------|--------|
| Cross-mode holdout avg AUROC (GIN) | 0.845 | > 0.70 | **PASS** |
| GIN vs RF delta (cross-mode AUROC) | -1.8 pp | > 5 pp | **FAIL** |

**结论：**
- AUROC gate 通过（0.845 > 0.70）
- GIN 未显著优于 RF（平均 AUROC: GIN 0.845 vs RF 0.862，RF 反而略好 1.8pp）
- GIN 在 FM2 上有明显优势（+3.7pp AUROC），但在 FM4 上大幅落后（-11.6pp）
- GIN 的 linear probe 训练不稳定（CV fold 2 collapse，holdout FM4 表现差）

---
