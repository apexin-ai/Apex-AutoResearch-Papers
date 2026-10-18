# code check smoke results

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check-smoke-results_20260518T112500_result.json`
- **Structured JSON:** [`b5b532ed609035ca50e8.json`](../../sessions/b5/b5b532ed609035ca50e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Smoke Test 结果汇总

### 进程状态
- 无 `run_lmeval` 进程运行中

### GPU
- **0% utilization, 0 MiB memory** — GPU 空闲

### Smoke Test: 1.3B baseline on lambada_openai
- **acc = 0.0000** (零准确率)
- **perplexity = 16,274,872.83** (极高，基本是随机)
- 模型: `/root/autodl-tmp/models_1.3b/transformer_1.3B_baseline` (1.21B params, bfloat16)
- 警告: `lm_head.weight` **MISSING** — 模型加载时 lm_head 被随机初始化，这是 acc=0 的直接原因
- 耗时 60s，batch_size=16，5153 samples

### 7B Results (Qwen2.5-7B-Instruct, func_comp)

| Depth | Direct | CoT |
|-------|--------|-----|
| 1 | 89.0% | 96.6% |
| 2 | 19.4% | 89.4% |
| 3 | 14.0% | 71.2% |
| 4 | 11.0% | 53.4% |
| 5 | 14.4% | 38.0% |

### Models 1.3B 磁盘
- `/root/autodl-tmp/models_1.3b/` 总计 19G

### 关键问题
**1.3B baseline 的 `lm_head.weight` 缺失**，导致模型输出完全随机。这个 checkpoint 的 LM head 没有保存或文件名不匹配，需要检查 checkpoint 内容。

---
