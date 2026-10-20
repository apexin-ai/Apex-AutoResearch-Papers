# ops gpu conflict cleanup

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-conflict-cleanup_20260515T175138_result.json`
- **Structured JSON:** [`18d75b0559a7c8e6e296.json`](../../sessions/18/18d75b0559a7c8e6e296.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**无需清理，当前状态已经是正确的。**

nvidia-smi 只显示 2 个 GPU 进程，每个 GPU 上各一个，且分配符合预期：

| GPU | PID | 实验 | 显存 | GPU利用率 |
|-----|-----|------|------|-----------|
| cuda:0 | 181094 | TaxEI fixed inject10 s123 (`v4_taxei_fixed_inject10_s123`) | 18756MiB | 92% |
| cuda:1 | 181223 | Random fixed inject10 s0 (`v4_random_fixed_inject10_s0`) | 18654MiB | 95% |
| cuda:2 | — | 空闲 | 0MiB | 0% |
| cuda:3 | — | 空闲 | 0MiB | 0% |

**tmux sessions（2个）：**
- `v4-taxei-fixed-inject10-s123` → cuda:0
- `v4-random-fixed-inject10-s0` → cuda:1

用户描述的冲突 PID（181792、181699）在 ps 输出中不存在。其他 swift 子进程（PID 181590、181686）是主训练进程的 data worker，未占用 GPU 显存，属正常现象。

两个实验都在正常训练中，无需任何操作。

---
