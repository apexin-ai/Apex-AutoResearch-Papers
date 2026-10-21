# eval s42 extended val sweep restart

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_s42-extended-val-sweep-restart_20260515T154656_result.json`
- **Structured JSON:** [`9d6d1d59d1be8ec300d1.json`](../../sessions/9d/9d6d1d59d1be8ec300d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU 0 不空闲。** pid 387617 正在运行，已跑 1h05m：

```
python3 eval_cwm_baseline.py --data_dir data \
  --checkpoint_dir checkpoints_cwm_rank32_alpha64/best \
  --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B \
  --output checkpoints_cwm_rank32_alpha64/best/eval_results.json --save_predictions
```

这是 CWM rank32-alpha64 ablation 的 eval，占用 13345 MiB / 32607 MiB。

**Checkpoint 情况**：1800→5200 全部 18 个 checkpoint 都已存在（实际有 26 个 ckpt，800→5800）。

**Sweep 脚本**：`run_extended_val_sweep.sh` 存在，内容正确，覆盖 18 个 step（1800-5200），使用 cuda:0，batch_size=1。

**4 GPU 全占满：**
| GPU | PID | 占用 | 进程 |
|-----|-----|------|------|
| 0 | 387617 | 13.3 GB | eval_cwm_baseline.py (ablation eval) |
| 1 | 295794 | 27.3 GB | s42-resume training |
| 2 | 266816 | 30.7 GB | 未知 |
| 3 | 381618 | 22.5 GB | 未知 |

按指示不 kill 残留进程。需要等 pid 387617 完成后才能启动 sweep。要我持续监控等它结束后自动提交，还是你来决定下一步？

---
