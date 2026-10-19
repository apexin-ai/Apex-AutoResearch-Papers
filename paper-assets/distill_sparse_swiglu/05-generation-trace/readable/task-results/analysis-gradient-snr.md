# analysis gradient snr

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gradient_snr_20260517T040234_result.json`
- **Structured JSON:** [`0947c12eb3bc98ed91fd.json`](../../sessions/09/0947c12eb3bc98ed91fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果：

**Gradient SNR (KL vs BCE) — 80 steps on LLaMA-3.1-8B + C4**

| Metric | KL | BCE | Ratio |
|--------|-----|-----|-------|
| Avg SNR | 5.77×10⁻⁵ | 1.00×10⁻⁵ | **5.76×** |

关键发现：
- **早期层（0-4）差异最大**：KL 的 SNR 比 BCE 高 34-156×，因为 KL 的 end-to-end gradient 让早期 predictor 接收到来自最终输出分布的强信号，而 BCE 对早期层的梯度几乎为零（local target 信息太局部）
- **后期层（27-31）差异缩小到 2-4×**：后期层更接近输出，两种 loss 都能提供有意义的梯度
- **KL 的 SNR 随训练增长**：从 step 1 的 9e-6 增长到 step 30 的 9.5e-5，说明优化信号随着 mask 学习越来越清晰
- **BCE 的 SNR 快速衰减**：step 10 后基本降到 ~1e-8 水平（早期层），符合 local proxy loss 梯度饱和的预期

结论：KL 的 coupled gradient 确实提供了更清晰的优化信号，尤其是对模型早期层。这解释了为什么 KL 训练的 predictor 最终质量更高。

脚本在 `/root/distill_sparse_swiglu/scripts/gradient_snr_analysis.py`，完整 JSON 结果在 `/root/distill_sparse_swiglu/artifacts/gradient_snr_results.json`。

---
