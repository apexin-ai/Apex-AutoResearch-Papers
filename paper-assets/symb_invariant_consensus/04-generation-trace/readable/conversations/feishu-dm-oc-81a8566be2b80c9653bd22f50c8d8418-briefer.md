# feishu dm oc 81a8566be2b80c9653bd22f50c8d8418 briefer

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 3
- **Tool calls:** 5
- **Original source:** `logs/chats/feishu_dm_oc_81a8566be2b80c9653bd22f50c8d8418_briefer.jsonl`
- **Structured JSON:** [`f60e4e6f61fecb3151a0.json`](../../sessions/f6/f60e4e6f61fecb3151a0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

8 recorded events

### User

_source line 1 · 2026-05-17T06:29:06.536742+00:00_

[飞书用户 曹晓玉 (ou_fe906a2a0b37a0531edeaa0539755598)]: 这项目原始idea是什么，用大白话和我讲明白

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:dm:oc_81a8566be2b80c9653bd22f50c8d8418:briefer",
  "source": "feishu:oc_81a8566be2b80c9653bd22f50c8d8418"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-17T06:29:14.351219+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:dm:oc_81a8566be2b80c9653bd22f50c8d8418:briefer",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-17T06:29:14.914204+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:dm:oc_81a8566be2b80c9653bd22f50c8d8418:briefer",
  "tool": "ToolSearch",
  "elapsed_ms": 562
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-17T06:29:18.090324+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:dm:oc_81a8566be2b80c9653bd22f50c8d8418:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "memory.md"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-17T06:29:18.626903+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/memory.md\", \"content\": \"# 文献调研：Answer-Conditioned Constraint Extraction from LLM Reasoning Traces\\n\\n**日期**: 2025-05-17  \\n**目标**: 为 D030 methods paper 寻找从 reasoning traces 提取 answer-discriminative 约束的技术参考\\n\\n---\\n\\n## 核心问题\\n\\n当前 SICA 提取的约束是 domain facts（无论答案如何都成立），导致 MaxSAT 聚合退化为 weighted majority vote。需要提取\\\"answer=A → X 成立; answer=B → Y 成立\\\"形式的判别性约束。\\n\\n## 最相关论文\\n\\n### 1. Math-Shepherd (ACL 2024)\\n- **核心思路**: 对每个推理步骤，从该步续写多条路径检查能否到达正确答案。步骤标签本质上是 outcome-conditioned 的——步骤\\\"正确\\\"当且仅当存在从该步到正确答案的延续路径。\\n- **适配价值**: 可直接借鉴其思路——对每个约束，检查它与哪些最终答案兼容。兼容答案集合不同的约束即为 discriminative constraints。\\n\\n### 2. GRACE: Discriminator-Guided Chain-of-Thought Reasoning (EMNLP 2023 Findings)\\n- **核心思路**: 训练 step-level discriminator（对比学习，正样本=正确步骤，负样本=错误步骤），解码时用 discriminator 评分引导生成正确推理步骤。\\n- **适配价值**: 其对比训练框架可直接用于训练\\\"约束判别器\\\"——给定约束+答案对，判断该约束是否支持该答案。\\n\\n### 3. DiVeRSe: Diverse Verifier on Reasoning Steps (ACL 2023)\\n- **核心思路**: 多 prompt 生成多样推理路径 + step-aware verifier 逐步验证 + 加权投票选答案。\\n- **适配价值**: 多样路径生成策略可用于增加约束多样性；step-level verification 思路可用于标注哪些步骤/约束是 answer-specific 的。\\n\\n### 4. Multi-Agent Debate / D3 Framework (2024)\\n- **核心发现**: 研究表明 debate 的性能增益主要来自 output aggregation 而非真正的论证交互——与 SICA 退化为 majority vote 的问题完全一致。\\n- **警示**: 简单的多 agent 对抗不足以产生 discriminative 信号，需要结构化的 answer-conditioned 论证。\\n\\n### 5. Atomic-SNLI / NLI Decomposition (2025)\\n- **核心思路**: 将假设分解为 atomic facts，逐个检查与前提的蕴含/矛盾关系，组合得到最终判断。\\n- **适配价值**: 可将每条约束视为 atomic fact，用 NLI 检查\\\"约束 C 蕴含 answer=A\\\"还是\\\"约束 C 与 answer=A 矛盾\\\"，从而标注约束的 answer-discriminative 属性。\\n\\n## 可行适配方案\\n\\n| 方案 | 改动量 | 需要训练 | 推理成本 |\\n|------|--------|----------|----------|\\n| **A. Outcome-conditioned labeling (Math-Shepherd 式)**: 对每条约束，用 LLM 续写检查与各候选答案的兼容性 | 中等（需修改约束提取 pipeline） | 否 | 高（每条约束需多次续写） |\\n| **B. NLI-based filtering**: 用 NLI 模型判断\\\"约束 C → answer A\\\"的蕴含关系，只保
…[truncated 587 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:dm:oc_81a8566be2b80c9653bd22f50c8d8418:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 536
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-17T06:29:18.627370+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:dm:oc_81a8566be2b80c9653bd22f50c8d8418:briefer",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-17T06:29:19.172020+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/ROADMAP.md\", \"content\": \"# symb_invariant_consensus — Research Dashboard\\n\\n> 最后更新: 2026-05-16 19:22 UTC | 更新原因: exp-001 完成，更新进展和近期任务\\n\\n## 核心方向\\nCapability Trap Analysis Paper：系统揭示为什么 symbolic consensus (SICA) 不能 beat voting (SC)——即使 extraction rate 高、diversity 存在，constraint quality 受 LLM capability 限制导致 aggregation 无贡献。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research (D025 Analysis Paper Pivot) + 审稿进行中\\n- **exp-001 完成** (2026-05-16): SICA 76.49% vs SC 76.24% = +0.25pp (n=804, n.s.)\\n  - FOLIO: 0.00pp (n=204) — sub-claim dead\\n  - ProofWriter D5: +0.33pp (n=600) — not significant\\n- **D025 pivot 数据锚定**: headline = \\\"+0.25pp on 804 questions, not significant\\\"\\n- **Plan 覆盖**: 19 实验，1 done (exp-001)，18 planned\\n- **Claim 状态**: C1(mechanism vacuous) 需 exp-013; C2(operating regime) 需 cross-family; C3(C0 predictor) 需 multi-model data\\n\\n## 近期任务\\n- [x] exp-001 完成，registry 修正 conclusion→success\\n- [ ] exp-002 K-ablation (K=6,8,11,12,16,20, 60题, ~6h GPU) — 启动中\\n- [ ] exp-013 constraint ablation (CPU, MaxSAT vs count-only) — 数据准备中\\n- [ ] Mistral-7B HF 下载 (DDL May 17 12:00 UTC, 3次ModelScope失败)\\n- [ ] exp-010/011 cross-family (Mistral/LLaMA) — 等模型就绪\\n- [ ] exp-017 StrategyQA + exp-018 ARC-Challenge — 等 exp-002 完成后\\n\\n## GPU 预算\\n- 分配: 1× RTX PRO 6000 Blackwell 98GB (cuda:0) on westd-32608\\n- 当前: exp-002 启动中 (~6h)\\n- 排队: exp-010 (1.5h) → exp-011 (1.5h) → exp-017 (1.5h) → exp-018 (1.5h)\\n- 累计已用: ~14h (exp-001)\\n- 预估剩余: ~18h GPU for all remaining experiments\\n\\n## 阻塞项\\n- Mistral-7B 下载损坏 (3次81.3%截断) → 尝试 HF 直下，DDL May 17 12:00 UTC\\n- ~~Agent session 停滞~~ → 已恢复\\n- ~~FOLIO sub-claim~~ → dead (0.00pp)\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D030 | 2026-05-17 | D030: 从 Analysis Paper 转向 Methods Paper — 利用诊断数据设计 | exp-001, exp-013 |\\n| D029 | 2026-05-17 | exp-002 最终
…[truncated 963 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:dm:oc_81a8566be2b80c9653bd22f50c8d8418:briefer",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 544
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-17T06:29:42.254793+00:00_

大白话讲这个项目的原始 idea：

---

**问题背景**：你让大模型（LLM）回答一个推理题，每次回答可能不一样。最常见的做法叫 **Self-Consistency (SC)**——让模型回答很多次，然后**数票**，哪个答案出现最多就选哪个。简单粗暴但有效。

**SICA 的核心想法**：数票太浪费信息了。模型每次回答时写了一大段推理过程，里面包含很多逻辑规则和事实（"约束"）。我们能不能把这些约束**提取出来**，扔给一个形式化求解器（MaxSAT），让它找出"满足最多约束的那个答案"？

打个比方：投票是"10个人说A、8个人说B，选A"；SICA 是"把每个人的论据拆成一条条逻辑规则，然后用数学方法找哪个答案和最多规则不矛盾"。

**理论上**，这应该比傻数票更聪明——因为你利用了推理过程中的结构化信息。

---

**实际结果**：不 work。SICA 和简单投票基本打平（+0.25pp，统计不显著）。

**为什么不 work**：提取出来的"约束"大多是领域常识（比如"三角形内角和180度"），不管答案是 A 还是 B 它都成立，没有区分力。MaxSAT 求解器拿到一堆对所有答案都成立的约束，最后退化成了变相数票。

**现在在干嘛**：项目已经 pivot 了两次——先转成"分析论文"（揭示为什么 symbolic consensus 打不过投票），最近又转向"方法论文"（基于诊断发现，设计能提取有区分力约束的新方法）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:dm:oc_81a8566be2b80c9653bd22f50c8d8418:briefer"
}
```

</details>

---

## Round 2

6 recorded events

### User

_source line 9 · 2026-05-17T06:34:27.055148+00:00_

[飞书用户 曹晓玉 (ou_fe906a2a0b37a0531edeaa0539755598)]: 你觉得还有救吗

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:dm:oc_81a8566be2b80c9653bd22f50c8d8418:briefer",
  "source": "feishu:oc_81a8566be2b80c9653bd22f50c8d8418"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-17T06:34:37.743757+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:dm:oc_81a8566be2b80c9653bd22f50c8d8418:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "decisions.yaml"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-17T06:34:38.284305+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/decisions.yaml\", \"content\": \"_next_id: 31\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 08:47 UTC\\n  summary: MVP 验证方案：50 题 MATH-500 分层子集，SICA vs SC@K=12\\n  rationale: SICA 核心价值取决于两个前提：(1) 能从推理 trace 可靠提取符号约束；(2) 跨路径矛盾率足够高（>5%）使形式化验证有意义。Reviewer\\n    给 impact 3/5，核心担忧是\\\"若矛盾率<5%则动机不成立\\\"。MVP 直接验证这两个前提，50 题按难度分层可同时观察 Extraction-Verification\\n    Paradox（难题提取差但矛盾多）。Pass 则进入全量实验冲 EMNLP/AAAI，Fail 则及时止损。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 08:52 UTC\\n  summary: 拒绝 CRD pivot，要求回归 SICA 原始方案\\n  rationale: Reviewer critical 审查发现 Agent 实施的是\\\"跨表征分歧诊断\\\"(CRD)，与 IDEA_BRIEF 定义的 SICA\\n    完全不同：CRD 用双表征（FOL+SymPy）做单解分歧检测，无多路径采样、无 MAX-SAT 共识——这正是 SICA 区别于 VERGE/D&P 的核心创新点。CRD\\n    的 novelty 定位与 VERGE 高度重叠（单输出验证+修复），无法支撑 EMNLP 投稿。同时 MVP 标准被静默替换，ROADMAP 的三条 pass\\n    criteria 从未测试。98GB GPU 完全能跑 QwQ-32B，无理由换 Qwen3-32B-AWQ。必须回归 SICA：K=12 多路径采样 →\\n    符号约束提取 → Z3 加权 partial MAX-SAT → 不变量共识打分。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 08:54 UTC\\n  summary: MVP 标准 v2：三档判定 + 矛盾绝对数 ≥5 + accuracy ≥SC+2pp + ProofWriter sanity check\\n  rationale: Reviewer warning 指出：(1) 5% 矛盾率阈值在 50 题上仅 2.5 题，置信区间极宽——改为绝对数 ≥5 题；(2)\\n    ≥SC+0.1pp 也过关无意义——改为 ≥2pp 或 p<0.1；(3) 灰色区间无处理——新增 Inconclusive 档，触发扩展到 100 题重测；(4)\\n    单域 MATH-500 不够——加 10 题 ProofWriter 做逻辑域 sanity check；(5) 模型不能模糊——固定 QwQ-32B，不可替换。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-15 12:02 UTC\\n  summary: MVP T=0.7 继续跑完（需要完整数据），diagnostic 自然结束后 GPU 带宽恢复；AIME 30 题排在 MVP 之后\\n  rationale: Temperature 诊断 4/5 题显示 T=0.7/0.9/1.0 均几乎不产生答案分歧——C2/C3 高风险 FAIL。但仍决定让\\n    MVP 跑完：(1) 50 题完整数据无论正负都有价值（负面结果=SICA 在强模型上无信号，本身是发现）；(2) GPU 已分配且无其他实验排队；(3)\\n    smoke test L5 有 3 条矛盾，50 题中 L4-5 有 20 题可能产生更多信号。MVP 完成后立即跑 AIME 30 题（QwQ-32B ~79.5%，分歧应更明显），作为\\\"高难度\\n    sweet 
…[truncated 10999 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:dm:oc_81a8566be2b80c9653bd22f50c8d8418:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 540
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T06:34:38.284982+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:dm:oc_81a8566be2b80c9653bd22f50c8d8418:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "report.md"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T06:34:38.285317+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/report.md\", \"content\": \"# Handover — 2026-05-17\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp-018-arc-v2 | Cross-domain validation: Qwen2.5-14B-Instruct 在 ARC-Challenge (科学多选, ABCD) 上 SICA vs SC——验证 capability trap 是否跨任务类型泛化（v2: build_generator bug 已修复） | — | — | — |\\n\\n## 待处理\\n- exp-011-llama8b-v3: Cross-family validation: LLaMA-3.1-8B-Instruct 在 D012 数据集(30PW+30FOLIO)上是否复现 SICA≈SC pattern——验证 capability trap 非 Qwen-specific（v3: 模型 shard 已修复，GPU 空闲后提交）（排队等待 GPU）\\n- pilot-contrastive-prompt: Contrastive Prompt Extraction: 将 prompt 改为\\\"列出支持答案X/反对答案Y的证据\\\"能否将 discriminative ratio 从 37.2% 提升至 >70%，并使 SICA(contrastive) > SC ≥3pp——验证 answer-conditioned 约束是否解决 SICA 机制 vacuous 问题（准备中）\\n- smoke-test-5q（准备中）\\n\\n## 近期结论\\n- **exp-010-mistral-v2** (failed): Cross-family validation: Mistral-7B-Instruct-v0.3 在 D012 数据集(30PW+30FOLIO)上是否复现 SICA≈SC pattern——验证 capability trap 跨模型家族泛化（v2: 修复 max-model-len=8192 防 400 循环） ← 基于 sica_expanded_14b\\n- **pilot-constraint-filtering** (negative): Constraint Consistency Filtering: 只保留在≥T条traces中重复出现的约束能否提升SICA accuracy超过SC——验证约束质量过滤是否解决capability trap ← 基于 sica_expanded_14b\\n- **exp-018-arc** (failed): Cross-domain validation: Qwen2.5-14B-Instruct 在 ARC-Challenge (科学多选, ABCD) 上 SICA vs SC——验证 capability trap 是否跨任务类型泛化（多选题型） ← 基于 sica_expanded_14b\\n\\n## 趋势\\n成功 9 / 负向 3 / 失败 8 / 共 26\\nsc_accuracy: 0.5333 ↓（近 3 次 success）\\nsica_accuracy: 0.5667 ↓（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-32608: 无 GPU 信息\\n\\n## 告警\\n- mvp_math50_t07: 已被终止 — unknown\\n- sica_aime30_t07: 已被终止 — unknown\\n- sica_aime30_v2: 已被终止 — unknown\\n- sica_aime30_v3: 已被终止 — unknown\\n- sica_proofwriter30: 训练失败 — unknown\\n- sica_folio30: 已被终止 — unknown\\n- sica_proofwriter30_v2: 已被终止 — unknown\\
…[truncated 350 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:dm:oc_81a8566be2b80c9653bd22f50c8d8418:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-17T06:34:56.028060+00:00_

坦率讲一下现状：

**原始 idea 是什么（回顾）：** 用符号逻辑（MaxSAT）来聚合多条推理路径的约束，理论上比简单投票（Self-Consistency）更聪明地选答案。

**现在怎么样了：**

实验跑了 26 个，核心发现是 SICA 的"符号聚合"机制基本是空转的：
- 提取出的约束没有判别力（37% discriminative ratio），MaxSAT 约束权重≈随机权重≈简单计数
- 唯一产生差异的场景是精确平票（6:6 tiebreak），本质上 SICA 退化成了一个"花哨的打平局方式"
- 扩大到 804 题后差距只有 +0.25pp，统计不显著

**"有救"的方向：**

项目已经 pivot 了两次：
1. 先从"证明方法有效"转到"分析为什么无效"（Analysis Paper）
2. 最新又转向 Methods Paper（D030）——利用诊断数据设计改进方法，比如 contrastive prompt 提取 answer-conditioned 约束

目前 `pilot-contrastive-prompt` 还在准备中，思路是让 LLM 直接生成"支持答案A/反对答案B"的约束，把 discriminative ratio 从 37% 拉到 70%+。如果这个 pilot 跑通，方法论文还有故事可讲。

**总结判断：** 原始 idea（符号约束自动 override 多数投票）基本死了。但项目积累了很扎实的诊断数据，如果 contrastive prompt 方向能把约束质量问题解决，转成一篇"我们发现了问题并解决了它"的 methods paper 还是有可能的。关键看下一个 pilot 的结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:dm:oc_81a8566be2b80c9653bd22f50c8d8418:briefer"
}
```

</details>

---

## Round 3

2 recorded events

### User

_source line 15 · 2026-05-17T09:39:52.729179+00:00_

[飞书用户 曹晓玉 (ou_fe906a2a0b37a0531edeaa0539755598)]: 现在什么情况

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:dm:oc_81a8566be2b80c9653bd22f50c8d8418:briefer",
  "source": "feishu:oc_81a8566be2b80c9653bd22f50c8d8418"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-17T09:40:24.802452+00:00_

当前状态比较艰难，直说：

**核心结论已经出来了：SICA 原始方法不 work。**

关键证据链：
- exp-001: SICA vs SC = +0.25pp（804题，不显著）
- exp-002: 所有 K 值下 SICA ≤ SC（gap 0 到 -5pp）
- exp-013: MaxSAT ≈ 简单计数 ≈ 随机权重 → 符号推理组件零贡献
- 约束判别率只有 37.2%，大部分提取出来的是"废话约束"

**当前状态：**
- 26 个实验跑了：9 成功 / 3 负向 / 8 失败
- 正在跑：exp-018-arc-v2（ARC 跨域验证）
- 排队：LLaMA-8B 跨家族验证、contrastive prompt pilot
- 项目已经 pivot 了两次——从"证明有效"→"分析为何无效"(Analysis Paper) → 最新转向"Methods Paper"(D030)，想利用诊断数据设计改进方案

**D030 的新方向：** 既然诊断清楚了失败原因（约束不判别、LLM 能力陷阱），就反过来设计 answer-conditioned 的约束提取方法。pilot-contrastive-prompt 就是测试这个思路——把 prompt 改成"列出支持/反对答案X的证据"看能不能把判别率从 37% 拉到 70%+。

**说"有没有救"：** Methods Paper 方向理论上还有一线机会——如果 contrastive prompt 能大幅提升约束判别率且带来显著 accuracy gain。但目前这个 pilot 还没结果，而且之前的实验失败率很高（8/26），工程阻力也不小。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:dm:oc_81a8566be2b80c9653bd22f50c8d8418:briefer"
}
```

</details>

---
