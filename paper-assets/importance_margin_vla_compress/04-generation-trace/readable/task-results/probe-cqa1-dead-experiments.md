# probe cqa1 dead experiments

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_probe_cqa1-dead-experiments_20260521T225749_result.json`
- **Structured JSON:** [`75b5cbbef3231810a48b.json`](../../sessions/75/75b5cbbef3231810a48b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已正常完成（非崩溃），结果如下：

**实验 1: eval_smolvla_official_l2norm_k090_object_seed42**
- 状态：**Completed**
- SR = **0.0%** (0/500)
- 所有 10 个 task 成功率均为 0%，mean_steps 全部 280（跑满上限）
- L2-norm pruning k=0.9 在 SmolVLA official 上完全失效

**实验 2: eval_smart_compress_m32_official**
- 状态：**Completed**
- SR = **53.4%** (267/500)，95% Wilson CI [49.0%, 57.7%]
- 各 task SR: 64%, 48%, 56%, 46%, 46%, 28%, 78%, 42%, 66%, 60%
- 结果已保存至 `eval_results/eval_smart_compress_m32_official.json`

两个实验的 registry 状态应从 RUNNING 更新为 COMPLETED。

---
