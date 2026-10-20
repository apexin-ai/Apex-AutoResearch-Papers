# ops gpu audit and accelerate reeval

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-audit-and-accelerate-reeval_20260523T132358_result.json`
- **Structured JSON:** [`831974e049835c55419c.json`](../../sessions/83/831974e049835c55419c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 审计和加速完成。

---

## GPU 审计报告

### GPU 0 — 41.8 / 97.9 GB, 96%（5 个进程）
| PID | 命令 | 运行时间 | 类型 |
|-----|------|---------|------|
| 118587 | `train.py contam_25 mistral` | 1h25m | **Batch 4 训练** — checkpoint 1064/1596 (67%), ETA ~40min |
| 123059 | `eval_lz.py contam_25 llama` | 56m | Mass eval chain (2/3) — 7500/14042 (53%) |
| 124248 | `eval_lz.py contam_5 mistral` | 50m | Mass eval |
| 128364 | `eval_lz.py contam_15_s3 llama` | 41m | Mass eval chain (1/4) |
| 128943 | `eval_lz.py contam_50_s3 llama` | 40m | Mass eval chain (1/3) |

### GPU 1 — 0 / 97.9 GB, 0% — 完全空闲

### GPU 2 — 8.8 / 97.9 GB, 94%（1 个进程）
| PID | 命令 | 运行时间 | 类型 |
|-----|------|---------|------|
| 137799 | `eval_lz.py clean` | 9m | **Clean seed re-eval** — 第 1/10 个 condition，刚开始 |

### GPU 3 — 17.4 / 97.9 GB, 97%（2 个进程）
| PID | 命令 | 运行时间 | 类型 |
|-----|------|---------|------|
| 126634 | `train.py contam_25_s2 mistral` | 46m | **Batch 5 训练** — checkpoint 532/1596 (33%), ETA ~86min |
| 131201 | `eval_lz.py contam_15_s1 llama` | 37m | **CRITICAL re-eval** — 7000/14042 (50%), ETA ~35min |

---

## 已执行的加速措施

Kill 了 6 个冗余/重复进程：
1. **PID 136064** — GPU 3 上 contam_15_s1 重复进程
2. **PID 135039** — GPU 3 上 contam_25 eval（GPU 0 已有相同 eval）
3. **PID 134427** — GPU 1 上 contam_50_s1 重复进程
4. **PID 138426** — GPU 2 上 clean eval 重复进程
5. **PID 139380** — chain 脚本在 kill #1 后自动启动的冗余 contam_50_s1
6. **PID 136059** — 产生 #5 的 chain 脚本 (`/tmp/run_eval_s1.sh`)

GPU 3 从 **4 进程 / 35 GB** 降至 **2 进程 / 17 GB**，contam_15_s1 速度应提升约 1 倍。

---

## 关键状态

- **contam_50_s1 re-eval: 已完成** — 结果保存于 `results/llama/contam_50_s1_results.json` (21:28)
- **contam_15_s1 re-eval: 进行中** — 50%, 预计 ~35 分钟后完成（~22:05）
- **Batch 5 GPU 1/2 训练: 已完成** — Llama 5% s3 / 25% s3 训练已结束
- **Batch 4 GPU 0 训练**: Mistral 25% s1, ETA ~40min
- **Batch 5 GPU 3 训练**: Mistral 25% s2, ETA ~86min
- **Clean seed re-eval**: GPU 2 上刚启动，10 个 condition 串行执行，预计 5-6 小时

**GPU 1 完全空闲**，可按需分配新任务。

---
