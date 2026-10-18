# fix cqa1 kill openvla deploy pi05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cqa1_kill_openvla_deploy_pi05_20260526T052450_result.json`
- **Structured JSON:** [`26c68a2cb47ab66cb523.json`](../../sessions/26/26c68a2cb47ab66cb523.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在正常加载模型，无报错。

**汇总：**

| 步骤 | 状态 |
|------|------|
| Kill OpenVLA (PID 29974, 4365) | KILLED_OK，GPU2/3 已释放 |
| Registry 标记 failed | `eval_openvla_attn_k09_goal_seed43_v3` 和 `eval_openvla_random_k05_object_seed42_v2` → DONE/failed |
| GPU2: π0.5 L2norm k=0.5 Long | PID 77656，tmux `eval_pi05_l2norm_k05_long_seed42`，模型加载中 |
| GPU3: π0.5 Random k=0.5 Long | PID 77827，tmux `eval_pi05_random_k05_long_seed42`，模型加载中 |

cqa1-33015 当前 4 GPU 全部在用：GPU0 random k=0.75, GPU1 attention k=0.75, GPU2 l2norm k=0.5 (new), GPU3 random k=0.5 (new)。

---
