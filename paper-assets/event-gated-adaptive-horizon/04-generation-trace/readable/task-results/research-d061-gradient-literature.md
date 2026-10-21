# research d061 gradient literature

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_d061-gradient-literature_20260516T014530_result.json`
- **Structured JSON:** [`4d9737564af15e065057.json`](../../sessions/4d/4d9737564af15e065057.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成并注册。核心结论：

**新颖性定位**：
- "Reconstruction 主导 representation" 是**已知**结论（DreamerV3 消融 + HarmonyDream 量化了 2 个数量级的 loss 差异）
- 但我们的三个贡献是**新颖**的：
  1. **梯度级别定量分解**（93%/7%/0%）——文献仅分析 loss 量级，未做 backward pass 分解
  2. **Reward head 梯度贡献精确为 0%**——比 "reward loss 小两个数量级" 更强的结论
  3. **Stop-gradient 作为因果诊断工具**识别 architectural no-op——无直接先例

**016e section 必须引用**：Hafner et al. 2023（DreamerV3 消融）、Shang et al. 2024（HarmonyDream loss 量级差异）、Chen et al. 2018（GradNorm 方法论基础）。

---
