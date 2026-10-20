# eval llama3b uniform ppl reeval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_llama3b_uniform_ppl_reeval_20260519T054206_result.json`
- **Structured JSON:** [`f90c5351331250aaa61e.json`](../../sessions/f9/f90c5351331250aaa61e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**CHECKPOINT NOT FOUND**

`llama3b_uniform_seed42` 的 checkpoint 已被删除。搜索过的路径：

1. `/root/autodl-tmp/provenance_weight_training/output/models/llama3b_uniform_seed42/final/` — 不存在
2. `/root/autodl-tmp/output/models/llama3b_uniform_seed42/final/` — 不存在
3. `find /root/autodl-tmp -path "*llama3b_uniform*" -name "*.safetensors"` — 无结果
4. `find /root -maxdepth 6 -path "*llama3b*" -name "*.safetensors"` — 无结果
5. `find /root -maxdepth 6 -type d -name "llama3b_uniform_seed42"` — 无结果

服务器上现存的模型目录中没有任何 `llama3b_*` checkpoint（uniform 和 adaptive 都不在）。只有之前的 eval 结果目录（`llama3b_uniform_hellaswag`、`llama3b_uniform_mmlu` 等）仍存在，说明 checkpoint 在 eval 完成后被清理了。

**需要重新训练 Llama-3.2-3B uniform 模型才能进行 5000 docs 的 PPL eval。**

---
