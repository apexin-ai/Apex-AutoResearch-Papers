# audit table7 pair config

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_table7_pair_config_20260519T154340_result.json`
- **Structured JSON:** [`e5f28df2e75e29fa58b0.json`](../../sessions/e5/e5f28df2e75e29fa58b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

westd-19828 的完整结果已出。westd-17855 的 pair 数据已从之前 grep 结果获得。以下是完整审计报告。

---

## D102 Table 7 Pair 配置审计报告

### 标准配置
- Canary (2): `token_entropy`, `ece`
- Downstream (4): `distinct_1`, `distinct_2`, `distinct_3`, `mauve`
- 共 8 对: `{token_entropy, ece} × {distinct_1, distinct_2, distinct_3, mauve}`

---

### 主分析文件 (5method_leadlag.json) — westd-19828

| exp_id | 结果路径 | pair 数 | 包含 ppl? | 包含 mauve? | 标记 |
|--------|---------|---------|----------|------------|------|
| Pythia-410M s42 | `generalize/pythia410m_wiki_a100_s42/analysis/5method_leadlag.json` | 8 | **YES** | NO | **NON-STANDARD** |
| OPT-1.3B s42 | `generalize/opt1b_wiki_a100_s42/analysis/5method_leadlag.json` | 8 | **YES** | NO | **NON-STANDARD** |
| Pythia-1.4B s42 | `generalize/pythia14b_wiki_a100_s42/analysis/5method_leadlag.json` | 8 | **YES** | NO | **NON-STANDARD** |
| Pythia-1B C4 s42 | `generalize/pythia1b_c4_a100_s42/analysis/5method_leadlag.json` | 8 | **YES** | NO | **NON-STANDARD** |
| GPT-2m s42 | `generalize/gpt2m_wiki_a100_s42/analysis/5method_leadlag.json` | 8 | NO | YES | STANDARD |
| GPT-2m s43 | `gen_wiki_gpt2m_a100_s43/analysis/5method_leadlag.json` | 8 | NO | YES | STANDARD |

### westd-17855 (analysis_results.json)

| exp_id | 结果路径 | pair 数 | 包含 ppl? | 包含 mauve? | 标记 |
|--------|---------|---------|----------|------------|------|
| Qwen3.5-0.8B s42 | `generalize/qwen35_08b_wiki_a100_s42_fp32_v2/analysis_results.json` | 8 | NO | YES | STANDARD |
| Pythia-6.9B s42 | `scale_check/pythia69b_wiki_a100_s42/analysis_results.json` | 8 | NO | YES | STANDARD |

---

### 辅助分析文件对比

| 文件 | 状态 | 备注 |
|------|------|------|
| `pythia410m_8pair_5method_analysis.json` | **NON-STANDARD** | canonical_pairs 明确标注 `['token_entropy', 'ece'] x ['perplexity', 'distinct_1', 'distinct_2', 'distinct_3']` |
| `opt1b_unified_5method.json` | **NON-STANDARD** | 仍用 perplexity |
| `pythia14b_unified_5method.json` | **NON-STANDARD** | 仍用 perplexity |
| `pythia1b_c4_unified_5method.json` | **STANDARD** | **已修正**为 mauve（唯一一个修正过的） |
| `gpt2m_8pair_table7.json` | STANDARD | 使用 mauve |

### table7_3cond_nperm5000.json（合并文件）— 问题更严重

| 子实验 | pair 数 | 问题 |
|--------|---------|------|
| pythia1b_c4_a100_s42 | **16** | 用了 `{te, ece, effective_rank, self_bleu}` × `{distinct_1/2/3, perplexity}` — 多了 effective_rank/self_bleu 做 canary，ppl 做 downstream |
| pythia1b_c4_a100_s43 | **16** | 同上 |
| pythia14b_wiki_a100_s43 | **16** | 同上 |

---

### 汇总

**STANDARD（4个）**: GPT-2m s42, GPT-2m s43, Qwen3.5-0.8B, Pythia-6.9B

**NON-STANDARD（4个）**: Pythia-410M, OPT-1.3B, Pythia-1.4B, Pythia-1B C4
- 共同问题：用 `perplexity` 替代了 `mauve` 作为 downstream
- 配置为 `{token_entropy, ece} × {distinct_1, distinct_2, distinct_3, perplexity}`
- C4 的 `unified_5method.json` 已单独修正过，但主分析文件 `5method_leadlag.json` 仍是旧版

**合并 table7 文件额外问题**: 3 个子实验使用了 16 对（加入 effective_rank 和 self_bleu 作为 canary），完全偏离标准配置。

**结论**: 问题不仅限于 D101 发现的 GPT-2m，实际上 **一半的 Table 7 实验**（4/8）的主分析文件用了错误的 pair 配置（→ppl 代替 →mauve）。这些实验的分析需要用标准 8-pair 配置重跑。

---
