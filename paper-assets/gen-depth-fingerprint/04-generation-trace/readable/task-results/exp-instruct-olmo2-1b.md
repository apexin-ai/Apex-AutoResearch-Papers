# exp instruct olmo2 1b

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_instruct-olmo2-1b_20260518T032633_result.json`
- **Structured JSON:** [`61eac6ba338288aef4a0.json`](../../sessions/61/61eac6ba338288aef4a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_053 结果

**注意**: `allenai/OLMo-2-1B-0725-Instruct` 不存在于 HuggingFace，使用已有的 `allenai/OLMo-2-0425-1B-Instruct` 数据（995 seeds, 4429 records）完成评估。服务器只有 1 张 GPU (RTX 5090)，不存在 cuda:2。

### OLMo-2-0425-1B-Instruct

| Metric | Instruct | Base | Delta |
|--------|----------|------|-------|
| Binary F1 (gen-1 vs gen-2+) | **0.8131** [0.8012, 0.8251] | 0.8454 [0.8358, 0.8554] | **-0.032** |
| 3-class macro F1 | **0.5748** [0.5605, 0.5897] | 0.7538 [0.7412, 0.7662] | **-0.179** |

### Spearman ρ 方向反转

**6/7 特征方向反转** — instruct 模型的深度信号方向与 base 完全相反：

| Feature | Instruct ρ | Base ρ | Direction |
|---------|-----------|--------|-----------|
| entropy_mean | **+0.482** | -0.639 | **REVERSED** |
| entropy_std | **+0.296** | -0.296 | **REVERSED** |
| entropy_min | **+0.080** | -0.387 | **REVERSED** |
| entropy_max | +0.306 | +0.067 | same |
| tail_decay | **+0.228** | -0.141 | **REVERSED** |
| ttr | +0.006 | -0.700 | **REVERSED** |
| hapax_ratio | +0.025 | -0.712 | **REVERSED** |

Base 模型中 entropy/TTR/hapax 随深度递减（文本趋向重复），instruct 模型中 entropy 反而随深度递增。ttr 和 hapax_ratio 在 instruct 中接近零相关（信号坍缩）。3-class F1 下降 17.9 个百分点，主要因为 gen-1 类 F1 从 0.523 暴跌到 0.256。

---
