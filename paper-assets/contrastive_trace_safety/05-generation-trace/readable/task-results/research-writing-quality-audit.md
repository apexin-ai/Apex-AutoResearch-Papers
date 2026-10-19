# research writing quality audit

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_writing_quality_audit_20260520T150735_result.json`
- **Structured JSON:** [`c684f71d24640d667e06.json`](../../sessions/c6/c684f71d24640d667e06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the information needed for a comprehensive review. Here are my findings:

---

## 任务 1: Related Work 覆盖度检查

蒸馏 research skill 提及的核心论文（跨 research + writing 两份 skill 共约 10 篇）逐一对照：

| # | 论文 | 引用? | 深度 | 备注 |
|---|------|-------|------|------|
| 1 | **Arditi (NeurIPS'24)** — refusal direction | Y | 简要讨论 | related_work L13: "identify a single refusal direction"，并与本文 multi-direction finding 做对比 |
| 2 | **RepE / Zou (2023)** — representation engineering | Y | 详细对比 | 作为 baseline 复现，报告了跨模型不一致性能 (0.756 vs 0.559) |
| 3 | **HarmThoughts** — 推理安全数据集 | Y | 简要讨论 | "step-level annotations"，同时作为本文数据来源 |
| 4 | **Zhou (ACL'24)** — alignment, safety across layers | Y | 仅提及 | "show safety-relevant information distributes across layers" — 一句话，未讨论其"安全信号预训练已存在"这一核心 claim |
| 5 | **Hewitt (EMNLP'19)** — control tasks, selectivity | Y | 详细对比 | 明确采用其方法 (control tasks, selectivity)，在 appendix 有验证 |
| 6 | **Kaya (2019)** — "overthinking", shallow-deep | **N** | 未出现 | 仅在 method.tex 作为 crossing rate 引用来源出现，related work 中完全缺失 |
| 7 | **PABEE (Zhou et al. 2020)** — "patience", early exit | **N** | 未出现 | 同上，仅在 method.tex 出现 |
| 8 | **Chen (Anthropic)** — CoT faithfulness ~25% | Y | 仅提及 | "Unfaithful reasoning~\cite{chen2025unfaithful}" — 一句话带过，未讨论其 "RL 后忠实度趋平" 这一关键发现 |
| 9 | **SafeThink** — safety steering | Y | 简要讨论 | Mitigation 段落中讨论 |
| 10 | **Burns/CCS (2023)** — latent truth directions | Y | 详细对比 | 作为 baseline 复现并报告失败原因 |

**缺失评估：**

- **Kaya (2019)** — **必须补**。Crossing rate 是本文核心贡献（metric-induced layer selection bias）的关键概念，Kaya 是该概念的原始提出者，不在 related work 讨论是明显遗漏。读者需要在 related work 中理解 crossing rate 的来源和其在效率领域的原始语境，才能理解本文将其用于安全探针选层的 novelty。
- **PABEE** — **建议补**。与 Kaya 互补，PABEE 的 "patience" 概念与本文的跨层一致性分析直接相关。至少应在 Probing Methodology 段落提及。

**深度不足：**

- **Zhou (ACL'24)** — 蒸馏 skill 指出其核心 claim "安全信号预训练已存在，对齐仅建立桥接关联"，但 related work 只提了 "information distributes across layers"。这个 claim 与本文的层选择分析高度相关（如果安全信号在不同层有不同功能，选层就更关键），值得展开讨论。
- **Chen (Anthropic)** — 其 "CoT 忠实度仅 ~25%，RL 后趋平" 的发现是本文"隐状态分析动机"的最直接支撑（文本不可信→需要看 hidden state），但仅一句 "unfaithful reasoning" 带过。

**总结**：覆盖面广（8/10 已引用），但 Kaya/PABEE 的缺失是结构性问题——本文最核心的 crossing rate 概念在 related work 中无来源追溯。Zhou 和 Chen 的讨论深度不足，浪费了构建动机链条的机会。

---

## 任务 2: 叙事结构对标

### 蒸馏建议 vs 当前 Intro

蒸馏 writing skill 建议的"许诺-颠覆"模式：先建立正面期望（"隐状态分析被寄望揭示真实推理"），再揭示隐藏缺陷（"但与文本一致吗？"/"但方法论选择本身就能反转结论"）。

**当前 Intro 结构分析**（5 段）：

- **P1**: 定义问题（self-jailbreak + CP）→ 提问 "can current probing methods reliably distinguish?"
- **P2**: 指出现有方法的局限 → 提出方法论问题 "how sensitive are probe conclusions to metric choice?" → 给出震撼结论 "14-layer to 61-layer divergence"
- **P3**: 实验设置 + 中心发现（metric choice determines HS advantage）
- **P4**: 详细结果描述（evidence gradient）
- **P5**: 贡献列表（3 项）

### Hook 强度评估

当前 hook 是 P1 末尾的问题："Before retrospective characterization can inform future detection systems, a prior question must be answered: can current probing methods reliably distinguish pre-CP from post-CP reasoning steps?"

**问题**：这是一个直接的研究问题，不是"许诺-颠覆"。读者没有先被建立起"hidden state probing works great"的期望，就直接被问了一个开放问题。这降低了戏剧张力。

P2 的 "We show this choice alone can reverse a study's central conclusion" 是全文最有力的一句话，但它出现在第二段，且没有先建立"通常我们认为层选择不重要"的正面预期。

### 与蒸馏建议的差距

1. **缺少正面预期建立**。蒸馏建议的 Chen 模式是"先承认推理模型'更忠实'再揭示仅 25%"——先给读者一个看似合理的信念，再打破。当前 Intro 从第一句就进入 problem mode，没有先让读者觉得"现有方法已经解决了这个问题"。

2. **震撼数据埋得太深**。"14-layer to 61-layer divergence depending solely on metric choice" 是极具说服力的数据，但出现在 P2 末尾。如果放在 P1 开头作为 teaser（类似 Arditi 的 "rank-1 edit, <$5"），冲击力更大。

3. **缺少"先建立对手最强论据再拆解"**。蒸馏建议的"突破局限型"需要先承认 hidden-state probing 的成功案例（Zhou, Arditi 等已证明 HS 能检测安全信号），再揭示其在 reasoning model 上的方法论脆弱性。

### 具体建议

P1 可重构为：

> Hidden-state probes have shown remarkable success in detecting safety violations: a single direction suffices to erase refusal behavior [Arditi], and linear probes achieve >95% accuracy on ethical judgments [Zhou]. These results promise a robust internal monitoring channel—one that bypasses the text entirely. But do these successes transfer to reasoning models, where safety failures emerge gradually from the model's own chain of thought? We show that the answer depends entirely on a methodological choice that has received almost no scrutiny: which transformer layer to monitor.

这样就实现了：正面建立期望 → 提出质疑 → 给出颠覆。

**总结**：当前 Intro 结构完整（5 段，贡献列表），信息量充足，但叙事缺乏"先扬后抑"的张力。最有力的数据（14-61 layer divergence）未被充分利用为 hook。改进空间中等偏大。

---

## 任务 3: 命名贡献检查

### "Commitment Point" (CP)

- **首次出现**：Abstract 第 1 句 "Detecting the commitment point (CP)"
- **定义**：Abstract + Intro P1 "the first reasoning step after which safety deliberation permanently ceases"
- **直觉解释**：有，"permanently ceases" 传达了不可逆性
- **加粗**：Intro 中 **Safety Commitment Point** (CP) 加粗；Method §3.1 再次加粗定义
- **突出度**：Abstract 和 Intro 都在前 2 句出现，突出度高

**评价**：命名优秀。"Safety Commitment Point" 简洁、直觉化、可引用。在 abstract 和 intro 中前置突出。

### "Crossing Rate"

- **首次出现**：Abstract "a crossing-rate composite metric masks the HS advantage"
- **定义位置**：Method §3.3 "crossing rate formalizes cross-layer prediction disagreement"
- **正式定义**：无明确数学定义。Method §3.3 仅说 "formalizes cross-layer prediction disagreement~\citep{kaya2019shallow,zhou2020bert}"，读者需要去查原文才能理解具体含义。Experiments §4.2 进一步解释了机制（shallow layers produce compressed representations → frequent threshold crossings → inflated crossing rate），但仍未给出公式。
- **直觉解释**：部分有。"threshold crossings" 给出了直觉，但 "crossing rate" 本身是个技术术语，不像 CP 那样自解释。
- **突出度**：Abstract 提及，Intro 贡献列表加粗，但不是以"我们命名的概念"出现，而是作为先验存在的概念引用。

**评价**：Crossing rate 不是本文命名的概念（来自 Kaya），但它是 metric bias 论证的核心。问题在于：(1) 缺少正式定义——读者在 abstract 就遇到这个术语，但直到 method 才有模糊解释；(2) 作为引用概念，相关原始工作（Kaya, PABEE）在 related work 中缺失。

### 被遗漏的可命名概念

1. **"Metric-induced layer selection bias"** — 已命名且加粗，作为贡献 #1。但偏长，不如 "metric bias" 或 "layer selection confound" 简洁。不过作为贡献声明的正式名称可以接受。

2. **"Evidence gradient"** — Experiments §4 P1 使用了这个术语（cross-validated → significant → exploratory），是很好的 framework 命名。但它没有加粗、没有在 abstract/intro 中突出。这是一个**被低估的命名机会**——"evidence gradient" 作为一种报告 methodology（不同模型/scale 给出不同置信度的结果），如果正式命名并在 abstract 中前置，可以成为方法论贡献的一部分。

3. **"Encoder-quality boundary"** — 贡献 #2 的名称。已加粗，但 "boundary" 这个词略弱——实际发现是 HS advantage 随 encoder quality 递减（384d: 4/4 → 1024d: 1/4），更像一个 "encoder-quality gradient" 而非硬边界。

4. **"Representation compression"** — 用于解释浅层 crossing rate 膨胀的机制。未命名为正式概念，但 "compressed representation effect" 或类似命名可以让论证更清晰。可选，非必须。

**总结**：CP 的命名和突出度很好。Crossing rate 缺正式定义是较明显的问题。"Evidence gradient" 是被遗漏的最大命名机会。

---

## 整体评估

**评分：B+**

**改进优先级排序**：

1. **（高优）Related Work 补 Kaya/PABEE**。Crossing rate 是核心贡献的基石概念，其来源必须在 related work 中追溯，否则审稿人会质疑 novelty 定位——你重新发现了别人的概念还是将其应用到了新领域？需要明确后者。

2. **（高优）给 crossing rate 一个正式定义**。在 Method §3.3 增加一行数学定义（如 $\text{CR}_\ell = \frac{1}{T-1}\sum_{t=1}^{T-1} \mathbf{1}[\hat{y}_t^{(\ell)} \neq \hat{y}_{t+1}^{(\ell)}]$），让 abstract 中的术语在 method 中有明确落地。

3. **（中优）Intro hook 重构为"许诺-颠覆"**。先建立 "HS probing works" 的正面预期（引 Arditi/Zhou），再揭示在 reasoning model 上的方法论脆弱性。这不需要大改，主要调整 P1 的前 3 句。

4. **（中优）加深 Zhou (ACL'24) 和 Chen (Anthropic) 的讨论**。Zhou 的 "安全信号预训练已存在" 和 Chen 的 "CoT 忠实度仅 25%" 都可以直接加强本文的动机论证。

5. **（低优）正式命名 "evidence gradient"**。如果在 abstract 中加一句类似 "We propose an evidence gradient framework that ranks findings by statistical rigor across model scales"，可以增加方法论贡献的可引用性。

---
