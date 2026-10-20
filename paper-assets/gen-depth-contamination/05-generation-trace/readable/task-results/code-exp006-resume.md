# code exp006 resume

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp006-resume_20260514T210748_result.json`
- **Structured JSON:** [`ea664d87a84211d5858c.json`](../../sessions/ea/ea664d87a84211d5858c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

- **清理**: 删除了 `graduated_a0.7_s456` 残留目录（仅含 `filter_config.json`）
- **脚本**: 无需修改，`run_one()` 已内置 skip 逻辑（检查 `eval_results.json`）
- **timeout**: 本次通过裸 tmux 启动，无 `timeout` 包装，不会再被 24h 杀掉
- **启动**: tmux session `exp_006_graduated_filtering` 运行中，GPU 88% 利用率
- **进度**: 33/50 skip 完成，`graduated_a0.7_s456` 正在训练（2814 steps, ~1.27 it/s）
- **剩余**: 18 runs（a0.7×3 + a0.9×5 + surprisal×5 + dsir×5），ETA ~13.5h（~05-15 18:30 UTC）
- **日志**: `~/runs/gen-depth-contamination/exp_006_resumed.log`

---
