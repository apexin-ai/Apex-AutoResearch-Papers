# monitor gpu status eval results

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_gpu_status_eval_results_20260514T135941_result.json`
- **Structured JSON:** [`5014ec7f52e6a90b6cd1.json`](../../sessions/50/5014ec7f52e6a90b6cd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。以下是汇总：

---

## 1. GPU 状态表

| GPU | VRAM | Util | PID | 任务 | 已运行 | 预估剩余 |
|-----|------|------|-----|------|--------|----------|
| **0** | **0/24564 MiB** | **0%** | — | **空闲** | — | — |
| 1 | 5857/24564 MiB | 52% | 365739 | 1.5B_d005_s42_aligned eval | 1h28m | ~0-30min |
| 2 | 3695/24564 MiB | 35% | 381056 | 0.5B_d100_s42_aligned eval | 9min | ~50-80min |
| 3 | 8985/24564 MiB | 69% | 362942 | 3B_d100_s42_aligned eval | 1h54m | ~0-60min |
| 4 | 8985/24564 MiB | 66% | 373931 | 3B_d005_s42_aligned eval | 51min | ~1-1.5h |
| 5 | 3695/24564 MiB | 36% | 374947 | 0.5B_d025_s42_aligned eval | 45min | ~15-45min |

## 2. 已完成 Eval 结果

### Non-aligned format (原始格式)

| Config | MMLU | GSM8K | ARC |
|--------|------|-------|-----|
| 0.5B_d000_s42 | 40.49 | 36.47 | 37.80 |
| 0.5B_d005_s42 | 29.29 | 36.01 | 28.58 |
| 0.5B_d100_s42 | 23.22 | 35.71 | 22.70 |
| 0.5B_d000_s123 | 41.82 | 34.04 | 39.76 |
| 1.5B_d000_s42 | 57.53 | 63.68 | 77.56 |
| 1.5B_d100_s42 | 59.33 | 64.97 | 76.88 |
| 1.5B_d000_s123 | 57.62 | 63.31 | 76.62 |
| 3B_d000_s42 | 63.37 | **11.68*** | 82.17 |
| 3B_d000_s123 | 63.62 | **17.59*** | 82.94 |
| 3B_raw (pretrained) | — | 60.50 | — |

*3B GSM8K 在 non-aligned 格式下结果异常低，疑似评测格式问题

### Aligned format

| Config | MMLU | GSM8K | ARC |
|--------|------|-------|-----|
| 0.5B_d000_s42 | 39.79 | 36.92 | 46.93 |
| 0.5B_d005_s42 | 32.55 | 36.24 | 32.85 |
| 1.5B_d000_s42 | 58.53 | 65.43 | 77.22 |
| 3B_d000_s42 | 63.40 | **11.98*** | 82.76 |

*3B GSM8K aligned 格式依然异常低，需检查评测逻辑

### Para-aligned format (paraphrase 版本)

| Config | MMLU | GSM8K | ARC |
|--------|------|-------|-----|
| 0.5B_d000_s42 | 44.28 | 28.07 | 47.92 |
| 0.5B_d005_s42 | 35.48 | 25.88 | 33.00 |
| 1.5B_d000_s42 | 60.96 | 55.70 | 75.47 |

## 3. 正在运行的 Eval

5 个 aligned eval 正在跑：
- **即将完成**：1.5B_d005 (GPU 1)、3B_d100 (GPU 3)
- **进行中**：0.5B_d025 (GPU 5)
- **刚启动**：0.5B_d100 (GPU 2)
- **中期**：3B_d005 (GPU 4)

## 4. 空闲 GPU

**GPU 0 完全空闲**。GPU 1 和 GPU 3 即将完成，预计 30min 内释放。

## 5. exp-002 进度

0.5B 信号提取 **已完成**（9/9 passed）：
- Qwen2.5-0.5B × {d000, d005, d100} × {mmlu, gsm8k, arc_challenge}
- 输出：`/root/autodl-tmp/exp002/signals/` 下 3 个模型目录，每个含 3 个 `signals_merged_*.json`

---
