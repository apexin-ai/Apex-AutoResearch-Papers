# ssh output head analysis

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_output-head-analysis_20260515T200957_result.json`
- **Structured JSON:** [`00b60b13d7a9b33e7bcd.json`](../../sessions/00/00b60b13d7a9b33e7bcd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已保存 (340KB)。结果如下：

---

## Output Head Analysis 结果

### 1. 各组平均差异

| Group | Count | Rel Change (mean±std) | Cosine Sim | Max Rel Change |
|-------|------:|----------------------|------------|----------------|
| **vision** | 685 | 0.0000±0.0000 | 1.0000 | 0.0000 |
| **projector** | 6 | 0.0000±0.0000 | 1.0010 | 0.0000 |
| **embedding** | 1 | 1.3287 | -0.0001 | 1.3287 |
| **llm** | 288 | 1.3156±0.3759 | 0.2178 | 1.8160 |
| **llm_final_norm** | 1 | 0.8628 | 0.9980 | 0.8628 |
| **head (lm_head)** | 1 | 1.4754 | 0.0002 | 1.4754 |

### 2. Vision encoder 验证
**Vision backbone 和 Projector 权重完全相同** (rel_change=0, cos_sim=1.0)。Untrained model 不仅保留了 SigLIP，也保留了 projector。只有 LLM 部分被重新初始化。

### 3. Top-10 差异最大的层
全部是 **LLM 早期层 (Layer 1-10) 的 self_attn q_proj/k_proj**，rel_change 1.74-1.82。

### 4. LLM 各层差异分布
**高度均匀**。rel_change 在所有 32 层间范围 1.22-1.37，cos_sim 在 0.13-0.22。没有任何层（包括 head）表现出显著更大的差异。

### 5. 关键发现

**不支持 "shallow adaptation" 假说。** Head 的 rel_change (1.4754) 仅比 LLM 均值 (1.3156) 高 ~12%，差异分布在整个 LLM 是均匀的。

但需要注意：这个比较是 **pretrained Llama + fine-tune vs random init**，差异被 pretrained vs random 主导。要精确量化 fine-tuning 改了哪里，需要对比 trained vs pretrained Llama base（fine-tuning 前后）。当前分析能确认的是：
- Projector 权重在两个模型间完全相同
- LLM 权重差异均匀分布在所有层，head 并无特殊地位
- 这与前 6 轮实验结果一致：trained 和 untrained 的内部表征结构相似，不是因为两者权重接近（权重差异极大），而是因为 vision backbone + projector 相同迫使了相似的表征结构

---
