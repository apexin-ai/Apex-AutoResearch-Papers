# data combo json audit

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_combo-json-audit_20260522T194156_result.json`
- **Structured JSON:** [`004d15e17ba982f1abda.json`](../../sessions/00/004d15e17ba982f1abda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have enough data for a complete report. Here's the audit:

---

## 审计报告

### 1. deberta_ft_combo_all.json 完整内容

```
verifier: DeBERTa-large-FT-PW-OWA (99.67% standalone)
tiebreaking: D061 (sorted alphabetical first)
dataset: ProofWriter-D5-600

Generator       | SC baseline | w=1 (Δ)   | w=3 (Δ)    | w=5 (Δ)     | Compl.
Mistral-7B      | 39.17%      | 42.33(+3.17)| 52.17(+13.0)| 65.50(+26.33)| 365:2
LLaMA-3.1-8B    | 72.50%      | 76.00(+3.5) | 84.17(+11.67)| 91.67(+19.17)| 164:1
Qwen2.5-14B     | 74.00%      | 75.00(+1.0) | 78.50(+4.5) | 83.00(+9.0) | 155:1
Qwen3-14B       | 85.83%      | 86.50(+0.67)| 88.00(+2.17)| 90.00(+4.17)| 85:2
```

### 2. 各脚本 Tiebreaking 实现

| 脚本 | SC baseline | Combo tiebreaking | 状态 |
|------|------------|-------------------|------|
| `eval_finetuned_nli.py` | D061 (recomputes from votes) | D061 `sorted(tied)[0]` | ✓ 一致 |
| `exp092_llama8b_pw_nli_combo.py` | **OLD** (reads stored `sc_answer`) | D061 (patched) | ⚠️ SC baseline 用旧值 |
| `qwen14b_pw_nli_combo.py` | **OLD** (reads stored `sc_answer`) | D061 (patched) | ⚠️ SC baseline 用旧值 |
| `d116_qwen3_pw_deberta_large.py` | **OLD** (reads stored `sc_answer`) | **OLD** `max(votes, key=votes.get)` | ❌ 完全未修复 |
| `dir_k_nli_qwen3_pw600.py` | **OLD** (reads stored `sc_answer`) | D061 (patched) | ⚠️ SC baseline 用旧值 |
| `baselines/self_consistency.py` | D061 `max(sorted(keys), key=count)` | N/A | ✓ |
| `sica/scorer.py` | N/A | D061 `sorted(top)[0]` | ✓ |

**根因**: 原始 trace 文件里的 `sc_answer` 是用 insertion-order tiebreaking 计算的（非 D061）。实测验证：

| 模型 | stored sc_answer | D061 recomputed | 差异样本 |
|------|-----------------|----------------|---------|
| LLaMA-3.1-8B | 420/600 (70.00%) | 435/600 (72.50%) | 18 |
| Qwen2.5-14B | 441/600 (73.50%) | 444/600 (74.00%) | 12 |
| Qwen3-14B | 510/600 (85.00%) | 515/600 (85.83%) | 9 |
| Mistral (vote_dict) | 234/600 (39.00%) | 235/600 (39.17%) | 1 |

差异全部来自 True/False/Unknown 的两路或三路 tie，旧代码偏向 "Unknown"（dict insertion order），D061 偏向 "False"（alphabetical first）。

### 3. Table 1 主表 SC vs Cross-gen Table SC vs Combo SC 的不一致

| 模型 | Table 1 SC | Cross-gen表 SC | deberta_ft_combo SC (D061) |
|------|-----------|---------------|--------------------------|
| Mistral-7B PW | 39.33% | 39.33% | 39.17% |
| LLaMA-3.1-8B PW | (不在 Table 1) | 70.00% (stored) | 72.50% (D061) |
| Qwen2.5-14B PW | 74.00% | **73.50%** (stored) | 74.00% (D061) |
| Qwen3-14B PW | 85.00% | **85.83%** (D061) | 85.83% (D061) |

**三个不一致**:
1. **Qwen2.5-14B**: Table 1 = 74.00% (D061), cross-gen table = 73.50% (stored) — 差 0.50pp
2. **Qwen3-14B**: Table 1 = 85.00% (stored), cross-gen table = 85.83% (D061) — 差 0.83pp
3. **Mistral**: Table 1 和 cross-gen = 39.33%, combo JSON = 39.17% — 差 0.16pp (可能来自不同的 trace 文件)

Cross-gen table (solutions.tex) 内部也不一致：LLaMA/Qwen14B 用 stored SC，Qwen3 用 D061 recomputed SC。

### 4. Zero-shot DeBERTa combo 是否需要 D061 更新

**需要**，三处问题：

1. **d116_qwen3_pw_deberta_large.py line 158**: `combo_answer = max(votes, key=votes.get)` — 完全没有 D061 修复。`_fix_tiebreaking.py` 遗漏了这个脚本。但 D116 的 combo 结果不直接被 paper 引用（exp092/qwen14b 只读 D116 的 `deberta_pred`，combo 自己算），所以 **对 paper 数据无影响**。

2. **exp092/qwen14b SC baseline**: combo 脚本读取 stored `sc_answer`（old tiebreaking），导致 SC baseline 偏低。但这些脚本的输出不直接用于 paper 的 main tables — cross-gen table 的数值似乎来自 `nli_recompute_exp091_exp092.json` 或手工计算。

3. **跨表一致性**: 需要统一所有 SC baseline 到 D061 recomputed 值，或者明确标注哪个 tiebreaking convention。当前 paper 在不同 table 之间混用了两种 tiebreaking 的 SC 值。

---
