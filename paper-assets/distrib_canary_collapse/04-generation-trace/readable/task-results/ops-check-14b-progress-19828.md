# ops check 14b progress 19828

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-14b-progress-19828_20260522T173945_result.json`
- **Structured JSON:** [`235aacdc054bb8911165.json`](../../sessions/23/235aacdc054bb8911165.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进度总览

| exp_id | 当前gen/总gen | 进程状态 | 完成? |
|--------|-------------|---------|------|
| t10_a050_v2 | **10/10** | PID 776064, 运行 8h34m | **已完成** |
| t15_a075 | **4/15** (~27%) | PID 793171, 运行 5h03m | 进行中，预计还需 ~14h |

注：t10_a050_v2 进程仍存活且有 gen_10 目录（无 metrics），但 gen_9/metrics.json 已存在，按 T=10 标准已完成。

---

## t10_a050_v2 完整 Metric 时序

```json
{
  "experiment": "t10_a050_s42_fp32_14b",
  "model": "pythia-1.4b-deduped",
  "alpha": 0.50, "T": 10, "seed": 42,
  "metrics": {
    "token_entropy": [2.9731, 2.1767, 2.1911, 2.2196, 2.2075, 2.2218, 2.1971, 2.2495, 2.2598, 2.2700],
    "distinct_1":    [0.0992, 0.0990, 0.0865, 0.0786, 0.0750, 0.0724, 0.0710, 0.0703, 0.0700, 0.0697],
    "distinct_2":    [0.5222, 0.5225, 0.4553, 0.3978, 0.3650, 0.3434, 0.3304, 0.3231, 0.3208, 0.3187],
    "distinct_3":    [0.8211, 0.8212, 0.7508, 0.6681, 0.6120, 0.5683, 0.5416, 0.5265, 0.5206, 0.5167],
    "perplexity":    [19.83, 21.05, 25.54, 26.95, 28.66, 30.24, 31.60, 31.96, 32.92, 34.80],
    "self_bleu":     [0.0118, 0.0114, 0.0124, 0.0130, 0.0137, 0.0135, 0.0141, 0.0142, 0.0138, 0.0141],
    "ece":           [0.0081, 0.1002, 0.1231, 0.1263, 0.1337, 0.1392, 0.1460, 0.1407, 0.1444, 0.1496],
    "effective_rank":[52.67, 75.71, 83.61, 83.78, 83.07, 82.47, 82.62, 82.41, 82.21, 82.56]
  }
}
```

## Drift Profile (gen_0 → gen_9)

| metric | gen_0 | gen_9 | 变化% | collapse? |
|--------|-------|-------|------|-----------|
| token_entropy | 2.973 | 2.270 | **-23.6%** | **YES** (>10%) |
| distinct_1 | 0.0992 | 0.0697 | **-29.7%** | **YES** (>20%) |
| distinct_2 | 0.5222 | 0.3187 | **-39.0%** | severe |
| distinct_3 | 0.8211 | 0.5167 | **-37.1%** | severe |
| perplexity | 19.83 | 34.80 | **+75.4%** | degrading |
| self_bleu | 0.0118 | 0.0141 | +19.0% | mild ↑ |
| ece | 0.0081 | 0.1496 | +1748% | severe |

**Collapse 判定：明确 collapse。** distinct_1 下降 30%，distinct_2/3 下降 37-39%，perplexity 接近翻倍。

**时序特征：**
- token_entropy 在 gen_0→1 骤降（2.97→2.18，-27%），之后稳定在 ~2.2（gen_1-9 几乎平坦）
- distinct_n 系列从 gen_1 开始单调下降，前 4 代下降最快，gen_6 后趋于饱和
- perplexity 全程单调上升，无收敛迹象
- effective_rank gen_0→2 跳升（52→83），之后稳定——表示表征维度没有坍缩，collapse 主要体现在生成多样性上

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "experiment": "t10_a050_s42_fp32_14b",
    "model": "pythia-1.4b-deduped",
    "alpha": 0.5,
    "T": 10,
    "seed": 42,
    "metrics": {
      "token_entropy": [
        2.9731,
        2.1767,
        2.1911,
        2.2196,
        2.2075,
        2.2218,
        2.1971,
        2.2495,
        2.2598,
        2.27
      ],
      "distinct_1": [
        0.0992,
        0.099,
        0.0865,
        0.0786,
        0.075,
        0.0724,
        0.071,
        0.0703,
        0.07,
        0.0697
      ],
      "distinct_2": [
        0.5222,
        0.5225,
        0.4553,
        0.3978,
        0.365,
        0.3434,
        0.3304,
        0.3231,
        0.3208,
        0.3187
      ],
      "distinct_3": [
        0.8211,
        0.8212,
        0.7508,
        0.6681,
        0.612,
        0.5683,
        0.5416,
        0.5265,
        0.5206,
        0.5167
      ],
      "perplexity": [
        19.83,
        21.05,
        25.54,
        26.95,
        28.66,
        30.24,
        31.6,
        31.96,
        32.92,
        34.8
      ],
      "self_bleu": [
        0.0118,
        0.0114,
        0.0124,
        0.013,
        0.0137,
        0.0135,
        0.0141,
        0.0142,
        0.0138,
        0.0141
      ],
      "ece": [
        0.0081,
        0.1002,
        0.1231,
        0.1263,
        0.1337,
        0.1392,
        0.146,
        0.1407,
        0.1444,
        0.1496
      ],
      "effective_rank": [
        52.67,
        75.71,
        83.61,
        83.78,
        83.07,
        82.47,
        82.62,
        82.41,
        82.21,
        82.56
      ]
    }
  }
}
```

</details>

---
