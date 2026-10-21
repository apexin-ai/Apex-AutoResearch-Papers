# ops 4b no evi d076 eval cuda1

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_4b_no_evi_d076_eval_cuda1_20260516T142358_result.json`
- **Structured JSON:** [`06e323bf17c0826e62c6.json`](../../sessions/06/06e323bf17c0826e62c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已提交完成。

**状态汇总：**
- **exp_id**: `plan_014_no_evidence_eval_d076` — RUNNING
- **PID**: 353322 on cuda:1
- **进度**: 1/247 batches (~39s/it)
- **参数**: `--no_evidence` ✓, batch_size=4, max_new_tokens=1024, seed=42, no-quantize ✓
- **模型**: Qwen3-4B + sft_no_evidence adapter (merged)
- **输出**: `/root/autodl-tmp/eval_results/plan_014_no_evidence_eval_d076`

**注意**: cuda:1 同时运行 LLaMA RSFT candidate gen (PID 353179, 17.9GB)——在我首次检查时不存在，属于竞态。eval 使用 9.6GB 未 OOM，但速度受影响（预计 ~2.7h 而非 30min）。如需加速可 kill RSFT gen，但该任务也是后续需要的，建议让两者共存完成。

---
