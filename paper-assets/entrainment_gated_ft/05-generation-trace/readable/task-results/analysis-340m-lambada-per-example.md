# analysis 340m lambada per example

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_340m-lambada-per-example_20260521T132510_result.json`
- **Structured JSON:** [`c56d5c645b14be9f2b6d.json`](../../sessions/c5/c56d5c645b14be9f2b6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 已注册 (`art_20260521_4c5bb3`)。

### 340M LAMBADA 关键发现

**A) Ambiguity α**：pure α=0.313，随 attention ratio 递减至 h3-1 的 0.266。与 1.3B (0.307) 几乎相同。

**B) Per-example classification**：
- **HGRN2** 是唯一从 attention 中净受益的架构（net +93 ~ +275），与 1.3B 一致
- **GDN** 反而受损严重（net -127 ~ -259），attention 使其丢失更多样本
- **RetNet** 接近持平但微负（-4 ~ -106）

**C) Jaccard**：均值 J=0.0888（1.3B: 0.095），同样很低。所有 permutation test p<0.01（显著但 effect size 极小，ES_normalized 仅 0.03-0.10），确认不同架构被 help/hurt 的样本几乎不重叠。

**D) Convergence σ**：340M 的 ρ=-0.5, p=0.45（**不显著**），与 1.3B 的 ρ=-1.0, p=0.017 形成对比。σ 序列为 [0.025, 0.012, 0.018, 0.011, 0.016]——非单调递减，h12-1 出现反弹。这说明 340M 尺度下 aggregate convergence 尚未建立，decoupling 现象在更大模型上才出现。

---
