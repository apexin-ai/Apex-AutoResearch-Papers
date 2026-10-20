# fix exp002 pipeline dosage lora

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp002_pipeline_dosage_lora_20260514T061310_result.json`
- **Structured JSON:** [`93406315ad359385da8c.json`](../../sessions/93/93406315ad359385da8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修复完成，已在远程服务器上直接修改并验证。

### 修改总结

**Bug 1 — Dosage 零填充**
- `compute_signals.py` 新增 `normalize_dosage()` 和 `extract_model_id()` 函数
- 从 checkpoint 路径自动提取 dosage 并归一化为三位格式（`_d5_` → `d005`，`_d25_` → `d025`）
- 输出文件名统一使用归一化后的 model_id（如 `signal_minkpp_mmlu_Qwen2.5-0.5B_d005_s42.json`）
- `aggregate_rrf.py` 不涉及 dosage 解析，无需修改

**Bug 2 — LoRA adapter 加载**
- `compute_signals.py`: 新增 `--adapter-path` 参数，传递到 minkpp 和 selfcritique 信号模块
- `signal_minkpp.py`: `load_model_and_tokenizer()` 支持 `adapter_path`，target model 用 base + PeftModel + merge_and_unload，ref model 仍加载纯 base
- `signal_selfcritique.py`: 同样支持 adapter_path，加载完整模型（base + adapter merged）
- `signal_embedding.py`: 使用 sentence-transformers，不涉及 LLM 加载，无需修改
- `signal_constat.py`: 仅读 eval JSON，无需修改

**使用示例**：
```bash
python compute_signals.py \
  --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B \
  --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter \
  --ref-model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B \
  --benchmark mmlu ...
```

---
