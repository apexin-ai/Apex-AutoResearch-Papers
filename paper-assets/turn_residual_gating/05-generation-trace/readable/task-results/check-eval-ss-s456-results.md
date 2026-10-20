# check eval ss s456 results

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval_ss_s456_results_20260524T011457_result.json`
- **Structured JSON:** [`d49c373fffe60016555c.json`](../../sessions/d4/d49c373fffe60016555c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。汇总如下：

---

## 1. AR Eval 状态
**已完成。** PID 129280 已退出。s456 AR 结果文件 `ss_s456_ar_n50.json` 于 05-24 08:59 生成。

## 2. SS 3-seed AR 结果对照表

### AR GAR (N=50 convs, autoregressive)

| Seed | β=0 mid GAR | β=0 PPL | β=3 mid GAR | β=3 PPL | β=5 mid GAR | β=5 PPL |
|------|:-----------:|:-------:|:-----------:|:-------:|:-----------:|:-------:|
| **s42** | 0.3471 | 1.4423 | 0.5933 | 1.5640 | 0.7170 | 1.7792 |
| **s123** | 0.4231 | 1.4408 | 0.5903 | 1.6070 | 0.7174 | 1.7852 |
| **s456** | 0.4325 | 1.4394 | 0.6050 | 1.5868 | 0.7157 | 1.8045 |
| **Mean** | **0.4009** | **1.4408** | **0.5962** | **1.5859** | **0.7167** | **1.7896** |
| **Std** | 0.047 | 0.001 | 0.008 | 0.022 | 0.001 | 0.013 |

**Base (unfinetuned):** β=0 mid GAR = 0.0186, PPL = 1.447 | β=3: 0.5315 | β=5: 0.7042

β=0 时 SS 平均 0.4009 vs Base 0.0186 → **21.6× improvement**。β=3/5 steering 相对 base 也有提升（0.596 vs 0.532, 0.717 vs 0.704）。

## 3. TF GAR 结果

| Config | GAR-ours mid | GAR-dongre mid |
|--------|:------------:|:--------------:|
| Base | 0.0227 | 0.0027 |
| SS s42 | 0.5025 | 0.3890 |
| SS s123 | **NaN** | **NaN** |
| SS s456 | 0.4964 | 0.3862 |

**s123 TF 结果为 NaN** — 该评估跑出了问题，需要重跑。s42 和 s456 TF 结果一致（~0.50 ours, ~0.39 dongre）。

## 4. GPU Chain 当前状态
- PID 108997 (gpu_chain_next.sh) 运行 7h50m
- 已完成: Step 1-4（s123 eval → s456 training → s456 eval → Qwen-1.5B Phase1 diag）
- **当前: Step 5/7 — Qwen-1.5B TG training** (PID 131153, 运行 ~8min, `train_phase2.py --seed 42`, 占用 30GB VRAM)
- 待完成: Step 6 (Qwen-1.5B eval), Step 7 (MMLU eval)

## 需要关注的问题
1. **s123 TF GAR = NaN** — 需要排查并重跑 TF eval
2. s42 的 β=0 AR GAR (0.347) 明显低于 s123/s456 (~0.43)，但 β=3/5 三个 seed 收敛一致

---
