# diagnose full gpu results collection

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_full-gpu-results-collection_20260522T011228_result.json`
- **Structured JSON:** [`b3f5b6e9d42e4afb7ae1.json`](../../sessions/b3/b3f5b6e9d42e4afb7ae1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 诊断 + 结果收集

### GPU 状态
| GPU | 利用率 | 显存 | 占用进程 |
|-----|--------|------|----------|
| 0 | 51% | 6071/97887 MiB | PID 140534 (test_eval_1_7b_sft_s42) |
| 1 | 52% | 6071/97887 MiB | PID 147596 (test_eval_1_7b_sft_s42_no_evi) |
| 2 | 0% | **空闲** | - |
| 3 | 91% | 32503/97887 MiB | PID 143166 (test_eval_14b_sft_s42_no_evi) |

### 实验结果

| 状态 | exp_id | 指标 / 进度 | ETA |
|------|--------|-------------|-----|
| **[DONE]** | test_eval_4b_rsft_s42_v2 | ign_f1=0.2501, P=0.3403, R=0.1977, evi_f1=0.6237, edcr=0.8288, trunc=214/500, fmt=499/500 | - |
| [RUNNING] | test_eval_1_7b_sft_s42 | **356/500 (71%)**, ~27s/it | ~1h |
| [RUNNING] | test_eval_1_7b_sft_s42_no_evi | **125/500 (25%)**, ~27s/it | ~2h50m |
| [RUNNING] | test_eval_14b_sft_s42_no_evi | **185/500 (37%)**, ~40-55s/it | ~3h30m |

### PID 状态
| PID | 状态 | 运行时间 |
|-----|------|----------|
| 140534 | ALIVE | 2h23m |
| 146485 | **DEAD** (已完成) | - |
| 147596 | ALIVE | 55m |
| 143166 | ALIVE | 1h58m |

### Registry 更新
- [✅] test_eval_4b_rsft_s42_v2: status=DONE, conclusion=success, metrics + paths 已更新
- [⏳] test_eval_1_7b_sft_s42: 仍在运行
- [⏳] test_eval_1_7b_sft_s42_no_evi: 仍在运行
- [⏳] test_eval_14b_sft_s42_no_evi: 仍在运行

**关键观察**: 4B RSFT test ign_f1=0.2501，对比 4B SFT test ign_f1=0.2232，RSFT 提升 +2.69 pp。但 recall 很低 (0.1977)，truncation 严重 (214/500=43%)。

---
