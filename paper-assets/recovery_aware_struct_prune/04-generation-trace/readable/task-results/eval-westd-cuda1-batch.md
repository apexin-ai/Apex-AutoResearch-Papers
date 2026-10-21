# eval westd cuda1 batch

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_westd_cuda1_batch_20260516T014615_result.json`
- **Structured JSON:** [`d75789abd5b27b9a0110.json`](../../sessions/d7/d75789abd5b27b9a0110.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均无法执行，汇报如下：

---

## 结果汇报

### 实验 1: eval_sft_grasp_20_westd — **OOM 失败**

- **原因**: westd cuda:1 **不是空闲的**。GRPO 训练 `grpo_unpruned_v2` (PID 75381) 正在 GPU 1 上运行，内存占用 81GB/95GB。eval 加载模型需要 ~14GB，总计超出 GPU 容量，触发 CUDA OOM。
- **GRPO 进度**: 仅完成 step 5/100 (save_steps=5)，远未结束。
- **Registry**: 已标记为 DONE(failed)，附 OOM 详情。

### 实验 2: eval_sft_alpha_0p5 — **模型不存在**

- **原因**: α=0.5 的 **SFT 模型从未训练**。
  - `sft_ablation/` 目录仅有: alpha_0.0, alpha_1.0, alpha_2.0, alpha_4.0 — **缺少 alpha_0.5**
  - `alpha_ablation/alpha_0.5/` 存在，但是 **pruned 模型**（含 `pruning_metadata.pt`），不是 post-SFT 模型
- **需要**: 先对 α=0.5 pruned 模型做 SFT 训练，才能跑 eval

### westd-11672 GPU 状态

| GPU | PID | 进程 | 显存占用 |
|-----|-----|------|----------|
| cuda:0 | 74134 | python (未查) | 17.6GB / 95GB |
| cuda:1 | 75381 | grpo_unpruned_v2 (step 5/100) | 81.2GB / 95GB |

### 后续建议

1. **GraSP eval**: 等 GRPO 训练结束后再跑，或在 westb-23072 的空闲 GPU 上跑
2. **α=0.5 eval**: 需要先在 `alpha_ablation/alpha_0.5/` 上启动 SFT 训练

---
