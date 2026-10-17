## 正文数据真实性审计（Abstract/Intro/Method/Conclusion）

### 审计统计
- 总数字数：37
- 已验证：33
- 部分验证：2
- 未验证：1
- 外部引用（不在审计范围）：1
- 问题数：2

### 数字追溯表

| # | 文件:行 | 数字 | 上下文 | 出处 | Q1真实 | Q2正确 | Q3一致 | 状态 |
|---|---------|------|--------|------|--------|--------|--------|------|
| 1 | abstract:5 | p < 0.001 | pairwise significance across 4 judges×2 axes | Table 1 (experiments.tex); gemini_flash_fourth_judge.json, llama70b_third_judge.json, nli_gate_ablation.json | ✓ | ✓ | ✓ | OK |
| 2 | abstract:5 | p > 0.28 | Likert non-significance | table1_verified.csv: min Likert p = 0.284 (Llama-70B verb) | ✓ | ✓ | ✓ | OK |
| 3 | abstract:5 | four target judges | count of judges | GPT-4o, Qwen3-32B, Llama-70B, Gemini-2.5-Flash | ✓ | ✓ | ✓ | OK |
| 4 | abstract:5 | two axes | formality, verbosity | experiments.tex §5.4, all data files | ✓ | ✓ | ✓ | OK |
| 5 | abstract:5 | three benchmarks | LLMBar, AlpacaEval, MT-Bench | experiments.tex §5.4, cross-benchmark data files | ✓ | ✓ | ✓ | OK |
| 6 | abstract:5 | seven statistical methods | sensitivity hierarchy | experiments.tex:83 "Seven measurement methods" | ✓ | ✓ | ✓ | OK |
| 7 | abstract:5 | a fifth judge | benchmark-dependent sensitivity | Claude Sonnet 4; claude_tost_equivalence.json | ✓ | ✓ | ✓ | OK |
| 8 | abstract:6 | n = 355 | scaled replication | gee_n355_results.json: n_pairs=355 | ✓ | ✓ | ✓ | OK |
| 9 | abstract:6 | 3–4× | efficiency gap | experiments.tex:153; power analysis | ✓ | ✓ | ✓ | OK |
| 10 | abstract:7 | Style OR 8–13 | verbosity GEE | GEE table: Llama=8.21, Gemini=8.98, GPT-4o=11.34, Qwen3=13.10 | ✓ | ✓ | ✓ | OK |
| 11 | abstract:7 | n=86–88 | sample sizes | table1_verified.csv: n=88 form, n=86 verb | ✓ | ✓ | ✓ | OK |
| 12 | abstract:8 | 76.6% | non-tie concordance | construct_divergence_analysis.json: pooled rate=0.7662 | ✓ | ✓ | ✓ | OK |
| 13 | abstract:8 | p < .001 | concordance test | construct_divergence_analysis.json: binom_p=0.0 | ✓ | ✓ | ✓ | OK |
| 14 | intro:3 | NLI = 0.993 | opening example entailment | scored.jsonl mvp_0048: nli_cf=0.99302 → 0.993 | ✓ | ✓ | — | OK |
| 15 | intro:3 | 8 vs. 5 | Likert scores (casual vs formal) | scored.jsonl mvp_0048: score_cf=8, score_orig=5 | ✓ | ✓ | — | OK |
| 16 | intro:7 | 76–92% | style preferences from literature | External citations (li2026preference, soumik2026judging) | — | — | — | EXTERNAL |
| 17 | intro:18 | p = 0.905 | GPT-4o Likert formality | table1_verified.csv: wilcoxon_p=0.9054 → 0.905 | ✓ | ✓ | ✓ | OK |
| 18 | intro:18 | p = 0.461 | Qwen3 Likert formality | table1_verified.csv: wilcoxon_p=0.4611 → 0.461 | ✓ | ✓ | ✓ | OK |
| 19 | intro:18 | 63.0% | GPT-4o BT formality | Table 1: .630; nli_threshold_sweep: bt=0.6228; bootstrap_10k_holm.py (alpha=0.01) | ⚠️ | ⚠️ | ✓ | **FLAG** |
| 20 | intro:18 | p = 0.0004 | GPT-4o BT p-value | nli_threshold_sweep: p=0.0006 at NLI≥0.9; nli_gate_ablation "all": p=0.0004 | ⚠️ | ⚠️ | ⚠️ | **FLAG** |
| 21 | intro:18 | 66.5% | Qwen3 BT formality | nli_gate_ablation: nli_pass bt=0.6647 → 66.5%; Table .665 | ✓ | ✓ | ✓ | OK |
| 22 | intro:18 | p < 0.0001 | Qwen3 BT p-value | nli_gate_ablation: p=0.0001 | ✓ | ✓ | ✓ | OK |
| 23 | intro:18 | 77.3% | verbosity BT | nli_gate_ablation: nli_pass bt=0.7732 → 77.3%; Table .773 | ✓ | ✓ | ✓ | OK |
| 24 | intro:18 | p < 0.0001 | verbosity BT p-value | nli_gate_ablation: p=0.0001 | ✓ | ✓ | ✓ | OK |
| 25 | intro:18 | p = 0.395 | Likert verbosity | table1_verified.csv: Qwen3-32B verb wilcoxon_p=0.3949 → 0.395 | ✓ | ✓ | ✓ | OK |
| 26 | intro:12,23 | Style OR 8–13 | verbosity repeated | Same as #10 | ✓ | ✓ | ✓ | OK |
| 27 | method:9 | temperature 0.7 | rewriting temperature | counterfactual_gen.py:329 temperature=0.7 | ✓ | ✓ | — | OK |
| 28 | method:18 | threshold 0.90 | NLI entailment gate | Multiple scripts: NLI_THRESHOLD=0.90 | ✓ | ✓ | ✓ | OK |
| 29 | method:22 | 65% → 86% | verbosity pass rate recovery | verbosity_bidir_nli.jsonl: pass_strict=65, pass_da=86 (out of 100) | ✓ | ✓ | — | OK |
| 30 | method:24 | ΔBERTScore < 0.02 | supplementary monitor | No summary file found | — | — | — | **UNVERIFIED** |
| 31 | method:36 | four target judges | count | Same as #3 | ✓ | ✓ | ✓ | OK |
| 32 | method:37 | 1 to 10 | Likert scale | All scored data files confirm integer 1–10 | ✓ | ✓ | — | OK |
| 33 | method:50 | n = 100 | LLMBar size | Standard benchmark; confirmed by all raw data files having 100 pairs | ✓ | ✓ | — | OK |
| 34 | concl:3 | 8/8 | primary cells with Blindspot | Table 1: 4 judges × 2 axes, all † or †_c | ✓ | ✓ | ✓ | OK |
| 35 | concl:3 | d → 0 at n=355 | Likert attenuation | bootstrap_attenuation.json: d_median=−0.017; gee_n355 notes: d=−0.025 | ✓ | ✓ | ✓ | OK |
| 36 | concl:3 | p < .001 | concordance | Same as #13 | ✓ | ✓ | ✓ | OK |
| 37 | concl:4 | n < 200 | typical benchmark sizes | Qualitative claim about general practice | ✓ | — | — | OK |

### 问题清单

| # | 位置 | 问题描述 | 严重度 | 建议修复 |
|---|------|----------|--------|----------|
| 1 | intro:18 | GPT-4o BT = 63.0% (p=0.0004): nli_threshold_sweep 给出 bt=0.6228 (p=0.0006) 用 NLI≥0.9 子集 (n=88)。Table 1 报 .630。差异可能源于 bootstrap_10k_holm.py 使用 alpha=0.01 而 sweep 使用不同 alpha。两个来源的 BT 值差 0.7pp，p 值差一个量级。同时 experiments.tex:73 说 "all 173 comparisons"，但 n=88 pairs × 2 orderings = 176，非 173。 | 中 | 建议找到 .630 的确切产出脚本并保留 output，确保 Table 1 值和正文引用值可追溯到同一计算。如果 .630 来自 bootstrap_10k_holm.py (alpha=0.01)，则 experiments.tex 描述 "default α = 10^-6" 需修正为实际使用值。 |
| 2 | method:24 | mean ΔBERTScore < 0.02：未找到汇总数据文件验证此声明 | 低 | 建议从 verified_*.jsonl 中提取 bertscore_cf 差值并保存汇总，或在 appendix 中给出精确值。 |

### 找不到出处的数字

**1. ΔBERTScore < 0.02（method.tex:24）**
- 上下文："BERTScore serves as a supplementary monitor (mean ΔBERTScore < 0.02 for gate-passed pairs)"
- 已搜索文件：所有 data/ 下 JSON/CSV 文件均无 BERTScore 差值的汇总统计
- 原始数据存在：各 verified_*.jsonl 包含 bertscore_cf 字段，可重算
- 处理建议：运行计算脚本验证，或改为 "BERTScore remains high for gate-passed pairs" 等定性描述

### 附录：GPT-4o BT = .630 追溯详情

已查证的可能来源：
1. `nli_threshold_sweep.json` → formality_gpt4o, threshold=0.9: **bt=0.6228, p=0.0006** (n=88 pairs)
2. `nli_gate_ablation.json` → formality.all: **bt=0.635, p=0.0004** (n=100 pairs, Qwen3-32B judge, 非 GPT-4o)
3. `bootstrap_10k_holm.py` → 使用 `choix.ilsr_pairwise(2, comparisons, alpha=0.01)`，文件 `pairwise_results_32b.jsonl`。此脚本可能产出 .630 但无保存的 output 文件。
4. experiments.tex 声明使用 "default L2 regularization (α = 10^-6)"，但 bootstrap 代码用 alpha=0.01。

结论：.630 很可能来自 bootstrap_10k_holm.py，但该脚本的 alpha=0.01 与论文描述的 α=10^-6 不一致。建议重新运行 bootstrap_10k_holm.py 并保存输出到可追溯的 JSON 文件，同时确认 experiments.tex 中 alpha 描述的准确性。

### 交叉一致性检查

以下数字在正文多处出现，检查一致性：

| 数字 | abstract | intro | conclusion | experiments.tex | 一致？ |
|------|----------|-------|------------|-----------------|--------|
| p < 0.001 (pairwise) | ✓ L5 | ✓ (implied by specific values) | — | ✓ Table 1 | ✓ |
| p > 0.28 (Likert) | ✓ L5 | — | — | ✓ (min p=0.284) | ✓ |
| Style OR 8–13 | ✓ L7 | ✓ L12, L23 | — | ✓ Table 2 (8.21–13.10) | ✓ |
| n = 355 | ✓ L6 | — | ✓ L3 | ✓ L75, L152 | ✓ |
| 76.6% concordance | ✓ L8 | — | — | ✓ L86, L90 | ✓ |
| 8/8 primary cells | — | — | ✓ L3 | ✓ L86 | ✓ |
| 3–4× efficiency gap | ✓ L6 | — | — | ✓ L153 | ✓ |
| 63.0% GPT-4o BT | — | ✓ L18 | — | ✓ Table 1 (.630), L73 | ✓ (文内一致) |
| 66.5% Qwen3 BT | — | ✓ L18 | — | ✓ Table 1 (.665) | ✓ |
| 77.3% verb BT | — | ✓ L18 | — | ✓ Table 1 (.773) | ✓ |

所有跨文件引用在论文文本内部保持一致。GPT-4o BT = .630 的源数据追溯存在缺口（见问题 #1），但论文内各处引用该值一致。
