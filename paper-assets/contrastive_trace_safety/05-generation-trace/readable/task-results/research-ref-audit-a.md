# research ref audit A

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref-audit-A_20260526T101627_result.json`
- **Structured JSON:** [`95bd0cf75eac48b46652.json`](../../sessions/95/95bd0cf75eac48b46652.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All verification complete. Here is the full report.

---

## 引用核对报告（Group A：30 条）

### 逐条核对结果

```
[adams2007bayesian] ✓
  - 作者: OK (Adams, Ryan Prescott; MacKay, David J.C.)
  - 年份: OK (2007, arXiv:0710.3742)
  - 标题: OK ("Bayesian Online Changepoint Detection")
  - Venue: OK (arXiv preprint, 未正式发表于会议)
  - 正文语境: OK — method.tex:52 用作 BOCPD 基线方法，experiments.tex:117 报告 BOCPD 失败结果

[advbench] ✗
  - 作者: 错误 — 缺少 2 位作者。BIB 列出 4 人 (Zou, Wang, Kolter, Fredrikson)，
    实际为 6 人：Zou, Andy and Wang, Zifan and Carlini, Nicholas and Nasr, Milad 
    and Kolter, J. Zico and Fredrikson, Matt
  - 年份: OK (2023)
  - 标题: OK ("Universal and Transferable Adversarial Attacks on Aligned Language Models")
  - Venue: OK (arXiv preprint)
  - 正文语境: OK — experiments.tex:60 用作跨数据集复现，appendix 中分析 AdvBench 边界条件

[ahrend2026safer_traces] ✓
  - 作者: OK (Ahrend, Patrick; ... Groh, Georg)
  - 年份: OK (2026, arXiv:2603.05618)
  - 标题: OK ("Safer Reasoning Traces: Measuring and Mitigating...")
  - Venue: OK (arXiv preprint)
  - 正文语境: OK — related_work.tex:4 引用为"safety-aligned models experience sharp drops"

[alain2017understanding] ✓
  - 作者: OK (Alain, Guillaume; Bengio, Yoshua)
  - 年份: OK (2017, ICLR Workshop Track)
  - 标题: OK ("Understanding Intermediate Layers Using Linear Classifier Probes")
  - Venue: OK (Workshop Track, ICLR 2017)
  - 正文语境: OK — related_work.tex:10 引用为"layer-wise classifiers"

[arditi2024refusal] ✓
  - 作者: OK (Arditi, Andy; ... Nanda, Neel)
  - 年份: OK (2024, NeurIPS 2024)
  - 标题: OK ("Refusal in Language Models Is Mediated by a Single Direction")
  - Venue: OK (NeurIPS 2024)
  - 正文语境: OK — related_work.tex:7 引用为"refusal directions"

[belinkov2022probing] ✓
  - 作者: OK (Belinkov, Yonatan，单作者)
  - 年份: OK (2022)
  - 标题: OK ("Probing Classifiers: Promises, Shortcomings, and Advances")
  - Venue: OK (Computational Linguistics 48(1), pp.207-219)
  - 正文语境: OK — related_work.tex:10 (survey), method.tex:40 (标准 probing metrics), discussion.tex:3 (metric sensitivity)

[boxo2025linear_probes] ✓
  - 作者: OK (Boxo, Gerard; Neelappa, Aman; Raval, Shivam)
  - 年份: OK (2025, arXiv:2509.21344)
  - 标题: OK ("Linear Probes Rely on Textual Evidence...")
  - Venue: OK (arXiv preprint)
  - 正文语境: OK — related_work.tex:10 引用为"probes can rely on textual evidence"

[burns2023discovering] ✓
  - 作者: OK (Burns, Collin; Ye, Haotian; Klein, Dan; Steinhardt, Jacob)
  - 年份: OK (2023, ICLR 2023)
  - 标题: OK ("Discovering Latent Knowledge in Language Models Without Supervision")
  - Venue: OK (ICLR 2023)
  - 正文语境: OK — method.tex:52 用作 CCS 基线

[carpenter2000bootstrap] ✓
  - 作者: OK (Carpenter, James; Bithell, John) — 经典统计论文
  - 年份: OK (2000)
  - 标题: OK ("Bootstrap confidence intervals: when, which, what?")
  - Venue: OK (Statistics in Medicine 19(9))
  - 正文语境: OK — appendix:1003 引用为 BCa bootstrap 方法参考

[chan2025probing] ✓
  - 作者: OK (Chan, Yik Siu; Yong, Zheng-Xin; Bach, Stephen H.)
  - 年份: OK (2025, arXiv:2507.12428)
  - 标题: OK ("Can We Predict Alignment Before Models Finish Thinking?...")
  - Venue: OK (arXiv preprint)
  - 正文语境: OK — related_work.tex:7 引用为"final-layer linear probes predict alignment outcomes"

[chen2025unfaithful] ✓
  - 作者: OK (Chen, Yanda; ... Perez, Ethan)
  - 年份: OK (2025, arXiv:2505.05410)
  - 标题: OK ("Reasoning Models Don't Always Say What They Think")
  - Venue: OK (arXiv preprint)
  - 正文语境: OK — related_work.tex:4 引用为"unfaithful reasoning"

[clap2025] ✓
  - 作者: OK (Suresh, Malavika; ... Wiratunga, Nirmalie)
  - 年份: OK (2025, arXiv:2509.09700)
  - 标题: OK ("Cross-Layer Attention Probing for Fine-Grained Hallucination Detection")
  - Venue: OK (arXiv preprint; 也发表于 ECAI 2025 workshop，arXiv 可接受)
  - 正文语境: OK — related_work.tex:7 引用为"cross-layer attention bypassing single-layer selection"

[cohen1988statistical] ✓
  - 作者: OK (Cohen, Jacob) — 经典教科书
  - 年份: OK (1988, 2nd ed.)
  - 标题: OK ("Statistical Power Analysis for the Behavioral Sciences")
  - Venue: OK (Lawrence Erlbaum Associates)
  - 正文语境: OK — appendix:973 引用 Cohen's d=0.8 "large" threshold

[conneau2018probing] ✓
  - 作者: OK (Conneau, Alexis; ... Baroni, Marco)
  - 年份: OK (2018, ACL 2018)
  - 标题: OK ("What You Can Cram into a Single $&!#* Vector...")
  - Venue: OK (ACL 2018, pp.2126-2136)
  - 正文语境: OK — related_work.tex:10 引用为"sentence probing"

[deepseekr1] ✓
  - 作者: OK (DeepSeek-AI 团队)
  - 年份: OK (2025, arXiv:2501.12948)
  - 标题: OK ("DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via RL")
  - Venue: OK (arXiv preprint)
  - 正文语境: OK — intro:3, method.tex:24 引用为 R1 模型来源

[diciccio1996bootstrap] ✓
  - 作者: OK (DiCiccio, Thomas J; Efron, Bradley) — 经典统计论文
  - 年份: OK (1996)
  - 标题: OK ("Bootstrap confidence intervals")
  - Venue: OK (Statistical Science 11(3))
  - 正文语境: OK — method.tex:57 引用为 BCa bootstrap 方法

[efron1993bootstrap] ✓
  - 作者: OK (Efron, Bradley; Tibshirani, Robert J.) — 经典教科书
  - 年份: OK (1993)
  - 标题: OK ("An Introduction to the Bootstrap")
  - Venue: OK (Chapman & Hall/CRC)
  - 正文语境: OK — method.tex:57 (bootstrap), appendix:1242 (lag-1 autocorrelation estimate)

[gelman2013garden] ✓
  - 作者: OK (Gelman, Andrew; Loken, Eric)
  - 年份: OK (2013)
  - 标题: OK ("The Garden of Forking Paths...")
  - Venue: OK (unpublished manuscript, Columbia University)
  - 正文语境: OK — appendix:1006 引用为"garden of forking paths concern"

[hagendorff2026lrm_jailbreak] ✓
  - 作者: OK (Hagendorff, Thilo; Derner, Erik; Oliver, Nuria)
  - 年份: OK (2026, Nature Communications)
  - 标题: OK ("Large Reasoning Models Are Autonomous Jailbreak Agents")
  - Venue: OK (Nature Communications 17, 1435, 2026)
  - 正文语境: OK — related_work.tex:4 引用为"sharp drops at output generation"

[harmthoughts] ✓
  - 作者: OK (Kakkar, Ishita; Zhang, Enze; Uppaal, Rheeya; Hu, Junjie)
  - 年份: OK (2026, arXiv:2604.19001)
  - 标题: OK ("When Safety Fails Before the Answer...")
  - Venue: OK (arXiv preprint)
  - 正文语境: OK — intro:3, method.tex:24 用作主要数据集

[hewitt2019control] ✓
  - 作者: OK (Hewitt, John; Liang, Percy)
  - 年份: OK (2019, EMNLP 2019)
  - 标题: OK ("Designing and Interpreting Probes with Control Tasks")
  - Venue: OK (EMNLP 2019, pp.2733-2743)
  - 正文语境: OK — related_work.tex:10, method.tex:57, appendix:533 引用为 control task 方法

[hu2026refusal_dynamics] ✓
  - 作者: OK (Hu, Xulin; ... Chen, Zhong)
  - 年份: OK (2026, arXiv:2605.02958)
  - 标题: OK ("Tracing the Dynamics of Refusal...")
  - Venue: OK (arXiv preprint)
  - 正文语境: OK — related_work.tex:4 引用为"sharp drops in refusal"

[jiang2025hiddendetect] ✗
  - 作者: OK
  - 年份: OK (2025)
  - 标题: 需更新 — BIB 用 arXiv 标题 "...against Large Vision-Language Models..."，
    但 venue 标注为 ACL 2025，ACL 发表版标题为 "...against Multimodal Large Language 
    Models..."（ACL Anthology: 2025.acl-long.724）
  - Venue: OK (ACL 2025 Main, pp.14880-14893)
  - 正文语境: OK — related_work.tex:7 列为 monitoring system 之一

[kaya2019shallow] ✓
  - 作者: OK (Kaya, Yigitcan; Hong, Sanghyun; Dumitras, Tudor)
  - 年份: OK (2019, ICML 2019)
  - 标题: OK ("Shallow-Deep Networks: Understanding and Mitigating Network Overthinking")
  - Venue: OK (ICML 2019, pp.3301-3310)
  - 正文语境: OK — related_work.tex:10 引用为"cross-layer disagreement"，method.tex:40 作为 crossing rate 概念参考

[mao2025selfjailbreak_reasoning] ✓
  - 作者: OK (Mao, Yingzhi; ... Sun, Le)
  - 年份: OK (2025, arXiv:2510.21285)
  - 标题: OK ("When Models Outthink Their Safety..." — 匹配最新版 v4 标题)
  - Venue: OK (arXiv preprint)
  - 正文语境: OK — related_work.tex:4 引用为"guardrail insertion"

[marks2024geometry] ✗
  - 作者: OK (Marks, Samuel; Tegmark, Max)
  - 年份: OK (2024，匹配 COLM 2024 发表年)
  - 标题: OK ("The Geometry of Truth: Emergent Linear Structure...")
  - Venue: 需更新 — BIB 标注为 arXiv preprint，但已正式发表于 COLM 2024（spotlight）
  - 正文语境: OK — related_work.tex:10 引用为"non-uniform layer-wise information distribution"

[meyoyan2026bertology] ✓
  - 作者: OK (Meyoyan, Gonzalo Ariel; Del Corro, Luciano)
  - 年份: OK (2026, arXiv:2601.13288)
  - 标题: OK ("A BERTology View of LLM Orchestrations...")
  - Venue: OK (arXiv preprint)
  - 正文语境: OK — related_work.tex:7 引用为"safety features distributed across layers"

[openthinker] ✗
  - 作者: 严重错误 — BIB 列出 7 人，其中 3 人为虚构作者。
    BIB: Guha, Marten, Keh, **Bhatia**, **Ragan-Kelley**, **Narang**, Hashimoto
    实际 50 人团队，Saumya Bhatia / Jonathan Ragan-Kelley / Sharan Narang 均不在作者列表中。
    此外 BIB 最后作者为 Hashimoto，实际最后作者为 Ludwig Schmidt。
    正确缩写应为: Guha, Etash and others (含 50 位作者，最后为 Schmidt, Ludwig)
  - 年份: OK (2025, arXiv:2506.04178)
  - 标题: OK ("OpenThoughts: Data Recipes for Reasoning Models")
  - Venue: OK (arXiv preprint)
  - 正文语境: OK — method.tex:24, experiments.tex:7 引用为 OT-7B 训练数据来源

[page1954cusum] ✓
  - 作者: OK (Page, E. S.) — 经典统计论文
  - 年份: OK (1954)
  - 标题: OK ("Continuous Inspection Schemes")
  - Venue: OK (Biometrika 41(1/2))
  - 正文语境: OK — method.tex:52 引用为 CUSUM 基线方法

[qwq] ✓
  - 作者: OK (Qwen Team)
  - 年份: OK (2024)
  - 标题: OK ("QwQ: Reflect Deeply on the Boundaries of the Unknown")
  - Venue: OK (Qwen Blog)
  - 正文语境: OK — intro:3, method.tex:24 引用为 QwQ 模型来源
```

---

## 汇总

**总计 30 条，✓ 26 条，✗ 4 条**

### ✗ 需修复的 4 条

| # | cite_key | 问题类型 | 严重程度 | 详情 |
|---|----------|----------|----------|------|
| 1 | `openthinker` | 虚构作者 | **严重** | 3/7 列出的作者 (Bhatia, Ragan-Kelley, Narang) 不在实际 50 人作者列表中；最后作者应为 Ludwig Schmidt 而非 Hashimoto |
| 2 | `advbench` | 缺失作者 | **中等** | 缺少 Nicholas Carlini 和 Milad Nasr（实际 6 人，BIB 只列 4 人） |
| 3 | `jiang2025hiddendetect` | 标题不一致 | **轻微** | BIB 用 arXiv 标题 ("Large Vision-Language Models")，ACL 2025 发表版标题改为 "Multimodal Large Language Models" |
| 4 | `marks2024geometry` | Venue 需更新 | **轻微** | 已发表于 COLM 2024 (spotlight)，BIB 仍标注为 arXiv preprint |

---
