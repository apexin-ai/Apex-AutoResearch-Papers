# ops gpu health full diagnosis

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-health-full-diagnosis_20260516T181822_result.json`
- **Structured JSON:** [`6b8e7ed8c480ef5aef11.json`](../../sessions/6b/6b8e7ed8c480ef5aef11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### GPU 状态总览

| GPU | 显存占用 | GPU利用率 | PID | 任务 |
|-----|---------|----------|-----|------|
| 0 | 8081/24564 MiB | 80% | 825638 | eval Llama-3.2-3B d005_s42 (aligned) |
| 1 | 0 MiB | 0% | — | **空闲** |
| 2 | 595/24564 MiB | 0% | 823710 | signals 1.5B-Instruct arc_challenge |
| 3 | 8313/24564 MiB | 82% | 822390 | eval Llama-3.2-3B d025_s42 (aligned) |
| 4 | 0 MiB | 0% | — | **空闲** |
| 5 | 0 MiB | 0% | — | **空闲** |

---

### exp_001_eval_llama32_3B_d000_s42_v3 诊断

**结论：PID 807025 已死，进程无 sentinel 无日志。但该 eval 之前已完成。**

- PID 807025 不存在（ps 返回空）
- `~/runs/` 下无对应 log 文件
- `/tmp/agent-ml-exit/` 无 sentinel
- 但 eval 结果目录已存在：`Qwen2.5-3B_d000_s42_v3_aligned/`（May 15 17:47），数据完整
- **无需重跑**，cron 可标记为 completed

---

### 其他两个实验状态

**exp_001_eval_llama32_3B_d005_s42** — 活跃
- PID 825638，GPU 0，运行 24 分钟
- tmux session: `eval_llama_d005`
- 任务：evaluate.py Llama-3.2-3B d005_s42 (mmlu/gsm8k/arc/humaneval, aligned)

**exp_002_signals_15B_instruct** — 活跃但有问题
- PID 823710，GPU 2，运行 35 分钟，仅 586 MiB（正常偏低）
- 实际跑的是 **arc_challenge**（非 mmlu）
- ⚠️ **发现重复提交**：同一 GPU 2 上有两个 wrapper：
  - PID 823705 (01:44 启动) → PID 823710 (活跃)
  - PID 826497 (01:57 启动，`_v2` session) → 子进程尚未出现在 nvidia-smi
  - 两个都是 `CUDA_VISIBLE_DEVICES=2`，相同命令，相同 output-dir → **C001 违规**

---

### CPU-only 后台进程（无 GPU 占用）

- exp006 IRT fitting（pooled_irt）: PID 740068, 758619, 807098, 807709 — 纯 CPU MCMC 采样，正常运行

---

### 可用 GPU 和建议

| GPU | 状态 | 可复用 |
|-----|------|--------|
| 1 | 完全空闲 | ✅ 立即可用 |
| 4 | 完全空闲 | ✅ 立即可用 |
| 5 | 完全空闲 | ✅ 立即可用 |
| 2 | 低占用但有重复提交 | ⚠️ 需先 kill PID 826497 的 v2 重复进程 |

**需要处理**：
1. GPU 2 的 `exp_002_signals_15B_instruct_arc_v2`（PID 826497）是重复提交，建议 kill 该 tmux session
2. exp_001_eval_llama32_3B_d000_s42_v3 的 cron 监控可以关闭/标完成（结果已在 May 15 生成）

---
