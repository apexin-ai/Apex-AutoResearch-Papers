# ops collect grid b0 2 reeval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect_grid_b0_2_reeval_20260518T060615_result.json`
- **Structured JSON:** [`183b4a5f51a5616f85cb.json`](../../sessions/18/183b4a5f51a5616f85cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

### 模型验证
两个 checkpoint 均为 **Qwen3ForCausalLM (hidden_size=1024)**，确认是 Qwen3-0.6B。上个 worker 报告的 "Mistral-Small-3.1-24B" 只是 tokenizer 元数据中的 regex warning 残留，模型本身正确。

### Re-eval 结果（eval_holdout, 5000 docs, max_length 2048）

| 实验 | Loss | Perplexity | Tokens |
|------|------|-----------|--------|
| grid_b0_2_seed123/final | 2.9139 | 18.43 | 4,077,068 |
| grid_b0_2_seed456/final | 2.9091 | 18.34 | 4,077,068 |

对比 checkpoint-5500 的结果（seed123: loss=2.8700, ppl=17.64），final checkpoint 的 ppl 略高（~18.3-18.4 vs 17.6），说明从 checkpoint-5500 继续训练到 final 后 holdout perplexity 有轻微上升，可能存在过拟合迹象。两个 seed 之间结果一致（ppl 差异 <0.1），cross-seed 复现性良好。

---
