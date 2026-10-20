# ssh fix collect concurrency

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_collect_concurrency_20260523T194030_result.json`
- **Structured JSON:** [`c23c07f3df9f638c783c.json`](../../sessions/c2/c23c07f3df9f638c783c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 报告

### 瓶颈原因
collect.py 已有 `ThreadPoolExecutor` 支持（`--workers` 参数），但所有本地 judge 进程启动时均未指定 `--workers`，默认为 1（完全串行请求）。vLLM continuous batching 无法发挥作用，KV cache 利用率极低。

### 修复方案
**方案 A：启动额外并行进程（零代码修改）**

为每个本地 judge 启动了新的 `collect.py --workers 32` 进程：
- `judge_llama_parallel` — `--config config_llama_arena_n17.yaml --workers 32`
- `judge_qwen_parallel` — `--config config_qwen_arena_n17.yaml --workers 32`
- `judge_mistral_parallel` — `--config config_mistral_arena_n17.yaml --workers 32`

原有串行进程未停止。新进程通过 `load_completed()` 跳过已完成项，JSONL 追加写入在 Linux 上是原子安全的。

### 吞吐量对比

| Judge | 串行速度 | 并行速度 (32 workers) | 加速倍数 |
|-------|---------|---------------------|---------|
| llama-3.3-70b | ~30/hr | ~450+/hr | **~15x** |
| qwen2.5-72b | ~30/hr | ~540+/hr | **~18x** |
| mistral-large-2 | ~30/hr | ~540+/hr | **~18x** |

### 预估完成时间

| Judge | 进度 | 剩余 | 预估完成 |
|-------|------|------|---------|
| llama-3.3-70b | 6497/18000 (36%) | 11503 | ~25h → **May 25 凌晨** |
| qwen2.5-72b | 9474/18000 (53%) | 8526 | ~16h → **May 24 晚** |
| mistral-large-2 | 9138/18000 (51%) | 8862 | ~16h → **May 24 晚** |

**全部在 May 26 DDL 前完成。** 速率仍在爬升中，实际完成可能更早。

### vLLM 状态

| 实例 | 并发请求 | 生成吞吐 | KV Cache | 状态 |
|------|---------|---------|----------|------|
| llama (8001) | 32 | 78.6 tok/s | 12.7% | 健康 |
| qwen (8002) | 33 | 75.7 tok/s | 29.2% | 健康 |
| mistral (8003) | 31 | 39.4 tok/s | 80.0% | 可控（曾达92%，已回落） |

### 注意事项
- 串行+并行进程可能产生少量重复行（串行进程每小时仅贡献几条），分析时 deduplicate 即可
- mistral 的 KV cache 偏高，如果后续出现 preemption/OOM，可考虑杀掉其串行进程或降低 workers 数
- 回滚方法：直接 kill 三个 `_parallel` tmux session，不影响原有进程和已有数据

---
