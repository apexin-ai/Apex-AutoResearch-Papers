# ops exp 029b metrics rescue

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp_029b_metrics_rescue_20260520T225918_result.json`
- **Structured JSON:** [`293251a64db183decb05.json`](../../sessions/29/293251a64db183decb05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

备份完成。以下是 exp_029b 完整轨迹：

**文件状态**: 219 行, 55883 bytes, 最后写入 2026-05-21 06:55:31, 最后 step=168000（train 行），最后 eval step=165000。文件完整，已备份至 `.bak`。

## 完整 eval/NVE/value_mean 轨迹

| Step | eval_return | ve_ratio (NVE) | value_mean |
|------:|------------:|---------------:|-----------:|
| 5,000 | 30.46 | — | 0.001 |
| 15,000 | 168.41 | 0.030 | 5.02 |
| 25,000 | 159.56 | 0.174 | 27.72 |
| 35,000 | 168.05 | 0.335 | 56.35 |
| 45,000 | 171.51 | 0.477 | 81.85 |
| 55,000 | **177.67** | 0.583 | 103.62 |
| 65,000 | 106.57 | 1.014 | 108.03 |
| 75,000 | 64.01 | 1.650 | 105.60 |
| 85,000 | 62.82 | 1.623 | 101.98 |
| 95,000 | 44.66 | 2.109 | 94.17 |
| 105,000 | 31.97 | **2.765** | 88.38 |
| 115,000 | 35.45 | 2.326 | 82.47 |
| 125,000 | 33.04 | 2.278 | 75.27 |
| 135,000 | 42.47 | 1.648 | 70.00 |
| 145,000 | 51.66 | 1.234 | 63.75 |
| 155,000 | 56.50 | 1.061 | 59.93 |
| 165,000 | 44.90 | 1.226 | 55.03 |

**关键观察**:
- 峰值 eval_return=177.67 @ step 55k，之后持续下降
- NVE 在 step 65k 突破 1.0（value expansion），105k 达峰值 2.77
- Gate 全程锁死在 dt=2（`gate_dt_2_frac=1.0`），gate 没有学到任何自适应行为
- 135k 之后 NVE 回落到 ~1.2，eval 略有回升但仍远低于峰值

---
