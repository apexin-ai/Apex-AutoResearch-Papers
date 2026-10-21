# analysis exp 007

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_007_20260518T194203_result.json`
- **Structured JSON:** [`27597611cabf642158fa.json`](../../sessions/27/27597611cabf642158fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 exp_007 正常完成，EXIT_CODE=0，6 代 checkpoint 齐全 (gen_0 ~ gen_5)。总训练时长约 10.7 小时 (May 18 16:54 ~ May 19 03:37)。

## 完整 Metrics (JSON)

```json
[
  {
    "generation": 0,
    "effective_rank": 417.547,
    "log_det": 2366.683,
    "perplexity": 9.554,
    "distinct_4": 0.7414,
    "train_loss": null,
    "mix_ratio": 0.0
  },
  {
    "generation": 1,
    "effective_rank": 476.725,
    "log_det": 2367.460,
    "perplexity": 10.282,
    "distinct_4": 0.6737,
    "train_loss": 1.7653,
    "mix_ratio": 0.2
  },
  {
    "generation": 2,
    "effective_rank": 481.621,
    "log_det": 2358.305,
    "perplexity": 10.741,
    "distinct_4": 0.4978,
    "train_loss": 1.6709,
    "mix_ratio": 0.2
  },
  {
    "generation": 3,
    "effective_rank": 486.541,
    "log_det": 2362.521,
    "perplexity": 11.137,
    "distinct_4": 0.4665,
    "train_loss": 1.4208,
    "mix_ratio": 0.2
  },
  {
    "generation": 4,
    "effective_rank": 490.346,
    "log_det": 2379.191,
    "perplexity": 11.512,
    "distinct_4": 0.4515,
    "train_loss": 1.3255,
    "mix_ratio": 0.2
  },
  {
    "generation": 5,
    "effective_rank": 492.655,
    "log_det": 2398.932,
    "perplexity": 11.833,
    "distinct_4": 0.4384,
    "train_loss": 1.3049,
    "mix_ratio": 0.2
  }
]
```

## 趋势分析

| Metric | Gen 0 → Gen 5 | 趋势 | 特征 |
|--------|---------------|------|------|
| **eff_rank** | 417.5 → 492.7 (+75.1, +18.0%) | 单调上升 | 无 collapse，持续扩展 |
| **log_det (SLV)** | 2366.7 → 2398.9 (+32.2, +1.4%) | Gen 2 dip (2358.3) 后反弹至 2398.9 超基线 | 典型 transitional: dip-then-recovery |
| **ppl** | 9.55 → 11.83 (+2.28, +23.9%) | 单调上升但增速放缓 | 远低于 r=0 的 76.78，退化温和 |
| **distinct_4** | 0.741 → 0.438 (-0.303, -40.9%) | 持续下降，Gen 1→2 最大跌幅 | 多样性损失显著但趋于平稳 |
| **train_loss** | 1.765 → 1.305 (-0.460) | 单调下降 | 训练正常收敛 |

**关键结论**: Gen 5 延续了 transitional 轨迹。log_det 在 Gen 2 触底后持续反弹，Gen 5 达到 2398.9（超基线 +32.2），确认 r=0.2 下 20% 真实数据足以阻止 spectral collapse。eff_rank 单调上升而非下降，与 r=0 的 collapse 模式完全相反。代价主要体现在 distinct_4 下降和 ppl 温和上升。

---
