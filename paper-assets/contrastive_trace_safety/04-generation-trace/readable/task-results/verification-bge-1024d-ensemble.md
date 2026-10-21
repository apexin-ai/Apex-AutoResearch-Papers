# verification bge 1024d ensemble

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verification_bge_1024d_ensemble_20260523T112237_result.json`
- **Structured JSON:** [`91703fd6008db2ff300f.json`](../../sessions/91/91703fd6008db2ff300f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 文件已复制到本地。以下是验证报告。

---

## 验证报告

### 可验证范围

4 个模型中，**仅 R1-8B** 的 hidden states 存在于 westd-15904 服务器上。OT-7B、QwQ-32B、R1-32B 的 hidden states 均不存在。

### 数据不一致性（关键发现）

服务器上的 `hidden_states_r1_8b_full/` 目录包含 **25 层 (L0-L24)**，与论文使用的 `hidden_states/` 目录 (**13 层 L12-L24**) 不同。原始数据目录已不在服务器上。对所有 25 层做 precision sweep，最高值为 0.585 (idx=19)，无法达到论文的 0.629。这表明两个数据集来自不同的提取流程。

### Task 4: BGE-1024d 文本编码器对比 (R1-8B)

| 指标 | 本次验证 | 论文值 |
|------|---------|--------|
| HS Precision | 0.539 | 0.629 |
| BGE-1024d Text Precision | 0.514 | 0.429 |
| ΔPrec (pp) | **+2.4** | **+5.8** |
| Bootstrap p | 0.044 | — |

**方向一致**（HS > Text），但绝对值因数据提取差异而偏移。HS precision 低于论文，text precision 高于论文，导致 gap 缩小。

### Task 5: 3-metric Ensemble Holdout (R1-8B)

| 指标 | 本次验证 | 论文值 |
|------|---------|--------|
| Ens Precision | 0.623 | 0.565 |
| Text Precision | 0.449 | 0.272 |
| Ens−Text (pp) | **+17.3** | **+19.3** |
| Bootstrap p | 0.067 | ≤0.002 |

Ensemble 选层：L14 (precision-best), L12 (BA-best), L13 (FPR-best)。方向一致，但 p 值偏高（0.067 vs ≤0.002），与数据差异一致。

### 缺失数据与重现步骤

要完整重现论文结果，需要：

1. **原始 hidden_states 目录**（R1-8B, 13 层 L12-L24）— 已不在服务器上。需用原始提取代码重新从 R1-8B 模型提取，或从备份恢复。
2. **OT-7B hidden states** — 需从 OpenThinker-7B 模型提取 (对应层范围待确认)。
3. **QwQ-32B hidden states** — 需从 QwQ-32B-preview 模型提取 (L63 为目标层)。
4. **R1-32B hidden states** — 需从 DeepSeek-R1-32B 模型提取 (L63 为目标层)。
5. **Text embedding .pkl 文件** — MiniLM-384d 和 BGE-1024d 的预计算 embeddings，可用验证脚本中的编码逻辑重新生成。

---
