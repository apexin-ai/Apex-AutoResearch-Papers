# eval token merging k05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_token_merging_k05_20260517T094313_result.json`
- **Structured JSON:** [`d6677d79ce7fe45aac2d.json`](../../sessions/d6/d6677d79ce7fe45aac2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全量 eval 运行正常。

## 报告

1. **rsync 状态**: 未使用 rsync/scp 直传（两台服务器不直连）。改为直接在 westd 上 patch 添加 merge 代码（4 处修改：argparse choices、register_acis_hook 函数、2 个调用点、summary dict），并额外添加了 `--k_ratio` CLI 覆盖参数。

2. **验证**: westd 上 `grep -c "merge"` = 10 处匹配，覆盖完整。

3. **dry-run**: 通过，无错误。Task 0 完成 2 episodes（0/2 SR，正常）。

4. **全量 eval 已启动**:
   - tmux session: `eval_merge_k05`
   - checkpoint: `libero_acis_stage1only_k07/stage1_done/checkpoint.pt`（用户指定的 `libero_acis_stage1only` 不存在，用 k07 替代）
   - k_ratio: 0.5（CLI 覆盖，log 确认 `Overriding k_ratio to 0.50`）
   - pruning-method: merge, merge_alpha: 1.0
   - 50 episodes/task, 10 tasks, libero_object
   - 输出: `eval_results/eval_merge_k05.json` + `eval_results/eval_merge_k05.log`

5. **注意**: westd 上还有另一个 tmux session `eval_k07_zero_mask` 在运行，两个 eval 共享 GPU 0，可能互相影响速度。

---
