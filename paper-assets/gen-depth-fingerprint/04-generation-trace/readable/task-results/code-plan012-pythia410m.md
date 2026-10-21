# code plan012 pythia410m

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan012-pythia410m_20260515T232431_result.json`
- **Structured JSON:** [`648f4b24e6f807ab1786.json`](../../sessions/64/648f4b24e6f807ab1786.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已在 cuda:3 上正常运行：

- **PID**: 256477
- **数据**: 18,423 样本 (4 generators), depth 分布: {0:3982, 1:3950, 2:3738, 3:3471, 4:3282}
- **模型**: Pythia-410M, QLoRA 4-bit, LoRA target=`["query_key_value"]`, trainable 1.58M/355M (0.44%)
- **进度**: Fold 1/5 训练中, ~8.4 it/s, 5529 steps/fold
- **预计**: ~60-70 分钟完成全部 5-fold CV

脚本：`end_to_end_classifier_pythia.py`（与 Qwen 版独立，避免干扰 cuda:0 上运行的 Qwen3-0.6B 实验）
日志：`logs/plan012_pythia410m.log`
Registry：`plan-012-pythia410m` → RUNNING

---
