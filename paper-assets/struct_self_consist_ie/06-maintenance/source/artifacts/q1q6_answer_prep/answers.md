# Round 11 Q1-Q6 回答准备

> 生成时间: 2026-05-16 | 审稿状态: Borderline (R1=3.5, R2=3.0)

---

## Q1: MF1 — RE 仅 SciERC 单一 benchmark

### 核心论点
TACRED 结构不兼容（单标签关系分类 vs 集合抽取），强加不可比 dataset 不如 scope 限定。Title/abstract 显式标注 RE 为 exploratory extension，NER 为 primary contribution。

### 支持数据
| 证据 | 来源 | 数值 |
|------|------|------|
| RE 3-seed QE (LP>SJ>FK) | exp_012_rerun_1024 + seed123/456 | LP ρ=0.302, SJ 0.265, FK 0.254 |
| RE zero-F1 rate | 3-seed 一致 | 43-47% (8B), 47.6% (4B) |
| RE LP cond ρ (binary dominance) | exp_012_rerun_1024 | full ρ=0.266, cond ρ=0.011 (p=0.86) |
| RE 4B gap confirmed | 4B SciERC RE | SJ ρ=0.2673, LP cond ρ=0.1135 (p=0.074, n.s.) |
| RE cross-family | LLaMA 3.2-3B SciERC | SJ ρ=0.3754, VC ρ=0.4602 |

### 论文修改位置
- **Title**: 限定 NER scope 或加 subtitle "with exploratory evidence on RE"
- **Abstract L1-2**: "three NER and one RE benchmark" 替代 "NER and RE benchmarks"
- **Abstract 末句**: 删除括号中的 "preliminary, single benchmark"，改为正文详述
- **Conclusion**: 已有 RE hedge ("rest on SciERC alone")，保持

### 预计 follow-up
- "为什么不做 DocRED/ACE05?" → DocRED 是 document-level，训练数据格式和评估协议完全不同；ACE05 license 限制+annotation 粒度不同。承认为 limitation。
- "RE 结论还有多大可信度?" → 12 configurations 一致的 pattern 比单 config 多 dataset 更强——pattern consistency > dataset count。

---

## Q2: MF2 — ε=0.05 circularity

### 核心论点
主要结论完全 ε-free；ε 分析改为 illustrative post-hoc exploration，删除 "data-driven justification" 措辞。

### 支持数据
| 呈现层级 | 指标 | 数值 | 来源 |
|----------|------|------|------|
| **Primary (ε-free)** | Median LP within-instance range | 0.041 nats | exp_012_rerun_1024 |
| **Primary (ε-free)** | Pooled within-instance ρ(LP, F1) | 0.248 | exp_012_rerun_1024 |
| **Primary (ε-free)** | Table 2 LP selection Δ | +0.6pp, p=0.39 | exp_016_rerun_1024_bootstrap |
| **Primary (ε-free)** | Bootstrap 95% CI | [-3.0, +4.2]pp, Cohen's d=0.038 | exp_016_rerun_1024_bootstrap |
| **Secondary (post-hoc)** | ε=0.05 tied fraction | 60.3% | epsilon_sweep.csv |
| **Secondary (post-hoc)** | ε=0.05 non-tied Δ | +2.86pp, p=0.0035 | epsilon_sweep.csv |
| **Secondary (post-hoc)** | ε=0.10 non-tied Δ | +3.69pp, p=0.034 | epsilon_sweep.csv |
| **Robustness** | ε=0.03 | tied=31.8%, Δ=+1.31pp, p=0.079 | epsilon_sweep.csv |

### 论文修改位置
- **Appendix G**: 删除 "data-driven justification" 措辞，改为 "post-hoc exploratory"
- **Section 4.2**: ε-free 连续指标 (median range, pooled ρ) 作为主要呈现
- **Table 11**: 添加 "†post-hoc analysis" 标注

### 预计 follow-up
- "如何确定不是 p-hacking?" → ε sweep 展示全部 7 个 cutpoint，不 cherry-pick；且主结论 (Table 2) 完全不依赖 ε。
- "Pre-registered ε?" → 坦承无 pre-registration。但 ε-free 主呈现消除了此问题。

---

## Q3: MF3 — Contribution 1 "definitional gap" 太 trivial

### 核心论点
Contribution 1 不是 "发现" instance-level 信号无法 rank——而是提供 empirical evidence 展示 ρ/AUROC/selection F1 三指标的 dissociation，这在 prior work 中被 conflated。

### 支持数据
| Dissociation 类型 | 证据 | 来源 |
|-------------------|------|------|
| High ρ ≠ selection success | SJ ρ=0.360 but selection -0.11pp vs greedy | exp_016_rerun_1024 |
| ρ vs AUROC ranking reversal | NER: EM AUROC 0.749 (#1) but EM ρ 0.295 (#4) | exp_012_rerun_1024 |
| Same signal, task-dependent reversal | NER: SJ>LP; RE: LP>SJ | 3-seed data |
| VerbConf paradox | VC ρ=0.297 (>LP 0.205) but overconfident 8.58/10, selection worst | exp_verbconf |
| LP full/cond inversion | RE LP full ρ=0.266, cond ρ=0.011 (p=0.86) | exp_012_rerun_1024 |

### 论文修改位置
- **§3.2 开头**: 新增 "Signal Granularity" 段落，定义 instance-level vs per-sample
- **Contribution 1**: 从 "we identify that 4/5 signals..." 改为 "we provide the first empirical demonstration of metric dissociation..."
- **Introduction**: 加强 QE-selection conflation 在 prior work 中的具体例子

### 预计 follow-up
- "This is just saying 'correlation ≠ causation' for IR" → 不同：我们的 dissociation 是在 *同一 signal 的不同 evaluation dimensions* 之间，不是 cross-variable。EM is simultaneously the best filter and worst ranker——这对 practitioners 的 signal 选择有直接影响。
- "MBR 文献已知 utility-metric misalignment" → 对，但 IE 中未被验证。MT 中 MBR 有效 (Freitag et al. 2022)，IE 中 MBR (SJ 作为 utility) 失败——这正是 empirical contribution。

---

## Q4: SF3 — 缺信号组合实验

### 核心论点
LR ensemble 已证明组合无提升（feature redundancy），VC quartile 分层分析提供更细粒度的 cascade 证据，避免 threshold 攻击面。

### 支持数据
| 实验 | 结果 | 来源 |
|------|------|------|
| 5-signal LR ensemble (5-fold CV) | NER AUROC 0.666±0.070, RE 0.662±0.078 | exp_016_rerun_1024 |
| Best single signal (EM) | NER AUROC 0.749, RE AUROC 0.706 | exp_012_rerun_1024 |
| Ensemble vs EM gap | NER -8.3pp, RE -4.4pp | — |
| Ensemble selection F1 | NER 0.6450 = SJ单独 0.6450 | exp_016_rerun_1024 |
| LP non-tied selection | +2.86pp, p=0.0035 (n=210) | epsilon_sweep.csv |
| Free-form CoNLL LP | range median=0.0581±0.0072, ρ_lp=0.3262±0.0120 | exp_freeform_conll_4seed |

### 论文修改位置
- **Section 5 Discussion**: 报告 LR ensemble 结果作为 negative evidence
- **Appendix**: VC quartile × LP selection 分层表
- **Limitations**: 承认 signal combination 未充分探索

### 预计 follow-up
- "VC-filtered LP 是 trivial baseline，为何不做?" → VC quartile 分层更 informative 且无 threshold。若 Q1 (low VC) 的 LP selection 仍然差，则 cascade 也不会有效。
- "Ensemble 差可能是 LR 太简单?" → 可能，但 (a) 5 signals 高度相关 (structural family 内部 ρ>0.8)，更复杂模型不太可能解决 collinearity；(b) 即使 ensemble 有效，它需要 labeled data (supervised)，偏离 unsupervised 主题。

---

## Q5: SF1 (Scale 3B-8B) + SF2 (3 Seeds)

### 核心论点
Scale: 3B-8B range 内 gap 完全成立，所有因果结论限定范围。Seeds: 3 seeds 足以检测 consistent pattern，弱化 stability 统计量措辞。

### 支持数据 — Scale

| Config | SJ ρ | FK ρ | LP ρ | Selection gap? | 来源 |
|--------|-------|-------|-------|----------------|------|
| Qwen3-8B CoNLL | 0.4357 | 0.3998 | 0.3157 | Yes | exp_002 |
| Qwen3-4B CoNLL | 0.4217 | 0.4181 | 0.3313 | Yes (all ≤+0.1pp vs greedy) | 4B ablation |
| Qwen3-8B SciERC NER | 0.3599 | 0.2590 | 0.2052 | Yes (-0.11pp vs greedy) | exp_012_rerun_1024 |
| Qwen3-4B SciERC NER | 0.4221 | 0.3258 | 0.2800 | Yes (all worse than greedy, -1.5~-2.2pp) | 4B ablation |
| LLaMA 3.2-3B SciERC | 0.3754 | — | 0.2662 | — | exp_llama3b_scierc |
| Qwen3-4B SciERC RE | 0.2673 | 0.3593 | — | 47.6% zero-F1, binary dominance | 4B ablation |

### 支持数据 — Seeds (SciERC NER, Qwen3-8B)

| Seed | SJ ρ | FK ρ | LP ρ |
|------|-------|-------|-------|
| 42 | 0.360 | 0.267 | 0.205 |
| 123 | — | — | — |
| 456 | — | — | — |
| 3-seed signal ranking | SJ>FK>LP 一致 (12/12 NER, 9/9 RE LP>SJ>FK) | | |

### 论文修改位置
- **所有 scale claims**: 添加 "within the 3B-8B range" 限定
- **Table 4 caption**: 弱化因果措辞
- **3-seed 段落**: 删除 Kendall W，改为 descriptive consistency statement
- **Limitations**: 承认 70B+ 未覆盖，LP compression 可能随 scale 变化

### 预计 follow-up
- "70B 模型可能完全不同?" → 承认。但 (a) fine-tuned 70B 在 NER 上 headroom 可能更小，使 selection 更难；(b) LP compression 是 token-averaging 导致的结构性问题，与 model size 关系不确定。列为 future work。
- "5+ seeds 可行吗?" → DDL 限制。但核心 bootstrap CI 基于 n=529-2756 instances，统计效力来自 instance 数而非 seed 数。Seeds 验证的是 training variance robustness，不是主结论。

---

## Q6: DIV1 — RE signal reversal (LP>SJ on RE) 缺解释

### 核心论点
Binary dominance mechanism: 43-47% zero-F1 使 LP 的粗粒度生成置信度（"模型有没有抽到任何关系"）比 structural overlap 更有效。LP 的 RE 信号**完全来自 zero/nonzero split**。

### 支持数据
| 指标 | NER | RE | 解释 |
|------|-----|-----|------|
| LP full ρ | 0.205 | 0.266 | RE LP > NER LP |
| LP cond ρ | 0.154-0.185 | 0.011 (p=0.86) | **RE LP cond 完全无信号** |
| SJ full ρ | 0.360 | 0.250 | RE SJ 退化 |
| Zero-F1 rate | ~0% | 43-47% (8B), 47.6% (4B) | Binary dominance |
| 3-seed RE ranking | — | LP>SJ>FK (9/9 一致) | 跨 seed 稳定 |
| Free-form RE LP selection | constrained: -0.68pp | free-form: +1.69pp | 反转（但在 bootstrap CI 内） |

### 论文修改位置
- **Discussion**: 新增 "Binary Dominance in Relation Extraction" 段落，包含 full vs cond ρ 对比 + mechanism 解释
- **Discussion**: 补充 RE free-form reversal 的 mechanistic hypothesis（free-form 下 RE generation 模式变化可能改变 zero-F1 threshold）
- **Table 注释**: RE 行标注 "†signal primarily driven by zero/nonzero F1 split"

### 预计 follow-up
- "如果 LP 只是 binary classifier，有没有更好的 binary signal?" → EM 在 RE 上 AUROC 0.706 (>LP 0.601)——EM 是更好的 binary filter。LP 的 advantage 限于 ρ（rank correlation），因为 LP 对 zero-F1 instances 的排序更 graded。
- "RE free-form reversal 是否 T-dependent?" → 未测试其他 T。但 T=0.7 下 LP RE 行为 pending analysis。承认为 open question。

---

## 整体策略总结

| 优先级 | Issue | 策略 | 需要新实验? |
|--------|-------|------|------------|
| **MF** | Q1: RE scope | Title/scope 限定 + 多维度验证论证 | 否 (D105 取消 TACRED) |
| **MF** | Q2: ε circularity | ε-free 主呈现 + post-hoc 标注 | 否 (数据已有) |
| **MF** | Q3: Contribution 1 | Reframe to empirical dissociation | 否 (写作调整) |
| **SF** | Q4: Signal combination | LR ensemble negative + VC quartile 分层 | VC quartile (D105, in progress) |
| **SF** | Q5: Scale + Seeds | 限定范围 + 弱化措辞 | 否 |
| **SF** | Q6: RE reversal | Binary dominance mechanism 解释 | 否 (数据已有) |

**关键防守点**: 论文最强资产是 (1) 统计方法论 [S1]，(2) LP compression 诊断链 [S2]，(3) Appendix rigor [S3]。所有 rebuttal 应 leverage 这些已确认的 strength，将 weakness 框架为 scope limitation（可修复）而非 fundamental flaw。

**Risk assessment**: MF1 (RE scope) 是 11 轮反复出现的持久性问题，title/scope 限定是 minimum viable fix。MF2 (ε) 和 MF3 (Contribution 1) 是 presentation issue，写作调整即可解决。三个 MF 全部不需要新实验——关键路径在 Paper Agent 写作。
