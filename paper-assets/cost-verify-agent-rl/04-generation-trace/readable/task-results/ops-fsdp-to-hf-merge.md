# ops fsdp to hf merge

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fsdp_to_hf_merge_20260520T093117_result.json`
- **Structured JSON:** [`173c8061199d03525b77.json`](../../sessions/17/173c8061199d03525b77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。v9d step 10 FSDP checkpoint 已合并为 HuggingFace 格式：

- **路径**: `/root/autodl-tmp/checkpoints/8b-cell-c-v9/global_step_10/actor/huggingface/`
- **模型**: Qwen3ForCausalLM, 8.19B params, bf16
- **文件**: 4 个 safetensors shard (4.6G + 4.6G + 4.7G + 1.5G ≈ 15.4GB)
- **耗时**: 43.8s（CPU-only，RAGEN 内置 `convert_fsdp_to_hf.py`）

可以直接用 `AutoModelForCausalLM.from_pretrained()` 加载做 OOD eval。

---
