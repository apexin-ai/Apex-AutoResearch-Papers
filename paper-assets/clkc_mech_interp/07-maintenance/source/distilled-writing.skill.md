---
name: distilled-writing
description: "跨语言知识冲突与机制可解释性领域的论文叙事结构、图表编排、结果呈现的写作共识"
scope: project
version: 1
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: [li2025taming, zhao2025steering, ifergan2024beneath, wang2025lost, xie2024adaptive, xu2024knowledge, zhao2024analysing, wendler2024llamas, kargaran2024mexa, feng2026finegrained, basu2026interpretability, boer2026probing, kialy2026universal, pham2026where, wong2026langfir, zhao2026when, li2023iti, wu2020emerging, muller2021first, hewitt2019designing, conneau2018xnli, rei2020comet, team2026qwen, xing2024evaluating, grattafiori2024llama]
  last_distilled: "2026-05-24T18:00:00Z"
---

## 叙事结构

**故事类型**：突破局限型占50%（4/8）——"以前假设X，我们发现X错了"。化繁为简型37%。代表：li2025taming推翻exclusive heads；ifergan2024beneath推翻consistency=sharing。**高**

**开篇**："LLMs can do X but fail at Y"占75%。wendler2024llamas用爱沙尼亚语翻译逸事是有效的例外。**高**

**Intro**：5-6段标准（7/8）。流程：能力→gap→现有局限→insight→贡献列表。贡献列表在末段是惯例。li2025taming的Problem/Mechanism/Algorithm/Experiment/Theory五标签是高辨识度变体。**7/8 高**

**张力**：最有效的是"概念重新定义"——把已知现象一分为二（consistency vs sharing, concept vs output space）比发现新现象更有冲击力。**3/8 中**

## Figure 1

**类型**：problem_illustration占50%。用具体例子可视化核心问题（wang2025lost的Ottawa→Toronto，ifergan2024beneath的绿蓝对比）。**高**

**设计**：对比布局（左=旧认知 vs 右=新发现）、颜色编码知识来源、真实模型输出。双面板对比效果最好（4/8）。**高**

## 结果呈现

**图表分工**：主结果对比→表格（5/8）；层级趋势→折线图；语言对→对称热力图按script排列显block-diagonal；概念→示意图。附录放per-language细粒度。**6/8 高**

**主结果表**：行=方法，列=数据集×指标分组。bold best主流（5/8），baseline 4-9个（median≈6）。干预类论文用mean±std（zhao2025steering）。**5/8 高**

**消融**：表格>柱状图，full_numbers为主（3/8），维度3-5个。**3/8 中**

## 图表节奏

Figure 1（动机）→ 2-3（机制分析）→ 4+（主结果）→ 末尾（消融/鲁棒性）。motivation→mechanism→results→ablation四阶段在6/8论文一致。主文median 7图3表。**高**

## 可模仿技巧

1. **失败案例做Figure 1**：wang2025lost Ottawa→Toronto让抽象可感（ACL SAC Highlights）
2. **贡献标签化**：li2025taming五标签结构（ICML Spotlight）
3. **paradox标题**：xie2024adaptive "Chameleon or Sloth"（ICLR 2024）
4. **概念拆分做贡献**：ifergan2024beneath一个定义改变就是一篇论文（NAACL Findings）
