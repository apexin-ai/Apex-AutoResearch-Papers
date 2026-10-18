# fix w38 cuda1 kill v2 deploy attn k09 s45

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_w38_cuda1_kill_v2_deploy_attn_k09_s45_20260528T005110_result.json`
- **Structured JSON:** [`9342eaea3e1252414cab.json`](../../sessions/93/9342eaea3e1252414cab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

- **已杀**: PID 885137 + 子进程 885146 (eval_pi05_attn_k085_long_seed44_strict_w38_v2)，registry 已标记 killed/DONE
- **已部署**: `eval_pi05_attn_k09_long_seed45_strict_w38` → westd-38929 cuda:1, PID 893099
  - Log 确认参数正确: `prune=attention, keep=0.9, eps=50, seed=45`
  - 模型加载中（尚未占 GPU 显存，约 2 分钟后上 GPU）

---
