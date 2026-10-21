# check p3 8b training progress

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_p3-8b-training-progress_20260514T085133_result.json`
- **Structured JSON:** [`61cc4770796233a87d37.json`](../../sessions/61/61cc4770796233a87d37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd 8B 训练进度汇总

| GPU | 任务 | 当前 step | Loss | 速度 | ETA (剩余) | 已有 ckpt |
|-----|------|-----------|------|------|------------|-----------|
| 0 | CWM seed123 eval | 4384/9784 (45%) | acc=58.1% | ~52s/8samples | ~几小时 | - |
| 1 | CWM v12 eval | 4440/9784 (45%) | acc=57.9% | ~51s/8samples | ~几小时 | - |
| 2 | 8B CWM train | ~530/6633 (8%) | 3.06 (step 500) | ~12s/step | ~20h (明天 ~13:00) | 100,200,300,400 |
| 3 | 8B CLS seed123 | ~926/6633 (14%) | 0.90 (step 850) | ~8.3s/step | ~13h (明天 ~06:00) | 200,400,600,800 |

**CWM 8B loss 趋势**: 23.07→17.57→9.38→4.80→4.27→3.57→3.06，eval_loss: 0.442 (step100) → 0.286 (step500)，稳步下降。

**CLS 8B loss 趋势**: 233→16.5→2.65→2.50→1.28→0.79→1.12→0.90，eval_loss: 0.086 (step200) → 0.093 (step800)，趋于收敛。

训练正常，4 个 GPU 满载运行，无异常。CLS 比 CWM 快约 1.5x（8.3s vs 12s/step），CLS eval_loss 已趋平。

---
