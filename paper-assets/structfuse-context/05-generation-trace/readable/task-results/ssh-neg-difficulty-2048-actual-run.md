# ssh neg difficulty 2048 actual run

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_neg_difficulty_2048_actual_run_20260513T224719_result.json`
- **Structured JSON:** [`6ede0559af85baa7b8fd.json`](../../sessions/6e/6ede0559af85baa7b8fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全，`stats_v3_2048.json` 实际已存在。以下是完整对比分析。

---

## 128 vs 2048 Token 对比结果

### 1. 完整 2048-Token 结果

| Strategy | Encoder | Pos Sim | Neg Sim | Margin | Margin Std | %Pos>Neg |
|---|---|---|---|---|---|---|
| Random | Qwen | **0.9855** | 0.9111 | 0.0743 | 0.2322 | 81.8% |
| Random | StarCoder | 0.7985 | 0.6045 | 0.1940 | 0.2788 | 78.0% |
| Embedding Distance | Qwen | **0.9855** | 0.9685 | 0.0170 | 0.1140 | 58.8% |
| Embedding Distance | StarCoder | 0.8079 | 0.7409 | 0.0670 | 0.2056 | 55.0% |
| Dataflow-Aware | Qwen | **0.9856** | 0.9563 | 0.0293 | 0.1407 | 73.9% |
| Dataflow-Aware | StarCoder | 0.8009 | 0.6818 | 0.1192 | 0.2264 | 70.4% |

### 2. 关键对比：Qwen pos_sim

| Strategy | 128-token | 2048-token | Delta |
|---|---|---|---|
| Random | 0.9804 | **0.9855** | **+0.0051** |
| Embedding Distance | 0.9804 | **0.9855** | **+0.0051** |
| Dataflow-Aware | 0.9805 | **0.9856** | **+0.0051** |

### 3. Margin 对比

| Strategy | Encoder | 128-token | 2048-token | Delta |
|---|---|---|---|---|
| Random | Qwen | 0.0816 | 0.0743 | -0.0073 |
| Random | StarCoder | 0.2039 | 0.1940 | -0.0099 |
| Embedding Distance | Qwen | 0.0209 | 0.0170 | -0.0039 |
| Embedding Distance | StarCoder | 0.1159 | 0.0670 | **-0.0489** |
| Dataflow-Aware | Qwen | 0.0309 | 0.0293 | -0.0016 |
| Dataflow-Aware | StarCoder | 0.1022 | 0.1192 | +0.0170 |

### 4. StarCoder/Qwen Margin Ratio

| Strategy | 128-token | 2048-token |
|---|---|---|
| Random | 2.50x | 2.61x |
| Embedding Distance | 5.54x | 3.94x |
| Dataflow-Aware | 3.30x | 4.07x |

---

## 核心结论

**Qwen pos_sim 在 2048 tokens 下为 0.9855，比 128-token 的 0.9804 反而更高（+0.005）。**

这明确回答了核心问题：

- Ceiling **不是**截断 artifact。增加 token 长度到 2048 后 pos_sim 不降反升。
- Ceiling 是 **Qwen 表征的结构性特征**——Qwen2.5-Coder-3B 的 pretrained representation space 将同仓库代码片段映射到极其接近的区域（cos_sim > 0.985），无论截断长度如何。
- 作为对照，StarCoder pos_sim 从 0.757-0.784（128t）上升到 0.799-0.808（2048t），变化幅度更大（+0.02~0.04），但绝对值远低于 Qwen，说明两个编码器的表征几何结构根本不同。

**对 D021 结论的影响**：

2048-token 结果**加强**了原有结论——Qwen 的 similarity ceiling 是其 pretrained representation 的内在属性，不是分析方法的 artifact。这使得 StructFuse 在 Qwen 上的 margin improvement 更有意义：在一个 pretrained space 几乎无法区分同仓库代码的编码器上，训练仍然能拉开正负样本距离。

---
