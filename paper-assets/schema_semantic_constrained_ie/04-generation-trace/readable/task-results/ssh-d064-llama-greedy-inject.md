# ssh d064 llama greedy inject

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d064_llama_greedy_inject_20260519T091746_result.json`
- **Structured JSON:** [`141c8860cdb512f81d6d.json`](../../sessions/14/141c8860cdb512f81d6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部搞定。当前状态汇总：

**GPU 0 — Llama 训练**
- 进度：90/573 步（15.7%），约 8.5s/步，预计还需 ~68 分钟
- Checkpoint 输出路径：`/root/autodl-tmp/checkpoints/llama_lora_docred_merged`
- 训练 PID：98705

**GPU 0 — Llama 串联（PID 99652，等待训练完成）**
- 训练结束后自动执行：
  1. Greedy unconstrained → `d064_llama_docred_greedy_unconstrained.jsonl`
  2. Greedy constrained S1 → `d064_llama_docred_greedy_constrained.jsonl`
  3. Beam-4 unconstrained → `d064_llama_docred_beam4_unconstrained.jsonl`
  4. Beam-4 constrained → `d064_llama_docred_beam4_constrained.jsonl`

**GPU 1 — Qwen beam-4 unc（PID 98185，正在运行）**
- 串联 PID 99686 等待 Qwen unc 完成后自动跑 Qwen beam-4 constrained

**脚本路径**：`scripts/d064_gpu0_llama_all_with_greedy.sh`
**日志路径**：`/root/autodl-tmp/schema_outputs/d064_gpu0_llama_cascade.log`

---
