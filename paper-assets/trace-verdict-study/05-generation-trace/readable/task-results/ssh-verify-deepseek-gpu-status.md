# ssh verify deepseek gpu status

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_deepseek_gpu_status_20260515T131311_result.json`
- **Structured JSON:** [`2c91a30544b7f1d407e6.json`](../../sessions/2c/2c91a30544b7f1d407e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### GPU 使用
| GPU | 型号 | 显存占用 | 利用率 |
|-----|------|---------|--------|
| cuda:0 | RTX PRO 6000 Blackwell | 71,235 / 97,887 MiB (73%) | 88% |
| cuda:1 | RTX PRO 6000 Blackwell | 22,421 / 97,887 MiB (23%) | 100% |

### 实验状态

**1. deepseek_no_trace_seed42** (PID 106822, cuda:0) — **运行中**
- 已运行 3h54m
- 训练进度：**71/444 steps (16%)**，~3.09s/step
- 预计剩余：~19 分钟完成训练（基于当前速度）
- 训练后会自动执行 evaluate.py

**2. deepseek_exception_only_seed42** (PID 107188, cuda:1) — **运行中**
- 已运行 2h58m
- 训练进度：**11/444 steps (2%)**，~15s/step
- 预计剩余：~108 分钟完成训练
- cuda:1 上每 step 耗时约为 cuda:0 的 5 倍（15s vs 3s），显存占用也低很多（23% vs 73%），可能是 batch size 不同或数据加载瓶颈

### deepseek_vota_seed42 评估结果（已完成）

| 指标 | 值 |
|------|-----|
| Accuracy | **84.45%** (baseline 71.5%, lift +12.9pp) |
| Pass P/R/F1 | 0.821 / 1.000 / 0.902 |
| Fail P/R/F1 | 1.000 / 0.454 / 0.625 |
| n | 1190 |

模型对 pass 类别 recall 100% 但 fail 类别 recall 仅 45.4%——倾向于预测 pass，漏掉过半的 fail case。

---
