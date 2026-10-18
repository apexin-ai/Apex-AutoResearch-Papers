# harvest deploy westd 27271

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest-deploy_westd-27271_20260523T115550_result.json`
- **Structured JSON:** [`6cd7f0415b5476d1ee74.json`](../../sessions/6c/6cd7f0415b5476d1ee74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Downloads are actively progressing (20M so far for goal shard). This will take a while at AutoDL proxy speeds (~1-2 hours for ~4.7GB each).

Here's the current status:

---

**E5 Spatial 结果 (已收割, registry 已更新为 DONE):**
- **attn_mean**: SR=**91.6%** (458/500), 95% CI [88.8%, 93.7%]
- **attn_rollout**: SR=**92.8%** (464/500), 95% CI [90.2%, 94.8%]
- 对比 attn_last: 88.8%

Per-task 最弱环节均为 Task 5 (bowl_on_ramekin): mean 40%, rollout 46%, last 也类似。

**OpenVLA 可用性:**
- 模型路径: `/root/autodl-tmp/openvla-7b-finetuned-libero-{goal,10,spatial}`
- 脚本: `/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py`
- Spatial baseline 已完成: **80%** SR

**OpenVLA 部署问题:**
- 两个模型有损坏的 safetensor 分片:
  - **libero-goal**: shard 1 = 14MB (应为 ~4.6GB)
  - **libero-10**: shard 3 = 2.4GB (应为 ~4.7GB)
- 正在后台重新下载 (PID 989638/989684)
- 下载完成后需要重新启动 eval 实验:
  - GPU 0: `eval_openvla_l2norm_k05_goal_seed42`
  - GPU 1: `eval_openvla_l2norm_k05_long_seed42`

**新部署: 待下载完成后启动** — 预计下载需要 1-2 小时。可以稍后检查下载状态并部署:
```bash
ls -lh /root/autodl-tmp/openvla-7b-finetuned-libero-goal/model-00001-of-00004.safetensors
ls -lh /root/autodl-tmp/openvla-7b-finetuned-libero-10/model-00003-of-00004.safetensors
```

---
