# check home full status 2h

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_home-full-status-2h_20260514T193400_result.json`
- **Structured JSON:** [`694f824250c9305bb506.json`](../../sessions/69/694f824250c9305bb506.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== GPU 状态 ===
RTX 5090 | 85°C | 532W/575W | 31727/32607 MiB (97.3%) | GPU-Util 100%
PID 3159474: python eval_repo_cls.py (seed123 ckpt-400 val@5120)

=== Tmux sessions ===
eval_8b_val5120_fix: 1 window (created Thu May 14 10:31:30 2026)

=== 已完成的 val@5120 结果 ===
| Checkpoint | N | Accuracy | F1_macro | F1_pass | F1_fail | Trunc% | Unparse% |
|---|---|---|---|---|---|---|---|
| 8B ckpt-3000 | 9335 | **89.50%** | **84.08%** | 93.37% | 74.78% | 2.5% | 0% |
| 8B conda ckpt-400 | 9335 | 80.47% | 75.84% | 86.42% | 65.27% | 2.5% | 0% |

Confusion matrices:
- **8B ckpt-3000**: TP=6902 FP=799 FN=181 TN=1453 (Prec=89.6% Rec=97.4%)
- **8B conda ckpt-400**: TP=5799 FP=539 FN=1284 TN=1713 (Prec=91.5% Rec=81.9%)

=== 正在运行 ===
当前 eval: **seed123 ckpt-400** (Qwen3-4B) val@5120
进度: **5904/9335** (63.2%), running_acc=**85.67%**, F1_macro=79.17%
速度: ~120 samples/min (batch ~8s/16样本)
预计完成: **~13:00 PDT** (还需 ~28 min)

=== 异常 ===
1. **val_sweep 脚本 OOM 崩溃** — 8B eval 完成后，sweep 脚本尝试在同一 GPU 上接力加载 seed123 ckpt-400 的 4B LoRA adapter，触发 `CUDA error: out of memory`（8B 模型残留显存未释放）。崩溃时间: 11:52。
2. **手动恢复** — tmux session `eval_8b_val5120_fix` 中已手动重启 seed123 eval (PID 3159474, 11:51 开始)，当前运行正常。
3. **Sweep 队列中断** — val_sweep.sh 不存在（未找到脚本文件），无法确认后续还有哪些 checkpoint 排队。如果 sweep 计划包含更多 checkpoint，需要手动逐个启动。

---
