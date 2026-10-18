# cleanup gpu collision fix 20260522

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cleanup_gpu_collision_fix_20260522_20260522T230218_result.json`
- **Structured JSON:** [`b8719283b57e13f402a0.json`](../../sessions/b8/b8719283b57e13f402a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成报告

### 任务 1: westd-41074:cuda:2
- **无需 kill** — cuda:2 上已无进程（重复实验已自行结束），GPU 空闲
- **已部署** `eval_pi05_random_k05_long_seed43_v2`
  - tmux session: `eval_pi05_random_k05_long_seed43_v2`
  - PID: **192839**（正在加载模型，376% CPU，尚未上 GPU，属正常加载阶段）
  - Registry 已更新（server=westd-41074, CUDA_VISIBLE_DEVICES=2）

### 任务 2: westd-38929:cuda:3
- **Killed PID 236139** — scan worker 残留的 `random --keep_ratio 0.5 --seed 43`（06:54 启动，比正确实验早 3 分钟）
- GPU 3 现在只剩 **PID 239588**（`random --keep_ratio 0.3 --seed 43`），10420→9709MiB，运行正常
- GPU 3 已从 20375MiB 降至 9709MiB，释放了 ~10GB

### 任务 3: westd-27271:cuda:0
- **L2norm k=0.3 Long s42**: PID 912230，GPU 0，10190MiB，正常运行中（Task 2 SR=92%，进展到 46%）
- **X-VLA Random k=0.95 Object**: **已消失** — PID 941409 不存在，无 tmux session，无 log 文件（`xvla_random_k095_object` 不在 logs 目录中）。该实验很可能在启动时就崩溃了，没有产生任何输出。
- GPU 0 上只有 L2norm 一个实验在跑
- GPU 1: PID 912303（eval_l2norm_k05_long_s43），正常运行

### nvidia-smi 摘要

| 服务器 | GPU | 进程 | 显存 | 状态 |
|--------|-----|------|------|------|
| westd-41074 | 0 | PID 185720 | 10737MiB | 运行中 |
| westd-41074 | 1 | PID 149709 | 10767MiB | 运行中 |
| westd-41074 | 2 | PID 192839 | 加载中 | **新部署** |
| westd-41074 | 3 | PID 59671 | 27526MiB | 运行中 |
| westd-38929 | 0 | PID 209581 | 10743MiB | 运行中 |
| westd-38929 | 1 | PID 84327 | 10190MiB | 运行中 |
| westd-38929 | 2 | PID 84491 | 10401MiB | 运行中 |
| westd-38929 | 3 | PID 239588 | 9700MiB | 运行中（已清理残留） |
| westd-27271 | 0 | PID 912230 | 10190MiB | 运行中（仅 L2norm） |
| westd-27271 | 1 | PID 912303 | 10343MiB | 运行中 |

**需要你决定**: westd-27271:cuda:0 上 X-VLA Object 实验需要重新部署吗？GPU 0 还有 ~87GB 空余。

---
