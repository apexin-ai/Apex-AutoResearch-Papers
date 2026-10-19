# 文献增量扫描简报 — 2026-05-16

## 扫描范围
2026 年 4-5 月 arXiv/会议论文，关键词覆盖：selective verification, self-verification + RL, adaptive computation + agent, cost-efficient verification, ALFWorld 2026, GRPO + agent, action-change + verification。

---

## 新发现论文（9 篇）

### Tier 1: 需关注的 ALFWorld 新 SOTA / 强 baseline

| 论文 | arXiv | 方法 | ALFWorld 结果 | 与 B-IAVR 关系 |
|------|-------|------|---------------|----------------|
| **PA-MoE** | 2602.17038 | Phase-Aware MoE + GiGPO | **93.8%** (Qwen2.5-1.5B) | 正交（架构创新），需作为 baseline 引用 |
| **SDAR** | 2605.15155 | On-policy self-distillation + GRPO | +9.4% over GRPO | 互补：改进 RL 训练本身，可与 B-IAVR 叠加 |
| **HCAPO** | 2603.08754 | Hindsight credit assignment | +13.8% over GRPO (7B) | 互补：更好的 credit assignment 可提升 verification step 的 reward signal |
| **SKILL0** | 2604.02268 | Skill context curriculum → zero-shot | +9.7% over GRPO | 互补：skill internalization + selective verification 可组合 |

### Tier 2: 方法层面相关

| 论文 | arXiv | 核心贡献 | 与 B-IAVR 关系 |
|------|-------|----------|----------------|
| **ACT** | 2603.08706 | RL 训练 critical judgment（非模仿 reflection） | 不同维度：ACT 改进 reflection 质量，B-IAVR 决定何时 reflect |
| **RWML** | 2602.05842 | 自监督 world model（embedding space gap reward） | 正交：改进 world model 准确性，与 verification timing 无关 |
| **Fission-GRPO** | 2601.15625 | 失败轨迹拆分为 recovery 训练实例 | 相关对比：reactive error recovery vs proactive verification |

### Tier 3: 背景/概念相关

| 论文 | arXiv | 与 B-IAVR 关系 |
|------|-------|----------------|
| **SelfBudgeter** | 2505.11274 | 平行概念（reasoning domain）：RL 学习 token budget 分配 |
| **CoVe** | 2603.01940 | 不同用途：verification 用于训练数据合成而非推理时 |

---

## 竞争格局更新

### 直接竞争者变化：无新增

**关键结论：截至 2026-05-16，未发现新的直接竞争者。** 没有论文同时做到以下三点的组合：
1. RL-trained binary verify/not-verify decision
2. 应用于 interactive agent trajectories（非 reasoning chains）
3. 使用 action-change signal 作为 verification trigger

现有竞争者格局不变：
- **ARES** (2603.07915)：最近的竞争者，但用 SFT router + token efficiency reward，非 action-change signal
- **Agent-Omit** (2602.04284, ICML'26)：RL 学 cost-efficient agent behavior，但方向相反（减少 context 而非选择性增加 verification）
- **Thinkless/AutoThink**：reasoning domain，非 interactive agent

### ALFWorld baseline 格局显著变化

旧认知：GiGPO (86.1%), ReflAct prompting (93.3%)
新格局：
- **PA-MoE+GiGPO: 93.8%**（1.5B 小模型新 SOTA，超过 prompting SOTA ReflAct 的 93.3%）
- HCAPO: +13.8% over GRPO（7B）
- SDAR: +9.4% over GRPO
- SKILL0: +9.7% over GRPO

ALFWorld 准确率已高度饱和（>93%），进一步支持 B-IAVR 聚焦 cost-efficiency 而非 accuracy 的定位。

### Agent RL 训练技术爆发

ZJU-REAL 组（SDAR, SKILL0）和其他组密集产出 GRPO 改进方案，形成方法库。B-IAVR 可从中选取最优训练基础设施。

---

## 对 Novelty Claim 的影响

### 核心 novelty 安全
B-IAVR 的三线交汇（RL-trained + interactive agent + selective verification + action-change reward）**仍然独特**。扫描确认无论文占据这个交叉点。

### 建议微调 framing

1. **ALFWorld baseline 更新**：论文中需引用 PA-MoE (93.8%) 作为新 baseline，而非仅 GiGPO (86.1%)。这强化了我们的论点——accuracy 已饱和，cost-efficiency 才是下一个前沿。

2. **ARES 对比需加强**：ARES 仍是最近的竞争者。建议在 Related Work 中明确区分：
   - ARES：continuous effort allocation + SFT bootstrap + token efficiency reward
   - B-IAVR：binary verify/not-verify + pure RL + action-change reward
   - 强调 B-IAVR 无需 difficulty-annotated data 的优势

3. **Agent-Omit 互补性**：建议在论文中提及 Agent-Omit 作为互补方向（减 vs 加），暗示可组合。

4. **Credit assignment 工具**：HCAPO 的 hindsight credit assignment 可能对 B-IAVR 训练有帮助——verification decision 的 reward 信号稀疏，HCAPO 的方法可改善这一点。

### 无需调整的部分
- Self-Guide 作为 predecessor 的定位不变，无新的 follow-up 工作竞争
- "selective verification" 在 interactive agent 中的空白仍然存在
- Action-change signal 作为 verification trigger 仍无人提出

---

## 行动建议

1. **必须**：更新论文中 ALFWorld baseline 表格，加入 PA-MoE (93.8%)
2. **必须**：Related Work 中加入 SDAR、HCAPO、SKILL0 作为 agent RL training 的最新进展
3. **可选**：探索 HCAPO 的 credit assignment 方法用于 B-IAVR 的 verification reward 训练
4. **可选**：在实验中加入 Agent-Omit + B-IAVR 组合实验，展示互补性
