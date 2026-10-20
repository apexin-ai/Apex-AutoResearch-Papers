# ops check exp022c exp023 progress

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-exp022c-exp023-progress_20260524T114334_result.json`
- **Structured JSON:** [`323194c4d8ff4acaf38c.json`](../../sessions/32/323194c4d8ff4acaf38c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### exp_022c (GPT-2 Medium, r=0.3, seed 42, GPU 1)

| 项目 | 状态 |
|------|------|
| GPU | GPU 1: 26.4/97.9 GB, 95% 利用率 |
| 进度 | **Generation 2/3 — 数据生成阶段 (9920/35000 samples, ~28%)** |
| Gen 0 | ✅ 完成 (eff_rank=23.09, ppl=15.45) |
| Gen 1 | ✅ 完成 (6200 steps, loss=2.4455, eff_rank=136.08, ppl=12.02) |
| Gen 2 | 🔄 生成合成数据中 |
| Gen 3 | ⏳ 未开始 |
| 日志 | `/root/runs/spectral_collapse_ews/exp_022c.log` (2873行, 持续增长) |
| 已运行 | ~4小时 (15:40 启动) |
| 预计剩余 | ~6-7小时 (Gen 2 数据生成+训练+评估 + 完整 Gen 3 循环) |

### exp_023 (GPT-2 Medium, r=0.25, GPU 0)

| 项目 | 状态 |
|------|------|
| GPU | GPU 0: 19.3/97.9 GB, 96% 利用率 |
| 进度 | **极早期 — 初始化/基线评估阶段** |
| 日志 | `/root/runs/spectral_collapse_ews/exp_023.log` (74KB, 438条 padding 警告) |
| 已运行 | ~33分钟 (19:11 启动) |
| 预计剩余 | ~11-13小时 (需完成 3 个完整训练 generation) |

### 已完成的结果文件

`/root/spectral_collapse_ews/results/phase1_gpt2m_fixed_mix_r03_seed42_results.json` 存在（含 gen 0-2 数据，可能来自先前运行），当前 exp_022c 运行将覆盖该文件。

---
