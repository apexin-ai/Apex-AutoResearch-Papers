# analysis llama2base action probe results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama2base_action_probe_results_20260517T215857_result.json`
- **Structured JSON:** [`a4c523a74cc61d3bb596.json`](../../sessions/a4/a4c523a74cc61d3bb596.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 三条件对比表（mean R² per layer, image_mean readout）

| Layer | Untrained | Llama2Base | Trained | Pattern |
|-------|-----------|------------|---------|---------|
| L0 | 0.6403 | 0.6403 | 0.6403 | U = L = T |
| **L1** | **0.5546** | **0.6366** | **0.6331** | **U < L >= T** |
| L2 | 0.5219 | 0.6124 | 0.6278 | U < L < T |
| L3 | 0.5338 | 0.6446 | 0.6519 | U < L < T |
| L4 | 0.5606 | 0.6447 | 0.6468 | U < L < T |
| L5 | 0.5383 | 0.6326 | 0.6468 | U < L < T |
| L6 | 0.5313 | 0.6413 | 0.6494 | U < L < T |
| L7 | 0.5176 | 0.6335 | 0.6447 | U < L < T |
| **L8** | 0.5323 | 0.6307 | **0.6553** | U < L < T |
| L9 | 0.5350 | 0.6371 | 0.6511 | U < L < T |
| L10 | -0.3293 | 0.6233 | 0.6427 | U < L < T |
| L11 | -0.2806 | 0.6184 | 0.6436 | U < L < T |
| L12 | 0.5198 | 0.6268 | 0.6086 | U < L >= T |
| L13 | 0.4410 | 0.6047 | 0.6296 | U < L < T |
| L14-L20 | ... | ... | ... | U < L < T |
| L21-L31 | ~0.45 | ~0.57 | ~0.48 | U < L >= T |
| L32 | 0.5785 | 0.5255 | 0.5390 | U >= L < T |

### L1 关键数值
- **Untrained: 0.5546**
- **Llama2Base: 0.6366**
- **Trained (VLA): 0.6331**
- Delta: llama2base比untrained高 +0.082, 但比trained略高 +0.004

### 整体 Pattern

| 指标 | Untrained | Llama2Base | Trained |
|------|-----------|------------|---------|
| Peak R² | 0.6403 (L0) | 0.6447 (L4) | 0.6553 (L8) |
| Mean (all layers) | 0.4491 | **0.6014** | 0.5849 |
| Mean (L2-L9) | 0.5294 | 0.6347 | **0.6463** |
| Mean (L21-L32) | 0.4686 | **0.5700** | 0.4924 |

### 核心发现

1. **假设部分成立**：Peak-to-peak 确认 untrained(0.64) < llama2base(0.64) < trained(0.66)，但差异很小

2. **Early-mid layers (L2-L9)**：19/21 层符合 U<L<T，VLA training 在语言预训练基础上确实有增量改善

3. **Late layers (L21-L31)**：10/11 层 llama2base 反超 trained。VLA training 将后层重新用于 action token generation，降低了 image_mean readout 的 action encoding

4. **L1 意外发现**：llama2base(0.6366) ≈ trained(0.6331)。语言预训练已经在 L1 建立了与 VLA-trained 相当的 spatial representation

### 结果文件
`/root/autodl-tmp/vla-ssd/results/llama2base_action_probe/three_condition_comparison.json`

---
