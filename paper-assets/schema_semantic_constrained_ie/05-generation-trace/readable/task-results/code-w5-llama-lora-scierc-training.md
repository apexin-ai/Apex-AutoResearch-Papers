# code w5 llama lora scierc training

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w5_llama_lora_scierc_training_20260515T163426_result.json`
- **Structured JSON:** [`0c4138c68f83a806c554.json`](../../sessions/0c/0c4138c68f83a806c554.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已启动。

**关键信息:**
- 脚本: `/root/schema_semantic_constrained_ie/scripts/train_lora_llama_scierc.py` (235 行)
- 关键改动: 用 regex 从 Qwen `<|im_start|>` 包裹的 prompt 中提取 system/user 内容，再通过 `tokenizer.apply_chat_template()` 重渲染为 Llama 格式（无需重写数据文件）
- LoRA 配置: r=16, alpha=32, dropout=0.05, target=q/k/v/o/gate/up/down_proj
- Dry-run (2 步): loss=0.2769, token_acc=92.9% ✓
- 训练: PID 285172, cuda:0, 32GB VRAM 占用, 333 steps × ~1.8s ≈ 10 min + eval/save + 合并
- 输出: `checkpoints/llama_lora_scierc/`（adapter）+ `llama_lora_scierc_merged/`（fp16 合并模型）
- 日志: `logs/w5_llama_lora_scierc_training.log`
- Registry: PREPARING → QUEUED → RUNNING + 详细 notes
- cuda:1 未碰

---
