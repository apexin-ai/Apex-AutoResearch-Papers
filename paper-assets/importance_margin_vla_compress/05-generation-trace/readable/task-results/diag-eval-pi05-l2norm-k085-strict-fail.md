# diag eval pi05 l2norm k085 strict fail

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval_pi05_l2norm_k085_strict_fail_20260527T115811_result.json`
- **Structured JSON:** [`59a416e282cc335399d0.json`](../../sessions/59/59a416e282cc335399d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**Part 1 — 诊断 `eval_pi05_l2norm_k085_long_seed42_strict`**:
- 实验**实际已成功完成**，SR=77.6%，结果已保存。
- 失败是监控系统的 false positive：监控在 `~/runs/` 找日志（不存在），实际日志在 `logs/` 目录下。进程正常退出，无 sentinel/W&B 信号导致监控误判。

**Part 2 — 已部署 `eval_pi05_l2norm_k07_long_seed42_strict`**:
- 服务器: cqa1-33015, GPU2
- PID: 274734
- 状态: RUNNING，模型加载中
- 预计运行时间: ~3.5h（libero_10 Long suite）
- 日志: `/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_l2norm_k07_long_seed42_strict.log`

---
