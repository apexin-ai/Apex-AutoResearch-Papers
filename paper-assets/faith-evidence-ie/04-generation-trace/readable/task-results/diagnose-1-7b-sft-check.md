# diagnose 1 7b sft check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_1_7b-sft-check_20260522T015908_result.json`
- **Structured JSON:** [`32b6f45f3294ad44ddd6.json`](../../sessions/32/32b6f45f3294ad44ddd6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部仍在运行，进度如下：

```
[RUNNING] test_eval_1_7b_sft_s42      | 469/500 | ~27s/it | ETA ~14 min
[RUNNING] test_eval_1_7b_sft_s42_no_evi | 235/500 | ~23s/it | ETA ~1.7h
[RUNNING] test_eval_14b_sft_s42_no_evi  | 260/500 | ~40s/it | ETA ~2.7h
```

GPU 状态：
| GPU | 占用 | 进程 |
|-----|------|------|
| 0 | 6071/97887 MiB | PID 140534 (1.7B SFT) |
| 1 | 6071/97887 MiB | PID 147596 (1.7B no-evi) |
| 2 | 19599/97887 MiB | PID 152873 (8B no-evi, 额外发现) |
| 3 | 32503/97887 MiB | PID 143166 (14B no-evi) |

1.7B SFT 马上完成（~14分钟），其他两个还需要数小时。

---
