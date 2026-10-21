# check cuda2 cosine status

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cuda2_cosine_status_20260521T154341_result.json`
- **Structured JSON:** [`aa9128bed1d53b865fc1.json`](../../sessions/aa/aa9128bed1d53b865fc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**cuda:2**:
- 当前进程: PID **620568**, 占用 90190 MiB, python — 这是 bs16_uniform_seed42 的实际 python 子进程（父进程 620563 是 bash wrapper，确认在运行）
- 旧 cosine PID **604879** 和 **606291** 均已不存在 ✓

**cuda:3**:
- 无 GPU 进程在运行（nvidia-smi 返回空）
- random_reweight_baseline_seed42 已**训练完成**: 6103/6103 steps, 耗时 3h47m58s, 模型已保存到 `random_reweight_baseline_seed42/final`, EXIT_CODE=0 ✓

---
