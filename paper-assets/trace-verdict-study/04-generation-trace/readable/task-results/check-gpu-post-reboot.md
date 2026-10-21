# check gpu post reboot

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_post_reboot_20260518T132017_result.json`
- **Structured JSON:** [`c7c6dc2a721f302be53d.json`](../../sessions/c7/c7c6dc2a721f302be53d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

## GPU 状态

| GPU | 型号 | 显存使用 | GPU-Util | 状态 |
|-----|------|---------|----------|------|
| cuda:0 | RTX PRO 6000 Black (98GB) | 49175 MiB / 97887 MiB | 0% | **幽灵占用** — 无进程但显存未释放，`gpu-reset` 不支持 |
| cuda:1 | RTX PRO 6000 Black (98GB) | 0 MiB / 97887 MiB | 0% | **空闲** |

GPU0 的 49GB 是残留显存（无对应进程），`nvidia-smi --gpu-reset` 不支持该卡。需要重启 nvidia driver 或忽略（下次启动训练时 CUDA 会自动回收）。

## PID 存活

| PID | 实验 | 状态 |
|-----|------|------|
| 434876 | qwen7b_full_trace_tail384_seed42 (cuda:0) | **已死** |
| 434952 | deepseek_full_trace_tail384_seed42 (cuda:1) | **已死** |

## 关键发现：训练已完成

两个实验在重启前已**训练完毕**，checkpoint 完整保存：

- `qwen7b_full_trace_tail384_seed42`: 3 个中间 checkpoint (148/296/444) + `final/`（adapter 155MB），完成时间 20:54
- `deepseek_full_trace_tail384_seed42`: 3 个中间 checkpoint (148/296/444) + `final/`（adapter 153MB），完成时间 20:54

路径：`/root/autodl-tmp/trace-verdict-study-checkpoints/{qwen7b,deepseek}_full_trace_tail384_seed42/final/`

## 无需重新训练，但可能需要评估

两个实验 `final/` 目录中没有 `eval_results.json`，说明评估尚未执行。如果需要评估，可以直接跑 evaluate.py。

## 其他活跃进程

只有 JupyterLab、TensorBoard 和几个 HTTP 文件服务器在运行，无 tmux session，无训练进程。

## 最近完成的实验日志

`/root/trace-verdict-study/logs/` 下有 12 个实验日志（codellama13b、deepseek、qwen15b 多个 truncation 变体），最新的是 `codellama13b_head2048_seed42.log`（11:30）。tail384 的两个实验没有日志文件在这个目录，可能日志在 nohup 输出或 wandb 中。

---
