# code grpo step500 eval

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo-step500-eval_20260521T134024_result.json`
- **Structured JSON:** [`5f391aa11c8b2926c347.json`](../../sessions/5f/5f391aa11c8b2926c347.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整 HT 统计结果已出。以下是 **Base → SFT → GRPO step 500** 三阶段完整对比：

---

## 完整评估报告：GRPO v3 Step 500

### 核心指标对比

| 指标 | Base | SFT | GRPO s500 | SFT→GRPO Δ |
|------|------|-----|-----------|-------------|
| **theta_mle** | 0.095 | 0.228 | 0.157 | **-0.071** |
| **lz\*** | 5.970 | 2.914 | 7.771 | **+4.857** |
| **accuracy_overall** | 70.24% | 73.39% | 71.44% | **-1.95pp** |
| **accuracy_seen** | 70.04% | 83.10% | 73.03% | **-10.07pp** |
| **accuracy_unseen** | 70.27% | 71.67% | 71.16% | **-0.51pp** |
| **lz\*_seen** | 2.498 | -0.395 | 3.410 | **+3.805** |
| **lz\*_unseen** | 5.427 | 3.278 | 7.000 | **+3.722** |

### HT 统计对比

| 指标 | Base | SFT | GRPO s500 | SFT→GRPO Δ |
|------|------|-----|-----------|-------------|
| **ht_parametric** | -0.0442 | -0.0078 | -0.0349 | **-0.0271** |
| **ht_param_seen** | -0.0485 | +0.0357 | -0.0282 | **-0.0639** |
| **ht_param_unseen** | -0.0434 | -0.0198 | -0.0362 | **-0.0164** |
| **ht_nonparametric** | 0.1748 | 0.1874 | 0.1678 | **-0.0196** |
| **guttman_errors** | 7,206,274 | 7,215,778 | 6,750,803 | **-464,975** |

### 关键发现

1. **污染信号被彻底破坏**：SFT 的 seen/unseen accuracy gap 从 11.43pp（83.10% vs 71.67%）缩小到 1.87pp（73.03% vs 71.16%），几乎回到 base 水平（-0.23pp）。lz\*_seen 从异常负值 -0.395 恶化到 3.410。

2. **整体能力下降**：overall accuracy 从 73.39%→71.44%，theta 从 0.228→0.157。GRPO 不仅没提升能力，反而比 SFT 退步，甚至 unseen accuracy 也从 71.67%→71.16%。

3. **HT 统计佐证**：
   - ht_param_seen 从 +0.0357（SFT 的正值=seen items 上表现异常好）→ -0.0282（GRPO 回到负值），说明 seen items 上的异常优势消失。
   - ht_nonparametric 从 0.1874→0.1678，Guttman errors 减少 46.5 万，说明 response pattern 变得更「随机」/less structured。
   - 整体 ht_parametric 从 -0.0078→-0.0349，接近 base 的 -0.0442，说明模型回归到更 aberrant 的状态。

4. **lz\* 全面恶化**：overall lz\* 从 2.914→7.771，比 base（5.970）还差。GRPO 使模型的作答模式变得更加不符合 IRT 模型预期。

### GRPO 训练状态

- Step 1732/3000（58%），ETA ~55 min
- grad_norm 已恢复到 0.41-0.50（此前一段时间为 0）
- reward=0.55，entropy=1.5
- clip_ratio 仍极低（~0.003-0.007）

### 判断

**GRPO v3 step 500 对模型是破坏性的。** 它没有实现"在保持污染信号的同时提升能力"的目标，而是：
- 将污染带来的 seen accuracy 优势几乎完全抹除（-10pp）
- 同时降低了整体能力（-1.95pp overall）
- 使 person-fit 统计量全面恶化

建议 **不继续** 当前 GRPO v3 训练，或需要从根本上修改 GRPO 的 reward 设计，加入保护 seen items accuracy 的约束。

---
