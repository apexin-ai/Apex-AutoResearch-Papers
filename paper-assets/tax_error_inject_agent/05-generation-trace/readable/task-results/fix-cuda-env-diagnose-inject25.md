# fix cuda env diagnose inject25

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cuda-env-diagnose-inject25_20260514T222902_result.json`
- **Structured JSON:** [`8eaebee5a694a874c9de.json`](../../sessions/8e/8eaebee5a694a874c9de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

### 诊断结果
- **根因**: `submit_training_job` 没有正确传递 `CUDA_VISIBLE_DEVICES`，导致 r2 版本的 inject10 (PID 95247) 和 inject25 (PID 95170) 都跑到 cuda:0，与 seed123 训练冲突 OOM
- PID 94635 (inject10 v1) 之所以正常，是因为它的 `CUDA_VISIBLE_DEVICES=2` 是在 tmux 里手动 export 的

### 当前 GPU 状态（全部正常）
| GPU | 显存占用 | 训练任务 | PID |
|-----|---------|---------|-----|
| cuda:0 | 19539/32607 MiB | taxei-seed123 | 92263 |
| cuda:1 | 19539/32607 MiB | random-seed123 | 93477 |
| cuda:2 | 19129/32607 MiB | inject10 (v1) | 94635 |
| cuda:3 | 18589/32607 MiB | **inject25 (新提交)** | **96835** |

### Registry 更新
- `v4-taxei-fixed-inject10`: PID 修正为 94635，gpu 为 cuda:2
- `v4-taxei-fixed-inject25`: spec 更新为新 PID 96835，gpu 为 cuda:3，含 OOM 诊断 note

---
