# analysis format compliance

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_format_compliance_20260522T113503_result.json`
- **Structured JSON:** [`dd8547d7beb6dd7846b7.json`](../../sessions/dd/dd8547d7beb6dd7846b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部拿到。汇总如下。

## W1 Format Compliance 分析结果

### 7B 模型 · 20% 剪枝率（主实验）

| Method | N | Accuracy | EOS Rate | Avg Len | Boxed Rate |
|--------|-----|----------|----------|---------|------------|
| **Dense (unpruned)** | 1319 | 90.83% | 98.71% | 594.0 | 0.00% |
| CKA-only SFT | 1319 | 63.91% | 99.01% | 198.1 | 0.00% |
| CKA-only GRPO | 1319 | 64.37% | 99.24% | 190.5 | 0.00% |
| Standard SFT | 1319 | 59.21% | 98.48% | 206.7 | 0.08% (1) |
| Standard GRPO | 1319 | 59.44% | 98.03% | 227.1 | 0.23% (3) |
| RASP SFT | 1319 | 61.49% | 98.26% | 216.5 | 0.00% |
| RASP GRPO | 1319 | 60.88% | 98.79% | 195.7 | 0.00% |
| Unstructured GRPO | 1319 | 87.64% | 98.18% | 600.0 | 0.08% (1) |

### 7B · 15% 剪枝率

| Method | N | Accuracy | EOS Rate | Avg Len | Boxed Rate |
|--------|-----|----------|----------|---------|------------|
| CKA-only SFT | 1319 | 72.18% | 99.01% | 200.3 | 0.00% |
| CKA-only GRPO (v2) | 1319 | 73.09% | 98.94% | 202.4 | 0.00% |
| Standard SFT | 1319 | 66.49% | 99.32% | 183.4 | 0.08% (1) |
| Standard GRPO (v2) | 1319 | 66.11% | 99.32% | 184.5 | 0.08% (1) |

### 1.5B 模型 · 20% 剪枝率

| Method | N | Accuracy | EOS Rate | Avg Len | Boxed Rate |
|--------|-----|----------|----------|---------|------------|
| CKA-only SFT | 1319 | 35.63% | 95.07% | 336.8 | 0.00% |
| CKA-only GRPO | 1319 | 35.48% | 94.69% | 349.5 | 0.00% |
| Standard SFT | 1319 | 22.90% | 90.45% | 516.7 | 0.00% |
| Standard GRPO | 1319 | 22.29% | 90.52% | 514.8 | 0.08% (1) |
| RASP SFT | 1319 | 26.91% | 94.16% | 378.6 | 0.00% |
| RASP GRPO | 1319 | 26.16% | 93.78% | 392.7 | 0.00% |

### 关键发现

1. **Boxed rate 对所有方法（含 dense）均为 ~0%**。DeepSeek-R1-Distill-Qwen-7B 的 SFT/GRPO 输出不使用 `\boxed{}` 格式，这不是一个有区分度的指标。

2. **EOS rate（非截断率）是更有意义的 format compliance 指标**：
   - 7B 全部方法都在 **98-99%+**，与 dense baseline（98.71%）基本一致
   - 1.5B 模型 EOS rate 略低（90-95%），但 CKA-only 方法（~95%）显著优于 Standard（~90%）
   - 结论：**结构化剪枝不会降低 format compliance**

3. **Avg response length**：pruned 模型显著短于 dense（~190-230 vs ~594 tokens）。这是 SFT/GRPO 训练教会了简洁回答，而非格式退化。Unstructured GRPO（600 tokens）保持了与 dense 相似的长度。

4. **无 Random / Depth-first 的 eval 文件**。Qwen cross-architecture 文件（N=200, EOS 27-37%）结构不同，未列入主表。

---
