# exp cross task bootstrap 119

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_cross-task-bootstrap-119_20260523T075027_result.json`
- **Structured JSON:** [`b73fa9ba301f07caae43.json`](../../sessions/b7/b73fa9ba301f07caae43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果文件：`data/cross_task_transfer_bootstrap_n1000.json`（25KB，三模型全部写入）。

---

## Bootstrap CI 报告（n=1000, 95% CI）

### 总运行时间
86.0 min（Llama 24.0min, Qwen 23.7min, Gemma 38.3min）

### 关键层分析

| Model | Layer | Direction | Mean | 95% CI | CI下界 >> 0.5? |
|-------|-------|-----------|------|--------|---------------|
| **Llama-3.1** | L13 | C→X | 0.9984 | [0.9925, 1.0000] | **是** (0.49 above chance) |
| **Llama-3.1** | L13 | X→C | 1.0000 | [1.0000, 1.0000] | **是** |
| **Qwen-3** | L23 | C→X | 0.9647 | [0.8950, 0.9950] | **是** (0.395 above chance) |
| **Qwen-3** | L23 | X→C | 1.0000 | [1.0000, 1.0000] | **是** |
| **Gemma-2** | L15 | C→X | 0.9682 | [0.9300, 0.9900] | **是** (0.43 above chance) |
| **Gemma-2** | L15 | X→C | 1.0000 | [1.0000, 1.0000] | **是** |
| **Gemma-2** | L17 | C→X | 0.9943 | [0.9850, 0.9975] | **是** |
| **Gemma-2** | L17 | X→C | 0.9943 | [0.9796, 0.9984] | **是** |
| **Gemma-2** | L21 | C→X | 0.7303 | [0.6525, 0.8275] | **是** (0.15 above chance) |
| **Gemma-2** | L21 | X→C | 0.9972 | [0.9874, 1.0000] | **是** |

### 结论

1. **没有任何一层的 CI 跨过 0.5**——所有关键层的跨任务迁移在统计上均显著。

2. **Gemma L21 C→X 是最弱的迁移**：mean=0.7303, CI=[0.6525, 0.8275]，CI 下界 0.6525 仍远高于 chance（0.5），但在所有关键层中最低。相邻的 L20 (CI=[0.7725, 0.9575]) 和 L22 (CI=[0.7050, 0.9075]) 也呈现类似的 C→X 下降趋势。

3. **X→C 方向一致性极强**：所有模型所有层的 X→C 迁移几乎都是 perfect（≥0.987），说明 XNLI 训练的语言探针在 Conflict 数据上泛化极好。

4. **C→X 方向在少数层出现下降**：主要是 Gemma L20-L22 区域，但即使最弱的也远超 chance。这可能反映 Conflict 数据在这些层的语言表示编码较弱，但仍携带足够的语言信号。

5. **Llama 最强**：所有层 CI 下界 ≥ 0.9699，跨任务迁移几乎完美。

---
