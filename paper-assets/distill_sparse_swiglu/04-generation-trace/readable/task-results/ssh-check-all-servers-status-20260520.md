# ssh check all servers status 20260520

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_all_servers_status_20260520_20260520T190019_result.json`
- **Structured JSON:** [`bd3d68f82d2b2509557c.json`](../../sessions/bd/bd3d68f82d2b2509557c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-34887

**GPU**: cuda:0 占用 48GB/97GB（100% util），cuda:1 空闲

**运行中进程**:
- `mse50_s123` (PID 235955) — `train_perlayer_mse.py`，**仍在训练阶段**，step 280/1000，~0.9s/step
  - 进展：sparsity 已从 0.406 收敛到 0.086（lambda=1000 在压稀疏度），mse 已降到 0.000033
  - 预计还需 ~11 分钟训完，之后进入 7-task eval（30-60 分钟）
  - tmux session `mse50_s123` 存活（C002 合规）

**已完成（PID 已消失）**:
- 133906 (qwen14b_teal30_uniform_gsm8k) — 日志 5/20 10:02 截止
- 115174 (qwen14b_teal275_uniform_eval_v3) — 5/19 22:26 截止
- 114094 (qwen14b_kl30_s42_eval_uniform_v3) — 5/19 23:54 截止

## westd-41718

**GPU**: cuda:0/cuda:1 均空闲（0 MiB）

**运行中进程**: 无（仅基础服务进程）

**已完成**:
- 152255 (qwen14b_teal30_uniform_hspiqa_v2) — 日志 5/19 23:25 截止

## mse50_s123 metrics

**尚未完成** — 当前在训练 step 280/1000，未进入 benchmark_eval 阶段。下次检查建议 ~45 分钟后。

---
