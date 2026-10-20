# ssh check mmlu paraphrase exit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-mmlu-paraphrase-exit_20260513T231124_result.json`
- **Structured JSON:** [`db07932df170f4aa5a3a.json`](../../sessions/db/db07932df170f4aa5a3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 判断：**成功完成**

日志明确显示 `vLLM generation: 100% 526/526` 完成全部 batches，进程正常退出。

### mmlu_paraphrases.json
- **路径**: `/root/autodl-tmp/exp001/paraphrases/mmlu_paraphrases.json`
- **大小**: 27.3 MB (27,276,927 bytes)
- **行数**: 407,015
- **条目数**: 14,042
- **QC pass**: 6,596/14,042 (47.0%)
- **完成时间**: 2026-05-14 06:57:24

### GPU 0
已完全释放：`0 MiB, 0%`

### 3 个 benchmark paraphrase 文件状态

| Benchmark | 文件 | 大小 | 完成时间 |
|-----------|------|------|----------|
| ARC-Challenge | `arc_challenge_paraphrases.json` | 1.7 MB | 05-14 03:52 |
| GSM8K | `gsm8k_paraphrases.json` | 2.1 MB | 05-14 04:11 |
| MMLU | `mmlu_paraphrases.json` | 27.3 MB | 05-14 06:57 |
| HumanEval | `humaneval_paraphrases.json` | 0.5 MB | 05-14 03:10 |

全部 4 个 paraphrase 文件均已生成完毕。

### 备注
- vLLM 初始化失败，回退到 transformers 生成（v1 日志），后续 v3 成功用 vLLM 完成
- MMLU 经过 3 轮生成尝试，最终 QC pass rate 47%——低于 ARC/GSM8K 通常水平，可能需要关注

---
