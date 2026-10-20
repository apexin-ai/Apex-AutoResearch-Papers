# ssh launch depth first evals westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_launch_depth_first_evals_westd_20260522T142126_result.json`
- **Structured JSON:** [`f9bd6b20bdeaf777f931.json`](../../sessions/f9/f9bd6b20bdeaf777f931.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 均已成功启动。

## 汇报

1. **磁盘可用**: 77GB（89% 已用）
2. **GRPO eval**: 启动成功，PID 51981，GPU 3 占用 12.6GB，已开始评估（7/1319 samples，~2s/it）
3. **SFT eval 结果**: 不存在，需要重跑
4. **SFT eval**: 启动成功，PID 52146，正在加载模型（检测到非均匀 MLP/Attention 结构），GPU 1 尚未完全加载
5. **model_path**:
   - GRPO: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_depth_first_20/checkpoint-100`
   - SFT: `/root/autodl-tmp/recovery_aware_struct_prune/sft_depth_first_20`

预计 GRPO eval 耗时 ~44 分钟（1319 samples × ~2s/it）。

---
