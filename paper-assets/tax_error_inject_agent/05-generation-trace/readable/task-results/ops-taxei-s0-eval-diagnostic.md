# ops taxei s0 eval diagnostic

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_taxei-s0-eval-diagnostic_20260516T132457_result.json`
- **Structured JSON:** [`a12e5e2a2a824ab4087b.json`](../../sessions/a1/a12e5e2a2a824ab4087b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

关键发现：

1. **GPU 0 正在运行 s0 clean eval**（PID 280386, 已运行 46秒）— 这正是 Step 3 要做的事。
2. **`llama31_taxei_s0_eval.json` 已经有 injected eval 结果**（文件名不同于预期的 `_injected.json`，而是 `_eval.json`）。
3. **之前的 eval 并没有失败**——`llama31_taxei_s0_eval.json` 包含完整结果。

## 产出汇总

### GPU 状态
| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| 0 | 16.8 GB | 89% | s0 clean eval (recovery.py), 刚启动 |
| 1 | 30.3 GB | 99% | 训练任务 |
| 2 | 24.7 GB | 99% | 训练任务 |
| 3 | 24.7 GB | 99% | 训练任务 |

### TaxEI s42 clean
- **success_rate = 0.766**, total = 47

### TaxEI s0 injected eval（`llama31_taxei_s0_eval.json`）
- **recovery_rate = 0.745**
- **detection_rate = 0.277**
- success_rate = 0.745
- total_episodes = 47

### 诊断：之前 eval 为什么报 "done" 但无输出
**eval 并没有失败**。injected eval 的输出文件是 `llama31_taxei_s0_eval.json`（不是 `_injected.json`），之前可能是找错了文件名。593KB 文件内容完整，包含 47 个 episode 的结果。

### 当前进行中
**s0 clean eval 正在 GPU 0 上前台运行**（PID 280386, recovery.py），输出到 `eval_results/llama31_taxei_s0_clean.json`。无需重新启动，等它跑完即可。

要我等它完成后验证 s0 clean 结果吗？

---
