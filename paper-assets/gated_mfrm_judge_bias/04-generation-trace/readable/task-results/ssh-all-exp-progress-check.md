# ssh all exp progress check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_all_exp_progress_check_20260523T071632_result.json`
- **Structured JSON:** [`4d49fff8dec94ea3b4b8.json`](../../sessions/4d/4d49fff8dec94ea3b4b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

### GPU 状态
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 69% | 73543 / 97887 MiB |
| 1 | 64% | 73569 / 97887 MiB |
| 2 | 68% | 667 / 97887 MiB |
| 3 | 0% | 空闲 |

---

### exp-015 — 合成 N=8 校准 (cuda:1, PID 291457)
- **状态: ⚠️ 疑似卡住/僵死**
- 进程存活但 **CPU=0.0%，RSS=3.7MB**，已运行 1h27m
- 进度: **8/20 seeds** (16/40 rows)，最后完成 seed=7
- GPU 1 占用 73GB 显存但进程 RSS 极低，可能是进程已退出但 GPU 内存未释放，或进程卡在 I/O 等待
- **需要人工排查**：建议检查 `cat /proc/291457/status` 看 State 字段，或查看是否有 nohup.out / stderr 日志

---

### exp-016 — Prior sensitivity (cuda:2, PID 316023)
- **状态: ✅ 运行中**
- 运行 17m03s，CPU=101%，RSS=1.7GB
- 进度: **结果目录为空，尚无 CSV 输出**（4 种 prior 全部跑完后一次性写入）
- GPU 2 仅用 667 MiB → 主要是 CPU 密集的 MCMC 采样
- 预估: 每个 prior 的 MCMC (warmup=2000 + samples=4000) 约 10-15 min，总计 ~40-60 min，**预计还需 ~25-45 min**

---

### exp-017 — Murphy-Topel coverage (cuda:0, PID 318082)
- **状态: ✅ 运行中**
- 运行 12m50s，CPU=105%，RSS=4.7GB
- 进度: **9/800 rows** (n_models={8,20,50,100} × 200 seeds)，当前在 n_models=8, seed=8
- 平均 ~1.4 min/row
- **预估剩余: ~18-19 小时**

---

**关键关注点**: exp-015 大概率已卡住（CPU 0% + RSS 3.7MB），建议优先排查。exp-017 总任务量很大（800 次模拟），预计明天上午才能完成。

---
