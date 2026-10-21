# code llama fewnerd progress check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_fewnerd_progress_check_20260519T002618_result.json`
- **Structured JSON:** [`5b45ba41908f15db685d.json`](../../sessions/5b/5b45ba41908f15db685d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态：**Running**

| 指标 | 值 |
|---|---|
| 进度 | 23000 / 24708 steps (93.1%) |
| Epoch | 2.79 / ~3.0 |
| Train loss | 0.0151 (稳定) |
| Eval loss | 0.0328 (逐步下降: 0.0344 → 0.0332 → 0.0328) |
| GPU | GPU:1, 30888/32607 MiB (95% util) |
| ETA | **~66 分钟 (~1.1 小时)** |

训练收敛良好，loss 已很低且 eval loss 持续下降，无过拟合迹象。预计约 1 小时后完成。

完成后需要启动推理流程 `run_llama_fewnerd_inference.sh`。建议训练结束后再来检查并启动推理。

---
