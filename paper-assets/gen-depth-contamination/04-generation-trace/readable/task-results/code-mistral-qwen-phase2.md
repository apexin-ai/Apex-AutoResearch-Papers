# code mistral qwen phase2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mistral_qwen_phase2_20260523T012707_result.json`
- **Structured JSON:** [`e56b5b38a2fabc81b9f9.json`](../../sessions/e5/e56b5b38a2fabc81b9f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job complete. Here are the results:

## Mistral-7B Qwen2.5-1.5B Cross-Scoring Results

### Pairwise AUC (θ = 0.60)

| Pair | Self-scored (Mistral) | Cross-scored (Qwen) | Δ |
|------|----------------------|--------------------|----|
| 0v1 | 0.9843 | **0.9170** | −0.0673 |
| 1v2 | 0.5935 | **0.5750** | −0.0185 |
| 2v3 | 0.5402 | **0.5369** | −0.0033 |
| 3v4 | 0.5232 | **0.5174** | −0.0058 |
| 4v5 | 0.5181 | **0.5175** | −0.0006 |

### K* 判定

**K\* = 1**（与 self-scored 一致）。0v1 远超 θ=0.60，1v2 < 0.60，后续对均在 chance 附近。

### Self-scored vs Cross-scored 对比

- **0v1 Δ = −0.067**：cross-scored 下降明显但仍极高 (0.917)，说明 depth-0→1 的信号在 scorer 间高度稳健
- **1v2 Δ = −0.019**：cross-scored 略降，两者都低于 θ，不影响 K* 判定
- **深层 (2v3–4v5)**：Δ 趋近于 0，均在 chance 水平，scorer 无实质差异

### Bootstrap CI

Pipeline 未输出 bootstrap CI，仅提供 5-fold CV std：0v1 ± 0.006, 1v2 ± 0.004, 2v3 ± 0.009, 3v4 ± 0.010, 4v5 ± 0.011。

### 结论

Cross-scoring 统一修正后，Mistral-7B 的 K*=1 结论不变。0v1 AUC 从 0.984 降至 0.917（−6.7pp），符合预期——self-scoring 存在轻微膨胀。论文主表应更新 Mistral-7B 行为 cross-scored 值：**0v1 = 0.917, 1v2 = 0.575**。

---
