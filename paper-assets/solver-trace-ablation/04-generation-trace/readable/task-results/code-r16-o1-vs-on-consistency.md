# code r16 o1 vs on consistency

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r16-o1-vs-on-consistency_20260520T054719_result.json`
- **Structured JSON:** [`a7348e80e0bd25c391d1.json`](../../sessions/a7/a7348e80e0bd25c391d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果保存在 `artifacts/r16_o1_vs_on_consistency.json` 和服务器 `/root/autodl-tmp/outputs/r16_o1_vs_on_consistency.json`。

## 核心发现

**O(1) binary ISR 在 ProofWriter-FOL 上退化为常数 1.0。** 402 个 proved 样本中，没有任何一个 conclusion 是 tautology（空前提可证），因此 binary ISR 永远输出 1。Pearson/Spearman 相关系数因零方差无法计算。

### 数值摘要

| 模型类型 | N | Agreement (binarized) | MAE | Mean LOO ISR | Mean Binary ISR |
|----------|---|----------------------|-----|-------------|----------------|
| exec-only | 234 | 34.2% | 0.954 | 0.046 | **1.0** |
| ISR-trained | 168 | 85.1% | 0.817 | 0.183 | **1.0** |
| **Aggregate** | **402** | **55.5%** | **0.897** | — | **1.0** |

### 不一致的根本原因

所有 179 个 disagreement 都是同一 pattern：**FP（binary=1, LOO=0）**。

典型例子（exec_s42 的退化证明）：
- Premises: `nice(charlie)`, `nice(charlie)`
- Conclusion: `nice(charlie)`
- O(1) binary: conclusion 不是 tautology → ISR=1
- O(n) LOO: 两个 premise 互为冗余，删任一个仍可证 → n_necessary=0 → ISR=0

Binary check 无法检测到「premise 是 conclusion 的重复副本」这种 Conclusion Echo (CE) hacking，因为 ground fact 不是逻辑重言式。LOO 能正确识别出所有 premise 都是冗余的。

### 含义

1. **训练时的 O(1) binary ISR 实际上等价于 proof success check** — 对所有证明成功的样本一视同仁给 ISR=1，完全丢失了证明质量信息
2. **这解释了为什么 ISR reward 在训练中仍然有效** — 它通过「不给 tautology reward」来间接鼓励非平凡证明，但其判别力完全依赖 tautology 检测这一路径，而 ProofWriter 中 tautology 并不存在
3. **ISR 训练的实际效果可能来自其他间接信号**（如鼓励更长/更复杂的 formalization），而非直接的 premise necessity 判别

---
