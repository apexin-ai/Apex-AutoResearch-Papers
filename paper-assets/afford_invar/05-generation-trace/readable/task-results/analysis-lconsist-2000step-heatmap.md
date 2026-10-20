# analysis lconsist 2000step heatmap

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lconsist-2000step-heatmap_20260519T234250_result.json`
- **Structured JSON:** [`75f9f92eda7c0e4af797.json`](../../sessions/75/75f9f92eda7c0e4af797.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成。汇总结果：

```
[L_consist checkpoint-2000] hm_ent=7.8 | hm_max≈uniform | hm_mean=uniform
  peak_dist=52.1±25.9px | mass_ratio=1.07x | topk_contain=0.020

L_consist 趋势: step 1000→0.000155, 1500→0.000047, 2000→0.000100
L_act 趋势:     step 1000→0.3555,   1500→0.4062,   2000→0.3652

判断: 无空间结构（预期内）
```

**详细分析:**

- **hm_ent=7.8 bits**（>7 阈值）→ 接近均匀分布，无空间集中
- **mass_ratio=1.07x** → 仅比随机(1.0x)高 7%，本质上等同于随机
- **peak_dist=52.1px** → 峰值位置距离目标远，无定向性
- **topk_containment=0.020** → 与均匀基线(~0.019)几乎一致
- **pass_rate_ratio>2.0x = 0%** → 没有任何 episode 展现有意义的集中

**训练日志补充观察:**
- 训练内 H_ent 在 step 1200-2500 曾降到 ~5.43（看似有结构），但 eval 上 7.8 说明这是训练数据上的 overfitting pattern，不是真正的空间 grounding
- L_consist 全程 <0.001，grad_ratio=0.0000 — 一致性损失对梯度零贡献
- 训练已续跑到 step 3590，checkpoint-3000 也已保存

**结论:** checkpoint-2000 无意外 positive signal。L_consist 训练出的 decoder 没有学到有意义的空间结构，heatmap 本质上是均匀分布。这符合纯 L_consist（无 L_transfer）的预期基线行为。

---
