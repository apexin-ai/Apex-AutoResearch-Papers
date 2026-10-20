# research literature related work

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-related-work_20260516T021630_result.json`
- **Structured JSON:** [`5c13635d06408d0f93a5.json`](../../sessions/5c/5c13635d06408d0f93a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已更新。以下是调研摘要：

---

## 调研摘要

### 引用信息修正
- **Q-BLoRA** (TACL 2025, arXiv:2407.17029): 作者修正为 Ao Shen, Qiang Wang, Zhiquan Lai, Xionglve Li, Dongsheng Li（原误为 Shinhyuk Seo）
- **QuRL** (arXiv:2602.13953): venue 确认为 **ICLR 2026**，作者补全为 Yuhang Li, Reena Elangovan, Xin Dong, Priyadarshini Panda, Brucek Khailany

### 新增 9 篇论文，分布在 4 个新 category：

**Category 32: Quantization + RL Precision Mismatch（3 篇，支撑 C2）**
- **FP8-RL** (2601.18150): FP8 rollout 偏离高精度 policy 导致 train-inference mismatch，KL 随训练累积 → 直接映射 QLoRA 精度不对称
- **Jet-RL** (2601.14243, MIT/NVIDIA): BF16-train + FP8-rollout 导致 catastrophic accuracy collapse → 支持 C2 "bf16 下不复现 decoupling" 的观察
- **BitRL** (2604.24273): 1-bit 量化下 RL 的理论分析，将量化建模为 structured perturbation，推导收敛界

**Category 33: Multi-Task LoRA Decoupling（3 篇，支撑 C2/C3）**
- **FlyLoRA** (NeurIPS 2025, 2510.08396): rank-wise MoE 实现 task decoupling，正交 random projection 减少 inter-task 干扰 → LoRA rank 不足导致任务竞争的直接证据
- **BADIT** (ICML 2026, 2605.05676): LLM 编码正交 basic abilities，tasks = abilities 的线性组合 → C2 的 formal framework（低 rank 无法同时表达多组 abilities）
- **TSSR** (Machine Learning 2025): 任务子网络独立运作、重叠极少 → QLoRA 受限空间下子网络自发分离

**Category 34: Multi-Task RL Gradient Imbalance（2 篇，支撑 C2/C3）**
- **Imbalanced Gradients** (Findings of EACL 2026, 2510.19178, Meta AI): 多任务 RL 中 gradient magnitude 与 learning gains 不相关，某些任务主导更新 → RE 可能压制 evidence learning
- **Stabilizing RL with LLMs** (2512.01374, Alibaba Qwen): 理论证明 token-level surrogate 有效的前提是 train-inference discrepancy 最小化 → QLoRA 量化违反此前提

**Category 35: Faithfulness Decay & Evidence Grounding（1 篇，支撑 C1/C4）**
- **Faithfulness Decay in CoT** (2602.11201): 推理链存在 Reasoning Horizon (70-85%)，超过后 token 对答案无影响 → 与 EDCR 诊断的 faithfulness 退化类似
- **FACTS Grounding Leaderboard** (2501.03200, Google DeepMind): 最佳 LLM grounding 得分 ~0.88，验证 faithfulness 约束带来 performance cost (C1)

### 与各 Claim 的关系
| Claim | 支撑论文 | 关系 |
|-------|---------|------|
| C1 (faithfulness 成本 ~8pp) | FACTS Grounding, Faithfulness Decay | 验证 faithfulness 约束普遍带来 performance cost |
| C2 (QLoRA GRPO decoupling) | FP8-RL, Jet-RL, BitRL, FlyLoRA, BADIT, TSSR, Imbalanced Gradients, Stabilizing RL | 多角度解释精度不对称 + rank 不足导致 decoupling |
| C4 (EDCR 诊断) | Faithfulness Decay | faithfulness decay 的诊断方法论类比 |

---
