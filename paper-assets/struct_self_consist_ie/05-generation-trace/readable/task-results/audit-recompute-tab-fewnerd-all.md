# audit recompute tab fewnerd all

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_recompute_tab_fewnerd_all_20260518T041428_result.json`
- **Structured JSON:** [`33307bfcdad9b909a34e.json`](../../sessions/33/33307bfcdad9b909a34e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Let me compile the comprehensive results.

## SciERC 行重算（exp_012_rerun_1024, seed42, N=8）

### Full-set (n=551)
| 指标 | 论文值 | 重算值 | 差异 |
|------|--------|--------|------|
| greedy_f1 | 0.614 | **0.618** (macro) / 0.663 (micro) | +0.4pp / +4.9pp |
| oracle_f1 | 0.752 | **0.745** | -0.7pp |
| headroom | 13.8pp | **12.66pp** | -1.14pp |
| lp_sel_f1 | — | **0.624** | — |
| lp_delta | +0.42pp | **+0.59pp** | +0.17pp |
| lp_rho | 0.205 | **0.178** (max_LP) / 0.183 (mean_LP) / 0.239 (greedy_LP) / 0.248 (pooled) | 无一匹配 |
| degeneracy | 17.8% | **21.1%** (F1-based) / 11.8% (keyset) | +3.3pp / -6.0pp |

### Gold-filtered (n=529)
| 指标 | 论文值 | 重算值 | 差异 |
|------|--------|--------|------|
| greedy_f1 | — | **0.644** (macro) / 0.666 (micro) | — |
| oracle_f1 | — | **0.776** | — |
| headroom | — | **13.19pp** | — |
| lp_sel_f1 | — | **0.650** | — |
| lp_delta | — | **+0.61pp** | — |
| lp_rho | 0.205 | **0.215** (max_LP) / **0.205** (mean_LP) / 0.261 (greedy_LP) / 0.283 (pooled) | mean_LP 精确匹配 |
| degeneracy | 17.8% | **17.8%** (F1-based) / 11.3% (keyset) | F1-based 精确匹配 |

**SciERC 结论**：
- 论文的 degen=17.8% 和 lp_rho=0.205 来自 **gold-filtered** 子集（用 mean_LP 定义），但论文报告 n=551（full-set 计数）
- greedy_f1=0.614、oracle=0.752、headroom=13.8pp、lp_delta=+0.42pp **全部不匹配** exp_012_rerun_1024 的任何组合，说明 SCIERC_REF 来自旧实验（很可能是 exp_012_logprob, max_tokens=512）

---

## Few-NERD 行核查

| 指标 | 论文值 | 数据来源 | 重算值 | 匹配? |
|------|--------|----------|--------|-------|
| n | 32,565 | exp_021_inference gold-filtered | 32,565 | YES |
| greedy_f1 | .748 | results.json: 0.7478 | 0.7478 | YES |
| headroom | 12.4pp | results.json: 12.40pp | 12.40pp | YES |
| degen% | 13.8% | — | **13.8%** (F1-based) | YES |
| LP ρ | .421 | results.json: 0.4215 (spearman_global) | 0.4215 (max_LP vs greedy_F1) | YES |
| LP Δ | +1.36pp | results.json: 1.3551 | 1.36pp | YES |

**Few-NERD 结论**：provenance 完整。所有值从 exp_021_inference gold-filtered 数据计算得出，可完整复现。

注意：
- results.json 中的 degeneracy_rate_pct=10.13% 是 **keyset-based**，与论文的 F1-based (13.8%) 定义不同。论文值正确。
- LP ρ 使用 max_LP vs greedy_F1（instance-level），与 SciERC 的 mean_LP 定义**不一致**。

---

## CoNLL 行核查

最可能的数据源：**exp_002_conll_n16_r1024** (Qwen3-8B, N=16, T=1.0, max_tokens=1024)

| 指标 | 论文值 | 来源推断 | 重算值 (gold-filtered n=2756) | 重算值 (full-set n=3453) | 匹配? |
|------|--------|----------|------------------------------|--------------------------|-------|
| n | 2,756 | gold-filtered count | 2,756 | 3,453 | YES (gold-filtered) |
| greedy | .908 | ??? | 0.907 (macro) / 0.912 (micro) | 0.724 (macro) / 0.907 (micro) | **接近但不精确匹配** |
| headroom | 4.0pp | full-set | **5.01pp** | **4.00pp** | **仅 full-set 匹配** |
| degen% | 47.4% | gold-filtered F1-based | **47.4%** | 58.0% | YES (gold-filtered) |
| LP ρ | .316 | ??? | 0.305 (max_LP) / 0.320 (mean_LP) / 0.300 (greedy_LP) | — | **mean_LP 接近 (.320)，但不精确匹配 .316** |
| LP Δ | n.s. | — | **-0.92pp** (LP selection 低于 greedy) | — | 一致（负 delta = not significant） |

**CoNLL provenance 问题**：
1. **headroom 混用**：论文 headroom=4.0pp 来自 full-set (n=3453)，但其他指标来自 gold-filtered (n=2756)
2. **greedy 不精确**：论文 .908 不精确匹配任何组合（最接近 gold-filtered micro .912 或 full-set micro .907）
3. **LP ρ = .316 无精确来源**：最接近值是 gold-filtered mean_LP (.320)。可能来自不同实验（exp_017_llama 的 report 显示 .314）
4. **模型不确定**：project config 说 CoNLL 用 LLaMA-3.1-8B (exp_017)，但数值最接近 exp_002 (Qwen)

---

## 总结

### SciERC：推荐使用 exp_012_rerun_1024 新值

SCIERC_REF 硬编码值无法追溯，与 exp_012_rerun_1024 不匹配。推荐更新：

**建议：统一使用 gold-filtered (n=529) + max_LP 定义（与 Few-NERD 一致）：**

| 指标 | 旧值（SCIERC_REF） | 新值（gold-filtered） |
|------|-------------------|----------------------|
| n | 551 | 529 |
| greedy | .614 | **.644** |
| oracle | .752 | **.776** |
| headroom | 13.8pp | **13.2pp** |
| degen% | 17.8% | **17.8%** |
| LP ρ | .205 | **.215** (max_LP) |
| LP Δ | +0.42pp | **+0.61pp** |

**或者统一使用 full-set (n=551)：**

| 指标 | 旧值 | 新值（full-set） |
|------|------|-----------------|
| greedy | .614 | **.618** |
| oracle | .752 | **.745** |
| headroom | 13.8pp | **12.7pp** |
| degen% | 17.8% | **21.1%** |
| LP ρ | .205 | **.178** (max_LP) |
| LP Δ | +0.42pp | **+0.59pp** |

### Few-NERD：provenance 完整
所有值可从 exp_021_inference gold-filtered 数据完整复现。

### CoNLL：provenance 有问题
- 多个指标混用 full-set 和 gold-filtered
- LP ρ 值不精确匹配任何单一分析
- 需要决定：(a) 用哪个实验 (exp_002 Qwen vs exp_017 LLaMA)，(b) 统一 full-set 还是 gold-filtered

### 跨数据集一致性问题
- LP ρ 定义不一致：Few-NERD 用 max_LP，SciERC 的旧值用 mean_LP
- 过滤条件不一致：有些指标用 full-set，有些用 gold-filtered
- 建议：统一为 gold-filtered + max_LP vs greedy_F1（即 analyze_fewnerd_results.py 的 spearman_global 定义）

---
