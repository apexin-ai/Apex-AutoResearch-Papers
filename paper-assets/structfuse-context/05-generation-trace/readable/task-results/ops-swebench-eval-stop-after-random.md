# ops swebench eval stop after random

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_swebench-eval-stop-after-random_20260516T002304_result.json`
- **Structured JSON:** [`500b8fd3218d790ab7b1.json`](../../sessions/50/500b8fd3218d790ab7b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**运行方式**：批量脚本 `run_swebench_eval_100.sh`（PID 61320），循环 3 个 checkpoint：random_s42 → embedding_distance_s43 → dataflow_aware_s43。

**措施**：利用脚本自带的 skip 逻辑，在后两个 checkpoint 的输出目录中创建了 placeholder `summary.json`（内容标记为 `skipped_by_director`）。脚本检测到 `summary.json` 已存在会自动跳过。

**验证**：
- 两个 placeholder 文件已就位
- random_s42 eval（PID 61328）仍正常运行（已跑 5h39m，状态 `Rl`）
- random_s42 完成后，脚本会 skip 剩余两个 checkpoint 并退出

后续如需恢复评测，删除这两个 placeholder 即可：
```
rm /root/autodl-tmp/structfuse/artifacts/swebench_retrieval_eval/{embedding_distance_s43_100,dataflow_aware_s43_100}/summary.json
```

---
