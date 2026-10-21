# diagnose urgent gpu check all 3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_urgent-gpu-check-all-3_20260522T150711_result.json`
- **Structured JSON:** [`3bf16b837085639e6fe5.json`](../../sessions/3b/3bf16b837085639e6fe5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### GPU 占用总览

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| cuda:0 | 32.5G / 95.6G | 85% |
| cuda:1 | 0 / 95.6G | 0% (空闲) |
| cuda:2 | 0 / 95.6G | 0% (空闲) |
| cuda:3 | 19.6G / 95.6G | 64% |

### 实验状态

| GPU | 实验 | 状态 | ign_f1 | truncated | format_ok | CodaLab |
|-----|------|------|--------|-----------|-----------|---------|
| cuda:0 | test_eval_14b_rsft_s42_no_evi | **RUNNING** 275/500 (55%) | - | - | - | - |
| cuda:2 | test_eval_4b_rsft_s42_v2_reeval | **DONE** ✅ | 0.2501 | 214/500 | 499/500 (99.8%) | ✅ 内置生成 |
| cuda:3 | test_eval_8b_rsft_s42_no_evi | **RUNNING** 337/500 (67%) | - | - | - | - |

### 已完成：4B RSFT v2 reeval
- **ign_f1 = 0.2501**（与原 test_eval_4b_rsft_s42_v2 完全一致，reeval 验证通过）
- evi_f1(TP) = 0.6237, EDCR = 0.8288
- CodaLab 文件已由 eval 脚本内置生成：`/root/autodl-tmp/test_eval_4b_rsft_v2_reeval/codalab_submission.json`（dict 格式，500 docs，keys: r/h/t/evidence）
- Registry 已更新为 DONE/success

### 仍在运行：预计完成时间
- **14B no-evi (cuda:0)**：275/500，均速 ~40s/doc，已跑 ~3h，预计还需 **~2.5h**（约 17:30 UTC）
- **8B no-evi (cuda:3)**：337/500，均速 ~33s/doc，已跑 ~3h，预计还需 **~1.5h**（约 16:30 UTC）

---
