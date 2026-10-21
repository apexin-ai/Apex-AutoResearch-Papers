# ssh gpu status check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu-status-check_20260514T170910_result.json`
- **Structured JSON:** [`7cbec9c753c7d264f281.json`](../../sessions/7c/7cbec9c753c7d264f281.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### GPU 状态
| GPU | 型号 | 显存占用 | 利用率 | 温度 |
|-----|------|---------|--------|------|
| 0 | RTX 5090 | 2MiB / 32607MiB | 0% | 29°C |
| 1 | RTX 5090 | 2MiB / 32607MiB | 0% | 29°C |
| 2 | RTX 5090 | 2MiB / 32607MiB | 0% | 28°C |
| 3 | RTX 5090 | 2MiB / 32607MiB | 0% | 27°C |

**无任何 GPU 进程运行。4 张卡全部空闲。**

---

### 实验状态

#### EXP_003 WNUT17 (PID 92215) — 已完成
- 进程：**已退出**
- 训练耗时：16分22秒，5 epochs
- **最终 metrics：**
  - train_loss = **0.105**
  - eval_loss = **0.0836**
  - train_samples/s = 8.33

#### EXP_001_SEED456 — 已完成
- 进程：**已退出**
- 产出文件：`report.json` (3.3KB), `run.log` (105KB), `samples.jsonl` (6.5MB)
- **最终 metrics：**
  - Full ρ(κ,F1) = +0.3383, p=4.35e-12
  - Full ρ(SJ,F1) = +0.2988, p=1.24e-09
  - Cond ρ(κ,F1) = +0.2330, Cond ρ(SJ,F1) = +0.3245
  - Structural > Surface: **NO** (delta=-0.0395)
  - Logprob (full): ρ=+0.3405, AUROC=0.6694
  - Logprob (cond): ρ=+0.0501, AUROC=0.5713
  - **Verdict: FAIL** — >30% samples F1=0，建议 T=0.7 重跑；Joint mode 要求 RE ρ_sj ≥ 0.40 未达标

#### EXP_017 LLAMA CONLL — 未找到
- 进程：**未运行**
- 日志：`logs/` 下未找到匹配 `*llama*conll*` 或 `*017*` 的文件
- `output/exp_017*/` 目录不存在

---

### 其他
- **Tmux：** 无活跃 session
- **GPU 进程：** 无

**结论：3 个实验均无存活进程，服务器完全空闲。EXP_003 和 EXP_001_SEED456 已跑完有结果，EXP_017 无任何痕迹（可能从未启动或路径/命名不同）。**

---
