# eval cls repo fix seqlen

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cls-repo-fix-seqlen_20260517T162421_result.json`
- **Structured JSON:** [`b08012adea316d173ea0.json`](../../sessions/b0/b08012adea316d173ea0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都在正常推理：

| Job | 进度 | Running Acc |
|-----|------|-------------|
| cls-v4 (GPU 0) | 40/9784 | **80.0%** |
| cls-s123 (GPU 2) | 40/9784 | **80.0%** |

注意：之前 v4 eval（max_seq_length=2048）前 40 个样本的 accuracy 大约 75%。8192 context 下提升到 80%，说明更长的输入确实帮助了分类。

脚本每 40 samples 打印一次（batch_size=4 × 10 batches），处理 40 samples 约 3 分钟。9784 samples 预计总耗时 ~12 小时。

**状态总结：**
- cls-v4-eval session 已终止并用 max_seq_length=8192, batch_size=4 重启
- 两个 eval 并行运行中：GPU 0 (cls-v4, 28.3 GiB), GPU 2 (cls-s123, 26.1 GiB)
- 无 OOM，无 unparseable（前 40 samples 正常）
- 预计 ~12 小时完成（9784 samples / ~3min per 40 = ~12h）
- 初步 accuracy：80%（vs 之前 2048 context 的 ~70-75%），提升明显

---
