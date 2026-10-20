# ssh check westd progress all

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-westd-progress-all_20260519T014021_result.json`
- **Structured JSON:** [`2e1a23883196a0bd3c5f.json`](../../sessions/2e/2e1a23883196a0bd3c5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## GPU 占用

| GPU | 显存 | 利用率 | 温度 | 进程 |
|-----|------|--------|------|------|
| 0 | 32.7/97.9 GB | 95% | 75°C | PID 93852 (eval_14b) |
| 1 | 54.4/97.9 GB | 62% | 53°C | PID 86378 (Gemma-2-9B) |
| 2 | 59.7/97.9 GB | 87% | 67°C | PID 93577 (Phi-4 d025) |
| 3 | 57.7/97.9 GB | 94% | 51°C | PID 90913 (Phi-4 d005) |

## 实验进度

| 实验 | GPU | Status | 进度 | 已用时间 | 预计剩余 | 最新 loss / acc |
|------|-----|--------|------|----------|----------|----------------|
| **Gemma-2-9B d025** | cuda:1 | Running | **82% (2775/3384)** | ~2h09m | ~28min | loss=1.159, acc=0.734 |
| **Phi-4 d005** | cuda:3 | Running | **37% (1188/3177)** | ~58min | ~1h37m | loss=1.217, acc=0.730 |
| **Phi-4 d025** | cuda:2 | Running | **3% (92/3384)** | ~3min | ~2h06m | loss=1.392, acc=0.686 |
| **14B eval batch** | cuda:0 | Running | MMLU **36% (5093/14042)** | ~5min | ~9min (当前 benchmark) | — |

**要点**：
- Gemma-2-9B d025 未完成（.done 不存在），但进度 82%，约 **28 分钟后完成**
- Phi-4 d005 进度 37%，约 **1.5 小时后完成**
- Phi-4 d025 刚启动（3%），约 **2 小时后完成**
- 14B eval batch 正在跑 MMLU（d000_s42），目前只有 `Qwen2.5-14B_d000_s42` 目录，尚无 eval_results.json 产出，MMLU 这个 benchmark 还需约 9 分钟

---
