# deploy a1 baseline object r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_a1-baseline-object-r2_20260524T133243_result.json`
- **Structured JSON:** [`4c55be426bbee5a1ff0b.json`](../../sessions/4c/4c55be426bbee5a1ff0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。总结：

**前一个 Worker 已在 GPU 0 上启动了 A1 eval**，我发现后杀掉了自己重复启动的 GPU 2 进程。

当前状态：
- **实验**: `eval-a1-baseline-object-s42` → RUNNING
- **服务器**: bjb1-32546, GPU 0, tmux session `a1_eval`, PID 462251
- **进度**: Task 0 完成 SR=65% (13/20)，Task 1 进行中，共 32/200 trials
- **日志**: `/tmp/a1_eval.log`，输出: `logs/eval_object_a1_vla_only_seed42.json`
- **Registry 已更新**

注意：Task 0 的 SR 只有 65%，远低于 A1 官方 Object 99.8%。后续需关注最终整体 SR，可能与 eval 框架差异、rollout 数、tokenizer 配置有关。

---
