# train sft unpruned baseline

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_sft_unpruned_baseline_20260515T222950_result.json`
- **Structured JSON:** [`c2ef7cdbc79e87142788.json`](../../sessions/c2/c2ef7cdbc79e87142788.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 RUNNING。

总结：

- **训练已在运行**：westd-11672 cuda:1，tmux session `sft_unpruned`，PID 66994
- **进度**：61/1870 steps (~3%)，~2s/step，预计约 60 分钟后完成
- **训练指标正常**：loss 0.92→0.72 下降中，token_accuracy 80→83%
- **磁盘问题已解决**：清理了未注册的 `sft_ablation/alpha_0.5` (6.2GB)，数据盘从 11GB→52GB 可用
- **模型来源**：`/root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B`（未剪枝原始模型，本地缓存）
- **输出目录**：`/root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline/`
- **Registry**: `sft_unpruned_baseline` 状态 RUNNING，完整 spec 已记录

---
