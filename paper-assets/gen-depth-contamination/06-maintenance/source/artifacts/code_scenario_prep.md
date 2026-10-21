# Code Domain Scenario Analysis — Mistral-7B & Qwen-7B

> 生成日期：2026-05-19。用于 Mistral-7B (~19:00 UTC) 和 Qwen-7B (~20:30 UTC) 结果到达前的叙事预案。

## 当前状态

| Model | Family | K* | AUC(1v2) | Status |
|-------|--------|-----|----------|--------|
| Qwen-1.5B | Qwen | 2 | 0.7382 | done |
| LLaMA-8B | Meta | 2 | 0.7394 | done |
| Pythia-1.4B | EleutherAI | 1 | 0.5983 | done (capacity-limited) |
| Pythia scorer on Qwen | cross-scorer | 2 | 0.7180 | done (D079) |
| Mistral-7B | Mistral AI | ? | ? | ~19:00 UTC |
| Qwen-7B | Qwen | ? | ? | ~20:30 UTC |

当前叙事：Code ceiling=2, 2/3 completed models 达到 ceiling, Pythia capacity-limited (K*=1)。

---

## Mistral-7B Scenarios

### M-A: K*=2（最可能）

**证据预期**：1v2 AUC > 0.60 (CI lower > 0.60), 2v3 AUC < 0.60。

**对 paper 核心 claim 的影响**：
- Code ceiling K*=2 confirmed by 3/4 architecture families (Qwen, Meta, Mistral)
- Mistral C4 K*=1 anomaly 被定性为 domain-specific one-wash：Mistral 在 Code (K*=2) 和 arXiv (K*=3) 均达 ceiling, 唯独 C4 one-wash
- 强化 "domain structure sets ceiling, model competence determines if reached" 框架
- Mistral 成为 domain dependence 的极端案例：C4=1, Code=2, arXiv=3, 三域三值

**需要修改的 framing**：
- paper_framing.md Code domain 段落：更新为 "3/4 architecture families reach ceiling"
- Abstract 中 Code 描述：更新架构族数量
- 无需修改核心 claim, 仅更新计数

**具体文字修改**：
- "Code: X/Y models across Z architecture families reach ceiling K*=2"
- 加一句：Mistral-7B exhibits the most extreme domain dependence in our study: K*=1 (C4), K*=2 (Code), K*=3 (arXiv), demonstrating that the same model can span the full range of observed K* values depending on domain structure.

### M-B: K*=1

**证据预期**：1v2 AUC < 0.60。

**对 paper 核心 claim 的影响**：
- Mistral 在 C4 和 Code 均 one-wash, 但 arXiv K*=3
- 不是 competence 问题（arXiv K*=3 证明模型有能力）
- 需要新解释：Mistral 对非结构化文本（web/code）的处理与其他模型系统性不同
- Code ceiling claim 从 "3/4 families" 弱化为 "2/3 families" (Qwen + Meta), 但仍 majority
- 与 Pythia 区分：Pythia one-wash 是 capacity, Mistral one-wash 是 model-specific（有 arXiv 反例）

**需要修改的 framing**：
- 引入 "model-specific sensitivity to domain structure" 概念
- Mistral 段落改为：Mistral exhibits a binary pattern, reaching ceiling only for highly structured text (arXiv K*=3) while washing in one generation for less structured domains (C4 K*=1, Code K*=1)
- 不影响 domain ceiling 核心 claim（2/3 families 仍达 ceiling, Mistral 归入 model-specific exception）

**具体文字修改**：
- Code section 加 caveat：Model-specific variation exists, with Mistral showing one-wash behavior on both C4 and Code despite reaching K*=3 on arXiv
- 讨论部分加段：This model-specific pattern (always 1 or 3, never 2) may reflect Mistral's training data distribution or tokenizer behavior on non-academic text

### M-C: K*=3（低概率）

**可能原因**：数据质量问题、Code domain 的 Mistral tokenizer 特殊行为。
**需要行动**：检查数据质量（depth 分布、features 分布），确认不是 bug。如果确认 K*=3，需要重新审视 Code ceiling 假说（ceiling 可能不是 2 而是 3 for some models）。

---

## Qwen-7B Scenarios

### Q-A: K*=2（最可能）

**证据预期**：1v2 AUC > 0.60, 2v3 < 0.60。

**对 paper 核心 claim 的影响**：
- Qwen 家族 Code domain scale invariance confirmed (1.5B=7B=K*=2)
- 与 C4 的 Qwen scale invariance (1.5B/7B/14B/32B all K*=2) 一致
- 最强证据：同模型家族不同 scale 给出相同 K*, 说明 K* 不是 model size artifact

**需要修改的 framing**：
- 仅更新计数和表格
- Scale invariance 叙事不变，加一个 Code domain 数据点

**具体文字修改**：
- 表格中填入 Qwen-7B 数据
- Scale invariance 段落加 Code domain 支持

### Q-B: K*=1

**证据预期**：1v2 AUC < 0.60。

**对 paper 核心 claim 的影响**：
- Scale-dependent K* on Code: Qwen-7B Code K*=1 而 Qwen-1.5B Code K*=2
- 反直觉（更大模型反而更差），需要解释
- 可能原因：7B 模型在 Code continuation 中更倾向复制输入结构，导致 depth 信号更弱
- 需要检查 features 分布（是否 7B 的 surprisal 变化更小）

**需要修改的 framing**：
- Scale invariance claim 加 domain caveat：Code domain shows scale sensitivity absent in C4 and arXiv
- 弱化 "K* is scale-independent" 为 "K* is largely scale-independent, with minor scale sensitivity in Code domain"

### Q-C: K*=3（低概率）

类似 M-C，需检查数据质量。

---

## 组合 Scenarios（按影响排序）

| Mistral | Qwen-7B | 概率 | 对叙事的影响 | 行动 |
|---------|---------|------|------------|------|
| K*=2 | K*=2 | **最高** | 最强：4/5 models, 3/4 families 达 ceiling | 仅更新数字 |
| K*=2 | K*=1 | 中 | Code 出现 scale 问题，需解释 | 加 scale caveat |
| K*=1 | K*=2 | 中 | Mistral non-academic one-wash | 加 model-specific 讨论 |
| K*=1 | K*=1 | 低 | 仅 Qwen-1.5B + LLaMA-8B 达 ceiling (2/5) | 需调 framing |
| 含 K*=3 | — | 极低 | 需检查数据 | 先验证再定叙事 |

## 最优路径 (M-A + Q-A)

Code section 最终文字：

> Code domain mirrors the C4 ceiling of K*=2. Among five model configurations spanning four architecture families, four reach the ceiling (4/5 models, 3/4 families). Pythia-1.4B (K*=1) lacks sufficient code generation competence to reach the domain ceiling, consistent with its lower code-related training exposure. Mistral-7B, which shows K*=1 on C4, reaches K*=2 on Code, confirming that its C4 anomaly is domain-specific rather than model-intrinsic.

## 应急预案

如果出现意外结果（K*=3 或数据异常），不急于修改论文。步骤：
1. 检查数据完整性（depth 文件行数、features 分布）
2. 与同模型其他域结果对比
3. 汇报 Director，等指示
