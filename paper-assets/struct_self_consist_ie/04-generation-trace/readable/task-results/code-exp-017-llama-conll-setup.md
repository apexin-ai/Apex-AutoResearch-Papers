# code exp 017 llama conll setup

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_017_llama_conll_setup_20260517T113201_result.json`
- **Structured JSON:** [`4975c74da41b4ad53873.json`](../../sessions/49/4975c74da41b4ad53873.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**exp-017 LLaMA-3.1-8B CoNLL-2003 LoRA fine-tune 已于 2026-05-15 完成**，无需重新训练。

关键信息：

- **Base model**: `/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct`
- **训练数据**: 14,041 train / 3,250 dev samples
- **配置**: 与 exp-007 SciERC 完全相同（LoRA rank=32, alpha=64, lr=2e-4, 5 epochs, effective batch=16），仅调大了 eval/save 间隔并启用了 `load_best_model_at_end`
- **结果**: train_loss=0.0392, eval_loss=0.0226, 耗时 2h22m
- **产出**: LoRA adapter 在 `checkpoints/llama3.1-8b-conll2003-lora/`，merged model 在 `checkpoints/llama3.1-8b-conll2003-merged/`（15GB, 4 shards）

完整记录已写入 `artifacts/exp_017_setup.md`。

---
