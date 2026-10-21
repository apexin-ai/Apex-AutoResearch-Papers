# ops fix gpu and submit bce30

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-gpu-and-submit-bce30_20260518T152954_result.json`
- **Structured JSON:** [`f7385a6ab3e3baa9fccc.json`](../../sessions/f7/f7385a6ab3e3baa9fccc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

1. **PID 79351 (GPU 0) 和 PID 80126 (GPU 1) 均已终止** — 登录 westd-41718 时两个进程都已不存在，两张 GPU 完全空闲。C1 ablation 也死了（registry 仍显示 RUNNING，需要后续处理）。

2. **BCE 30% 训练已在 GPU 0 启动成功** — PID 82360，Step 100/1000 已完成（1.12s/step），预计 ~15 分钟完成。
   - 遇到两个问题并解决：
     - W&B 未登录 → 添加 `WANDB_MODE=offline`
     - CUDA OOM（内存碎片化） → 添加 `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`

3. **Registry 已更新** — bce_30pct_s42 状态为 RUNNING。

4. **注意** — GPU 1 上的 C1 ablation (`c1_ablation_bce_kl_targets_s42`) 也已死亡，registry 仍显示 RUNNING，需要决定是否重新提交。

---
