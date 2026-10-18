# analysis checkpoint diversity test

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_checkpoint-diversity-test_20260516T111238_result.json`
- **Structured JSON:** [`e314de7db27d38fd541f.json`](../../sessions/e3/e314de7db27d38fd541f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

测试完成，结果如下：

| Step | Noise Diversity Std | Ratio to Pretrained | Verdict |
|------|-------------------|---------------------|---------|
| **pretrained** | **0.178** | 1.00 | REF |
| step_005000 | 0.054 | 0.30 | PASS |
| step_010000 | 0.036 | 0.20 | WARN |
| step_015000 | 0.039 | 0.22 | WARN |
| step_020000 | 0.048 | 0.27 | WARN |
| step_025000 | 0.041 | 0.23 | WARN |
| step_029999 | 0.041 | 0.23 | WARN |

### 关键发现

1. **Diversity 主要在前 5K steps 急剧下降**：pretrained 0.178 → step 5K 0.054（下降 70%）。这是最大的跌幅。

2. **5K→10K 进一步下降**：0.054 → 0.036（再降 33%），之后基本稳定在 0.036-0.048 区间，不再恶化。

3. **退化模式是逐步的而非突变**：最大跌幅在前 5K steps，10K 之后趋于平稳。

4. **注意**：本测试使用合成观测（随机图像），绝对值与真实数据上的 std=0.006 有差异。但相对趋势可靠——pretrained 比 fine-tuned 高 4-5x，与之前报告的 0.104 vs 0.006 比例（17x）量级一致。真实图像上 collapse 更严重，可能因为模型对 in-distribution 输入更 confident。

### Early Stopping 可行性

- **Early stopping 在 5K step 能保留最多 diversity**（ratio 0.30 vs 后续的 0.20-0.23），但即使 5K step 也已经丢失了 70% 的 diversity。
- 如果目标是保持 diversity > 0.05（PASS 阈值），5K 是唯一勉强通过的 checkpoint。
- **结论**：early stopping 是一个部分缓解方案（5K step），但不能根本解决 mode collapse。需要在训练过程中显式保护 diversity（如 IMM/anchor loss）。

结果已保存至服务器 `eval_results/action_diversity_by_step.json`。

---
