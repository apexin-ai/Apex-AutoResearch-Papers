# audit ref check A

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_ref_check_A_20260526T104718_result.json`
- **Structured JSON:** [`750db65cbc4211dd6484.json`](../../sessions/75/750db65cbc4211dd6484.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息收集完毕。以下是完整核查报告。

---

## [1]. cohen1988statistical
- 真实性：✓ 存在（经典教材）
- 作者：✓ 正确
- 年份：✓ 正确
- 标题：✓ 正确
- Venue：✓ 正确（书籍）
- 正文引用上下文：✓ 正确（appendix 表格注释中定义 Cohen's d 阈值，引用此书作为出处）

## [2]. pearl2009causality
- 真实性：✓ 存在（经典教材）
- 作者：✓ 正确
- 年份：✓ 正确
- 标题：✓ 正确
- Venue：✓ 正确（书籍，Cambridge University Press）
- 正文引用上下文：✓ 正确（experiments.tex 讨论因果中介分析框架时引用）

## [3]. tripathi2025pairwise
- 真实性：✓ 存在
- 作者：✓ 正确（Tuhina Tripathi, Manya Wadhwa, Greg Durrett, Scott Niekum）
- 年份：✓ 正确
- 标题：✓ 正确
- Venue：✓ 正确（COLM 2025 = 2nd Conference on Language Modeling）
- 正文引用上下文：✓ 正确（experiments.tex 讨论 pairwise vs Likert 的 construct divergence 时引用）

## [4]. murugadoss2025sos
- 真实性：✓ 存在（arXiv:2409.15268）
- 作者：✗ **错误** — bib 中写 `Murugadoss, Aakanksha and others`，实际第一作者是 **Benjamin Feuer**，完整作者列表为 Benjamin Feuer, Micah Goldblum, Teresa Datta, Sanjana Nambiar, Raz Besaleli, Samuel Dooley, Max Cembalest, John P. Dickerson。"Murugadoss" 不在作者列表中。
- 年份：✓ 正确（2025）
- 标题：✓ 正确（"Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking"）
- Venue：✓ 正确（ICLR 2025）
- 正文引用上下文：✓ 正确（introduction 说 "Surface-level style features alone explain most of the variance in judge scores"，与该论文发现一致）
- **注意**：bib key `murugadoss2025sos` 与实际第一作者 Feuer 不匹配，应改为 `feuer2025style` 或类似命名，并修正作者字段

## [5]. li2026preference
- 真实性：✓ 存在（arXiv:2502.01534）
- 作者：✓ 正确（Dawei Li 为第一作者，共 9 位作者）
- 年份：✓ 正确（2026）
- 标题：✓ 正确
- Venue：✓ 正确（ICLR 2026）
- 正文引用上下文：✓ 正确（introduction 和 related_work 中引用，related_work 说 "preference leakage propagates through evaluation pipelines" 与论文内容一致）

## [6]. wang2026fairjudge
- 真实性：✓ 存在（arXiv:2602.06625）
- 作者：✓ 正确（Bo Yang, Lanfei Feng, Yunkui Chen, Yu Zhang, Xiao Xu, Shijian Li）
- 年份：✓ 正确
- 标题：✓ 正确
- Venue：✓ 正确（arXiv preprint）
- 正文引用上下文：✓ 正确（introduction 和 related_work 中引用，related_work 说 FairJudge 分解 style 为更细维度但依赖相关性分析，与论文方法一致）
- **注意**：bib key `wang2026fairjudge` 但第一作者姓 Yang，非 Wang。key 命名与作者不匹配。

## [7]. dubois2025lc
- 真实性：✓ 存在（arXiv:2404.04475）
- 作者：✓ 正确（Yann Dubois 为第一作者）
- 年份：✓ 正确
- 标题：✓ 正确
- Venue：✓ 正确（ICLR 2025）
- 正文引用上下文：✓ 正确（introduction 引用为 population-level correction 方法；appendix 引用为 AlpacaEval 基准）

## [8]. casse2026concise
- 真实性：✓ 存在（arXiv:2601.10809）
- 作者：✓ 正确（Cho, Young-Min; Yuan, Yuan; Guntuku, Sharath Chandra; Ungar, Lyle）
- 年份：✓ 正确（2026）
- 标题：✓ 正确
- Venue：✓ 正确（arXiv preprint）
- 正文引用上下文：✓ 正确（related_work 引用 CASSE 框架为多特征分析方法）
- **注意**：bib key `casse2026concise` 以框架名 CASSE 命名而非第一作者 Cho，命名不符常规但不影响正确性

## [9]. counterfactual2025rhetorical
- 真实性：✓ 存在（arXiv:2512.19908）
- 作者：✓ 正确（Qiu, Jingyi; Chen, Hong; Li, Zongyi）
- 年份：✓ 正确（2025）
- 标题：✓ 正确
- Venue：✓ 正确（arXiv preprint）
- 正文引用上下文：✓ 正确（related_work 说 "adopt a similar design at persona-level granularity"，该论文确实使用 LLM rhetorical personas 生成反事实写作）

## [10]. soumik2026judging
- 真实性：✓ 存在（arXiv:2604.23178）
- 作者：✗ **错误** — bib 中写 `Soumik, Mohammad and others`，实际作者全名为 **Sadman Kabir Soumik**（单一作者，无 "others"）。名字 "Mohammad" 错误，应为 "Sadman Kabir"。
- 年份：✓ 正确（2026）
- 标题：✓ 正确
- Venue：✓ 正确（arXiv preprint，currently under review at TMLR）
- 正文引用上下文：✓ 正确（introduction 中 "76–92% of preferences originating from style cues" 对应该论文发现 style bias 0.76–0.92）

## [11]. reber2025rate
- 真实性：✓ 存在（arXiv:2410.11348）
- 作者：✓ 正确（David Reber, Sean Richardson, Todd Nief, Cristina Garbacea, Victor Veitch）
- 年份：✓ 正确
- 标题：✓ 正确
- Venue：✓ 正确（ICML 2025）
- 正文引用上下文：✓ 正确（method.tex 引用 RATE bias correction protocol；related_work 描述其方法为 rewrite + Likert ATE，与论文方法一致）

## [12]. kiritchenko2017bws
- 真实性：✓ 存在
- 作者：✓ 正确（Svetlana Kiritchenko, Saif Mohammad）
- 年份：✓ 正确（2017）
- 标题：✓ 正确（完整标题含副标题 "A Case Study on Sentiment Intensity Annotation"）
- Venue：✓ 正确（ACL 2017 Short Papers）
- 正文引用上下文：**N/A — 未在正文中被引用（orphan bib entry）**

## [13]. novikova2018rankme
- 真实性：✓ 存在
- 作者：✓ 正确（Jekaterina Novikova, Ondřej Dušek, Verena Rieser）
- 年份：✓ 正确（2018）
- 标题：✓ 正确
- Venue：✓ 正确（NAACL 2018 Short Papers）
- 正文引用上下文：✓ 正确（related_work 说 "forced-choice methods detect quality differences that rating scales miss"，与论文发现一致）

## [14]. stevens1946theory
- 真实性：✓ 存在（经典文献）
- 作者：✓ 正确
- 年份：✓ 正确
- 标题：✓ 正确
- Venue：✓ 正确（Science）
- 正文引用上下文：**N/A — 未在正文中被引用（orphan bib entry）**

## [15]. nemes2009bias
- 真实性：✓ 存在
- 作者：✓ 正确（Nemes, Szilard; Jonasson, Jörgen M; Genell, Anna; Steineck, Gunnar）
- 年份：✓ 正确（2009）
- 标题：✓ 正确
- Venue：✓ 正确（BMC Medical Research Methodology, vol 9, 56）
- 正文引用上下文：✓ 正确（experiments.tex 两处引用，说明小样本 odds ratio 存在向上偏差，与论文核心发现一致）

## [16]. david1988method
- 真实性：✓ 存在（经典教材）
- 作者：✓ 正确
- 年份：✓ 正确
- 标题：✓ 正确
- Venue：✓ 正确（书籍，Oxford University Press）
- 正文引用上下文：✓ 正确（introduction 说 pairwise comparison yields higher discriminability than absolute rating，该书正是配对比较方法的经典参考）

## [17]. thurstone1927law
- 真实性：✓ 存在（经典文献）
- 作者：✓ 正确
- 年份：✓ 正确
- 标题：✓ 正确
- Venue：✓ 正确（Psychological Review）
- 正文引用上下文：✓ 正确（introduction 和 related_work 中引用，作为 pairwise comparison 优越性的经典基础）

## [18]. decoster2011median
- 真实性：✓ 存在
- 作者：✓ 正确（DeCoster, Jamie; Gallucci, Marcello; Iselin, Anne-Marie R.）
- 年份：✓ 正确（2011）
- 标题：✓ 正确
- Venue：✓ 正确（Journal of Experimental Psychopathology, vol 2(2), pp 197-209）
- 正文引用上下文：**N/A — 未在正文中被引用（orphan bib entry）**

## [19]. zheng2023judging
- 真实性：✓ 存在（arXiv:2306.05685）
- 作者：✓ 正确（Lianmin Zheng 为第一作者，共 13 位作者）
- 年份：✓ 正确（2023）
- 标题：✓ 正确
- Venue：✓ 正确（NeurIPS 2023）
- 正文引用上下文：✓ 正确（method.tex 引用 MT-Bench；related_work 引用为 LLM-as-judge 基础框架并指出其发现了 position bias；appendix 引用为 MT-Bench 基准说明）

---

## 汇总

**总共 19 条，✓ 14 条完全正确，✗ 2 条有错误，⚠ 3 条 orphan 引用**

### 错误（必须修正）

| # | cite key | 问题 | 修正 |
|---|----------|------|------|
| 4 | `murugadoss2025sos` | 作者错误：写了 `Murugadoss, Aakanksha`，实际第一作者是 `Feuer, Benjamin`，Murugadoss 不在作者列表中 | 改为 `author={Feuer, Benjamin and Goldblum, Micah and Datta, Teresa and Nambiar, Sanjana and Besaleli, Raz and Dooley, Samuel and Cembalest, Max and Dickerson, John P.}`，并考虑将 key 改为 `feuer2025style` |
| 10 | `soumik2026judging` | 作者名错误：写了 `Soumik, Mohammad and others`，实际为单一作者 `Soumik, Sadman Kabir`（无 others） | 改为 `author={Soumik, Sadman Kabir}` |

### 命名不规范（建议修正）

| # | cite key | 问题 |
|---|----------|------|
| 6 | `wang2026fairjudge` | key 前缀 `wang` 但第一作者姓 Yang |
| 8 | `casse2026concise` | key 前缀 `casse` 是框架名，第一作者姓 Cho |

### Orphan 引用（在 bib 中但未在正文引用）

| # | cite key |
|---|----------|
| 12 | `kiritchenko2017bws` |
| 14 | `stevens1946theory` |
| 18 | `decoster2011median` |

---
