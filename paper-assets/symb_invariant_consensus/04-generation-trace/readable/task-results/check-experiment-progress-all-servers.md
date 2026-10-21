# check experiment progress all servers

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_experiment-progress-all-servers_20260523T141505_result.json`
- **Structured JSON:** [`418d5ed4d2aad99f9b93.json`](../../sessions/41/418d5ed4d2aad99f9b93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

| 服务器 | GPU | 实验 | 进度 | 预计剩余 | 状态 |
|--------|-----|------|------|---------|------|
| westd-30973 | cuda:0 | — | — | — | 空闲 |
| westd-30973 | cuda:1 | — | — | — | 空闲 |
| westd-30973 | cuda:2 | LLaMA seed456-v2 | 415/600 (69%) | ~3.5h | 运行中 |
| westd-30973 | ~~cuda:1~~ | LLaMA seed789-v2 | 325/600 (54%) | — | **已终止** (EXIT_CODE=143) |
| westd-16639 | cuda:0 | LLaMA seed789 | 470/600 (78%) | ~2.5h | 运行中 |
| westd-16639 | cuda:1 | — | — | — | 空闲 |
| westd-16639 | cuda:2 | Qwen seed789 | 534/600 (89%) | ~1.2h | 运行中 |
| westd-16639 | cuda:3 | Qwen seed456 resume | 559/600 (93%) | ~0.8h | 运行中 |

### 关键发现

**FOLIO NLI combo: 未启动。** westd-30973 上没有 `nli_folio_deberta/bart/roberta` 相关 tmux session 或日志文件。

**接近完成 (>90%):**
- Qwen seed456 resume — 559/600 (93%)，预计 ~45 分钟完成

**接近完成 (>85%):**
- Qwen seed789 — 534/600 (89%)，预计 ~1.2 小时完成

**异常:**
- **westd-30973 LLaMA seed789-v2 被 SIGTERM 终止**（EXIT_CODE=143），停在 325/600。vLLM（port 8001）已关闭，GPU 1 空闲。日志最后时间戳 20:40，之后被 kill。
- **westd-30973 有 2 个 GPU 完全空闲**（cuda:0, cuda:1），可用于部署 FOLIO NLI 实验或重启 seed789-v2。
- westd-16639 cuda:1 空闲。

---
