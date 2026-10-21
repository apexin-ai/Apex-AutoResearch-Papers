# urgent cqa1 direct fix p0 v4

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_cqa1-direct-fix-p0-v4_20260526T225654_result.json`
- **Structured JSON:** [`bdfcef2321e9c90ed49a.json`](../../sessions/bd/bdfcef2321e9c90ed49a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

```
== Step 1: Kill GPU 2 ==
结果: 服务器只有 2 块 GPU (0, 1)，GPU 2 不存在，kill 为空操作

== Step 2: 脚本确认 ==
脚本路径: /root/autodl-tmp/importance_margin_vla_compress/eval_pi05_pruning_libero.py
参数格式确认: 正确，但 prune_mode 只支持 none/random/l2norm，不支持 "attention"

== Step 3: 部署 ==
GPU 0 tmux (pi05_l2norm_k07_long_rerun): 创建成功，实验运行中
GPU 1 tmux (pi05_attn_k07_long_rerun): 创建成功，但实验立即失败 — "attention" 不是有效的 prune_mode
GPU 2 tmux (pi05_attn_k075_long): 创建成功，但实验立即失败 — 同上 + GPU 2 物理不存在

== Step 4: 验证 ==
GPU 0: PID=551487 显存=10695MiB 日志=在写（已开始 eval，l2norm n_keep=179/256）
GPU 1: 失败 — prune_mode "attention" invalid (choose from none/random/l2norm)
GPU 2: 失败 — GPU 不存在 + prune_mode invalid

预存进程:
  GPU 0: PID 499267 (OpenVLA attn_prune k=0.75 libero_goal) 15470MiB
  GPU 1: PID 397225 (OpenVLA attn_prune k=0.5 libero_10) 16099MiB

== Step 5: GPU 3 日志 ==
PID 732826: 已死
GPU 3: 不存在（服务器仅 2x NVIDIA RTX PRO 6000 Blackwell 97GB）
```

**需要 Director 决策：**
1. `eval_pi05_pruning_libero.py` 不支持 `attention` prune mode（只有 none/random/l2norm）。是否需要先给脚本添加 attention pruning 支持，还是改用其他 prune_mode？
2. 服务器只有 2 块 GPU，GPU 1 被预存 OpenVLA 实验占用。是否 kill PID 397225 以腾出 GPU 1？

---
