# research grpo forgetting recovery

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_grpo_forgetting_recovery_20260514T222706_result.json`
- **Structured JSON:** [`ef145b6261e3475b0b0f.json`](../../sessions/ef/ef145b6261e3475b0b0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。以下是结果摘要。

---

## 5 篇核心论文

### 1. Mitigating the Alignment Tax of RLHF (EMNLP 2024)
Lin et al. | [arXiv 2309.06256](https://arxiv.org/abs/2309.06256)

RLHF 导致模型遗忘 SFT 能力（alignment tax）。发现**模型权重插值**（SFT 与 RLHF checkpoint 线性插值）在 alignment-forgetting Pareto 前沿表现最优。提出 HMA 对不同层设不同插值比例。

### 2. Online Merging Optimizers for Boosting Rewards and Mitigating Tax (2024)
Qwen 团队 | [arXiv 2405.17931](https://arxiv.org/abs/2405.17931) | [GitHub](https://github.com/QwenLM/online_merging_optimizers)

在 RLHF 每个优化步实时合并 RL policy 和 SFT 参数，将梯度方向锚定在 SFT 优化方向上。Qwen/LLaMA 1.8B-8B + DPO/KTO 上验证，14 个 benchmark 同时提升 reward 并降低 alignment tax。

### 3. FRPO: Robust Policy Optimization to Prevent Catastrophic Forgetting (2025)
Sabbaghi et al. | [arXiv 2602.08813](https://arxiv.org/abs/2602.08813)

修改 GRPO 的 advantage 计算，加入 entropic risk 项——强调低 reward 轨迹，抑制高方差策略。**无额外计算开销**，直接替换 GRPO 即可。核心论点：标准 GRPO 找到的高 reward 解是脆弱的。

### 4. RL-Struct: Structured Output + GRPO (2025)
[arXiv 2512.00319](https://arxiv.org/abs/2512.00319)

针对 JSON 结构化输出 + RL 的挑战，提出**分层 reward**（structure → format → content → validity）。4B 模型上 1000 样本达 80%+ 结构准确率。解决单一 reward 让模型在格式和内容间混淆的问题。

### 5. GRPO + LoRA 不稳定性（综合多源）
[GRPO++ blog](https://cameronrwolfe.substack.com/p/grpo-tricks) | [HF GRPO+LoRA handbook](https://huggingface.co/blog/Weyaxi/engineering-handbook-grpo-lora-with-verl) | [arXiv 2504.20834](https://arxiv.org/abs/2504.20834)

**已知问题**：GRPO + LoRA 低秩更新时 advantage 估计方差增大，TRL 默认 KL β=0.0，策略易大幅偏离。Full-token GRPO 在 LoRA 下"未能提升性能"。建议 β≥0.01、rank≥16、lr~1e-6。

---

## 综合诊断

你们的"先崩后恢复"是 **三因素叠加**：

1. **Alignment tax**：GRPO 梯度覆盖 SFT 关系抽取能力，rank=4 的 LoRA 参数同时承载旧能力和新优化目标，冲突剧烈
2. **KL 约束过弱（β=0.001）+ 低秩放大不稳定性**：策略快速偏离 SFT 分布，训练前 20 步即崩塌
3. **Reward proxy mismatch**：reward↑ 但 F1↓ 是经典 reward hacking——模型可能学会生成格式正确但关系错误的输出

U 型恢复的原因：崩塌后模型在新策略空间中缓慢重新发现部分抽取模式，但 LoRA 容量不足 + reward 噪声导致恢复不完全。

---

## 最值得尝试的 2 个方案

| | 方案 A：增强正则化 | 方案 B：分层 Reward |
|---|---|---|
| 改动 | KL β: 0.001→0.04, rank: 4→16, lr: 5e-6→1e-6 | reward 拆为 format + entity + relation，分权重 |
| 成本 | 低（改配置即可） | 中（需重写 reward 函数） |
| 针对问题 | 策略偏离过快 | reward hacking |
| 优先级 | **先试这个** | A 不够再加 |

备选方案 C：集成 Qwen 团队的 Online Merging Optimizer，每步锚定 SFT 方向，实现复杂度中等但同源验证过。

已将完整调研存入 `memory.md`，三个缓解方案存入 `ideas.md`。

---
