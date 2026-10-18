# deploy westd27271 check and deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd27271_check_and_deploy_20260522T163501_result.json`
- **Structured JSON:** [`f57fd02c8b5e1200c9e6.json`](../../sessions/f5/f57fd02c8b5e1200c9e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 GPU 都不空闲，不部署。

**cuda:0** (4606 MiB, 1% util) — **在跑**：
- PID 81215: `eval_xvla_pruning_libero.py --suite libero_goal --keep_ratio 0.7 --mode l2_norm` (X-VLA L2norm k=0.7 Goal), 349% CPU

**cuda:1** (3 MiB, 0% util) — **已预约**：
- tmux session `xvla_spatial` 中有一个排队链：正在 `while pgrep ... libero_goal; do sleep 30; done` 等 cuda:0 的 goal 实验跑完，然后会在 cuda:1 上依次跑 X-VLA Random 全套（Object/Spatial/Goal/Long × k=0.95/0.9/0.7，共 12 个实验）

两个 GPU 均被 X-VLA 评估占用/预约，无法部署 π0.5 Long 实验。

---
