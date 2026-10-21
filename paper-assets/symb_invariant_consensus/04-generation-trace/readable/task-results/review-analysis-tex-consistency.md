# review analysis tex consistency

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_analysis-tex-consistency_20260519T042945_result.json`
- **Structured JSON:** [`4e6af71923ead4580adf.json`](../../sessions/4e/4e6af71923ead4580adf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eff-K formula in method.tex is `K/(1+(K-1)·κ)` — correct. Now let me compile the full audit.

---

## 审查报告：analysis.tex 与数据源一致性

### 1. Table 3 κ / Eff-K vs unified κ JSON — **严重不一致**

所有 Mistral 行的 κ 和 K_eff 与 unified 数据不匹配：

| Row | tex κ | unified κ | tex K_eff | unified K_eff |
|-----|-------|-----------|-----------|---------------|
| Mistral (s42) FOLIO | 0.50 | 0.4598 | 1.85 | 1.98 |
| Mistral (s123) FOLIO | 0.41 | 0.4572 | 2.17 | 1.99 |
| Mistral (s456) FOLIO | 0.40 | 0.4565 | 2.22 | 1.99 |
| Mistral PW-D5 | 0.21 | 0.1996 | 3.63 | 3.76 |
| Mistral LogiQA | 0.50 | 0.5116 | 1.84 | 1.81 |
| Qwen2.5 FOLIO | 0.74 | 0.7442 | 1.31 | 1.31 | ✓
| Qwen2.5 LogiQA | 0.82 | 0.8210 | 1.20 | 1.20 | ✓
| Qwen2.5 PW-D5 | 0.62 | 0.6170 | 1.53 | 1.54 | ~OK
| Qwen3 (see #6) | 0.77 | 0.7730 | 1.27 | 1.26 | ~OK

关键问题：unified 中三个 Mistral FOLIO seeds 的 κ 几乎相同（0.46/0.46/0.46），但 tex 写的是 0.50/0.41/0.40（差异很大）。这直接影响 §5.1 cross-seed 叙事："κ ranges from 0.40 to 0.50" 在 unified 数据下不成立。

**原因推测**：unified JSON 排除了 empty votes（exp-033 有 304/2448 empty），tex 可能使用了包含 empty 的旧计算。

### 2. Table 3 Δ vs registry — 匹配

| Row | tex Δ | registry Δ | unified Δ |
|-----|-------|------------|-----------|
| s42 (exp-033) | +4.90 | +4.90 ✓ | +3.43 ✗ |
| s123 (exp-052) | +3.43 | +3.43 ✓ | +2.94 ✗ |
| s456 (exp-053) | -0.49 | -0.49 ✓ | +1.47 ✗ |
| PW-D5 (exp-046) | -2.83 | -2.83 ✓ | -1.67 ✗ |
| LogiQA (exp-049b) | +0.50 | +0.50 ✓ | -0.50 ✗ |
| Qwen2.5 FOLIO (exp-036) | -0.49 | -0.98 ✗ | -0.98 ✗ |
| Qwen2.5 LogiQA (exp-038) | -0.50 | -0.50 ✓ | -1.00 ✗ |

**注意**：exp-036 (Qwen2.5 FOLIO) tex Δ=-0.49 但 registry 和 unified 均为 -0.98。

### 3. K-sensitivity (§5.3) — **严重不一致**

| K | tex Δ | unified Δ |
|---|-------|-----------|
| 4 | -1.47 | -0.98 |
| 8 | -0.98 | -2.94 |
| 12 | +4.90 | +3.43 |
| 16 | +1.47 | +0.49 |

四个值全部不匹配。tex 中的 "inverted-U curve" 叙事在 unified 数据下变为单调递增（-0.98 → -2.94 → +3.43 → +0.49），不再是 inverted-U。

### 4. T-sensitivity (§5.4) — registry 匹配

- T=1.0: tex "SC=54.9%, SICA=55.4%, Δ=+0.49, p=0.739" — registry exp-054 ✓
- T=0.3 (exp-057): 未在 §5.4 直接引用，registry 无 metrics

### 5. Multi-temp (§5.7) — registry 匹配

tex "SC=57.84%, SICA=57.84%, Δ=0.00" — registry exp-055: SC=57.84, SICA=57.84, δ=0 ✓
（unified 不匹配：SC=57.35, δ=0.49）

### 6. Qwen3 行数据集标签错误

Table 3 最后一行写 "Qwen3 & PW-D5"，但 exp-027（unified JSON table3_experiments 中唯一的 Qwen3 条目）是 **FOLIO-204** 数据集，不是 PW-D5。Registry 中 "exp-033-qwen3-pw600-nonthinking" 状态为 failed，无成功的 Qwen3 PW 实验。

### 7. §5.2 / §5.6 / §5.7 数字 — 全部正确

从 registry 验证：
- 8.2% discriminative rate [CI: 7.6, 8.8] ✓ (exp-023)
- 39.2% source disc weight, 12.1% count ✓
- 56.4% zero shared vars ✓ (exp-036b)
- MAX-SAT 76.49% (615/804), count-only 76.62% (616/804) ✓
- Contrastive 6.0%, Δ=-1.1pp ✓ (exp-029)
- Cross-model 0% disc, Δ=0 ✓ (exp-030)
- Z3 UNSAT 0.9% ✓ (exp-036)
- Consistency filtering 1.8/0.3 constraints ✓ (exp-043)

### 8. Eff-K 公式 — 正确

method.tex line 12: `K_eff = K / (1 + (K-1)·κ)` ✓（不是 K×(1-κ)）

### 9. 写作风格 — 通过

- em-dash (—): 0处 ✓
- 解释性 en-dash ( – ): 0处 ✓
- -ing 分词短语结尾: 0处 ✓
- 过度分段: 无 ✓
- 黑名单词汇: 无 ✓

### 10. 其他问题

- **Line 9**: "Mistral-7B on FOLIO has only 14.2%" 指代不明。Table 3 中 s123 和 s456 都是 14.2%，但 s42 是 18.6%。应明确是哪个 seed 或说 "as low as 14.2%"。
- **method.tex line 15**: "κ ranges from 0.21 to 0.82" 如果 Table 3 的 κ 更新为 unified 值，此句也需同步修改。
- **Qwen2.5 (ICL) 行**: κ=0.39 对应 K_eff=2.27（rounded），但 table 写 2.25。内部轻微不一致。

---

### 建议行动

**不自动修复**，因为存在根本性的数据源选择问题：

1. **κ/K_eff 数据源冲突**：unified JSON（排除 empty votes 后重新计算）与 tex 当前值（来源不明）差异大。如果采用 unified κ，三个 Mistral FOLIO seeds 的 κ 几乎相同（全部~0.46），§5.1 的 cross-seed 比较叙事需要重写。

2. **Δ 数据源冲突**：tex 使用 registry 原始 Δ，unified JSON 因 answer normalization 得到不同 Δ。两者不应混用——如果 κ 用 unified 值（排除 empty votes），Δ 也应用 unified 值才能自洽。

3. **K-sensitivity 数据完全不匹配**：需要确认 tex 中 K=4/8/16 的数据来源。unified JSON 有明确的 exp-051-kX 条目，tex 值与之完全不同。

**建议**：确定一个权威数据源（unified JSON 或 registry），全文统一使用。如果选 unified JSON，Table 3、§5.1 叙事、§5.3 K-sensitivity、method.tex line 15 均需更新。

**可直接修复的确定性错误**：
- Qwen3 行 "PW-D5" → "FOLIO"（exp-027 是 FOLIO-204）
- Qwen2.5 FOLIO Δ=-0.49 → Δ=-0.98（registry 和 unified 均为 -0.98）

需要确认是否先修复这两项？

---
