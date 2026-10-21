# diagnose eval vla only object seed45

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-vla-only-object-seed45_20260516T145848_result.json`
- **Structured JSON:** [`bd5c353bdb1f0bdb89a6.json`](../../sessions/bd/bd5c353bdb1f0bdb89a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**实验没有失败——它已经成功完成。**

### 证据

- 输出文件 `eval_object_vla_only_seed45.json` 于 2026-05-16 20:36:31 写入，包含完整结果
- 日志 `eval_object_vla_only_seed45.log` 显示 10 个任务 × 20 rollouts = 200 次评估全部跑完，无报错
- 最终输出：`Overall success rate (vla_only): 9.0% (18/200)`
- 进程正常退出（return_code=0）

### "失败"的原因

这个 evaluate 脚本**不会向 W&B 上报指标**——它只把结果写到本地 JSON 文件。所以"5次无有效 W&B 指标输出"是因为脚本本身不集成 W&B，不是因为进程崩溃。

### GPU cuda:4 状态

当前空闲：1MiB 显存占用，0% 利用率，P8 省电状态。可用。

### 结论

| 项目 | 结果 |
|------|------|
| 失败根因 | **无失败**，实验正常完成，只是没有 W&B 集成 |
| 是否需要重试 | 不需要，结果已完整 |
| cuda:4 可用性 | 可用（空闲） |
| 实验结果 | vla_only mode, object benchmark, seed=45, overall 9.0% |

---
