# deploy cqa1 gpu3 results and profiling

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-gpu3-results-and-profiling_20260525T201654_result.json`
- **Structured JSON:** [`cdd11801239e92f36209.json`](../../sessions/cd/cdd11801239e92f36209.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

### P1: 结果读取 + Profiling

**L2norm k=0.5 seed43 (eval_pi05_l2norm_k05_long_seed43_postfix_v2)**
- libero_10: **SR=53%** (265/500), 214.5 min
- libero_object: **SR=32%** (160/500), 150.2 min
- 无 goal/spatial 结果文件（实验只跑了这 2 个 suite）
- Registry 已更新为 DONE/success

**Profiling latency (GPU3)**
- k=1.0: 200 ± 26 ms
- k=0.9: 207 ± 42 ms (0.968x)
- k=0.5: 186 ± 20 ms (1.076x)
- 结论: **negative** — token pruning 对 π0.5 延迟改善极小（~7.6%），因为 vision tokens (768) 只占 LLM 总序列的一小部分，decoding 开销主导推理时间
- Registry 已更新为 DONE/negative，artifact 已注册

### P2: Zeromask 日志修复

- **zeromask_l2norm_k09** (PID 676529): 正在跑 libero_object，T1 ep=30 (97%)
- **zeromask_random_k09** (PID 675752): 正在跑 libero_object，T1 ep=40 (100%)
- 两个 tmux session 已通过 `pipe-pane` 捕获后续日志到:
  - `/root/runs/importance_margin_vla_compress/zeromask_l2norm_k09_object_seed42.log`
  - `/root/runs/importance_margin_vla_compress/zeromask_random_k09_object_seed42.log`
- 脚本会在完成时自动保存 JSON 到 `eval_results/`

GPU3 现已空闲（profiling 完成后进程退出）。

---
