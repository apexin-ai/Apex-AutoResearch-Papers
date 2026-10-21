# ssh check mmlu completion

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-mmlu-completion_20260513T231038_result.json`
- **Structured JSON:** [`37bae24c50d67b0f63e1.json`](../../sessions/37/37bae24c50d67b0f63e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. 进程状态
PID 204467 和 204472 均已退出（**正常完成**，非崩溃）。

### 2. GPU 0 状态
**GPU 0 完全空闲** — 0% 利用率，0 MiB 显存占用。

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 0% | 0 / 24564 MiB |
| 1 | 99% | 7330 MiB |
| 2 | 99% | 9492 MiB |
| 3 | 46% | 17327 MiB |
| 4 | 49% | 5829 MiB |
| 5 | 24% | 18665 MiB |

### 3. MMLU paraphrase 生成 — 正常完成
日志最后一行：
```
2026-05-14 06:57:24 [INFO] Saved 14042 paraphrases to mmlu_paraphrases.json (6596/14042 passed QC)
```
vLLM generation 跑满 526/526，之后完成了 similarity scoring（SentenceTransformer QC），进程正常退出。

### 4. 全部 4 个 benchmark paraphrase 文件

| Benchmark | 路径 | 条目数 | 文件大小 |
|-----------|------|--------|----------|
| MMLU | `/root/autodl-tmp/exp001/paraphrases/mmlu_paraphrases.json` | 14042 | 26 MB |
| ARC-Challenge | `/root/autodl-tmp/exp001/paraphrases/arc_challenge_paraphrases.json` | 1172 | 1.7 MB |
| GSM8K | `/root/autodl-tmp/exp001/paraphrases/gsm8k_paraphrases.json` | 1319 | 2.1 MB |
| HumanEval | `/root/autodl-tmp/exp001/paraphrases/humaneval_paraphrases.json` | 164 | 489 KB |

MMLU 的 QC 通过率 47%（6596/14042），3-attempt flow 已全部完成。GPU 0 现在空闲可用。

---
