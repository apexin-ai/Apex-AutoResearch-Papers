# mvp launch pipeline

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_mvp_launch_pipeline_20260520T125507_result.json`
- **Structured JSON:** [`46f6cb53821adc959d5b.json`](../../sessions/46/46f6cb53821adc959d5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MVP 流程全部运行正常。汇报：

---

**MVP 启动完成**

| 阶段 | 状态 | 详情 |
|------|------|------|
| 8B 下载 | 完成 | 5/5 safetensors，总计 ~15.3 GiB |
| 8B 验证 | 通过 | 36 layers, 4096 hidden, vocab=151643 |
| vLLM serve | 运行中 | PID 28488，端口 8000，FlashAttn v2 |
| counterfactual_gen | 运行中 | PID 29480，前 3 条（mvp_0000-0002）处理正常 |

**修复记录**：
- FlashInfer 不兼容 Blackwell（sm120），设 `VLLM_USE_FLASHINFER_SAMPLER=0` 绕过

**处理速度**：每条约 10-15 秒（3 次 LLM 调用），100 条预计约 20-25 分钟完成。

**产出文件**：`/root/causal_style_decomp_judge/data/counterfactuals.jsonl`（已有 3 条，持续追加中）

**注意**：Qwen3-8B 的 `counterfactual_text` 包含了 `&lt;think>` 标签（Qwen3 默认 thinking mode），后续管线如果需要纯文本需要做 strip。

---
