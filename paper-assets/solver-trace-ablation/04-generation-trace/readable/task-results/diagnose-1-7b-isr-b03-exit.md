# diagnose 1 7b isr b03 exit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_1_7b-isr-b03-exit_20260516T214442_result.json`
- **Structured JSON:** [`8de8f0056404417f2cae.json`](../../sessions/8d/8de8f0056404417f2cae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：**预期的 training collapse 没有发生。**

- **训练完成**：500/500 步，正常结束，耗时 ~2h
- **最终统计**：prove_rate=0.165, mean_isr=0.053
- **模型已保存**：两个 safetensors 文件（~6.4GB total）+ checkpoint-500

训练**没有** collapse。最后几步 prove_rate 在 0.0~0.625 之间波动（batch variance 大），整体 prove_rate≈16.5% 维持了非零学习信号。ISR 很低（0.053），说明 ISR 惩罚在 1.7B 模型上压制了 metric gaming 但没有导致零梯度崩溃。

---
