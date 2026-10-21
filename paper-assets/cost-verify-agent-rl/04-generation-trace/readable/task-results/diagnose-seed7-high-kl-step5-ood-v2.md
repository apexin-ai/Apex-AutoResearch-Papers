# diagnose seed7 high kl step5 ood v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_seed7_high_kl_step5_ood_v2_20260522T002408_result.json`
- **Structured JSON:** [`4b2211dbc05dc2dffaf5.json`](../../sessions/4b/4b2211dbc05dc2dffaf5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 根本原因：v1 实际上**成功完成了**，被误判为失败

`seed7_high_kl_step5_ood.log` 完整记录了执行过程：

- Ray 正常初始化，CUDA_VISIBLE_DEVICES=3
- ALFWorld 环境正常加载（134 OOD tasks）
- 验证完成，耗时 ~24 分钟
- **EXIT_CODE=0**（正常退出）

**OOD 评估结果**（134 episodes，完整可靠）：
| 指标 | 值 |
|------|-----|
| success (pass@1) | **9.70%** (13/134) |
| num_actions | 45.9 |
| action_is_valid | 65.6% |
| pass@2 | 18.3% |
| pass@4 | 35.1% |
| pass@16 | 83.3% |
| pass@64 | 100% |

监控系统误判原因：进程退出时 W&B teardown 报了 `BrokenPipeError`，可能导致 sentinel 文件未写入或 W&B run 未正确关闭，监控系统检测不到完成信号就判定为 "process dead"。

### v2 从未真正启动

- 不存在 `seed7_high_kl_step5_ood_v2.log`
- PID 968497 已不存在（v1 的实际 PID 是 981591）
- v2 复用了旧 PID 968497 监控，发现进程已死，直接判定失败

### 不需要修复重跑

v1 已经产出了完整的 134-episode OOD 评估结果。seed7 high-KL step5 的 OOD success rate 是 **9.70%**。这个结果可以直接使用。

唯一需要做的是把这个结果从 log 中提取并正式记录，同时修正实验追踪系统中 v1/v2 的状态为"v1 succeeded, v2 unnecessary"。

---
