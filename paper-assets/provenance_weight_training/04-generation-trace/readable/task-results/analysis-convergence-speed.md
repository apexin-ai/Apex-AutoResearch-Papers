# analysis convergence speed

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_convergence-speed_20260516T144315_result.json`
- **Structured JSON:** [`7d588007ab7a978ce2e5.json`](../../sessions/7d/7d588007ab7a978ce2e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表已生成并注册。

## 分析结论

**数据限制**：eval_loss 数据极度稀缺——adaptive_fix_seed42 仅有 3 个 eval 点（step 500/1000/1500），uniform_seed42 完全没有中间 eval 记录。因此主图使用 smoothed training loss。

**核心发现**：

1. **训练 loss 几乎无差异**：adaptive 的 unweighted training loss 与 uniform 全程高度重叠，平均差异仅 +0.028（~1.4%）。这是预期的——adaptive 上调了"难"样本的权重，导致梯度更偏向高 loss 样本，从而 training loss 略高。

2. **无交叉点**：adaptive 的 training loss 从未低于 uniform。差异自始至终为正且稳定，说明两种方法在训练集上的收敛速度本质相同。

3. **真正的差异体现在 eval**：从 `eval_perplexity_results.json` 最终评估看：
   - adaptive_seed42 final: loss=2.8704, PPL=17.64
   - uniform_seed42 final: loss=2.8732, PPL=17.69
   - **Δ = −0.0028（adaptive 更好 0.10%）**

4. **前 1500 步 eval 下降速率**（仅 adaptive 有数据）：
   - Step 500: 3.1283
   - Step 1000: 3.1044（−0.024）
   - Step 1500: 3.0869（−0.018）
   
   单侧数据无法对比，但下降速率在递减。

**结论**：adaptive weighting 的优势不在"训练更快"���而在最终模型质量略优。训练收敛速度本质相��，因为两者看的是同一份数据、同一个模型架构，区别仅在于样本权重分配。要准确量化收敛速度差异，��要对两个实验都启用定期 eval（建议每 500 步做一次 eval）。

---
