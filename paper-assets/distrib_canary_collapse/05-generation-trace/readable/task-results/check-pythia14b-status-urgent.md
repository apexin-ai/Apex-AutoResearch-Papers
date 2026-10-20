# check pythia14b status urgent

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_pythia14b_status_urgent_20260517T191454_result.json`
- **Structured JSON:** [`b6fd046e65d091344edf.json`](../../sessions/b6/b6fd046e65d091344edf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
Status: DEAD
Current gen: 7/10 (gen_7 training completed, crash on save)
Last activity: 2026-05-18 03:05
GPU utilization: 0% on both GPUs, no processes
EXIT_CODE: 1
Error: "No space left on device (os error 28)"
```

**死因**: gen_7 的 fine-tuning 跑完了（5000/5000 steps, loss=0.019），但在 `model.save_pretrained()` 时磁盘满了。`/dev/md0` 250G 已 100% 占满（剩余 484K）。

**gen_7 状态**: checkpoint 目录存在但不完整（save 失败），synthetic_data 和 trainer 目录已生成。

**需要决策**: 清理磁盘空间后可以从 gen_7 重跑（模型权重没保存成功，需要用 gen_6 的 checkpoint 重新训练 gen_7），还是需要其他处理？

---
