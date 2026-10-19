# ops gpu server audit loop4

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_server_audit_loop4_20260516T003330_result.json`
- **Structured JSON:** [`5d0ed773b14bb05ade15.json`](../../sessions/5d/5d0ed773b14bb05ade15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计报告：westd-34887 (2026-05-16 08:33 UTC)

### GPU 状态

| GPU | 显存占用 | GPU-Util | 进程 |
|-----|---------|----------|------|
| cuda:0 | 39,594 / 97,887 MiB (40%) | 90% | 2 个进程 |
| cuda:1 | 37,660 / 97,887 MiB (38%) | 94% | 2 个进程 |

### 活跃进程详情

| PID | GPU | 命令 | 显存 | 运行时间 | 状态 |
|-----|-----|------|------|---------|------|
| 181121 | cuda:0 | `eval_benchmark.py --condition mistral_dense --tasks lm_eval` | 21,246 MiB | 28 min | **活着** (Rl) |
| 184120 | cuda:0 | `debug_mask_verify.py` | 18,334 MiB | 6 min | **活着** (Sl), 正在加载 MMLU 数据集 |
| 174850 | cuda:1 | `eval_benchmark.py --condition mistral_kl_s42 --tasks lm_eval` | 21,280 MiB | 59 min | **活着** (Rl) |
| 179918 | cuda:1 | `lm_eval_sparse.py --predictor_path predictor_kl_normalized.pt --tasks arc/wino/mmlu/gsm8k` | 16,364 MiB | 41 min | **活着** (Rl) |

### 指定进程状态

- **PID 179913** (lm_eval_kl_s42 wrapper): shell wrapper 仍活着 (Ss+)。之前的 EXIT_CODE=129 (SIGHUP) 记录于 **2026-05-15T23:53:53Z**，是上一次运行的退出码。当前是重新启动的运行，子进程 PID 179918 正在正常执行。
- **PID 179918** (lm_eval_sparse.py): **活着**，cuda:1 上跑了 41 分钟，95% CPU。
- **PID 184120** (debug_mask_verify.py): **活着**，cuda:0 上跑了 6 分钟。日志显示正在加载模型权重 + MMLU 数据集（网络不可达，回退到本地缓存）。

### Mistral Eval 状态

两个 Mistral downstream eval 同时在跑：
1. **mistral_kl_s42** (PID 174850, cuda:1) — 59 min，输出到 `results/plan_009_mistral`
2. **mistral_dense** (PID 181121, cuda:0) — 28 min，输出到 `results/plan_009_mistral`

注意：PID 174845 的原始命令链是 `mistral_kl_s42 → mistral_dense` 串行执行，当前还在跑第一个 (kl_s42)。PID 181121 是独立启动的 mistral_dense。当 174850 完成 kl_s42 后，174845 会再启动一个 mistral_dense——可能会冲突。

### lm-eval 结果文件

| 路径 | 内容 |
|------|------|
| `results/lm_eval/` | results.json, results_full.json, results_table.md (**dense eval 已完成**) |
| `results/plan_007/` | results.json, results_full.json, results_table.md + 子目录 (consolidated, debug_*, remaining_conditions 等) |
| `results/plan_009_mistral/` | **空目录** (Mistral eval 仍在进行) |
| `results/lm_eval_kl_s42/` | **不存在** (sparse eval PID 179918 尚未产出结果) |

### tmux sessions

`tmux ls` 被 read-only 模式阻止，但从 ps 输出可见至少一个 session：
- **lm_dense** — 启动 dense eval 的 session，运行 19h44m

---
