# ops mmlu results collect

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mmlu-results-collect_20260524T094315_result.json`
- **Structured JSON:** [`62be16a10434e9ce3191.json`](../../sessions/62/62be16a10434e9ce3191.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。

---

## Eval 结果

| Model | MMLU (5-shot acc) | GSM8K strict-match | GSM8K flexible-extract |
|-------|------------------:|-------------------:|-----------------------:|
| Vanilla Qwen3-8B | **0.7493** ± 0.0035 | **0.8764** ± 0.0091 | **0.8832** ± 0.0088 |
| ACT s1 ckpt-8000 | 0.7356 ± 0.0036 | 0.8461 ± 0.0099 | 0.8484 ± 0.0099 |
| R3-only s1 ckpt-6500 | **0.7505** ± 0.0035 | ⏳ 运行中 (1207/1319, 91%) | ⏳ 运行中 |

**R3-only GSM8K ETA**: ~112 items × ~4s/it ≈ **7-8 分钟后完成**。PID 651783 已跑 7h13m。

关键发现：
- R3-only MMLU **0.7505 > Vanilla 0.7493**，训练没有损害通用能力，反而微升
- ACT 两项均下降（MMLU -1.37pp, GSM8K -3.03pp strict），说明 ACT 训练对通用能力有损

---

## exp-003-len512-v3 训练进度

| 指标 | 值 |
|------|-----|
| 当前 step | **2405 / 8000** (30%) |
| 最新 checkpoint | checkpoint-2000 (May 24 12:32) |
| 速度 | ~46s/step |
| 剩余 | 5595 steps × 46s ≈ **71.5h ≈ ~3 天** |
| PID | 553700, 已跑 1d 7h 26m |

---

## GPU 状态

| GPU | 利用率 | 显存 |
|-----|--------|------|
| GPU 0 | 100% | 34.1 / 97.9 GB (eval) |
| GPU 1 | 97% | 41.3 / 97.9 GB (training) |

---
