# ops check xvla k01 seed44 result

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-xvla-k01-seed44-result_20260520T193617_result.json`
- **Structured JSON:** [`00086f395c657c2a962a.json`](../../sessions/00/00086f395c657c2a962a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验**成功完成**，但结果是全零。

**结果摘要：**
- **状态**: 正常完成（进程已退出，结果文件已写入）
- **Success Rate**: **0.0%** (0/500)
- **95% Wilson CI**: [0.0%, 0.8%]
- **所有 10 个任务**: 均为 0/50 (0%)
- **结果文件**: `/root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_prune_k01_libero_object_seed44.json`
- **耗时**: 131.1 分钟（~7864 秒）
- **配置**: L2 norm prune, keep_ratio=0.1, 50→5 vision tokens, seed=44

k=0.1（仅保留 10% vision tokens，50→5）的剪枝过于激进，模型完全丧失了任务执行能力。

---
