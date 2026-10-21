# ops prompt test then exp006

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prompt_test_then_exp006_20260515T173948_result.json`
- **Structured JSON:** [`2e6080368a5733f02e9c.json`](../../sessions/2e/2e6080368a5733f02e9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Qwen3-32B-FP8 开始加载到 GPU（2.5GB，正在加载权重中）。exp-006 确认正常运行。

---

## 总结

### 任务 1: exp012 Prompt 诊断测试

```
=== PROMPT TEST RESULTS ===
Variant 1 (v2 exact + structured):      10 entities, format OK (gen_tokens=160)
Variant 2 (v2 no empty-list + structured): 13 entities, format OK (gen_tokens=207)
Variant 3 (simplified + structured):     13 entities, format OK (gen_tokens=272)
Variant 4 (v2 exact + free gen):         9 entities, format OK (gen_tokens=142)
VERDICT: Plan A SUCCESS (all 4 variants)
```

关键发现：**即使是原始 v2 prompt + StructuredOutputsParams（Variant 1），LLaMA-8B 也正确提取了 10 个实体。** exp012 中 148K 全空输出的问题不是 prompt 本身导致的，而是批量推理场景下的其他因素（可能与批量数据组合、vLLM 批处理、或特定输入文本有关）。

### 任务 2: exp-006 提交

- 已通过 `submit_training_job` 提交，tmux session: `exp006_interaction_2x2`
- Qwen3-32B-FP8 正在加载（PID 312411, VLLM::EngineCore）
- 40 batches × 1000 samples = 40000 extractions，timeout 3h
- 日志: `~/runs/schema-dag-extraction/exp006_interaction_2x2.log`

---
