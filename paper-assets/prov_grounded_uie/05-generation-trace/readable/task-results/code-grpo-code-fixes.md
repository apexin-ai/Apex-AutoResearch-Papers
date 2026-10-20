# code grpo code fixes

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo-code-fixes_20260512T165540_result.json`
- **Structured JSON:** [`f682ad707cab2562551a.json`](../../sessions/f6/f682ad707cab2562551a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**ALL CHECKS PASSED.** 汇总：

## 修改内容

### train_grpo.py
- **第 67 行**：`max_prompt_length` 未加回 GRPOConfig 构造 — **TRL 1.1.0 的 GRPOConfig 不支持此参数**，加了会报 `TypeError`。改为注释说明。
- **第 90 行**：reward_fn kwargs 中新增 `nli_device` 传递。

### config.py
- **第 47 行**：`SFTArgs.report_to` 默认值 `"wandb"` → `"none"`
- **第 75 行**：`GRPOArgs.report_to` 默认值 `"wandb"` → `"none"`
- **第 86-89 行**：`RewardArgs.nli_model_name` 默认值改为 `/root/autodl-tmp/.hf_cache/ms_deberta/cross-encoder/nli-deberta-v3-large`
- **第 90-93 行**：新增 `RewardArgs.nli_device` 字段，默认 `"cpu"`

### rewards.py
- **第 32-39 行**：`_get_nli_model()` 新增 `device` 参数，不再硬编码 `"cuda"`，默认 `"cpu"`
- **第 96 行**：`_batch_nli_scores()` 新增 `device` 参数并传递给 `_get_nli_model`
- **第 144 行**：`provenance_fidelity_reward()` 从 kwargs 读取 `nli_device`
- **第 203 行**：调用 `_batch_nli_scores` 时传入 `device=nli_device`

## Dry-run 输出
```
max_prompt_length=2048          ← GRPOArgs 中仍有该字段可用
NLI model: /root/autodl-tmp/.hf_cache/ms_deberta/cross-encoder/nli-deberta-v3-large
NLI device: cpu
report_to: none
Reward weights: prov=0.4, struct=0.4, fmt=0.2
Dataset: 2 samples, keys=['prompt', 'gold_relations', 'sentences', 'document_text']
GRPOConfig OK: max_completion_length=2048, report_to=[]
ALL CHECKS PASSED
```

## Critical 问题结论

**`max_prompt_length` 在 TRL 1.1.0 的 `GRPOConfig` 中不存在。** 可用的 max 相关参数只有 `max_completion_length`、`max_steps`、`max_grad_norm`、`vllm_max_model_length`、`max_tool_calling_iterations`。如需限制 prompt 长度，需在数据预处理阶段用 tokenizer 截断。

---
