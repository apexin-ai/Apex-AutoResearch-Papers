# ssh fix seed42 bootstrap v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-seed42-bootstrap-v2_20260520T052426_result.json`
- **Structured JSON:** [`1c3e60a5be0367e050b1.json`](../../sessions/1c/1c3e60a5be0367e050b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## FILE NOT FOUND — 停止并报告

**Qwen2.5-7B FewNERD seed42 推理数据不存在。**

### 调查结果

1. **所有 FewNERD fine-tuned 模型都是 Qwen3-8B**，没有 Qwen2.5-7B：
   - `exp_021_fewnerd_full/adapter_config.json` → `base_model: Qwen/Qwen3-8B`
   - `ft_fewnerd_smoke/adapter_config.json` → `base_model: Qwen/Qwen3-8B`
   - `qwen3-8b-fewnerd-5epoch-lora` → Qwen3-8B
   - `llama3.1-8b-fewnerd-lora` → LLaMA 3.1-8B
   - `qwen25-32b-fewnerd-qlora-s42` → Qwen2.5-32B
   - **无 Qwen2.5-7B FewNERD checkpoint**

2. **所有 37648 行 FewNERD n8 samples.jsonl** 都来自 Qwen3-8B（greedy F1 ~0.748）：

   | 目录 | greedy_f1 | 模型 |
   |------|-----------|------|
   | `exp_021_inference` (seed42) | 0.7478 | Qwen3-8B |
   | `exp_021_fewnerd_n8_seed123` | 0.7480 | Qwen3-8B |
   | `exp_021_fewnerd_n8_seed456` | 0.7486 | Qwen3-8B |
   | `fewnerd_seed789_merged` | 0.7478 | Qwen3-8B |

3. `exp_031_fewnerd_t12` greedy F1 = 0.789，但这是 temperature=1.2 的变体，不是标准 seed42 数据。

### 结论

服务器上从未训练过 Qwen2.5-7B FewNERD fine-tuned model，因此不存在 greedy F1 ~0.784 的推理输出。任务描述中的 "Qwen2.5-7B" 可能是对实际使用的 Qwen3-8B 的误标。

需要 Director 确认：
- 实际目标是否就是 Qwen3-8B 的 `exp_021_inference/`（greedy F1 = 0.748）？
- 还是需要先训练一个 Qwen2.5-7B FewNERD LoRA 并跑推理？

---
