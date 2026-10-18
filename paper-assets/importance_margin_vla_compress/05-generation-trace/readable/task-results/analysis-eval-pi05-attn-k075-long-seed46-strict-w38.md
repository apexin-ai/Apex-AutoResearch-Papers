# analysis eval pi05 attn k075 long seed46 strict w38

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_attn_k075_long_seed46_strict_w38_20260528T103600_result.json`
- **Structured JSON:** [`74bd8e5abec9c76f91e9.json`](../../sessions/74/74bd8e5abec9c76f91e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## seed46 结果：50.6%

**确认参数**：prune=attention, keep=192/256 tokens/image, EXIT_CODE=0, 无错误

### Per-task breakdown (seed46)

| Task | Description | SR |
|------|------------|-----|
| T0 | alphabet soup + tomato | 62% |
| T1 | cream cheese + butter | 64% |
| T2 | stove + moka pot | 54% |
| T3 | black bowl → drawer | 34% |
| T4 | white mug → left plate | 36% |
| T5 | book → back shelf | 52% |
| T6 | white mug → plate | 74% |
| T7 | alphabet soup + cream | 30% |
| T8 | both moka pots → stove | 12% |
| T9 | yellow mug → microwave | 88% |

### 5-seed 汇总

用 seed42=49.8%(w41）、seed43=52.0%（cqa1），与你给的 2-seed mean 50.9% 一致：

| Seed | Server | SR |
|------|--------|-----|
| 42 | w41 | 49.8% |
| 43 | cqa1 | 52.0% |
| 44 | w41 | 51.6% |
| 45 | w41 | 53.0% |
| 46 | w38 | 50.6% |

**5-seed mean = 51.4% ± 1.24pp** (sample std, n-1)

Range: 49.8%–53.0% (3.2pp span)

### Plateau hypothesis 判断

**一致。** seed46 (50.6%) 落在 5-seed 分布的中间偏低位置，与 mean 偏差仅 -0.8pp。5-seed std=1.24pp 非常小，确认 Attention k=0.75 处于稳定 plateau zone。所有 5 个 seed 均在 ±2pp 内波动，无 outlier。

### 注意事项

- seed42 在 registry 中有两个成功记录：w41=49.8% 和 cqa1=52.4%。上面用 49.8% 与你给的 2-seed baseline 对齐。如果改用 cqa1=52.4%，5-seed mean 变为 51.92%±1.06pp。
- T8（both moka pots）在所有 seed 中持续低分（6%–12%），是全局难题，非压缩引起。

---
