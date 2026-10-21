# eval home d063 val sweep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_home-d063-val-sweep_20260514T174745_result.json`
- **Structured JSON:** [`e1d65fff52926af786e0.json`](../../sessions/e1/e1d65fff52926af786e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Sweep 脚本启动成功（PID 3153913），正在等待 8B ckpt-3000 完成。

汇总当前状态：

```
=== 已完成的 val@5120 结果 ===
| Checkpoint                    | Accuracy | F1_macro | Unparseable% | Truncated% |
|-------------------------------|----------|----------|-------------|-----------|
| 8B conda ckpt-400 val@5120    | 80.47    | 75.84    | 0.0%        | 2.51%     |

=== 正在运行 ===
8B westd ckpt-3000 val@5120: 1968/9335 = 21.1% (PID 3151214, tmux: eval_8b_val5120_fix)

=== 排队中 (nohup PID 3153913, 等 8B 完成后自动启动) ===
1. seed123 ckpt-400 val@5120
2. seed123 ckpt-600 val@5120
3. seed123 ckpt-800 val@5120
4. v5 ckpt-600 val@5120
5. v5 ckpt-4000 val@5120
6. v5 ckpt-4400 val@5120
7. v5 ckpt-4600 val@5120

=== 路径确认 ===
checkpoints_repo_cls_8b_westd/      → checkpoint-200, 2400, 2600, 2800, 3000
checkpoints_repo_cls_seed123_home/  → checkpoint-200, 400, 600, 800, 1000
checkpoints_repo_cls_v5/            → checkpoint-600, 4000, 4200, 4400, 4600
checkpoints_repo_cls_8b_conda_westd/ → (8B conda variant, ckpt-400 已完成 val)

=== 注意 ===
- 所有旧 results/ 下的结果都是 test@2048，不是 val@5120
- seed123 在 checkpoints_repo_cls_seed123_home/ (非 checkpoints_repo_cls_seed123/)
- v5 在 checkpoints_repo_cls_v5/ (非 checkpoints_repo_cls_v5_conda/)
- 4B 模型默认用 Qwen/Qwen3-4B，无需指定 --model_name
```

监控命令：
- 进度: `wc -l results/repo_cls_8b_ckpt3000_val5120/eval_repo_cls_predictions.jsonl`
- Sweep log: `tail -20 results/val_sweep.log`
- 进程: `ps -p 3151214,3153913 -o pid,stat,etime`

---
