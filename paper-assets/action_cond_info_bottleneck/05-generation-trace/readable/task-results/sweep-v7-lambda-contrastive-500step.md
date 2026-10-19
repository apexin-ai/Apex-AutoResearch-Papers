# sweep v7 lambda contrastive 500step

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_sweep_v7-lambda-contrastive-500step_20260516T103522_result.json`
- **Structured JSON:** [`bfeb57cb1e0dd6e1c213.json`](../../sessions/bf/bfeb57cb1e0dd6e1c213.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两档训练完成。Probe A 因 dtype bug 无法运行（需要修复 probe 脚本中的 bfloat16 兼容性，但不影响本次分析）。

---

## 结果汇总

### 指标对比表

| Step | lambda | total_loss | task_loss | ib | div | **ctr** | scorer_mean | scorer_std |
|------|--------|-----------|-----------|------|--------|---------|-------------|-----------|
| 400 | 0.1 | 0.1243 | 0.0503 | 0.1790 | -0.3711 | **1.0000** | 0.535 | 0.375 |
| 500 | 0.1 | 0.1668 | 0.0947 | 0.1986 | -0.3750 | **1.0000** | 0.520 | 0.377 |
| 400 | 1.0 | 1.0241 | 0.0503 | 0.1803 | -0.3730 | **0.9999** | 0.535 | 0.375 |
| 500 | 1.0 | 1.0672 | 0.0951 | 0.1971 | -0.3750 | **0.9999** | 0.520 | 0.377 |

### 分析

1. **task_loss 未受干扰**：两档 task_loss 完全一致（step 400: 0.0503 vs 0.0503），contrastive 只是在 total_loss 上叠了一个常数偏移。

2. **contrastive loss 几乎不动**：lambda=0.1 下 ctr 从头到尾 = 1.0000；lambda=1.0 仅微降至 0.9999。这意味着 **scorer 对不同 condition 产出的 weights 几乎相同**（cos_sim≈1），且 500 steps 内梯度信号不足以改变这一状态。

3. **scorer 行为两档相同**：scorer_mean/std 的演化轨迹完全一致，说明 lambda 只影响了 total_loss 的绝对值，未改变模型学习动态。

4. **根因**：contrastive loss = `cos_sim(w_orig, w_shuffled).mean()` 在 cos_sim≈1 附近梯度极其平坦，无法有效推动 scorer 分化。这不是 lambda 的问题，而是 **loss 设计本身在高相似度区域缺乏梯度信号**。

### 推荐

- **完整训练暂用 lambda=1.0**（唯一有微弱信号的档位，且不伤 task_loss）。
- **但更关键的是修改 contrastive loss 公式**——当前 cosine similarity 在高相似区几乎没有梯度。建议改为：
  - `1 - cos_sim` 再加 margin（hinge loss: `max(0, cos_sim - margin)`）
  - 或 InfoNCE 风格（温度缩放 + cross-entropy），梯度更均匀
  - 或直接用 negative L2 distance

是否需要我修改 contrastive loss 实现？

---
