# ops seed123 eval and seed456 launch

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_seed123_eval_and_seed456_launch_20260521T100047_result.json`
- **Structured JSON:** [`c657b318ace4421cff3a.json`](../../sessions/c6/c657b318ace4421cff3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

seed456 训练确认正常运行：
- **PID**: 693144
- **GPU**: GPU-48463d2b（即 GPU 1），15080 MiB
- **GPU 0**: 无新进程 — **GPU 隔离正常**

---

### 汇总

**1. seed123 eval 结果**

| 指标 | 值 | 95% CI |
|------|-----|--------|
| Accuracy | **80.2%** | [77.8%, 82.5%] |
| Majority baseline | 71.5% | — |
| Lift | +8.7pp | [+5.7pp, +11.8pp] |
| Pass P/R/F1 | 0.88 / 0.84 / 0.86 | — |
| Fail P/R/F1 | 0.64 / 0.70 / 0.67 | — |

**2. seed456 训练**
- PID: **693144**，tmux session: `seed456`
- 日志: `/tmp/seed456_train.log`
- 模型加载完成，正在进入训练循环

**3. GPU 隔离**: 正常。seed456 仅在 GPU 1 上，GPU 0 无新进程。

---
