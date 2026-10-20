# code write inference script

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_write-inference-script_20260514T080343_result.json`
- **Structured JSON:** [`03dd493f9e2a12a70bc0.json`](../../sessions/03/03dd493f9e2a12a70bc0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过，无 ImportError，参数列表正确显示。

`/root/autodl-tmp/freige/eval/inference.py` 已创建，包含：
- **模型加载**: 4-bit NF4 QLoRA + SDPA + 自动检测 adapter vs 完整模型
- **Prompt 构造**: 与 SFT/GRPO 训练一致的 Qwen3 chat template（`enable_thinking=False`）
- **批量推理**: greedy decoding，batch 级错误容忍，截断检测
- **输出解析**: 三级修复（直接解析 → 提取 `[...]` → 截断 JSON 补全），`str(x or "")` None 保护
- **评测**: DocREDEvaluator 计算 F1/Ign-F1/Evi-F1/EDCR/format compliance
- **输出**: `metrics.json` + `predictions.json`（含 per-doc gold_triples、format_ok、truncated）

---
