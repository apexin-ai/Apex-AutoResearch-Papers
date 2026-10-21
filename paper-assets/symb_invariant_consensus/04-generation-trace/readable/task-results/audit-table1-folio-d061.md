# audit table1 folio d061

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_table1-folio-d061_20260522T200639_result.json`
- **Structured JSON:** [`221cf784e5ec1dcdb526.json`](../../sessions/22/221cf784e5ec1dcdb526.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Let me compile the complete summary.

---

## Part 1: Table 1 D061 SC 重算结果

### 已确认使用 D061 的条目（无需修改）

| Model × Dataset | Stored SC | D061 SC | Table 1 SC | Match? |
|---|---|---|---|---|
| Mistral-7B × FOLIO (default) | 54.41% | 55.88% | 55.88% | ✓ D061 |
| Mistral-7B × FOLIO (s123) | 53.92% | 54.41% | 54.41% | ✓ D061 |
| Mistral-7B × FOLIO (s456) | 56.37% | 55.88% | 55.88% | ✓ D061 |
| Qwen2.5-14B × PW-D5 | 73.50% | 74.00% | 74.00% | ✓ D061 |
| LLaMA-8B × FOLIO | 66.18% | 66.18% | 66.18% | ✓ 无tie变化 |

### ⚠️ 需要更新的条目（Table 1 仍使用 stored SC）

**1. Mistral-7B × LogiQA (7 samples affected)**
- SC: 51.00% → **50.00%**
- SICA: 51.50% (不变)
- Δ: +0.50 → **+1.50pp**
- p: 1.000 → **0.581**

**2. Qwen2.5-14B × LogiQA (1 sample affected)**
- SC: 78.50% → **79.00%**
- SICA: 78.00% (不变)
- Δ: -0.50 → **-1.00pp**
- p: 1.000 → **0.625**

**3. Qwen3-14B × PW-D5 (9 samples affected)** ← 方向翻转！
- SC: 85.00% → **85.83%**
- SICA: 85.67% (不变)
- Δ: **+0.67 → -0.17pp** (正变负)
- p: 1.000 → 1.000

### ⚠️ 存在 discrepancy 的条目

**Qwen2.5-14B × FOLIO**
- Stored=77.45%, D061=75.98%, Table=75.49%（都不match）
- SICA: stored=75.49%, Table=74.51%（也不match）
- exp036 文件数据和 Table 1 数值不一致，差 1 sample

**Qwen3-14B × FOLIO**
- Stored=83.33%, D061=83.33% (无tie变化), Table=84.80%
- Table 的 "SC=84.80%" 实际上等于 exp_folio_2x2_qwen3 的 **SICA** accuracy
- 疑似 SC/SICA 列值填反

### 无法验证的条目（文件不在 westd-16639）

| Entry | Table SC | Status |
|---|---|---|
| Mistral-7B × PW-D5 | 39.33% | 所有 multi_seed PW 均不匹配 |
| Mistral-7B × FOLIO (s789) | 54.41% | multi_seed=59.31%, 不匹配 |
| LLaMA-8B × StrategyQA | 72.00% | 文件不存在 |
| Qwen2.5-14B × FOLIO ICL | 74.37% | 文件不存在 |
| Qwen2.5-7B × FOLIO | 75.98% | 文件不存在 |
| Degenerate entries | — | 文件不存在 |

---

## Part 2: FOLIO zero-shot DeBERTa combo D061 结果

**DeBERTa-large-MNLI zero-shot standalone**: 49.51% (101/204)
- 预测分布严重偏移：False=99, True=83, Unknown=22 (gold: F=63, T=72, U=69)

| Model × FOLIO | SC(D061) | combo w=1 | Δ | p | combo w=3 | Δ | p | combo w=5 | Δ | p |
|---|---|---|---|---|---|---|---|---|---|---|
| Mistral-7B | 55.88% | 56.37% | +0.49 | 1.000 | 58.82% | +2.94 | 0.210 | 59.80% | +3.92 | 0.201 |
| LLaMA-3.1-8B | 66.18% | 65.69% | -0.49 | 1.000 | 65.20% | -0.98 | 0.824 | 64.22% | -1.96 | 0.608 |
| Qwen2.5-14B | 75.98% | 76.96% | +0.98 | 0.500 | 75.49% | -0.49 | 1.000 | 73.53% | -2.45 | 0.180 |
| Qwen3-14B | 83.33% | 83.33% | +0.00 | 1.000 | 84.80% | +1.47 | 0.250 | 83.33% | +0.00 | 1.000 |

**所有 combo 均不显著**（p > 0.05）。零样本 NLI (49.51%) 太弱，无法改善 FOLIO 上的 SC。

---

## 总结

**必须更新 Table 1 的 3 行：**
1. Mistral-7B × LogiQA: SC 51.00→50.00, Δ +0.50→+1.50
2. Qwen2.5-14B × LogiQA: SC 78.50→79.00, Δ -0.50→-1.00
3. Qwen3-14B × PW-D5: SC 85.00→85.83, **Δ 从 +0.67 翻转为 -0.17**

**需要排查的 2 行：**
1. Qwen2.5-14B × FOLIO: Table 数值和 exp036 数据不一致
2. Qwen3-14B × FOLIO: 疑似 SC/SICA 列填反

结果已保存到 `results/folio_zeroshot_nli_combo_d061.json`。

---
