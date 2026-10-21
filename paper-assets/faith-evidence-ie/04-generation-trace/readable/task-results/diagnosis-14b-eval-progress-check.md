# diagnosis 14b eval progress check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_14b-eval-progress-check_20260523T153642_result.json`
- **Structured JSON:** [`ad39ffcd6d7445ac6228.json`](../../sessions/ad/ad39ffcd6d7445ac6228.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 14B RSFT s43 Eval 状态汇总

### GPU 状态
| GPU | 显存占用 | 总显存 | 利用率 |
|-----|---------|--------|--------|
| 0 | 32,479 MiB | 97,887 MiB (33%) | 84% |
| 1 | 40,521 MiB | 97,887 MiB (41%) | 96% |
| 2 | 32,479 MiB | 97,887 MiB (33%) | 87% |
| 3 | 40,379 MiB | 97,887 MiB (41%) | 96% |

**4 卡全部占用，无空闲 GPU。**

### 4 个 Eval 进度

| Eval | GPU | 进度 | 速度 | 预计剩余 |
|------|-----|------|------|---------|
| plan017_14b_rsft_s43_eval (dev with-evi) | cuda:0 | **126/985** (12.8%) | ~20s/doc | ~4.5h |
| plan017_14b_rsft_s43_no_evi_eval (dev no-evi) | cuda:2 | **144/985** (14.6%) | ~15s/doc | ~3.5h |
| test_eval_14b_rsft_s43_with_evi (test with-evi) | cuda:1 | **10/32** batch (31.3%) | ~206s/batch | ~75min |
| test_eval_14b_rsft_s43_no_evi (test no-evi) | cuda:3 | **10/32** batch (31.3%) | ~205s/batch | ~75min |

所有 4 个进程状态正常（S, running ~40min）。test eval 预计约 75 分钟后完成，dev eval 预计 3.5-4.5 小时后完成。

---
