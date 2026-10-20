# analysis seed coverage audit

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_seed_coverage_audit_20260518T100136_result.json`
- **Structured JSON:** [`59f97210c6f41fb85411.json`](../../sessions/59/59f97210c6f41fb85411.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== Seed 覆盖盘点 (k=1 RSFT) ===

| Model | Scale | Seeds with k=1 eval | Need training | Need eval | GPU-h/seed (train+eval) |
|-------|-------|---------------------|---------------|-----------|------------------------|
| Qwen3-4B | 4B | 42,43,44,45 ✅ | — | — | — |
| Qwen3-1.7B | 1.7B | 42 (eval 🔄94%) | 43, 44 | 42,43,44 | ~0.25+2.5h |
| Qwen3-8B | 8B | — | 44 | 42,43,44 | ~0.8+3h |
| LLaMA-3.1-8B | 8B | — | 43, 44 | 42,43,44 | ~0.7+2.5h |

当前 GPU 状态：4卡全占（D102 s42 eval: 1.7B@GPU2 94%, LLaMA@GPU3 68%, 8B-s42@GPU0 51%, 8B-s43@GPU1 50%）

### 详细状态

**4B** — 完成。4 seeds 已有 k=1 eval（原始 CED 训练数据即 k=1，2718 samples）。

**1.7B** — s42 训练完成，eval 即将结束。需补 s43, s44。
- 数据: `/root/autodl-tmp/freige/outputs/rsft_scored_1_7b_k1/rsft_train.jsonl` (3021 samples)
- 训练时间: ~15min/seed, eval ~2.5h/seed

**8B** — s42, s43 训练完成，eval 分别 ~51%/50%。需补 s44。
- 数据: `/root/autodl-tmp/rsft_scored_qwen3_8b_k1/rsft_train.jsonl` (3018 samples)
- 训练时间: ~48min/seed, eval ~3h/seed

**LLaMA** — s42 训练完成，eval ~68%。需补 s43, s44。
- 数据: `/root/autodl-tmp/rsft_scored_llama_3_1_8b_k1/rsft_train.jsonl` (2952 samples)
- 训练时间: ~43min/seed, eval ~2.5h/seed

### 总计需补

- **5 个训练**: 1.7B×2 + 8B×1 + LLaMA×2 = ~2.7 GPU-hours
- **5 个新 eval** + **4 个正在跑的 eval** = ~13 GPU-hours eval（可 4 卡并行 → ~3.5h 墙钟）
- **脚本已写到**: `/root/autodl-tmp/freige/scripts/seed_expansion/`

### 执行顺序建议

1. 等当前 4 个 eval 完成（~1-2h 后）
2. 用空出的卡并行跑 5 个训练（1.7B 两个可共享 1 卡顺序跑，8B 和 LLaMA 各占 1 卡）
3. 训练完后并行跑 5 个 eval

---
