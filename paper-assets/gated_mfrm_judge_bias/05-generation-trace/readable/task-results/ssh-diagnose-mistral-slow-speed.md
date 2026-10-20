# ssh diagnose mistral slow speed

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose_mistral_slow_speed_20260522T082205_result.json`
- **Structured JSON:** [`d51292965751f2787d2a.json`](../../sessions/d5/d51292965751f2787d2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**根本原因：模型本身大 1.75x，不可通过配置修复。**

架构对比：

| | Mistral-Large-2 | Llama-3.3-70B | Qwen2.5-72B |
|---|---|---|---|
| 参数量 | **~123B** | ~70B | ~72B |
| hidden_size | **12288** | 8192 | 8192 |
| 层数 | **88** | 80 | 80 |
| 注意力头数 | **96** | 64 | 64 |
| AWQ 权重 | **61 GB** | 38 GB | 39 GB |

生成脚本对三个模型完全一致（`MAX_TOKENS=2048`, `workers=8`, 无 model-specific 配置差异）。vLLM 启动参数也合理（`max-model-len=4096`, `gpu-memory-utilization=0.90`）。

**速度差异分析**：
- Mistral 每个 token 的计算量约为 70B 模型的 2-2.5x（hidden_size 宽 50% + 多 10% 层）
- 权重加载带宽需求 61/38 ≈ 1.6x
- KV cache 剩余空间：Mistral ~25 GB vs Llama/Qwen ~47-48 GB（但 8 并发下不构成瓶颈）
- 实测 3-5x 慢于 70B 模型，符合预期

**不可修复。** 无配置调优能让 123B 模型达到 70B 的速度。

**当前进度和 ETA**：
- Llama: 400/485, ~0.09/s → 约 **16 分钟**完成
- Qwen: 320/499, ~0.08/s → 约 **37 分钟**完成
- Mistral: 60/499, ~0.02/s → 约 **5.4 小时**完成

---
