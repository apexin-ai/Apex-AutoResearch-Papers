# check k4 pipelines urgent

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_k4_pipelines_urgent_20260522T151111_result.json`
- **Structured JSON:** [`b9602ea91318cfeb36f2.json`](../../sessions/b9/b9602ea91318cfeb36f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## K=4 Pipeline 状态

**s123** (PID 59565): Phase 3 进行中
- Phase 1 训练: ✅ DONE (final ckpt 152MB @ 23:04, 2700 steps)
- Phase 2 PPL: ✅ DONE — `wikitext2_ppl = 8.8897`
- Phase 3 Downstream 7-task: 🔄 RUNNING (PID 65980, 启动 23:04, 当前在 tokenizing ~78%/58702 samples)
- Phase 4 Sparsity: ⏳ Pending

**s456** (PID 59879): Phase 3 进行中
- Phase 1 训练: ✅ DONE (final ckpt 152MB @ 23:04, 2700 steps)
- Phase 2 PPL: ✅ DONE — `wikitext2_ppl = 8.8828`
- Phase 3 Downstream 7-task: 🔄 RUNNING (PID 66278, 启动 23:05, 同步进行)
- Phase 4 Sparsity: ⏳ Pending

**GPU**: 0/1 各持 48GB 显存, util 0%（处于 tokenization 间隙）
**Tmux**: 无（用 nohup 启动，符合 C002）
**两个 seed PPL 一致性极佳**: 8.8897 vs 8.8828 (Δ=0.007)

Downstream eval 任务: arc_challenge, winogrande, mmlu, gsm8k, hellaswag, piqa, boolq @ teal_global sparsity=0.3 uniform。当前在 mmlu/hellaswag 这类大数据集的 tokenization 阶段，预估还需 30-60 min 完成 Phase 3，之后 Phase 4 sparsity 分析约 10-15 min。

---
