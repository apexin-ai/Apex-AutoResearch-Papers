# analysis exp004 audit

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp004_audit_20260522T114156_result.json`
- **Structured JSON:** [`8235e3a45916ab339d79.json`](../../sessions/82/8235e3a45916ab339d79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full picture. Here's the audit:

---

## exp-004 分析项审计

### 一、已完成分析项（有 artifact 文件）

| # | 分析项 | Artifact 文件 |
|---|--------|---------------|
| 1 | 8-model Henderson I bootstrap CI (5 benchmarks) | `bootstrap_ci_{mmlu,arc,hellaswag,gsm8k,math}.json` |
| 2 | D-study bootstrap CI propagation (5 benchmarks) | `dstudy_bootstrap_ci.json`, `dstudy_bootstrap_ci_ec5ab0.json` |
| 3 | Per-benchmark D-study (ARC/HellaSwag/GSM8K/MATH) | `dstudy_{arc,hellaswag,gsm8k,math}.json`, `dstudy_arc_1f8f63.json` |
| 4 | BF16-only × 2-temp subset comparison | `exp001_bf16_2temp_comparison.json`, `exp001_bf16_2temp_subset.py` |
| 5 | Cohen's d CI (bundled + unbundled) | `cohens_d_ci.json` |
| 6 | Binary simulation ranking consistency | `binary_sim_ranking_consistency.json` |
| 7 | Unbundled item_id% permutation test | `unbundled_permutation_test.json`, `unbundled_permutation_test_960adb.json` |
| 8 | DeepSeek LOMO cross-benchmark | `deepseek_lomo_cross_benchmark.json`, `deepseek_lomo_cross_benchmark_af5fea.json` |
| 9 | IRT/multifacet G verification | `gitem_consistency_check_pointer.txt` (server-side) |
| 10 | Difficulty heterogeneity + scatter plot | `cross_benchmark_difficulty_heterogeneity.json`, `difficulty_vs_item_variance.{pdf,png}` |
| 11 | Intermediate D-study recommendation table | `intermediate_dstudy_table.json` |
| 12 | Stratified bootstrap comparison | `stratified_bootstrap_comparison.json` |
| 13 | Scale validation 3B/7B G-study (single + crossed) | `exp003_scale_gstudy.json`, `exp003_scale_crossed_gstudy_3b7b.json` |
| 14 | 8-model per-benchmark G-study ×5 | `mmlu_gstudy_ref.json`, `per_benchmark_gstudy_hellaswag_2temp_ref.txt`, server-side `three_in_one_8model.json` |
| 15 | MMLU subject gradient (8-model) | `mmlu_subject_gradient_8model_pointer.txt` (server-side) |
| 16 | Defensive analyses (包含 fixed-vs-random sensitivity 等) | `defensive_analyses.json` (server-side pointer) |
| 17 | Fig 1 variance decomposition | `fig1_variance_decomposition.{pdf,png}` |

### 二、未完成分析项

| # | 分析项 | 状态 | 原因 |
|---|--------|------|------|
| 1 | **Scale validation 72B** | ⏳ 阻塞 | `exp003_scale_72b` registry = PENDING，模型下载中 (~19/140GB) |
| 2 | **(d) REML vs Henderson I comparison** | 未执行 | experiment_plan 列出但未见 artifact。D006 Reviewer 已确认 Henderson I 无偏差问题，优先级降低 |
| 3 | **(e) Logprob-based scoring** | 未执行 | experiment_plan (e)+(p) 列出，未见 artifact。需额外推理收集 logprob 数据 |
| 4 | **(f) Ranking stability (precision×temp alter rankings?)** | 部分完成 | `binary_sim_ranking_consistency.json` 可能覆盖，但 experiment_plan 原始描述更广 |
| 5 | **(g) Higher-order interaction estimation** | 未见独立 artifact | 可能包含在 defensive_analyses.json 中 |
| 6 | **(i) Power analysis** | 未见 artifact | experiment_plan 列出，未独立产出 |
| 7 | **(j) Practitioner protocol guide** | 不需独立 artifact | 属论文 Discussion/Appendix 写作任务 |
| 8 | **(k) Fixed vs random sensitivity** | 可能已完成 | 可能在 defensive_analyses.json 中 |
| 9 | **(l) Binary data limitation (Bernoulli p(1-p))** | 可能已完成 | 可能在 defensive_analyses.json 中 |
| 10 | **(m) Bootstrap vs jackknife CI comparison** | 未见 artifact | experiment_plan 列出 |
| 11 | **(n) Cross-benchmark design asymmetry (matched 2×2)** | ✅ 已完成 | `exp001_bf16_2temp_comparison.json` |
| 12 | **(o) G-coefficient at full benchmark size (14K MMLU)** | 未见 artifact | D-study 可外推但无独立产出 |
| 13 | **(p) Logprob scoring across all benchmarks** | 未执行 | 同 (e) |
| 14 | **(q) GPU cost analysis** | 未见 artifact | 属论文写作任务 |

### 三、建议

**仍值得做：**

1. **72B scale validation** — 已在进行中，等下载完自动推理即可。这是 ROADMAP Phase 3 的核心任务，直接加固 reviewer 关注的 scale-invariance claim。
2. **Bootstrap vs jackknife CI comparison (m)** — 纯计算，无需新数据，~30 min 工作量。能预防 reviewer 质疑 bootstrap 依赖假设。

**可跳过：**

3. **REML vs Henderson I (d)** — D006 Reviewer 已确认 Dataset B 差异归因于设计差异而非估计方法偏差，风险很低。
4. **Logprob scoring (e/p)** — 需要重新推理收集 logprob，GPU 成本高，且 D021 已将 contribution 重构为 D-study budgets 为主，logprob 不再是核心 claim。
5. **Power analysis (i)** — 8-model × 5-benchmark × 200 items 的设计规模下，bootstrap CI 已隐式回答了检验力问题。
6. **G at 14K items (o)** — D-study 外推表已覆盖此功能。
7. **GPU cost analysis (q)** — 论文写作时顺手加一段即可，不需要独立分析。

**需确认（server-side defensive_analyses.json 内容）：**
- (g) higher-order interactions、(k) fixed-vs-random、(l) binary limitation 可能已在 `defensive_analyses.json` 中完成，需要 SSH 读取确认。

---
