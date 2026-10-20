# diagnose full server status

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_full-server-status_20260522T214808_result.json`
- **Structured JSON:** [`4183e390630f04ae6ed6.json`](../../sessions/41/4183e390630f04ae6ed6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 当前状态

| GPU | 显存占用 | 总显存 | 利用率 | 当前进程 |
|-----|---------|--------|--------|---------|
| 0 | 9.6 GB | 95.6 GB | 59% | PID 194600 — test_eval_4b_rsft_s42_no_evi (运行 3h32m) |
| 1 | 31.7 GB | 95.6 GB | 92% | PID 194682 — rsft_generate 14b_s43 (运行 3h32m) |
| 2 | 5.9 GB | 95.6 GB | 48% | PID 189485 — test_eval_1_7b_rsft_s42_no_evi (运行 5h35m) |
| 3 | 18.4 GB | 95.6 GB | 72% | PID 196512 — test_eval_llama_rsft_s42_no_evi (运行 3h11m) |

### Registry 标记 RUNNING 的 6 个实验（全部已完成，进程已死）

| exp_id | PID | PID alive? | metrics.json? | ign_f1 | 状态判断 |
|--------|-----|-----------|---------------|--------|---------|
| test_eval_14b_rsft_s42 | 97434 | **DEAD** | 有 test_summary.json | 0.3849 (test) | **→ DONE** |
| eval_llama_rsft_s42_no_evi_2048 | 95606 | **DEAD** | **有** | **0.5559** | **→ DONE** |
| d140_4b_sft_s42_with_evi_2048 | 93402 | **DEAD** | **有** | 0.3946 | **→ DONE** |
| d140_8b_sft_s42_no_evi_2048_fix | 87302 | **DEAD** | **有** | **0.5019** | **→ DONE** |
| d140_1_7b_sft_s42_no_evi_2048_fix | 87382 | **DEAD** | **有** | 0.4233 | **→ DONE** |
| d140_4b_sft_s42_no_evi_2048_fix | 88987 | **DEAD** | **有** | 0.4016 | **→ DONE** |

### ROADMAP 提及的 test_eval / plan017 实验

| exp_id | 状态 | 输出 | 关键指标 |
|--------|------|------|---------|
| test_eval_14b_rsft_s42 | **DONE** | codalab_submission.json + predictions.json | ign_f1=0.3849 (test), 500 docs |
| test_eval_14b_rsft_s42_no_evi | **DONE** | codalab_submission.json + predictions.json | ign_f1=0.3926 (test), 500 docs |
| test_eval_4b_rsft_s42_no_evi | **RUNNING** (PID 194600) | 目录空，尚未产出 | — |
| test_eval_1_7b_rsft_s42_no_evi | **RUNNING** (PID 189485) | 目录空，尚未产出 | — |
| test_eval_llama_rsft_s42_no_evi | **RUNNING** (PID 196512) | 目录空，尚未产出 | — |
| plan017_14b_rsft_no_evidence_eval | **DONE** | metrics.json | **ign_f1=0.5432** (dev) |
| plan017_14b_rsft_s43_generate | **RUNNING** (PID 194682) | 4800 lines (~600/3053 docs, ~20%) | — |

### 可标 DONE 的实验（6 个 registry + 3 个已完成）
1. `test_eval_14b_rsft_s42` — ign_f1=0.3849 (test)
2. `test_eval_14b_rsft_s42_no_evi` — ign_f1=0.3926 (test)
3. `eval_llama_rsft_s42_no_evi_2048` — ign_f1=0.5559 (dev)
4. `d140_4b_sft_s42_with_evi_2048` — ign_f1=0.3946 (dev)
5. `d140_8b_sft_s42_no_evi_2048_fix` — ign_f1=0.5019 (dev)
6. `d140_1_7b_sft_s42_no_evi_2048_fix` — ign_f1=0.4233 (dev)
7. `d140_4b_sft_s42_no_evi_2048_fix` — ign_f1=0.4016 (dev)
8. `plan017_14b_rsft_no_evidence_eval` — ign_f1=0.5432 (dev)

### 仍在运行（4 个进程占满 4 卡）
1. `test_eval_4b_rsft_s42_no_evi` — GPU 0, 已跑 3.5h
2. `test_eval_1_7b_rsft_s42_no_evi` — GPU 2, 已跑 5.5h
3. `test_eval_llama_rsft_s42_no_evi` — GPU 3, 已跑 3h
4. `plan017_14b_rsft_s43_generate` — GPU 1, 已跑 3.5h, ~20% 进度

---
