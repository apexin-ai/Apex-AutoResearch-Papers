# monitor gpu progress

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_gpu_progress_20260513T235422_result.json`
- **Structured JSON:** [`e0222b6f7d22cc3de033.json`](../../sessions/e0/e0222b6f7d22cc3de033.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### GPU 利用率快照

| GPU | 显存占用 | GPU-Util | 实验 | PID |
|-----|---------|----------|------|-----|
| 0 | 23622/24564 MiB | 53% | sft_d100_05B | 235248 + **238461 (额外进程, 1622MiB)** |
| 1 | 3667/24564 MiB | 35% | eval_05B_d000_s42 | 229375 |
| 2 | 3667/24564 MiB | 34% | eval_05B_d000_s123 | 229521 |
| 3 | 17327/24564 MiB | 26% | sft_0pct_3B_s123 | 216254 |
| 4 | 5829/24564 MiB | 45% | eval_3B_d000_s42_v2 (非15B) | 221376 |
| **5** | **0/24564 MiB** | **0%** | **无进程 ✓** | — |

### 各实验进度

| 实验 | GPU | 进度 | 速度 | ETA |
|------|-----|------|------|-----|
| **sft_0pct_3B_s123** | 3 | 2860/3125 (91.5%) | ~4.4s/step | **~19 min** |
| **sft_d100_05B** | 0 | 831/4159 (20.0%) | ~1.05s/step | **~58 min** |
| **eval_05B_d000_s42** | 1 | GSM8K 598/1319 (45%) | ~5.3s/it | GSM8K剩 ~64 min，后续还有 arc_challenge + humaneval |
| **eval_05B_d000_s123** | 2 | GSM8K 571/1319 (43%) | ~5.5s/it | GSM8K剩 ~68 min，后续还有 arc_challenge + humaneval |
| **eval_3B_d000_s42_v2** | 4 | MMLU 阶段，刚启动 | ~36 it/s | MMLU 14042 items，预计 ~6.5 min for MMLU |

### 异常发现

1. **exp_001_eval_15B_d000_s123 已失败** — 参数错误 `unrecognized arguments: --gpu 0`，EXIT_CODE=2
2. **exp_001_eval_3B_d000_s42_v2 前次被 kill** — 之前在 MMLU 34% 时被杀（EXIT_CODE=137），但当前 GPU 4 上 PID 221376 仍在运行（可能是重启后的新实例）
3. **GPU 0 有额外进程** PID 238461 占用 1622MiB，不属于 sft_d100_05B（主进程 PID 235248）
4. **两个 eval_05B 实验** 在下载 GSM8K 数据时都遇到 HuggingFace 连接超时（重试后恢复）

### sft_dosage_100.jsonl 数据完整性

- 总行数：**66,533**
- 包含 MMLU 内容：**0 行**（不含 MMLU 数据）
- 格式：chat messages 格式，keys = `['messages']`

---
