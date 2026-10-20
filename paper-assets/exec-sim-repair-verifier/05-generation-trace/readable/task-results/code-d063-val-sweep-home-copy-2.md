# code d063 val sweep home

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d063-val-sweep-home_20260514T060839_result.json`
- **Structured JSON:** [`e8dcd47f983fbe0a70fa.json`](../../sessions/e8/e8dcd47f983fbe0a70fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Val sweep 已启动，10 个 checkpoint 串行跑 val eval（9335 样本/checkpoint）。预计每个约 20-30 分钟，总计约 3-5 小时。

**已完成：**
- `eval_repo_cls.py` 添加了 `--split` 参数（choices=val/test，default=test）
- 数据路径自动切换为 `swebench_{split}.jsonl`
- 输出 JSON 包含 `split` 字段

**正在运行：**
- tmux session `val_sweep`，日志 `/home/sonny/exec-sim-repair-verifier/val_sweep.log`
- 结果写入 `val_eval_results/` 目录
- 10 个 checkpoint：seed123 (200/400/600/800/1000) + v5 (600/4000/4200/4400/4600)

稍后检查进度时用 `tail val_sweep.log` 即可。需要我现在轮询等待，还是你晚点问我结果？

---
