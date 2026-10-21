# research reconvla deep read

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_reconvla-deep-read_20260513T222507_result.json`
- **Structured JSON:** [`e2f2b509617a09948283.json`](../../sessions/e2/e2f2b509617a09948283.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/reconvla-comparison-report.md`。

核心发现：

**ReconVLA 确实是最直接竞争者**——同样在 flow-matching VLA 上用 CP + K=10 samples 做 inference-time action improvement。但差异化在三个方法论层面成立：

1. **Scalar vs Per-DOF**：ReconVLA 将 7D action error 压缩为 1 个标量 Euclidean distance，丢失所有维度信息和协方差结构。ACR-VLA 保留 40D per-DOF conformal features。

2. **Selection vs Correction**：ReconVLA 只能从 K=10 candidates 中选最好的（argmin CQR bound），永远不修改 action。ACR-VLA 的 CRM 能合成优于任何单个 sample 的 action。

3. **Static vs Online Calibration**：ReconVLA 用 offline split conformal（部署后 $q_\tau$ 固定），ACR-VLA 用 ACI+COC 在线适应。

**重要纠正**：ReconVLA 不是简单的 Euclidean argmin——它训练了一个 CQR 神经网络做分位数回归。我们当前的 SampleConsensus baseline（raw Euclidean argmin）低估了 ReconVLA。

**建议**：
- 必须实现 **ReconVLA Medium baseline**（CQR + argmin，~6h 工作量），从论文可完整复现
- paper_framing.md 中 ReconVLA 描述需提高精度
- Framing 策略：不是 "better ReconVLA"，而是 "从 sample selection 到 uncertainty-conditioned correction 的范式跃迁"

Sources:
- [ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework](https://arxiv.org/abs/2604.16677)
- [ReconVLA HTML full text](https://arxiv.org/html/2604.16677v1)

---
