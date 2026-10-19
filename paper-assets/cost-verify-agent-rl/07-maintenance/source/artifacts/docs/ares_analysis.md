# ARES 方法细节分析

> 论文: Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents
> arXiv: 2603.07915 | 2026-03-09
> 作者: Jingbo Yang, Bairu Hou, Wei Wei, Yujia Bao, Shiyu Chang (UCSB)
> GitHub: UCSB-NLP-Chang/Ares（仅 README，无代码，截至 2026-05-15）

## 方法摘要

ARES 针对支持可配置 reasoning effort（high/medium/low）的 thinking LLM，训练一个轻量级 router（Qwen3-1.7B）在 multi-step agent 任务中为每一步预测最低充分的 reasoning effort level。核心思路：简单步骤（如打开 URL）用 low effort，复杂步骤（如解析复杂网页结构）用 high effort。训练分两阶段：SFT（oracle 标注数据）+ RL（GRPO，composite reward）。在 TAU-Bench 上实现 52.7% token 削减且性能持平或微升。

## 训练流程详解

### Phase 1: SFT Router 训练

**数据构造三阶段流水线：**

1. **轨迹收集**：用 base agent（gpt-oss-20b）在最高 effort（e_high）下采集 N 条成功轨迹，选择最短的一条 τ* 作为参考轨迹。理由：固定高质量 action sequence，将长程优化问题转化为独立的逐步标注。

2. **Effort 标注**：对参考轨迹的每一步 t：
   - 在每个 effort level（low/mid/high）下各采样 K=3 次
   - 检查 ≥M=2 次是否能复现 ground-truth action a*_t
   - 验证函数 𝒱 定义：
     - Tool-use agents: tool name + key parameters 精确匹配
     - Web agents: interaction 完全一致（如 "click[1316]"）
     - Deep-research agents: LLM judge 判断语义等价
   - 候选集 C_t = {e ∈ {low,mid,high} | 3 次中 ≥2 次正确}
   - 标签 y_t = C_t 中 cost 最低的 level
   - 如果没有 level 通过鲁棒性检验，丢弃该步

3. **Rationale 生成**：用 teacher model（GPT-5）为每个标注步骤生成 3-5 句理由，考虑 observation 复杂度、任务进展、子任务难度。

**Router 输入/输出：**
- 输入：interaction history h_t = (x, o₁, a₁, ..., o_{t-1}, a_{t-1}) + 当前 observation o_t
- 输出：rationale r_t（3-5 句）+ effort label y_t ∈ {low, mid, high}

**SFT 超参：**
- 模型：Qwen3-1.7B
- Loss：standard next-token prediction
- LR: 5×10⁻⁶ | Epochs: 3 | Batch: 64 | Warmup: 0.1 | Weight decay: 0.01
- 训练数据量：43,358 步（TAU）、12,366 步（BrowseComp-Plus）、1,718 步（WebArena）

### Phase 2: RL 精调（GRPO）

**Composite Reward：**
- Outcome reward: +5.0（任务成功）/ 0.0（失败）
- Cost reward（轨迹平均）: c(e_t) = {-0.2 low, -0.5 mid, -1.0 high}，R_cost = (1/T)Σc(e_t)
- Format reward: -1.0（模板格式错误）

**GRPO 超参：**
- 16 outputs per prompt（group-wise advantage）
- Max seq: 4096 prompt + 512 response
- LR: 1.5×10⁻⁶（constant）| KL coef: 0.01 | Epochs: 5 | Batch: 32

**RL 提升（TAU-Bench Retail）：**
- SFT → RL: 54.8% → 58.5% accuracy, 652k → 476k tokens

## 度量方式详解

### "Effort" 不是连续的——是 3 个离散等级

ARES 的 effort 是 LLM API 的预设 reasoning level（high/medium/low），不是 token 预算或 FLOPs。论文未公开每个 level 的具体 token 限制（依赖于 gpt-oss-20b 的内部配置）。

### Cost 指标

| 指标 | 定义 |
|------|------|
| T_total | 整个 eval set 的总 reasoning tokens |
| T_task | 每任务平均 reasoning tokens |
| T_step | 每步平均 reasoning tokens |
| Token reduction % | 1 - T_total(ARES) / T_total(High) |

### 关键结果数据

**Table 1 — SFT Router（主实验）：**

| Benchmark | Method | Accuracy | Total Tokens | Token Reduction |
|-----------|--------|----------|-------------|-----------------|
| TAU Retail | Low | 35.0% | 25k | — |
| TAU Retail | Medium | 47.3% | 137k | — |
| TAU Retail | High | 54.8% | 1,007k | baseline |
| TAU Retail | **ARES** | **54.8%** | **652k** | **35.2%** |
| TAU Airline | High | 38.0% | 873k | baseline |
| TAU Airline | ARES | 36.0% | 678k | 22.3% |
| BrowseComp+ | High | 42.7% | 1,841k | baseline |
| BrowseComp+ | ARES | 41.3% | 1,071k | 41.8% |
| WebArena | High | 45.0% | 2,763k | baseline |
| WebArena | **ARES** | **46.5%** | **1,512k** | **45.3%** |

**Table 2 — RL 精调（TAU-Bench only）：**

| Domain | SFT Acc | RL Acc | SFT Tokens | RL Tokens |
|--------|---------|--------|------------|-----------|
| Retail | 54.8% | 58.5% | 652k | 476k |
| Airline | 36.0% | 42.0% | 678k | 133k |

**Table 5 — 跨模型泛化（gpt-oss-120b）：**

| Method | Accuracy | Tokens |
|--------|----------|--------|
| High | 67.8% | 558k |
| ARES (router trained on 20b) | 65.2% | 428k |

## ALFWorld 适用性分析

### ARES 未在 ALFWorld 上实验

ARES 的三个 benchmark（TAU-Bench, BrowseComp-Plus, WebArena）均为 text-based tool/web interaction，不涉及 embodied/interactive agent 环境。

### 适用性障碍

1. **Effort level 不适用**：ARES 依赖 LLM API 的可配置 reasoning level（high/mid/low）。ALFWorld 场景中 agent 的 "verification" 是显式的 self-check 行为（如 Self-Guide 的 reflection），不是 reasoning effort 控制。

2. **验证函数 𝒱 需重新定义**：ARES 用 tool name/parameter 精确匹配或 LLM judge 验证 action 等价性。ALFWorld 的 action space 更简单（go to, pick up, put, open, close, use, examine），但 verification 的语义不同——不是 "这一步用 low effort 能否产生相同 action"，而是 "这一步是否需要显式验证"。

3. **问题结构差异**：ARES 解决 "effort allocation"（每步投入多少推理资源），B-IAVR 解决 "verification gating"（是否执行额外验证步骤）。前者是 continuous resource allocation，后者是 binary decision。

### 如果要在 ALFWorld 上实现 ARES-style baseline

需要将 ARES 的 3-level effort 重新映射为 verification 决策：
- **方案 A（最自然）**：将 ARES 框架简化为 binary SFT router（verify/skip），用 ARES 的数据标注流程生成 ALFWorld 训练数据。
- **方案 B（保留 3-level）**：定义 3 种 verification intensity（no-check / quick-check / full-reflection），但这在 ALFWorld 中缺乏自然语义。

## 复现工作量评估

### 代码状态

GitHub 仓库（UCSB-NLP-Chang/Ares）截至 2026-05-15 仅有 README，无训练/推理代码。**必须从零实现。**

### 工作量分解（在 ALFWorld 上实现 ARES-style SFT router baseline）

| 阶段 | 内容 | 人时 | GPU 时 |
|------|------|------|--------|
| 数据标注 | 收集 always-on 成功轨迹 → 每步 3-level probing → 标签生成 | 8-12h | 20-30h（3×K 次 inference） |
| Rationale 生成 | GPT-5 或替代 teacher model 生成 rationale | 4-6h | ~0（API 调用） |
| Router 训练 | Qwen3-1.7B SFT，标准 next-token prediction | 2-3h | 4-8h（1.7B 模型训练快） |
| 评估 | ALFWorld 16-episode eval × 多次 | 2-3h | 8-12h |
| **总计** | | **16-24h** | **32-50h** |

### 前置依赖

- 需要 Phase A always-on baseline 成功（≥50% success rate）才能产出有意义的标注数据
- 需要 ALFWorld action equivalence 验证函数（较简单，action space 有限）
- 不需要 RL 阶段（SFT-only 作为 baseline 足够）

### 可复用组件

- Qwen3-1.7B：已有模型，与 B-IAVR 共享
- ALFWorld 环境：已搭建（exp027 在用）
- verl-agent 框架：可复用 SFT trainer
- 验证函数：ALFWorld action 精确匹配即可

## 与 B-IAVR 的关键差异

| 维度 | ARES | B-IAVR (Ours) |
|------|------|---------------|
| **决策类型** | 3-level effort allocation (low/mid/high) | Binary verify/skip |
| **训练方法** | SFT on oracle-labeled data (+optional GRPO) | RL (GRPO) with action-change reward |
| **训练信号来源** | Pre-computed labels via exhaustive probing | Online reward: action change after verification |
| **Router 架构** | 独立 Qwen3-1.7B router，与 agent LLM 分离 | 同一模型（Qwen3-1.7B）内 control token |
| **数据需求** | 大量标注数据（43k+ steps for TAU） | 无需预标注，RL 在线学习 |
| **适用场景** | Reasoning tasks (tool-use, web, research) | Interactive agent tasks (ALFWorld) |
| **Cost 定义** | Reasoning tokens per step | Verification invocations per episode |
| **Verification 语义** | "用多少推理资源" | "是否执行额外验证步骤" |
| **Oracle 依赖** | 需要成功参考轨迹 + 穷举验证 | 不需要 oracle，reward from environment |
| **核心 novelty** | 首个 per-step effort routing for agents | 首个 RL-trained selective verification for interactive agents |
| **Base agent LLM** | gpt-oss-20b (proprietary) | Qwen3-1.7B (open-source, same as router) |
| **RL reward** | +5.0 task success - cost penalty | Task success + action-change informativeness |
| **Benchmark** | TAU-Bench, BrowseComp+, WebArena | ALFWorld |
| **最佳 token 削减** | 52.7% (TAU Airline, RL) | TBD (Phase B) |

## Phase D 对比实验建议

### 最小对比方案（推荐）

实现 **ARES-style SFT binary router** 作为 baseline：
1. 用 always-on baseline 的成功轨迹
2. 每步 probing：verify/skip 两种模式各采样 3 次
3. 标签 = 最低 cost 的通过模式
4. SFT 训练 Qwen3-1.7B
5. 评估：success rate + verification reduction %

这比完整 ARES 复现简单得多（省略 3-level、rationale 生成、RL 阶段），且直接对标 B-IAVR 的 binary 决策空间。

### 预计对比叙事

"SFT router (ARES-style) 需要 oracle 轨迹 + 穷举标注，而 B-IAVR 通过 RL 在线学习 verification policy，无需预标注数据。在相同模型规模和 benchmark 下，B-IAVR 的 verification reduction 和 success rate 与 SFT baseline comparable/superior，同时消除了数据标注成本。"
