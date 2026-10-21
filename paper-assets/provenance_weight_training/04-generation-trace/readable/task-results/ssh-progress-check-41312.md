# ssh progress check 41312

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_progress_check_41312_20260517T205057_result.json`
- **Structured JSON:** [`2077d81cae9564092f05.json`](../../sessions/20/2077d81cae9564092f05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

综合分析。计算速度和 ETA。

关键发现：所有 4 个 checkpoint 间的训练速度一致为 **2.11 s/step**。step_metrics 文件存在 ~38-57 min 的写入延迟（OS buffer 未 flush），实际进度比文件记录更前。

| 实验 | 估算当前 step/total | 最近 loss | 速度 | eval_data_path | 预估完成 (UTC) |
|------|---------------------|-----------|------|----------------|----------------|
| qwen06b_uniform_seed42 (GPU0) | ~5565/6103 | 1.93 | 2.11 s/step | **无** | **~21:12 UTC May 17** |
| ess_only_seed456 (GPU1) | ~3000/6103 (eval中) | 2.88 | 2.11 s/step + 44min/eval | 有 | **~03:17 UTC May 18** |
| ess_only_seed123 (GPU2) | ~3000/6103 (eval中) | 2.46 | 2.11 s/step + 44min/eval | 有 | **~03:13 UTC May 18** |
| random_reweight_seed456 (GPU3) | ~1870/6103 | 0.95 | 2.11 s/step + 44min/eval | 有 | **~06:00 UTC May 18** |

**状态详情：**
- 全部 4 进程存活，GPU 利用率 93-100%，温度 62-73°C
- GPU 显存：GPU0 (uniform) 46GB/98GB；GPU1-3 均 75GB/98GB（额外显存用于 eval 数据）
- uniform 实验 **没有** `--eval_data_path`，只做训练，最先完成（约 19 分钟后）
- ess_only 两个实验当前均在执行 step 3000 的 eval（每次 eval ~44 min）
- random 实验刚完成 step 1500 的 eval，已恢复训练
- 每 500 步触发一次 eval + save（有 eval_data_path 的实验）

**注意：** uniform 实验用了 `--max_steps 6103` 而非 `--num_train_tokens`，且无 eval，所以显存占用低且速度稳定无中断。

---
