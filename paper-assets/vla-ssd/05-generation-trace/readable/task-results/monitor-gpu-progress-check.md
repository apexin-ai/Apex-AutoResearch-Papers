# monitor gpu progress check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_gpu_progress_check_20260521T073106_result.json`
- **Structured JSON:** [`62c1628078bc2b57e54a.json`](../../sessions/62/62c1628078bc2b57e54a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在正常运行，汇报如下：

---

### 实验 1: object_pipeline_ridge_v2 (cuda:0, PID 541379)
- **运行时间**: 17 分 39 秒
- **当前阶段**: Phase 6 (counterfactual analysis) — condition `wrong`, 1000/5000 samples
- **已完成**: Phase 1-5 全部完成（feature extraction → Ridge probing → attention profile → cross-instruction classification → RSA analysis）
- **Phase 6 进度**: ~50s/200 samples，`wrong` condition 还剩 4000 samples (~16 min)；假设 4 个 condition，总共还需 ~60-70 min
- **GPU**: 90% 利用率，15.3/97.9 GB 显存
- **异常**: 无。Phase 4 cross-instruction classification 全层准确率 1.000，Phase 5 best RSA = 0.6216 (L28)

### 实验 2: nora_goal_untrained_cf (cuda:1, PID 541450)
- **运行时间**: 17 分 38 秒
- **当前阶段**: 第 2 个 condition `empty`, 4800/5000 samples（即将完成）
- **已完成**: condition `wrong` (cos_dist=0.0143, cross-task d=7.7111)
- **进度**: 2/4 conditions，`empty` 约 1 min 内完成，之后还有 `shuffled` + `paraphrased`
- **预估剩余**: ~20-25 min（每个 condition ~10 min）
- **GPU**: 41% 利用率，8.5/97.9 GB 显存
- **异常**: 无

两个实验均健康运行，预计实验 2 先完成（~20-25 min），实验 1 稍后（~60-70 min）。

---
