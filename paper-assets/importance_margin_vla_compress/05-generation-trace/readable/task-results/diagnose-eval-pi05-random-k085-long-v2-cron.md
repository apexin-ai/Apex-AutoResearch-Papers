# diagnose eval pi05 random k085 long v2 cron

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_random_k085_long_v2_cron_20260526T182840_result.json`
- **Structured JSON:** [`6fe20d48d7869abb6723.json`](../../sessions/6f/6fe20d48d7869abb6723.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕（status=DONE, conclusion=success, metrics 已填入）。

**结果汇总：**

| 指标 | 值 |
|------|-----|
| **Overall SR** | **44.4%** (222/500) |
| 运行时间 | 267.8 min |

**Per-task SR：**

| Task | SR |
|------|-----|
| T0 alphabet soup + tomato | 52% |
| T1 cream cheese + butter | 46% |
| T2 stove + moka pot | 58% |
| T3 black bowl → drawer | 74% |
| T4 white mug → left plate | 12% |
| T5 book → back shelf | 32% |
| T6 white mug → plate | 42% |
| T7 alphabet soup + cream | 44% |
| T8 both moka pots → stove | 10% |
| T9 yellow mug → microwave | 74% |

日志路径：`~/runs/importance_margin_vla_compress/eval_pi05_random_k085_long_seed42.log`
结果JSON：`/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.85_libero_10_seed42.json`

v2 重跑确认 SR=44.4%，与 v1 一致。

---
