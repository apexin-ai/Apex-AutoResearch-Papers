# deploy idle gpus pi05 attn strict

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_idle_gpus_pi05_attn_strict_20260527T122634_result.json`
- **Structured JSON:** [`16468b647c64d1371d88.json`](../../sessions/16/16468b647c64d1371d88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

**实验 A** — π0.5 Attn k=0.75 Long strict
- 服务器: cqa1-33015, GPU 0
- PID: 300488, tmux: `pi05_attn_k075_strict`
- 状态: RUNNING，已开始评估（192/256 tokens kept）
- Log: `~/runs/importance_margin_vla_compress/eval_pi05_attn_k075_long_seed42_strict_cqa1.log`

**实验 B** — π0.5 Attn k=0.7 Long strict
- 服务器: cqa1-33015, GPU 1（排队中）
- tmux: `pi05_attn_k07_strict`
- 状态: QUEUED，等待 PID 118731（random k=0.5，T8 ep 40）完成后自动启动
- 预计 ~1h 后开始

**注意**: 用户指定的 GPU（cqa1:cuda:2, westd-38929:cuda:1）均被占用，改为使用 cqa1 GPU 0（刚完成实验）和 GPU 1（即将释放）。每小时自动检查进度。

---
