# diagnosis 14b eval progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_14b-eval-progress_20260523T154523_result.json`
- **Structured JSON:** [`adaac45ac7d6b75a0b55.json`](../../sessions/ad/adaac45ac7d6b75a0b55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个进程全部在运行，无已完成的 eval。汇总：

| 任务 | GPU | PID | 运行时长 | 进度 | 速度 | 预估剩余 |
|------|-----|-----|---------|------|------|---------|
| dev with-evi | cuda:0 (32GB/98GB, 79%) | 260780 | 49min | **146/985** (15%) | ~20s/doc | ~4.7h |
| dev no-evi | cuda:2 (32GB/98GB, 82%) | 260930 | 49min | **171/985** (17%) | ~17s/doc | ~3.8h |
| test with-evi | cuda:1 (41GB/98GB, 96%) | 261715 | 44min | **12/32** batch (38%) | ~205s/batch | ~1.1h |
| test no-evi | cuda:3 (41GB/98GB, 97%) | 261858 | 44min | **12/32** batch (38%) | ~205s/batch | ~1.1h |

**预计完成顺序**：test 两个 eval 约 1 小时后完成，dev no-evi 约 4 小时后，dev with-evi 约 5 小时后（dev 集 985 docs 远多于 test 的 32 batch）。

---
