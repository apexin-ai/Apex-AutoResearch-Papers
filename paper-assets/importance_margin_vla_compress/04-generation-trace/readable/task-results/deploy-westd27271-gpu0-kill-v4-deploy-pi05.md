# deploy westd27271 gpu0 kill v4 deploy pi05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd27271_gpu0_kill_v4_deploy_pi05_20260527T104101_result.json`
- **Structured JSON:** [`3acd8573b961a6ccceb2.json`](../../sessions/3a/3acd8573b961a6ccceb2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

- **PID 830291** (OV Attn k=0.5 Goal v4) 已 kill，registry 标记 `conclusion=killed`
- **π0.5 Random k=0.85 strict** 已在 westd-27271 GPU0 启动，tmux session `pi05_rand_k085`，模型加载中，registry 状态 RUNNING
- 首次部署因 tmux 内无 conda 环境导致 `python: command not found`，已修复（加 `source conda.sh && conda activate base`）

---
