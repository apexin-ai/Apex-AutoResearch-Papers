# diagnose eval supp failures bjb2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-supp-failures-bjb2_20260523T043016_result.json`
- **Structured JSON:** [`30733d501fe98c45077e.json`](../../sessions/30/30733d501fe98c45077e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果：两个实验**未失败，仍在正常运行**

### 证据

| 实验 | PID (bash/python) | GPU | GPU 显存 | GPU 利用率 | 进度 |
|------|-------------------|-----|----------|-----------|------|
| eval-supp-obj-reconvla-s42 | 523238 / 523250 | cuda:1 | 5210MiB | 30% | task 1/10 完成 (75%) |
| eval-supp-goal-crm005-s42 | 524322 / 524332 | cuda:2 | 5139MiB | 30% | task 1/10 完成 (85%) |

- 4 个 PID 均存活（`/proc/&lt;PID>/status` 可访问）
- nvidia-smi 显示 GPU 1 和 GPU 2 上有对应 python 进程在跑
- 日志输出正常：两个实验各完成了 10 个 task 中的第 1 个（每 task 20 rollouts）

### 误报原因

监控系统判定 "process dead 5× with no sentinel/W&B" 是**假阳性**。这两个 eval 任务不产生 sentinel 文件或 W&B run，监控的存活检测逻辑不适用于纯 evaluate.py 任务。

### 结论

- **无需重试，无需修复** — 两个实验正在正常推进
- 每个实验需跑 10 tasks × 20 rollouts = 200 个 rollout，目前各完成 20 个（10%），预计还需较长时间
- 监控系统对 eval 任务的存活判定机制需要改进（增加对 log 文件增长或进程存活的检查）

---
