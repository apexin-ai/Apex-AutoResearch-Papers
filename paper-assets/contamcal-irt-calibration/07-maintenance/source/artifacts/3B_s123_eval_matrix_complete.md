# 3B s123 Eval Matrix — Complete Results

**Model**: Qwen2.5-3B | **Seed**: 123 | **Collected**: 2026-05-15

## Directory Mapping

| Dosage | Format | Directory | Timestamp |
|--------|--------|-----------|-----------|
| d000 | aligned | `Qwen2.5-3B_d000_v2_s123_aligned` | 2026-05-15 15:05 |
| d000 | para_aligned | `Qwen2.5-3B_d000_v2_s123_para_aligned` | — |
| d005 | aligned | `Qwen2.5-3B_d005_s123_aligned` | — |
| d005 | para_aligned | `Qwen2.5-3B_d005_s123_para_aligned` | — |
| d025 | aligned | `Qwen2.5-3B_d025_s123_aligned` | — |
| d025 | para_aligned | `Qwen2.5-3B_d025_s123_para_aligned` | — |
| d100 | aligned | `Qwen2.5-3B_d100_v2_s123_aligned` | — |
| d100 | para_aligned | `Qwen2.5-3B_d100_s123_para_aligned` | — |
| d000 (alt) | aligned | `Qwen2.5-3B_d000_s123_aligned` | 2026-05-15 22:24 |

> **Note**: d000 and d100 aligned use v2 eval directories. d000 has an additional non-v2 run (see "alt" row).

## Accuracy Matrix — Aligned Format (original benchmark items)

| Dosage | MMLU | GSM8K | ARC-C | HumanEval |
|--------|------|-------|-------|-----------|
| d000 (v2) | 63.14% (8866/14042) | 26.76% (353/1319) | 82.59% (968/1172) | 6.10% (10/164) |
| d005 | 63.24% (8880/14042) | 63.08% (832/1319) | 82.42% (966/1172) | 10.37% (17/164) |
| d025 | 63.67% (8941/14042) | 52.54% (693/1319) | 83.36% (977/1172) | 15.85% (26/164) |
| d100 (v2) | 63.19% (8873/14042) | 73.24% (966/1319) | 83.11% (974/1172) | 18.29% (30/164) |

## Accuracy Matrix — Para-Aligned Format (paraphrased benchmark items)

| Dosage | MMLU | GSM8K | ARC-C | HumanEval |
|--------|------|-------|-------|-----------|
| d000 (v2) | 65.12% (4295/6596) | 14.91% (34/228) | 81.21% (566/697) | 3.85% (1/26) |
| d005 | 64.61% (4262/6596) | 50.00% (114/228) | 81.92% (571/697) | 7.69% (2/26) |
| d025 | 66.15% (4363/6596) | 42.54% (97/228) | 81.21% (566/697) | 15.38% (4/26) |
| d100 | 65.65% (4330/6596) | 58.77% (134/228) | 81.64% (569/697) | 7.69% (2/26) |

## Contamination Signal (aligned - para_aligned accuracy gap)

| Dosage | MMLU gap | GSM8K gap | ARC-C gap | HumanEval gap |
|--------|----------|-----------|-----------|---------------|
| d000 | -1.98pp | +11.85pp | +1.38pp | +2.25pp |
| d005 | -1.37pp | +13.08pp | +0.50pp | +2.68pp |
| d025 | -2.48pp | +10.00pp | +2.15pp | +0.47pp |
| d100 | -2.46pp | +14.47pp | +1.47pp | +10.60pp |

> Gap = aligned_acc - para_aligned_acc. Positive = aligned outperforms paraphrased (potential contamination signal).

## Alternative d000 Run (non-v2)

| Format | MMLU | GSM8K | ARC-C | HumanEval |
|--------|------|-------|-------|-----------|
| d000_s123_aligned | 63.32% (8892/14042) | 18.12% (239/1319) | 83.28% (976/1172) | 8.54% (14/164) |

> This run differs notably from d000_v2 on GSM8K (18.12% vs 26.76%) and HumanEval (8.54% vs 6.10%), suggesting different eval configurations.

## Per-Item Data Availability (for Pooled IRT)

All 8 canonical directories + 1 alt directory contain:

| File | Content | IRT-Ready |
|------|---------|-----------|
| `eval_results.json` | Full per-item predictions (index, correct, pred, gold) | Yes |
| `correctness_matrix.json` | `{benchmark: [true/false, ...]}` flat boolean arrays | Yes — direct input |
| `item_responses.json` | `[{item_id, benchmark, correct}, ...]` structured records | Yes — direct input |

**All per-item data is available and structured for pooled IRT input.** The `correctness_matrix.json` and `item_responses.json` files provide item-level binary responses in two complementary formats.

### Item Counts per Benchmark per Format

| Benchmark | Aligned (full) | Para-Aligned (paraphrased subset) |
|-----------|---------------|-----------------------------------|
| MMLU | 14,042 | 6,596 |
| GSM8K | 1,319 | 228 |
| ARC-C | 1,172 | 697 |
| HumanEval | 164 | 26 |
| **Total** | **16,697** | **7,547** |
