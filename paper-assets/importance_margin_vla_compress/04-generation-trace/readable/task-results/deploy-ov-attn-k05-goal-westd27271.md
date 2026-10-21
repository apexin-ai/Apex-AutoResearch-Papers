# deploy ov attn k05 goal westd27271

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_ov_attn_k05_goal_westd27271_20260527T101738_result.json`
- **Structured JSON:** [`a2237ba1a4b4505a3007.json`](../../sessions/a2/a2237ba1a4b4505a3007.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。实验 `eval_openvla_attn_k05_goal_seed42_v4` **已在 westd-27271 GPU0 上运行**，无需重新提交。

状态：
- **PID 830291**，17:55 启动，已运行 ~2.4h
- 当前进度：Task 1/10（`open the middle drawer of the cabinet`），30/50 episodes，~1.5 eps/min
- Attention pruning 正常：256 → 128 vision tokens (k=0.5)
- 模型路径：`/root/autodl-tmp/openvla-7b-finetuned-libero-goal`（实际路径，非任务中假设的 `models/` 子目录）

Registry 已更新为 RUNNING，failure_reason 已清空。conclusion 字段不支持置空，但实验跑完后会被正确覆盖。

---
