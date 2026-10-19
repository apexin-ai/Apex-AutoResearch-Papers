# diagnose eval perdof norm01 seed44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-perdof-norm01-seed44_20260517T104628_result.json`
- **Structured JSON:** [`86540893792571822c61.json`](../../sessions/86/86540893792571822c61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**进程状态：已正常完成（非异常退出）**

PID 531963 不存在，但实验已**跑完全部 10 个 task × 10 rollouts = 100 episodes**，结果已保存。

### 实验结果

| 指标 | 值 |
|------|-----|
| 模式 | crm_perdof, max_correction_norm=0.1 |
| Benchmark | object (10 tasks) |
| Seed | 44 |
| **Overall success rate** | **8.0% (8/100)** |

逐任务成功率：

| Task | Success Rate |
|------|-------------|
| salad_dressing | 20% (2/10) |
| orange_juice | 30% (3/10) |
| chocolate_pudding | 20% (2/10) |
| bbq_sauce | 10% (1/10) |
| alphabet_soup / cream_cheese / ketchup / tomato_sauce / butter / milk | 0% (0/10) |

### 结论

- 进程**正常退出**，不是 OOM 或 CUDA error
- 结果已保存到 `logs/eval_object_perdof_norm01_seed44.json`
- 无需重试，实验已完整完成
- GPU 上当前有其他 3 个 python 进程在运行（PID 474319 在 GPU0, 587763 在 GPU2, 588037 在 GPU3）

---
