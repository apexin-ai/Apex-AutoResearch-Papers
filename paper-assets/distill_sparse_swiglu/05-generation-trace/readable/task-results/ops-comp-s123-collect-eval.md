# ops comp s123 collect eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_comp-s123-collect-eval_20260518T092608_result.json`
- **Structured JSON:** [`111a12e9b52f82985384.json`](../../sessions/11/111a12e9b52f82985384.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个步骤完成。总结：

**Step 1 - 训练结果收集** ✅
- kl_comp_30pct_s123 训练完成：final_loss=0.7617, 1000 steps, compensation 0.837% params
- Registry 已更新为 DONE/success

**Step 2 - PPL eval** ✅
- WikiText2 PPL = **8.9768**，C4 PPL = **16.0401**
- 与 s42 完全一致（两个 seed 共用同一 base predictor，compensation 不影响 PPL 路径）
- Registry kl_comp_30pct_s123_ppl 已标记 DONE/success

**Step 3 - rsync checkpoint 到 34887** ✅
- 通过 `scp -P 34887` 从 41718 传 compensation.pt 到 34887
- 在 34887 上完成 predictor + compensation 合并（273.2 MB）
- 路径：`/root/distill_sparse_swiglu/checkpoints/kl_comp_30pct_s123/predictor_with_comp.pt`

**Step 4 - 41718 cuda:1** 
- 无需额外任务（PPL eval 已包含 C4，不需要重复）
- 两卡均空闲，可用于后续 downstream eval

---
