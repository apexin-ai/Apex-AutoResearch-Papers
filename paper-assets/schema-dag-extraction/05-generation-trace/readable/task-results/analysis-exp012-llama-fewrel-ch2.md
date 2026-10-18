# analysis exp012 llama fewrel ch2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp012_llama_fewrel_ch2_20260515T223657_result.json`
- **Structured JSON:** [`c7b75f0dbd8aa0a5e2cf.json`](../../sessions/c7/c7b75f0dbd8aa0a5e2cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp012 分析结果

**Channel 2 BCS effect 在 LLaMA-3.1-8B 上确认 — POSITIVE**

### 核心数据

| 条件 | Low BCS | High BCS | Δ | Qwen3 参考 |
|------|---------|----------|---|-----------|
| count=8 | 0.7812 | 0.5104 | **-27.1pp** | -31.2pp |
| count=16 | 0.7552 | 0.5156 | **-24.0pp** | N/A |

### 统计检验
- 全 54 batch BCS-accuracy 相关：**Pearson r=-0.39 (p=0.004), Spearman ρ=-0.43 (p=0.001)** — 显著
- Random batches 单独回归不显著（BCS 范围太窄 0.65–0.90，方差不够）
- 无 floor effect：均值 accuracy=0.77，范围 0.41–0.98

### 跨模型对比
- LLaMA Δ=-27.1pp ≈ Qwen3 Δ=-31.2pp 的 **87%**
- 两个模型方向一致、量级接近，BCS confusability effect 跨模型家族泛化

### 对论文的意义
- **跨模型复现成功**：BCS effect 不是 Qwen3 特异的，LLaMA-3.1-8B 同样表现出强烈的 schema confusability 效应
- 最强统计论据是 54 batch 整体相关（p<0.004），而非单 batch 对比
- 建议论文呈现：controlled comparison 给直觉（-27pp），overall correlation 给统计支撑

---
