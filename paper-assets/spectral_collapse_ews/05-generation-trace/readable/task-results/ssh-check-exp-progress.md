# ssh check exp progress

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-exp-progress_20260519T135233_result.json`
- **Structured JSON:** [`282a1adef8a5231efa17.json`](../../sessions/28/282a1adef8a5231efa17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### exp_009 (r=0.25, cuda:0, pid=247492)
**状态: RUNNING** — 已运行 18h05m，当前在 **Gen 9** 训练阶段 (step 2200, loss=1.2971)

日志显示 Gen 9 已完成 37500 样本生成，正在 fine-tuning，已到 step 2200。接近完成（通常约 2500 steps）。

**完整 results JSON（Gen 0–8）：**

```json
[
  {
    "generation": 0,
    "effective_rank": 417.5472106933594,
    "log_det": 2366.682861328125,
    "perplexity": 9.553585720044504,
    "distinct_4": 0.7414389763779528,
    "top_10_singular_values": [1942.816, 488.368, 407.616, 284.336, 227.260, 210.670, 181.438, 171.560, 168.540, 162.467]
  },
  {
    "generation": 1,
    "effective_rank": 476.66156005859375,
    "log_det": 2362.134765625,
    "perplexity": 10.238942219689196,
    "distinct_4": 0.6498661417322835,
    "train_loss": 1.80109278963089,
    "mix_ratio": 0.25,
    "controller_ratio": 0.25
  },
  {
    "generation": 2,
    "effective_rank": 482.84356689453125,
    "log_det": 2363.101806640625,
    "perplexity": 10.652554699554909,
    "distinct_4": 0.4973248031496063,
    "train_loss": 1.697985660381317,
    "mix_ratio": 0.25,
    "controller_ratio": 0.25
  },
  {
    "generation": 3,
    "effective_rank": 489.4678955078125,
    "log_det": 2380.876953125,
    "perplexity": 11.018671418188633,
    "distinct_4": 0.4419055118110236,
    "train_loss": 1.4132862640237809,
    "mix_ratio": 0.25,
    "controller_ratio": 0.25
  },
  {
    "generation": 4,
    "effective_rank": 491.21258544921875,
    "log_det": 2393.37060546875,
    "perplexity": 11.343002049773526,
    "distinct_4": 0.42981496062992125,
    "train_loss": 1.3425281575345993,
    "mix_ratio": 0.25,
    "controller_ratio": 0.25
  },
  {
    "generation": 5,
    "effective_rank": 495.8443603515625,
    "log_det": 2421.21826171875,
    "perplexity": 11.668743109320236,
    "distinct_4": 0.4191555118110236,
    "train_loss": 1.3076749965000152,
    "mix_ratio": 0.25,
    "controller_ratio": 0.25
  },
  {
    "generation": 6,
    "effective_rank": 498.5948791503906,
    "log_det": 2436.37841796875,
    "perplexity": 11.973914122440608,
    "distinct_4": 0.3969055118110236,
    "train_loss": 1.316501470246315,
    "mix_ratio": 0.25,
    "controller_ratio": 0.25
  },
  {
    "generation": 7,
    "effective_rank": 500.66448974609375,
    "log_det": 2447.076171875,
    "perplexity": 12.29451624012561,
    "distinct_4": 0.38890157480314963,
    "train_loss": 1.303484043006897,
    "mix_ratio": 0.25,
    "controller_ratio": 0.25
  },
  {
    "generation": 8,
    "effective_rank": 505.81884765625,
    "log_det": 2463.805419921875,
    "perplexity": 12.631141659500072,
    "distinct_4": 0.36570472440944884,
    "train_loss": 1.3039245527935028,
    "mix_ratio": 0.25,
    "controller_ratio": 0.25
  }
]
```

---

### exp_010 (pure_collapse, seed43, cuda:1, pid=283142)
**状态: RUNNING** — 已运行 8h00m，当前在 **Gen 4** 生成阶段 (5120/50000 samples)

已完成 Gen 0–3 的 metrics：

| Gen | effective_rank | log_det | perplexity | distinct_4 | train_loss |
|-----|---------------|---------|------------|------------|------------|
| 0 | 417.55 | 2366.68 | 9.55 | 0.7415 | — |
| 1 | 490.83 | 2462.62 | 11.37 | 0.5997 | 1.6245 |
| 2 | 496.24 | 2466.63 | 13.57 | 0.5048 | 1.2609 |
| 3 | 494.04 | 2438.38 | 16.22 | 0.4778 | 1.1248 |

---

### 异常
无 error/crash。两个实验均正常运行。exp_009 日志有 `padding_side='left'` 警告，不影响结果。

**关键观察**: exp_010 (pure_collapse, r=0.0) 的 perplexity 退化远快于 exp_009 (r=0.25)——Gen 3 已到 16.22 vs exp_009 Gen 3 仅 11.02，符合预期。

---
