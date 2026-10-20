# ops training progress check v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_training-progress-check-v2_20260514T083329_result.json`
- **Structured JSON:** [`f010c4b6de68d01d5511.json`](../../sessions/f0/f010c4b6de68d01d5511.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

| GPU | 实验 | PID | 状态 | 已运行 | 进度 | 预估剩余 | 关键指标 |
|-----|------|-----|------|--------|------|----------|---------|
| cuda:0 | eval_15B_d100_s42 | 325310 | 运行中 | 55m | MMLU✓, GSM8K 508/1319 (38%) | ~1h25m (GSM8K) + ARC + HumanEval ≈ **2h** | GPU 48%, 5.8GB |
| cuda:1 | eval_05B_raw | 318424 | 运行中 | 1h42m | MMLU✓, GSM8K 1163/1319 (88%) | ~14m (GSM8K) + ARC + HumanEval ≈ **30-40m** | GPU 34%, 3.6GB |
| cuda:2 | sft_d025_05B_v3 | 324158 | **已完成** | — | 100%, EXIT_CODE=0 | **GPU 已释放** | final loss 1.52, acc 0.67 |
| cuda:3 | sft_d100_3B | 319555 | 运行中 | 1h39m | 1322/4159 steps (32%) | **~3h27m** | loss 1.17, acc 0.72, 4.4s/step |
| cuda:4 | sft_d005_15B | 271916 | 即将完成 | 5h21m | 3015/3177 steps (95%) | **~10m** (或已完成) | loss 1.30, acc 0.72, 18.5GB |
| cuda:5 | eval_3B_raw_gen | 318748 | 运行中 | 1h41m | GSM8K 891/1319 (67%) | GSM8K ~50m + HumanEval ≈ **1h+** | GPU 62%, 6.6GB |

要点：
- **cuda:2 已空闲**，可立即提交新任务
- **cuda:4 预计几分钟内释放**（训练已到 95%，或刚完成）
- **cuda:1 约 30-40min 后释放**（GSM8K 即将完成，还剩 ARC+HumanEval）
- **cuda:3 最慢**，3B 模型 d100 全量 SFT 还需约 3.5h
- **cuda:0/cuda:5** 各有 1-2h eval 任务

---
