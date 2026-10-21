# infra olmo data recovery verify

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_olmo_data_recovery_verify_20260521T193747_result.json`
- **Structured JSON:** [`bd14ed096d5eb5673d16.json`](../../sessions/bd/bd14ed096d5eb5673d16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### OLMo-2-7B 数据状态

| Benchmark | 行数 | Conditions | 状态 |
|-----------|------|-----------|------|
| **MMLU** | 57,600 | 288/288 | **OK** — 已从 288K 过滤恢复，原始备份在 `.bak_unfiltered` |
| **ARC** | 57,600 | 288/288 | **OK** — 同上 |
| **HellaSwag** | 57,600 | 288/288 | **OK** — 同上 |
| **GSM8K** | 57,600 | 288/288 | **OK** — 完整 |
| **MATH** | ~42,000 | 210/288 | **运行中** (PID 64774) — 还差 78 conditions，全在 temp=0.7 的 prompt 3-6 |

设计矩阵：2 temps × 6 prompts × 6 seeds × 4 orderings = 288 conditions × 200 items = 57,600/benchmark。MMLU/ARC/HellaSwag/GSM8K 全部匹配，无需额外操作。

### Accuracy 合理性

| Benchmark | Accuracy |
|-----------|----------|
| MMLU | 61.56% |
| ARC | 76.11% |
| HellaSwag | 63.37% |
| GSM8K | 70.10% |
| MATH | 29.38% (不完整数据) |

均在 OLMo-2-7B-Instruct 的合理范围内。

### MATH 缺失分析
- 80 个缺失 condition 全在 **temp=0.7**
- 按 prompt 分布：prompt 3 缺 8，prompt 4/5/6 各缺 24
- 当前 PID 64774 正在补跑，预计还需处理 78 conditions × 200 items = 15,600 条

### Yi 状态（附带）
Yi 的 ARC/GSM8K/HellaSwag/MMLU 均 57,600 完整，MATH 56,600（也在跑，PID 68476）。

### 结论
- MMLU/ARC/HellaSwag/GSM8K 已恢复完成，**无需任何操作**
- OLMo MATH 和 Yi MATH 正在 GPU 上补跑，等进程结束即可
- 不存在需要手动过滤或恢复的数据

---
