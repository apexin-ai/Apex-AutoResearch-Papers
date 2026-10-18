# exp r3n5 strategy classify

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_r3n5_strategy_classify_20260516T045604_result.json`
- **Structured JSON:** [`0d4fdade4a4686b9f591.json`](../../sessions/0d/0d4fdade4a4686b9f591.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果

### Part 1: 策略分类 Accuracy

| Model | Accuracy | nucleus recall | temp09 recall | topk50 recall |
|-------|----------|---------------|---------------|---------------|
| Pythia-1.4B | **52.3%** | 53.3% | 41.4% | 62.2% |
| OLMo-1B | **54.8%** | 60.8% | 47.9% | 55.8% |
| GPT-2 XL | **65.4%** | 84.5% | 50.7% | 61.0% |
| **Mean** | **57.5%** | | | |

策略分类准确率偏低（chance=33.3%），三种策略的特征分布存在大量重叠。

### Part 2 & 3: Depth Estimation Pipeline 对比

| Method | Pythia | OLMo | GPT-2 XL | **Mean** |
|--------|--------|------|----------|----------|
| Cross-strategy LOO (ref) | 61.2% | 59.5% | 56.6% | **59.1%** |
| **Predicted two-stage** | 69.3% | 69.5% | 73.0% | **70.6%** |
| Naive pooled | 70.9% | 71.2% | 73.9% | **72.0%** |
| Oracle two-stage | 74.6% | 78.5% | 82.0% | **78.4%** |
| Within-strategy (ref) | 74.5% | 78.4% | 81.6% | **78.2%** |

### 结论

**Two-stage pipeline 理论上可行（oracle: 78.4%），但实际不如 naive pooling（70.6% < 72.0%）。**

- Oracle two-stage（78.4%）≈ within-strategy（78.2%），验证了"已知策略 → 用专属分类器"的理论上限
- Predicted two-stage（70.6%）比 cross-strategy LOO（59.1%）高 +11.5pp，但比 naive pooled（72.0%）低 1.4pp
- 瓶颈在策略分类：仅 57.5% 准确率，错误传播导致 7.7pp 损失（oracle → predicted）
- **Rebuttal 论点**：(1) oracle 实验证实 two-stage 架构的理论价值 (+19.3pp over LOO)；(2) 统计特征不足以区分策略，需要辅助元数据（如 generation config）才能实现；(3) 实际部署中 naive pooled 是更稳健的选择

产出文件：`results/two_stage_pipeline_results.json`（服务器上）

---
