# diagnose eval openvla l2norm k05 long seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_openvla_l2norm_k05_long_seed42_20260527T011451_result.json`
- **Structured JSON:** [`c80dd1738e264e80865d.json`](../../sessions/c8/c80dd1738e264e80865d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验未失败，是监控误报。**

实验 `eval_openvla_l2norm_k05_long_seed42` 已于 2026-05-27 09:01:58 正常完成：

- **Overall SR: 16.4%** (82/500, 10 tasks × 50 episodes)
- 结果已保存: `eval_results/openvla_l2norm_prune_k05_10_seed42.json`

**误报原因**: 该实验没有生成 `/tmp/agent-ml-exit/` 下的 sentinel 文件，也没有 W&B 日志，监控系统 5 次轮询未检测到存活信号后自动判定失败。

**服务器现状**: GPU 0 空闲可用，GPU 1/2/3 分别在跑 l2norm k=0.95、l2norm k=0.75、attn k=0.95。磁盘 72% (72G 剩余)。

诊断报告已写入 `artifacts/diagnosis_eval_openvla_l2norm_k05_long_seed42.md`。

---
