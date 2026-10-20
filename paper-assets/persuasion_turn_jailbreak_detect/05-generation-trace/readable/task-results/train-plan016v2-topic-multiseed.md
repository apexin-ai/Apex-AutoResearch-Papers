# train plan016v2 topic multiseed

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_plan016v2-topic-multiseed_20260518T061237_result.json`
- **Structured JSON:** [`a2dee5f27a02b95fb205.json`](../../sessions/a2/a2dee5f27a02b95fb205.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

**Plan 016v2 Topic Control — 3-seed (42/123/456) 统计**

| K | DD OOD F1 (mean±std) | IID F1 (mean±std) |
|---|---|---|
| k=1 | 0.591 ± 0.132 | 0.811 ± 0.062 |
| k=2 | 0.593 ± 0.166 | 0.899 ± 0.035 |
| k=3 | 0.568 ± 0.167 | 0.930 ± 0.035 |
| k=5 | 0.573 ± 0.206 | 0.982 ± 0.016 |
| full | 0.541 ± 0.207 | 0.974 ± 0.022 |

关键发现：
- DD OOD F1 均值 0.54-0.59，**远低于 persuasion treatment 的 1.0**，但标准差很大（0.13-0.21），seed=123 是明显异常值（full F1=0.25）
- IID F1 稳定高（0.81-0.97），说明 topic encoder 在分布内任务上有效，但 OOD 泛化不稳定
- 这更加强了结论：**persuasion-specific features 是跨攻击泛化的关键驱动力，topic classification 不够**

已更新 registry metrics 和注册 artifact。远程结果文件：
- `results/plan_016v2_topic_seed42.json`
- `results/plan_016v2_topic_seed123.json`
- `results/plan_016v2_topic_seed456.json`
- `results/plan_016v2_topic_3seed_summary.json`

---
