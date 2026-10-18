# ops westd27271 kill m128 deploy pi05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd27271-kill-m128-deploy-pi05_20260521T075250_result.json`
- **Structured JSON:** [`046f6fd3ff5d9b2ef3b6.json`](../../sessions/04/046f6fd3ff5d9b2ef3b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**Part 1** — M128 eval v2 (PID 188254) 已 kill，registry 更新为 DONE/failed，failure_reason 已记录。

**Part 2/3** — π0.5 checkpoint 和 eval 脚本在 westd-27271 上都不存在，无法在短期内就绪。

**Part 4 (fallback)** — 已启动 OpenVLA L2norm k=0.3 rerun：
- tmux session: `eval_l2norm_k03`
- PID: 193983，GPU0 已占 15.5GB
- exp_id: `eval_openvla_l2norm_k03_object_seed42_rerun`
- GPU1 上 M32 VTC train (PID 921279) 未受影响

---
