# ops check deepseek ae seed123

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_deepseek_ae_seed123_20260520T152323_result.json`
- **Structured JSON:** [`542f594268fa523e08a4.json`](../../sessions/54/542f594268fa523e08a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### deepseek_ae_only_seed123 — **已完成** ✓

进程 PID 626709/626719 已退出，训练+评估全部跑完，`EXIT_CODE=0`。

**eval_results.json:**

| 指标 | 值 | 95% CI |
|------|-----|--------|
| **Accuracy** | **98.3%** | [97.6%, 99.0%] |
| Majority baseline | 71.5% | — |
| **Lift** | **+26.8pp** | [+24.4pp, +29.2pp] |
| pass P/R/F1 | 0.98 / 0.99 / 0.99 | — |
| fail P/R/F1 | 0.98 / 0.96 / 0.97 | — |

Checkpoints: 148 → 296 → 444 (final), n=1190 样本。

---

### deepseek_loop_only_seed456 — **运行中**

- PID 633962 alive，已运行 28 分钟，状态 `Ss+`
- GPU 0: **100% util**, 71595/97887 MiB

---

### GPU 状态

| GPU | Util | 显存 |
|-----|------|------|
| 0 | 100% | 71.6G / 97.9G |
| 1 | 0% | 0 / 97.9G |

---
