# deploy multiscale eval bjb1 18228

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_multiscale-eval-bjb1-18228_20260517T183745_result.json`
- **Structured JSON:** [`c308e000a55981d3bb26.json`](../../sessions/c3/c308e000a55981d3bb26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成，验证通过。

**状态汇总：**

| 实验 | GPU | 显存占用 | 进程状态 | Registry |
|------|-----|---------|---------|----------|
| `eval-k1-crm-multiscale-object-seed43-r2` | cuda:1 | 5632 MiB | 运行中 (PID 702904) | RUNNING |
| `eval-k1-crm-multiscale-object-seed44-r2` | cuda:3 | 5632 MiB | 运行中 (PID 703107) | RUNNING |

**已完成的操作：**
1. Checkpoint 同步并验证 MD5 一致 (`0ff34166af306f8e12ffc0549ba54ef4`)
2. evaluate.py 和 crm_k1_model.py 从 bjb2-28827 同步到 bjb1-18228（multi-scale 支持确认：6 matches）
3. SmolVLA 模型确认存在
4. 两个 eval 任务在 tmux session `eval-k1-seed43` / `eval-k1-seed44` 中运行
5. Registry 注册完毕，parent 指向 `train-crm-k1-accg-object-seed42-v2`

---
