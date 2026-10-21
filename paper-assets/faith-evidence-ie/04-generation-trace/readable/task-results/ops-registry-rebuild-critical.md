# ops registry rebuild critical

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry-rebuild-critical_20260522T221047_result.json`
- **Structured JSON:** [`008d2a3bd3877a07ac56.json`](../../sessions/00/008d2a3bd3877a07ac56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已完整恢复，无需额外操作。

## 汇报

**Registry 现状：336 条记录（远超预期的 229 条）。所有任务列出的关键实验均已存在且 metrics 正确。**

### P0: test_eval_* 系列 — 全部 ✓

| exp_id | registry ign_f1 | 已知值 | 状态 |
|---|---|---|---|
| test_eval_8b_rsft_s42 | 0.3353 | 0.3353 | ✓ |
| test_eval_8b_rsft_s42_no_evi | 0.3319 | 0.3319 | ✓ |
| test_eval_14b_rsft_s42_no_evi | 0.3926 | 0.3926 | ✓ |
| test_eval_8b_sft_s42 | 0.3106 | 0.3106 | ✓ |
| test_eval_8b_sft_s42_no_evi | 0.2935 | 0.2935 | ✓ |
| test_eval_4b_sft_s42 | 0.2232 | 0.2232 | ✓ |
| test_eval_4b_rsft_s42_v2 | 0.2501 | 0.2501 | ✓ |
| test_eval_4b_rsft_s42_v2_reeval | 0.2501 | 0.2501 | ✓ |
| test_eval_1_7b_rsft_s42 | 0.2933 | 0.2933 | ✓ |
| test_eval_14b_sft_s42 | 0.3886 | 0.3886 | ✓ |
| test_eval_llama_sft_s42 | 0.3420 | 0.3420 | ✓ |
| test_eval_llama_rsft_s42 | 0.3599 | 0.3599 | ✓ |
| test_eval_14b_rsft_s42 | 0.3849 | — | ✓ |

### P1: plan017_* 系列 — 全部 ✓

| exp_id | ign_f1 | 状态 |
|---|---|---|
| plan017_14b_sft | N/A (training) | success ✓ |
| plan017_14b_sft_s43 | N/A (training) | success ✓ |
| plan017_14b_ced_scoring | N/A (scoring) | success ✓ |
| plan017_14b_rsft_train | N/A (training) | success ✓ |
| plan017_14b_rsft_eval | 0.5886 | success ✓ |
| plan017_14b_rsft_no_evidence_eval | 0.5432 | success ✓ |

### P2: d102_* 系列

已有：d102_8b_rsft_k1_s42, d102_8b_rsft_k1_s43 (ign_f1=0.5471), d102_1_7b_rsft_k1_s42, d102_llama_rsft_k1_s42 — 全部 success ✓

**缺失但服务器上无数据：** d102_8b_rsft_k1_s44, d102_1_7b_rsft_k1_s43, d102_1_7b_rsft_k1_s44 → 服务器 `/root/autodl-tmp/eval_results/` 下无对应目录，无法恢复。

### P3: plan_006 — ✓

plan_006_qwen3_8b_rsft_eval: ign_f1=0.5433, success ✓

### 4 个 RUNNING 条目

均为今天提交的活跃任务，进程在运行中：
- `test_eval_1_7b_rsft_s42_no_evi` — PID 189480, 运行 6h
- `test_eval_4b_rsft_s42_no_evi` — PID 194600, 运行 4h
- `test_eval_llama_rsft_s42_no_evi` — PID 196512, 运行 3.5h
- `plan017_14b_rsft_s43_generate` — PID 194682, 运行 4h

**结论：恢复 0 条新条目。Registry 已完整，所有论文关键实验的 metrics 与已知值完全匹配。缺失的 3 个 d102 multi-seed 条目（s44/s43）在服务器上没有结果文件。**

---
