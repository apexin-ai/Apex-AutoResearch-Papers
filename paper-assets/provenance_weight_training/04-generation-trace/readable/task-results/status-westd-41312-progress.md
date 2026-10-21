# status westd 41312 progress

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_westd-41312-progress_20260516T141918_result.json`
- **Structured JSON:** [`a2d9730d8b69c7bf4392.json`](../../sessions/a2/a2d9730d8b69c7bf4392.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。汇总如下：

---

## 实验进度汇总（westd-41312）

所有 4 个进程均存活，max_steps 均为 **6103**。

### cuda:0 — llama3b_uniform (PID 3112)
- **状态**: ALIVE
- **模型**: Llama-3.2-3B
- **当前 step**: ~1000/6103 (**16.4%**)
- **训练速度**: 5.22 s/step
- **已完成 eval**: step 500 → eval_loss=**2.5689**（eval 耗时 87min）
- **当前**: 刚触发 step 1000 的 eval
- **Checkpoint**: checkpoint-500
- **预估剩余**: 训练 ~7.4h + eval（~11 次 × 87min ≈ 16h）= **~23h**

### cuda:1 — llama3b_adaptive (PID 4005)
- **状态**: ALIVE
- **模型**: Llama-3.2-3B
- **当前 step**: ~980/6103 (**16.1%**)
- **训练速度**: 5.33 s/step
- **已完成 eval**: step 500 → eval_loss=**2.5808**（eval 耗时 86min）
- **Checkpoint**: checkpoint-500
- **预估剩余**: **~23h**

### cuda:2 — hybrid_rho04 (PID 3656)
- **状态**: ALIVE
- **模型**: Qwen3-0.6B（scored_data_hybrid.jsonl, adaptive+filter, rho=0.4）
- **当前 step**: ~1500/6103 (**24.6%**) — 正在跑 step 1500 的 eval（eval 进度 59%）
- **训练速度**: 2.42 s/step
- **Eval 历史**:
  - step 500: eval_loss=**3.1170**
  - step 1000: eval_loss=**3.0953**
- **Checkpoints**: checkpoint-500, checkpoint-1000
- **预估剩余**: 训练 ~3.1h + eval（~9 次 × 44min ≈ 6.6h）= **~10h**

### cuda:3 — hybrid_rho06 (PID 3727)
- **状态**: ALIVE
- **模型**: Qwen3-0.6B（scored_data_hybrid_rho06.jsonl, adaptive+filter, rho=0.6, tau=0.7）
- **当前 step**: ~1500/6103 (**24.6%**) — 正在跑 step 1500 的 eval（eval 进度 64%）
- **训练速度**: 2.24 s/step
- **Eval 历史**:
  - step 500: eval_loss=**3.1160**
  - step 1000: eval_loss=**3.0916**
- **Checkpoints**: checkpoint-500, checkpoint-1000
- **预估剩余**: **~10h**

---

## Part 2: hybrid 完成确认

**hybrid 实验均未完成**，目前仅在 ~24.6%，远未达到之前报告的 77-79%。这些是新启动的实验（运行约 2h53m），不是之前的那批。

- 无 post-hoc eval 输出（`/root/autodl-tmp/output/eval/` 目录不存在）
- 两个 hybrid 均正卡在 eval 上（67823 个 eval 样本，每次 eval 约 44min）

**关键瓶颈**: eval 集太大（67823 样本），eval 耗时占总时长 2/3 以上。Llama-3B 的 eval 更是每次 87min。如果不需要如此频繁的 eval，可以考虑增大 eval_steps 或减小 eval 集。

---
