# eval w5 qwen docred lora metrics and constrained

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_w5_qwen_docred_lora_metrics_and_constrained_20260516T015205_result.json`
- **Structured JSON:** [`cc74f76a060edd4c5a2e.json`](../../sessions/cc/cc74f76a060edd4c5a2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务完成。

---

**任务 1：w5_qwen_docred_lora_unconstrained_eval metrics**

| 指标 | 全量 (998) | 排除 FAIL (927) |
|------|-----------|----------------|
| ET_pct | 0% | 0% |
| RV_pct | 0.27% | 0.27% |
| DR_pct | 0.76% | 0.76% |
| CF_pct | 0.12% | 0.12% |
| E_F1 | 82.15 | 85.72 |
| E_P / E_R | 85.44 / 79.11 | 85.44 / 86.00 |
| R_F1 | 40.86 | 42.20 |
| R_P / R_R | 36.41 / 46.56 | 36.41 / 50.17 |
| parse_fail_rate | 7.11% | — |

vs Llama unconstrained: E_F1 82.15 vs 83.93, R_F1 40.86 vs 43.72, DR_pct 0.76% vs 0.49%. Qwen 略低且 fail 率更高 (7.11% vs 2.3%)。

Registry 已更新（metrics + conclusion=success + notes）。

---

**任务 2：w5_qwen_docred_lora_constrained_eval**

另一个 worker 已提交该任务。已确认：
- PID **321568**，cuda:1，CUDA_VISIBLE_DEVICES=1（wrapper 控制）
- 无重复进程，模型已加载，2/998 开始推理
- Registry 已创建：status=RUNNING，spec 完整填写

---
