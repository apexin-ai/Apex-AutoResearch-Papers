# ops rerun l2norm k07 seed43 westd27271

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_rerun-l2norm-k07-seed43-westd27271_20260520T221911_result.json`
- **Structured JSON:** [`334b8a2ae3996db13c4b.json`](../../sessions/33/334b8a2ae3996db13c4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**脚本参数确认**：`--mode` (choices: baseline/random_prune/l2norm_prune) + `--k_ratio` (float, default 0.5) — 之前错误用了 `--keep_ratio`。

**进程状态**：
- tmux session: `eval_l2norm_k07_s43_v2`
- 服务器: westd-27271, GPU 0
- 日志: `/tmp/eval_l2norm_k07_s43_v2.log`

**初始日志确认 pruning 生效**：
```
[*] L2 norm pruning: k=0.7
[L2 Pruning] 256 -> 179 vision tokens (k=0.7)
```
256 × 0.7 = 179.2 → 保留 179 tokens，符合预期。

**Registry**: `eval_openvla_prune_l2norm_k07_seed43_v2` → RUNNING，parent = `eval_openvla_prune_l2norm_k07_seed43`。

预计运行约 4 小时（参考旧 run 238 分钟）。

---
