# code prep exp 020 folio

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-exp-020-folio_20260517T083230_result.json`
- **Structured JSON:** [`ed1f5f1935aa47628a13.json`](../../sessions/ed/ed1f5f1935aa47628a13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本就绪。汇总：

**脚本**: `/root/symb_invariant_consensus/scripts/run_exp020_llama8b_folio204.sh` (已创建, +x)
- 语法检查通过

**模型**: `/root/autodl-tmp/models/Llama-3.1-8B-Instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct/` 
- 4 个 safetensors 分片完整 ✓

**数据**: `data/folio_full.json`
- 204 题 ✓

**参数**: K=12, T=0.7, max-tokens=4096, seed=42（与 exp-011 一致）

**输出**: `results/exp020_llama8b_folio204/exp020_results.json`

**预估运行时间**: LLaMA-8B + 204题 × K=12 采样，约 1.5-2.5 小时（参考 exp-011 的 60 题约 40min 外推）。

可随时通过 `submit_training_job` 提交。

---
