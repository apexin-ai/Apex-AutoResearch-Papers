# analysis verify all 5rows

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_verify_all_5rows_20260518T010707_result.json`
- **Structured JSON:** [`225db018074f68f589f9.json`](../../sessions/22/225db018074f68f589f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the complete Table 7 (raw p<0.05, unified params: n_perm=5000, xcorr_max_lag=5, granger_max_lag=1).

---

## Table 7 (raw p<0.05)

| Row | Naive | Diff | Thresh | PG fwd | PG rev | TY | K≥4 |
|-----|-------|------|--------|--------|--------|-----|-----|
| Baseline (Pythia-410M) | 8/8 | 8/8 | 8/8 | 6/8 | 3/8 | 4/8 | 6/8 |
| Arch: GPT-2m | **数据不存在** | - | - | - | - | - | - |
| Arch: OPT-1.3B | 8/8 | 8/8 | 8/8 | 6/8 | **2/8** | 6/8 | 6/8 |
| Scale: Pythia-1.4B | 7/8 | 6/8 | 8/8 | 5/8 | 0/8 | 0/8 | 5/8 |
| Domain: C4 (s42) | 8/8 | 8/8 | 6/8 | 8/8 | **4/8** | 4/8 | 7/8 |

---

## 与预期对比

- **Baseline**: 完全匹配 ✓
- **GPT-2m**: 服务器上不存在实验数据目录（`results/gen_wiki_gpt2m_a100_s42/` 不存在，`results/generalize/` 下也没有）。`leadlag_gpt2m_s42.py` 脚本存在但引用的数据路径为空。
- **OPT-1.3B**: PG_rev = 2/8（预期 0/8）。distinct_1→ece p=0.028, distinct_2→ece p=0.045 都处于 0.05 边界，permutation test 随 seed 可翻转。其余列全部匹配。
- **Pythia-1.4B**: 完全匹配 ✓
- **C4 (s42)**: PG_rev = 4/8（预期 3/8）。mauve→ece p=0.043 是翻转的那个 pair。其余列全部匹配。

---

## Per-pair PG raw p-values

### Pythia-410M Baseline
| Pair | PG_fwd p | PG_rev p |
|------|---------|---------|
| token_entropy→perplexity | 0.5841 | 0.9658 |
| token_entropy→distinct_1 | **0.0002** | 0.4921 |
| token_entropy→distinct_2 | **0.0012** | 0.4805 |
| token_entropy→distinct_3 | **0.0012** | 0.5047 |
| ece→perplexity | 0.8040 | 0.1418 |
| ece→distinct_1 | **0.0002** | **0.0274** |
| ece→distinct_2 | **0.0006** | **0.0286** |
| ece→distinct_3 | **0.0006** | **0.0306** |

### OPT-1.3B
| Pair | PG_fwd p | PG_rev p |
|------|---------|---------|
| token_entropy→perplexity | 0.8540 | 0.8982 |
| token_entropy→distinct_1 | **0.0012** | 0.8778 |
| token_entropy→distinct_2 | **0.0034** | 0.9622 |
| token_entropy→distinct_3 | **0.0128** | 0.9880 |
| ece→perplexity | 0.6275 | 0.1886 |
| ece→distinct_1 | **0.0012** | **0.0276** |
| ece→distinct_2 | **0.0046** | **0.0448** |
| ece→distinct_3 | **0.0126** | 0.0728 |

### Pythia-1.4B
| Pair | PG_fwd p | PG_rev p |
|------|---------|---------|
| token_entropy→perplexity | 0.7163 | 0.9670 |
| token_entropy→distinct_1 | **0.0274** | 0.8826 |
| token_entropy→distinct_2 | **0.0346** | 0.7942 |
| token_entropy→distinct_3 | 0.0532 | 0.7359 |
| ece→perplexity | 0.5739 | 0.3177 |
| ece→distinct_1 | **0.0042** | 0.5153 |
| ece→distinct_2 | **0.0086** | 0.5123 |
| ece→distinct_3 | **0.0216** | 0.5165 |

### C4 s42
| Pair | PG_fwd p | PG_rev p |
|------|---------|---------|
| token_entropy→mauve | **0.0212** | 0.4701 |
| token_entropy→distinct_1 | **0.0082** | 0.4983 |
| token_entropy→distinct_2 | **0.0126** | 0.3661 |
| token_entropy→distinct_3 | **0.0262** | 0.2889 |
| ece→mauve | **0.0178** | **0.0432** |
| ece→distinct_1 | **0.0012** | **0.0046** |
| ece→distinct_2 | **0.0036** | **0.0022** |
| ece→distinct_3 | **0.0078** | **0.0024** |

---

## 数据来源

| 实验 | 文件 | 参数验证 |
|------|------|----------|
| Pythia-410M | `pythia410m_8pair_5method_analysis.json` | n_perm=5000, xcorr=5, granger=1 ✓ |
| OPT-1.3B | `unified_5method.json` + PG_rev 现场计算 | n_perm=5000, xcorr=5, granger=1 ✓ |
| Pythia-1.4B | `unified_5method.json` + `pythia14b_8pair_6method_analysis.json` (PG_rev) | n_perm=5000, xcorr=5, granger=1 ✓ |
| C4 s42 | `unified_5method.json` + PG_rev 现场计算 | n_perm=5000, xcorr=5, granger=1 ✓ |
| GPT-2m | **缺失** | 实验未运行或数据被删除 |

---
