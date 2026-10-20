# diagnose llama31 s123 failures

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_llama31-s123-failures_20260516T150211_result.json`
- **Structured JSON:** [`afcce71d1523b5fbdac1.json`](../../sessions/af/afcce71d1523b5fbdac1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结论：**两个实验训练实际已完成，EXIT_CODE=129 是假阳性。**

- 两个实验都跑满 3387/3387 steps (epoch=3.0)
- checkpoint-3387 完整（adapter_model.safetensors ~160MB + optimizer/scheduler 等全部存在）
- SIGHUP 发生在训练结束后，推测是 tmux/SSH session 断连导致的信号传播
- **可直接用 checkpoint-3387 进行 eval，无需重训**

报告已写入 `artifacts/diagnose_llama31_s123_failure.md`。

---
