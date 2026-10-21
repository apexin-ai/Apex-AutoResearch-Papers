# eval gemma2 arc s42 westd

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_gemma2-arc-s42-westd_20260521T062806_result.json`
- **Structured JSON:** [`89169eab5a4ea1a3c661.json`](../../sessions/89/89169eab5a4ea1a3c661.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 GPU 全部在跑 GSM8K s0 eval：

| GPU | PID | 进程 | 已运行 |
|-----|-----|------|--------|
| cuda:0 | 482994 | gemma-2-9b d000_s0 GSM8K | 12 min |
| cuda:1 | 481803 | Qwen2.5-14B d100_s0 GSM8K | 25 min |
| cuda:2 | 482914 | Qwen2.5-14B d050_s0 GSM8K | 12 min |
| cuda:3 | 483072 | phi-4 d000_s0 GSM8K | 12 min |

你说的 "fill Worker 启动的 GSM8K eval" 就是这些。kill cuda:0/2/3 上的三个进程（PID 482994, 482914, 483072）会丢失它们各自 ~12 分钟的进度。cuda:1 的 Qwen14B d100_s0 不动。

确认 kill 这 3 个进程？还是等它们跑完再启动 ARC eval？GSM8K eval 通常还需要多久可以先查一下。

---
