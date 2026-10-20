# analysis reward diag v1

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_reward_diag_v1_20260513T001750_result.json`
- **Structured JSON:** [`c9dd3171ef171eacc224.json`](../../sessions/c9/c9dd3171ef171eacc224.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**reward_diag_v1 完成，conclusion=success，Route A 可行。**

### 核心数据

| 分量 | mean | std | p10→p90 range | top10-bot10 gap |
|------|------|-----|---------------|-----------------|
| **Composite** | 0.646 | **0.136** | 0.474→0.780 | 0.483 |
| Provenance | 0.547 | 0.172 | 0.339→0.716 | 0.641 |
| Structural F1 | 0.569 | 0.223 | 0.227→0.822 | 0.766 |
| Format | 1.000 | 0.000 | 1.0→1.0 | 0.0 |

### 关键发现

1. **Composite std=0.136 >> 0.05 阈值** — reward 函数有充足的区分度，GRPO 有梯度信号可学
2. **Format 恒为 1.0** — SFT 模型已完美掌握格式，format reward 在 GRPO 阶段贡献零梯度，等于死权重（占 20% weight）
3. **Structural F1 方差最大 (std=0.223)** — 这是 GRPO 的主要学习信号来源
4. **Provenance 分布偏右但有长尾（9 个零值）** — 部分样本 evidence 完全错误，有改进空间
5. **grpo_v1b 默认 LR = 5e-6** — 这可能太保守，加上 KL=0 / clipped_ratio=0 的问题，说明策略确实未更新

### 建议推论

- v1b 失败的原因不是 reward 缺乏区分度，而是 LR 太低 + 可能的 generation 参数问题
- 下一轮 GRPO 可以考虑把 format weight 降到 0 或很低（它已饱和），把权重分配给 provenance 和 structural

---
