# diagnose eval llama sft s42 no evidence std

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_llama_sft_s42_no_evidence_std_20260520T112815_result.json`
- **Structured JSON:** [`5a01840631b2f2fb2b32.json`](../../sessions/5a/5a01840631b2f2fb2b32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因：迁移导致目录嵌套。** SFT adapter 被放入了同名包裹目录，实际文件在 `/root/autodl-tmp/sft_output_llama_3_1_8b/sft_output_llama_3_1_8b/`，而 eval 脚本传入的是外层空目录 `/root/autodl-tmp/sft_output_llama_3_1_8b/`。

`inference.py` L408 检测 `adapter_config.json` 是否存在来判断是 adapter 还是 full model。外层目录没有该文件 → 走 full model 分支 → tokenizer 加载失败（空目录无 tokenizer 文件）。

**修复**：将内层目录内容移到外层（`mv .../sft_output_llama_3_1_8b/sft_output_llama_3_1_8b/* .../sft_output_llama_3_1_8b/`），然后重跑 eval。基座模型 Meta-Llama-3.1-8B 已确认存在。

报告已写入 `artifacts/diagnose_eval_llama_sft_s42_no_evidence_std.md`。

---
