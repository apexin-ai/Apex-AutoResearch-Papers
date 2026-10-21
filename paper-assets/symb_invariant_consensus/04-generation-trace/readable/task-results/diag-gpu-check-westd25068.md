# diag gpu check westd25068

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu-check-westd25068_20260519T043248_result.json`
- **Structured JSON:** [`c4cfa465b4a17d36a607.json`](../../sessions/c4/c4cfa465b4a17d36a607.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-25068 GPU 状态

| GPU | 预期实验 | 实际状态 | PID | 进度 | 备注 |
|-----|---------|---------|-----|------|------|
| cuda:0 | exp-051 K=20 | **空闲 (已完成)** | — | 204/204 (全部K值完成) | k4/k8/k16/k20 均 204/204，k20 耗时 124.3min，日志显示 FULL_MVP_DONE |
| cuda:1 | exp-034 Qwen-14B PW-600 | **运行中** 97% | 69808 (runner) / 68555 (vLLM:8001) | ~565/600 | Qwen2.5-14B-Instruct, 01:44 启动，估计很快完成 |
| cuda:2 | 空闲 | **空闲** | — | — | 确认空闲 |
| cuda:3 | exp-058 T=0.5 | **运行中** 97% | 150540 (runner) / 149633 (vLLM:8003) | ~203/204 | Mistral-7B FOLIO-204 T=0.5, 11:13 启动，即将完成 |

**磁盘**: 12G/30G (39%)
**vLLM 进程**: 2 个 (port 8001 = Qwen2.5-14B for exp034, port 8003 = Mistral-7B for exp058)
**tmux sessions**: exp033_run, exp034_run, exp035_run, exp058_run, exp058_vllm, model_dl_25068

**关键发现: cuda:0 和 cuda:2 均空闲，可立即部署新实验。** exp-051 已全部完成（4 个 K 值各 204 题），exp-034 和 exp-058 均接近尾声。

---
