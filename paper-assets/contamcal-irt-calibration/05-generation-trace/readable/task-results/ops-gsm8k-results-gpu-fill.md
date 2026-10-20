# ops gsm8k results gpu fill

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gsm8k_results_gpu_fill_20260514T190540_result.json`
- **Structured JSON:** [`e4aac0b943f93efec681.json`](../../sessions/e4/e4aac0b943f93efec681.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 子任务 A: exp_006_irt_05B_gsm8k — DONE/success

| 指标 | 值 |
|------|-----|
| Joint gamma | 0.3463 (95% CI: [-0.65, 1.40], 不排除零) |
| Joint 诊断 | Rhat=1.008, ESS=956, 0 divergences — **全部 OK** |
| Per-bench 诊断 | Rhat=1.53, ESS=7 — **未收敛** |
| 总时间 | 799s |

**Baselines MAE (GSM8K)**:

| 方法 | MAE |
|------|-----|
| B4_linear_regression | **0.0030** |
| B0_raw / B1 / B5 | 0.0034 |
| B3_vanilla_4pl | 0.0123 |
| **IRT_4pl_gamma** | **0.0195** |
| B6_dcr_fuzzy | 0.2634 |
| B2_2pl_gamma | 0.3202 |

### 子任务 B: GPU 填充

| GPU | 任务 | 状态 | PID |
|-----|------|------|-----|
| cuda:0 | 3B d100 para aligned eval | RUNNING | 426813 |
| cuda:1 | 1.5B d025 para aligned eval | RUNNING | 426474 |

**额外发现**:
- 1.5B d100 aligned 结果已存在 → 注册为 DONE（MMLU 0.593, GSM8K 0.650, ARC 0.769, HumanEval 50/164）
- 1.5B d100 para aligned 也已存在
- GPU 2 意外空闲（0 MiB），之前应跑 exp-002 signals — 可能需要检查

---
