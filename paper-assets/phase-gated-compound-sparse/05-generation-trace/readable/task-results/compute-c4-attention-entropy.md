# compute c4 attention entropy

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_compute_c4-attention-entropy_20260514T070654_result.json`
- **Structured JSON:** [`1fefab85532c5f971b18.json`](../../sessions/1f/1fefab85532c5f971b18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Problem 3 是 intermediate_algebra，正在生成长推理链（可能 2048 tokens，需要 ~2 分钟）。实验已稳定运行，无报错。

---

## 实验设计说明

**目标**：直接测量 head pruning 对 attention entropy 和 KV importance discrimination 的影响，验证 C4 claim（entropy-discrimination collapse mechanism）。

**实验流程**（每个问题）：
1. 生成推理 trace（greedy，max 2048 tokens）
2. 基于 quantile 分割为 3 个 phase（low/mid/high sparsity）
3. Dense forward (`output_attentions=True`) → 基线 entropy + head/KV importance
4. 对每个 sparsity level (0.15, 0.20, 0.25, 0.30)：
   - **Importance-pruned** forward → 测量 active heads 的 entropy 变化
   - **Random-pruned** forward → 对照组
5. 计算 per-layer 和 phase-conditioned metrics

**核心度量**：
- **Attention entropy delta**：pruned vs dense 每层平均 entropy 变化（importance 预期更大增幅 → entropy collapse）
- **KV importance Gini delta**：pruning 后 importance 分布的集中度变化（importance pruning 预期 Gini 下降 → discrimination 丧失）
- **CV delta**：importance 分布变异系数变化
- **Phase-conditioned analysis**：low_sparsity phase（distributed attention）预期效应最强

**预期结果**：
- Importance pruning → attention entropy 显著上升（尤其 low-sparsity phase）→ KV importance Gini 下降
- Random pruning → entropy 变化平坦或对称 → Gini 无系统性变化
- 差异随 sparsity level 增大而加剧

**配置**：
- 模型：DeepSeek-R1-Distill-Qwen-7B (bf16, eager attention)
- 数据：MATH-500 stratified 30 problems (6/level)
- GPU：cuda:1 (RTX PRO 6000 Blackwell, 96GB)
- tmux session：`c4_entropy`

**提交状态**：已提交运行，前 2 个问题分别 12s、25s 完成，预计总运行 ~30-60 min（多数问题序列 <1000 tokens，部分 2048 tokens 的需要更长生成时间）。

**产出路径**：`/root/autodl-tmp/pacs/results/c4_attention_entropy/c4_entropy_results.json`

---
