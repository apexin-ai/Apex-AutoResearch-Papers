# train perlayer kl k4 s123 fix

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_perlayer_kl_k4_s123_fix_20260522T133918_result.json`
- **Structured JSON:** [`2e8562a0aaf84f34a76f.json`](../../sessions/2e/2e8562a0aaf84f34a76f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**两个训练都在正常跑。** 情况总结：

- **s123 (PID 59575)**: Step 100/2700，dt=185.6s（100步用了约 3 分钟），kl=0.0938，avg_sp=0.400 — 正常训练中
- **s456 (PID 59889)**: Step 100/2700，dt=185.0s，kl=0.0864，avg_sp=0.399 — 正常训练中

**之前的判断有误**：s123 并没有因 wandb 崩溃。pipeline 脚本中已经有 `WANDB_MODE=disabled`，训练从一开始就成功启动了。log 看起来"卡住"只是因为 `log_every=100`，每 100 步才输出一行。

`tmux kill-session` 杀掉了 tmux 窗口，但底层的 nohup 进程链存活了（bash 59570 → python 59575），log 文件继续写入。

**不需要修复或重提交。** 按 ~1.86s/step 估算，2700 步约需 84 分钟（约 1.5 小时）完成 Phase 1。两个 GPU 都满载运行中。

---
