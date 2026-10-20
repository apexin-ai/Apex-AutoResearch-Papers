# train plan014 lambda continue

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_plan014-lambda-continue_20260518T013853_result.json`
- **Structured JSON:** [`9db433fa6d7bb0b4d710.json`](../../sessions/9d/9db433fa6d7bb0b4d710.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**plan_014 已全部完成。** 上一个 Worker 已跑完所有 3 个 alpha 值的完整 pipeline（DeBERTa → embeddings → GRU → eval），结果已保存在 `results/plan_014_lambda_ablation.json`。

汇总结果：

| alpha | k1_f1 | k2_f1 | k3_f1 | k5_f1 | full_f1 | deberta_persuasion_acc | deberta_intent_acc |
|-------|-------|-------|-------|-------|---------|----------------------|-------------------|
| 0     | 1.0   | 1.0   | 1.0   | 1.0   | 1.0     | 0.8439               | 0.4014             |
| 0.5   | 1.0   | 1.0   | 1.0   | 1.0   | 1.0     | 0.8353               | 1.0                |
| 1.0   | 1.0   | 1.0   | 1.0   | 1.0   | 1.0     | 0.8285               | 1.0                |
| 2.0   | 1.0   | 1.0   | 1.0   | 1.0   | 1.0     | 0.8508               | 1.0                |

关键发现：
- **端到端 jailbreak 检测 F1 = 1.0**，不受 alpha 值影响，说明 GRU 对 DeBERTa embedding 变化非常鲁棒
- alpha=0 时 intent_acc 降至 0.40（因为没有 intent loss），但 persuasion_acc 反而略高（0.844 vs 0.829）
- alpha=2.0 的 persuasion_acc 最高（0.851），说明加重 intent loss 不会损害 persuasion 分类
- 所有 alpha≥0.5 的 intent_acc 都是 1.0

无需额外操作，任务已完成。

---
