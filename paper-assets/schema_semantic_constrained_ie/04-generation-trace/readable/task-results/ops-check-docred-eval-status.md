# ops check docred eval status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_docred_eval_status_20260515T230058_result.json`
- **Structured JSON:** [`b461cf59640d1c62c2a5.json`](../../sessions/b4/b461cf59640d1c62c2a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

save_project_file 不支持写 artifacts。直接输出报告结果：

## DocRED LoRA Unconstrained Eval — 状态报告

**检查时间**: 2026-05-15，两个进程均已运行约 3 小时

### 1. w5_llama_docred_lora_unconstrained_eval — **RUNNING**

| 项目 | 值 |
|------|-----|
| PID | 303525 (存活, 已运行 3h02m54s) |
| GPU | cuda:0, 利用率 89%, 显存 16921/97887 MiB |
| 进度 | **~728/998 (73%)** |
| FAIL | 17 次 (超时, E=0 R=0, 63.1s/次) |
| 输出 | `outputs/w5_llama_docred_lora_unconstrained_eval.jsonl` (728 行) |
| 速度 | ~15s/sample |
| **预计剩余** | **~1h 10m** |
| timeout | 14400s (4h)，充裕 |

### 2. w5_qwen_docred_lora_unconstrained_eval — **RUNNING**

| 项目 | 值 |
|------|-----|
| PID | 304006 (存活, 已运行 2h57m29s) |
| GPU | cuda:1, 利用率 88%, 显存 17343/97887 MiB |
| 进度 | **~514/998 (51%)** |
| FAIL | 37 次 (超时) |
| 输出 | `outputs/w5_qwen_docred_lora_unconstrained_eval.jsonl` (514 行) |
| 速度 | ~21s/sample |
| **预计剩余** | **~2h 50m** |
| timeout | 86400s (24h)，充裕 |

### 汇总

两个实验均正常运行，GPU 利用率高 (88-89%)，无 OOM 或异常退出迹象。Qwen 比 Llama 慢 (~21s vs ~15s/sample)，FAIL 率也更高 (37 vs 17)。

Registry 状态需更新：**Llama 应从 QUEUED → RUNNING**。

---
