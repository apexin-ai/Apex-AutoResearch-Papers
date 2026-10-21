# analysis eval pi05 baseline object seed42 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-pi05-baseline-object-seed42-r2_20260521T045550_result.json`
- **Structured JSON:** [`7a6fa6222a294280f54b.json`](../../sessions/7a/7a6fa6222a294280f54b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**π0.5 r2 分析完成。**

**核心结论：NO-GO。** r2 完整 run（200 episodes, 10 tasks × 20 rollouts）SR = 0.0%，全部 task 均为零。

关键发现：
- 5 个 fix 均已在代码层面确认实现（MEAN_STD, image [-1,1], vision tower 437 keys, padding_side right）
- 唯一未生效的是 `TORCH_COMPILE_DISABLE=1`（进程环境中缺失），但不影响自定义 wrapper 路径
- **diag 日志暴露深层问题**：所有 action sample 的 gripper 值恒定 ~0.98（永远 open），机器人无法抓取任何物体
- lerobot native API 也因 torch.compile 兼容性崩溃

**Plan B 的可行路径**：先设 `TORCH_COMPILE_DISABLE=1`，重试 lerobot native API (`policy.predict_action_chunk`)，对比其 action 输出。如果 native API 也 0%，说明 fine-tuned 模型本身有问题，需要回退到 OpenPI 原始代码验证。

---
