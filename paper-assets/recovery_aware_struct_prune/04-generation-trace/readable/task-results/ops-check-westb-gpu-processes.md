# ops check westb gpu processes

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_westb_gpu_processes_20260517T132844_result.json`
- **Structured JSON:** [`a3e793eb281b806485a8.json`](../../sessions/a3/a3e793eb281b806485a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**cuda:0 — PID 710618**
- 任务：`eval_gsm8k.py`，评估 `pruned_cka_only_20` 模型，200 samples
- 输出：`eval_cka_only_20_n200.json`
- 启动时间：19:29，已跑 ~2h
- 进度：21:01 时 50/200 (acc=0.4400)，当前应约 75%，预计还需 ~30min
- 属于本项目 ✓

**cuda:1 — PID 715803**
- 任务：`eval_gsm8k.py`，同样评估 `pruned_cka_only_20`，200 samples
- 输出：`eval_postprune_cka_only_20.json`
- 来自 tmux session `scoring_ablation_random`，是 cka_only ablation 的 Step 2/4
- 启动时间：20:28，已跑 ~1h
- 进度：50% (99/200)，预计还需 ~44min
- 属于本项目 ✓

**tmux sessions：**
- `scoring_ablation_random`：正在运行 cka_only 的 post-prune eval（cuda:1 上的进程）
- `scoring_ablation_v2`：已完成，gradient SFT recovery 训练已结束并保存到 `sft_gradient_20`，终端空闲

**注意**：两个进程都在评估同一个模型 (`pruned_cka_only_20`)，但输出文件名不同。可能是重复评估——PID 710618 不是从 tmux 启动的（`?` 终端），可能是之前 agent 发起的。

---
