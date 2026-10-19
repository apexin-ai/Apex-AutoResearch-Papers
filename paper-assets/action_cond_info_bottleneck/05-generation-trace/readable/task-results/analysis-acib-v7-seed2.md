# analysis acib v7 seed2

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_acib_v7_seed2_20260516T170511_result.json`
- **Structured JSON:** [`bc069b5ac759e71d59a6.json`](../../sessions/bc/bc069b5ac759e71d59a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## acib_v7_seed2 训练结果汇总

### 训练指标 (step 20000, final)

| 指标 | 值 |
|------|-----|
| total_loss | 0.1352 |
| task_loss | 0.0516 |
| ib_loss | 0.8530 |
| contrastive_loss (ctr) | 0.8639 |
| div | -0.2383 |
| scorer_mean | 0.229 |
| scorer_std | 0.314 |
| β | 0.01 |
| 训练时长 | 3.3h |
| EXIT_CODE | 0 (正常) |

### Checkpoint 文件

| Checkpoint | 大小 |
|------------|------|
| checkpoint-5000 | 1.3G |
| checkpoint-10000 | 1.3G |
| checkpoint-15000 | 1.3G |
| checkpoint-20000 | 1.3G |

### Probe A: 固定图像，交换 language instruction → cos similarity

| Pair | cos | l2 |
|------|-----|----|
| bbq_sauce vs black_bowl_cookie | **0.566** | 5.380 |
| bbq_sauce vs black_bowl_cabinet | **0.524** | 5.634 |
| black_bowl_cookie vs black_bowl_cabinet | **0.749** | 1.228 |

bit_identical = False (所有 pair)

### Probe B: 跨任务自然观测 → cos similarity

| Pair | cos | l2 |
|------|-----|----|
| bbq_sauce vs black_bowl_cookie | **0.536** | 5.240 |
| bbq_sauce vs black_bowl_cabinet | **0.618** | 5.242 |
| black_bowl_cookie vs black_bowl_cabinet | **0.626** | 2.737 |

### 与 seed1 (step-5000) 对比

| 指标 | seed1 step-5000 | seed2 step-20000 |
|------|-----------------|------------------|
| Probe A cos range | [0.476, 0.894] | [0.524, 0.749] |

seed2 在训练完成后，Probe A cos 区间收窄且上界更低（0.749 vs 0.894），说明训练更充分后语义相似 pair（两个 black_bowl 指令）的 scorer 输出也有了更明显的分化。

### 结论

- **Language conditioning 有效**：Probe A cos 全部 <0.8，bit_identical=False，scorer 对不同 language instruction 产生不同的 importance weights
- **Task-dependent importance maps**：Probe B cos 全部 <0.7，不同任务的空间注意力分布有显著差异，排除了 position prior
- **seed2 复现 seed1 结论**：两个 seed 一致表明 log-barrier contrastive loss (λ=0.1) 稳定地强制了 language conditioning
- 语义相似指令（两个 black_bowl）cos=0.749 > 语义不同指令 cos≈0.53-0.57，符合预期——相似指令应产生更接近的 importance pattern

---
