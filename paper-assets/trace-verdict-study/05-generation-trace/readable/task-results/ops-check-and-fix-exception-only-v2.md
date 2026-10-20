# ops check and fix exception only v2

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_and_fix_exception_only_v2_20260515T071918_result.json`
- **Structured JSON:** [`27a8eb6d944aad15ca1f.json`](../../sessions/27/27a8eb6d944aad15ca1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**cuda:1** — `vota_exception_only_seed42_v2` 训练中，状态正常
- PID 79633，71280 MiB 显存，100% GPU 利用率
- 进度 24/444 步 (5%)，~10.65s/step
- loss 从 0.956 降到 0.735，token accuracy 0.837，趋势正常
- 有 `--gradient_checkpointing`，不会再 OOM
- 训练完后会自动跑 eval（命令里 `&&` 串联了 evaluate.py）
- **预计训练剩余 ~75 分钟（约 1h15m），加 eval ~10min，总计约 16:40 完成**
- 注意：该 session 没有 log file redirect（输出在 tmux pane 里），不影响训练但没有持久化日志

**cuda:0** — analysis Worker 正在跑 `full_trace_label_only` 的 eval
- 两个 eval 进程（PID 80087 + 80437），各占 16186 MiB，共 ~32 GB
- 看起来被重复提交了一次（一个直接启动，一个 nohup 包装），但不影响 cuda:1 上的训练

**无需干预**，exception_only_v2 正在正常训练。基于 vota_no_ae 的 ~1.9h wall clock，本次因有 gradient_checkpointing 会稍慢，预计 ~1.5-1.7h 完成训练 + eval。

---
