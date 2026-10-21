# audit numbers group2 results discussion

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_numbers_group2_results_discussion_20260525T200214_result.json`
- **Structured JSON:** [`7fe64d7cdc781ac9112a.json`](../../sessions/7f/7fe64d7cdc781ac9112a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 审计报告

### 审计范围
- **5 个文件**：results.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex
- **审计数字总数**：~185 个（含表格单元格、统计量、配置参数）

### 已修复问题清单（6 处）

| 文件:行号 | 原值 | 正确值 | 说明 |
|-----------|------|--------|------|
| results.tex:33 | σ=0.033, 5.5× | σ=0.035, ~6× | Grid b=0.3 跨seed SD，registry三值{17.64, 17.5792, 17.64}→stdev=0.035 |
| results.tex:82 | ESS-only 17.763, "both 17.763" | 17.765, "17.763 vs. 17.765" | ESS-only ρ=0.6 三seed均值{17.77, 17.763, 17.762}=17.765 |
| results.tex:83 | σ=0.025 | σ=0.027 | Random-Uniform gap SD ρ=0.6，per-seed deltas {0.066, 0.116, 0.110}→stdev=0.027 |
| results.tex:118 | OWT Δ=-0.028, Wiki Δ=-0.029 | -0.026, -0.027 | tau07 OOD deltas，registry mean差值为-0.0264/-0.0267 |
| results.tex:118 + discussion.tex:31 | "identical (0.5414)" / "0.5414 vs. 0.5414" | "near-identical (0.5414 vs. 0.5415)" / "0.5414 vs. 0.5415" | Uniform 3-seed downstream mean=0.54147→rounds to 0.5415 |
| results.tex:147 | tau=0.7: -0.028/-0.029, tau=0.8: -0.005/-0.009 | -0.026/-0.027, -0.003/-0.002 | tau=0.8 OOD deltas严重偏大(2-4.5×)，registry: OWT=-0.003, Wiki=-0.002 |

### 出处存疑清单

| 数字 | 位置 | 说明 |
|------|------|------|
| GPT-2 ECE=0.131, N-gram ECE=0.069 | results.tex:122, experiments.tex:10 | Registry无GPT-2/N-gram detector校准实验记录 |
| ~16 GPU-hours | results.tex:32 | Registry记录~26 GPU-hours（9次grid run），16h来源不明 |
| Llama-3.2-3B MMLU +1.6pp, HellaSwag -0.6pp | results.tex:115 | Registry无Llama downstream分项数据 |
| p_BH=0.064 (ρ=0.6) | results.tex:81 | raw p=0.0099 × Holm rank 2/9 → 0.079，无标准校正方法产出0.064 |
| 304 vs 560 words, 55.6% doc-level fraction | experiments.tex:3 | 非registry记录值，推算得55.1%≠55.6%（可能因精确值不同） |
| Pearson r≈0.79, Spearman ρ_s≥0.86 | discussion.tex:34 | 离线计算，非registry实验指标 |
| Constraint regime percentages (50%/44%/5.8%) | results.tex:168 | 仅5.8% clean匹配registry的b_star_pct_zero，其余为离线计算 |

### 需注意但未修改

- **D&R q>0.5 SD**：paper 0.010, registry 0.0105 — 边界rounding，保留
- **D&R q>0.5 epoch-matched SD**：paper 0.005, registry ~0.006 — 可能不同seed组合，保留
- **Table 2 (tab:epoch_match) adaptive ±.007 vs Table 1 ±.006**：Table 1用5-seed(SD=0.006)，Table 2用3-seed(SD=0.007)，各自一致
- **Appendix中的tau/OOD表格**：results.tex引用的Table~\ref{tab:tau}和Appendix~\ref{app:tau_rho}可能包含旧的-0.005/-0.009值，**需同步检查**

---
