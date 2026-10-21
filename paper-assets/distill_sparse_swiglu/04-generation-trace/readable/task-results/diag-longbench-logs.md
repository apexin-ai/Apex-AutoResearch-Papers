# diag longbench logs

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_longbench_logs_20260525T054829_result.json`
- **Structured JSON:** [`f21b665e53c40ed18f20.json`](../../sessions/f2/f21b665e53c40ed18f20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因总结：** 不是单一 bug，而是 5 次迭代中 4 个不同根因依次暴露：

1. **v1**: `HF_HUB_OFFLINE=1` + 数据未缓存 + `THUDM/LongBench` loading script 被 datasets>=3.x 拒绝
2. **v2**: 两个进程同时抢 GPU + 无 flash-attn → OOM
3. **v3**: 单卡放不下 8B 模型 + 32k token KV cache → OOM
4. **v4**: multi-GPU 但 CUDA 内存碎片化（reserved 17.98GB > requested 13.98GB）
5. **v5**: 手动 kill（Director 放弃 LongBench）

**v6 的修复组合：** `--multi_gpu --batch_size 1` + 单进程顺序执行 + 数据已缓存 → 成功。

**无日志的原因：** 所有失败 run 使用 tmux 但未 nohup 重定向，违反 C002，traceback 随 tmux session 消失。

报告已写入 `artifacts/longbench_diagnosis.md`。

---
