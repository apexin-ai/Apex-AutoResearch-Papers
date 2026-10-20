# ops server health sim check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server_health_sim_check_20260515T024634_result.json`
- **Structured JSON:** [`be3b6067691d6913f990.json`](../../sessions/be/be3b6067691d6913f990.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器健康检查报告 — cqa1-21977

### 1. GPU 利用率

| GPU | 显存占用 | 利用率 | 温度 | 状态 |
|-----|----------|--------|------|------|
| 0 | 8985/24564 MiB (37%) | 71% | 43°C | eval 运行中 |
| 1 | 3695/24564 MiB (15%) | 35% | 36°C | eval 运行中（低利用率） |
| 2 | 5857/24564 MiB (24%) | 51% | 49°C | eval 运行中 |
| 3 | 17651/24564 MiB (72%) | 76% | 57°C | SFT 训练中 |
| 4 | 3727/24564 MiB (15%) | **0%** | 31°C | ⚠️ 未知进程占用 |
| 5 | 17981/24564 MiB (73%) | 25% | 48°C | SFT 训练中（低利用率） |

无 OOM 风险。GPU 5 利用率偏低（25%），可能处于 data loading 阶段。

---

### 2. 进程存活状态

| PID | 实验 | 状态 | 运行时间 |
|-----|------|------|----------|
| 466755 | exp_001_sft_d025_3B_v2 (GPU 3) | ✅ ALIVE | 2h53m |
| 471296 | exp_001_sft_3B_d100_s123 (GPU 5) | ✅ ALIVE | 2h34m |
| 473954 | exp_001_eval_15B_d100_s123_aligned (GPU 2) | ✅ ALIVE | 2h12m |
| 475651 | exp_001_eval_05B_d005_s123_aligned (GPU 1) | ✅ ALIVE | 1h58m |
| 477489 | exp_001_eval_3B_d100_v2_aligned (GPU 0) | ✅ ALIVE | 1h45m |
| 481167 | exp006-oracle-gsm8k-extended (CPU) | ✅ ALIVE | 1h27m |
| 652931 | exp_004_sim_sweep_v4 (CPU) | ❌ **DEAD** | — |

---

### 3. exp_004_sim_sweep_v4

**进程已死亡。** `/root/autodl-tmp/exp004/` 目录不存在，项目目录下也无 sim_sweep_v4 相关文件。需要调查失败原因并决定是否重跑。

---

### 4. exp006-oracle-gsm8k-extended-v2

**v2 已完成** — 日志显示 `Pipeline complete in 759.6s`，结果已保存到 `results_pooled_05B_15B_gsm8k_oracle_extended_v2/`。

PID 481167 是**非 v2 版本**（output-dir 为 `results_pooled_05B_15B_gsm8k_oracle_extended`，无 _v2），输出目录仍为空，MCMC sampling 进行中（4 chains × 6000 iterations, sequential）。运行 1h27m，预计还需 ~30-60min。

---

### 5. SFT 训练进度

| 实验 | 进度 | 当前速度 | 预计剩余时间 | 预计完成 |
|------|------|----------|-------------|----------|
| d025_3B_v2 (PID 466755) | **2457/3384 (72.6%)** | ~4.1s/step | ~63 min | ~10:56 UTC |
| 3B_d100_s123 (PID 471296) | **2191/4159 (52.7%)** | ~4.7s/step | ~154 min (~2.6h) | ~12:30 UTC |

---

### 6. 磁盘空间

| 分区 | 已用/总量 | 使用率 | 状态 |
|------|-----------|--------|------|
| `/` (root) | 26G/30G | **85%** | ⚠️ 接近满 |
| `/root/autodl-tmp/` | 116G/169G | 69% | 正常 |

分项：HF cache 64GB、exp001 6.8GB、exp006 9.4MB

---

### 7. 异常

1. **PID 652931 (sim_sweep_v4) 已死**，无输出目录，需调查
2. **未知进程 PID 488065** 占用 GPU 4 — 是 `eval 0.5B_d005_s123_para_aligned`（带 paraphrase），运行仅 6m25s，不在预期列表中
3. **根分区 85%** — 建议清理，避免训练产出写满磁盘
4. **GPU 5 利用率仅 25%** — d100 训练数据量大，可能处于 tokenization/data loading 间歇

---
