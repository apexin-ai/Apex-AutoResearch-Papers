# status check all running

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_check_all_running_20260516T054357_result.json`
- **Structured JSON:** [`0be2e66d77660aa6fae7.json`](../../sessions/0b/0be2e66d77660aa6fae7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

### westd-16980

| exp_id | status | progress | ETA | GPU |
|--------|--------|----------|-----|-----|
| w6_mistral_scierc_constrained | **ALIVE** (14m) | **176/551** (32%) | ~23 min (avg 3.7s/sample) | cuda:0 86%, 14.7/95.8 GiB |
| w5_qwen_docred_lora_constrained_eval | **ALIVE** (3h49m) | **486/998** (49%) | ~2.8h (avg ~20s/sample) | cuda:1 85%, 17.0/95.8 GiB |

### westd-21461

| exp_id | status | progress | ETA | GPU |
|--------|--------|----------|-----|-----|
| w6_mistral_docred_unconstrained | **ALIVE** (14m) | **~84/998** (8%) | ~2.5h (est ~10s/sample) | cuda:0 90%, 14.9/95.8 GiB |
| w6_mistral_docred_constrained | **ALIVE** (8m) | **~47/998** (5%) | ~2.6h (est ~10s/sample) | cuda:1 86%, 14.9/95.8 GiB |

### 注意事项

1. **w5_qwen_docred_lora_constrained_eval**: 最后一个样本 `[486] Bill Warner (writer)` **FAIL** (E=0 R=0, 耗时 76.1s)，疑似超时/解析失败。其余样本正常。

2. **westd-21461 两个实验没有 log 文件** — unconstrained 的 `~/runs/` log 是旧进程的（已被 SIGHUP kill，EXIT_CODE=129），当前进程没有 tee 到 log；constrained 的 log 文件完全不存在。进度只能从 output jsonl 行数推断（84 和 47 行）。

3. 所有 4 个进程都在正常运行，GPU 利用率健康（85-90%）。

---
