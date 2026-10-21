# diagnose eval plan 014 no evidence

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_plan_014_no_evidence_20260516T013029_result.json`
- **Structured JSON:** [`051d1ce0c3de893817ca.json`](../../sessions/05/051d1ce0c3de893817ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

逻辑清楚了。代码的模型加载流程：

1. `model_path` 有 `adapter_config.json` → 视为 adapter，`base_model` 作为底座
2. 然后**无条件**检查：adapter 存在但 `--sft_adapter` 未设 → 报错
3. `load_model_and_tokenizer` 中：`sft_adapter_path` 会被 merge 进底座，`adapter_path` 作为顶层 LoRA 叠加

问题在于代码假设通过 `model_path` 传入的 adapter 一定是 RSFT/DPO/GRPO 等**下游 adapter**，需要先 merge SFT 再叠加。但 plan_014 的 adapter 本身就是 SFT adapter，不需要叠加，只需要 merge。

**修复方案**：把 SFT adapter 路径从 `--model_path` 改为 `--sft_adapter`，`--model_path` 直接传底座模型。这样不会触发 adapter 检测逻辑，SFT adapter 通过 `sft_adapter_path` 被 merge 进底座后直接推理。

修复后的完整命令：

```bash
CUDA_VISIBLE_DEVICES=X python -m freige.eval.inference \
  --model_path /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_no_evidence_output \
  --data_path /root/autodl-tmp/data/docred \
  --split dev \
  --batch_size 4 \
  --max_new_tokens 1024 \
  --seed 42 \
  --output_dir /root/autodl-tmp/eval_results/sft_no_evidence_noquant \
  --no-quantize \
  --no_evidence
```

（`X` 替换为实际空闲 GPU 编号，提交前 `nvidia-smi` 确认显存 < 2GB。）

**改了什么**：去掉 `--base_model`，把 `--model_path` 改为底座 Qwen3-4B，SFT adapter 路径移到 `--sft_adapter`。这样底座直接加载，SFT adapter 通过 merge 方式合入，不触发"必须有 sft_adapter"的校验。

---
