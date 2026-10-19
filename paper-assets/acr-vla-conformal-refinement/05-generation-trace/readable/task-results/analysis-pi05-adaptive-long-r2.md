# analysis pi05 adaptive long r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pi05-adaptive-long-r2_20260526T101850_result.json`
- **Structured JSON:** [`e6b58ba5fc7ccd32560d.json`](../../sessions/e6/e6b58ba5fc7ccd32560d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已转 DONE/negative。**结果不是真实算法负面信号，而是 GPU OOM 系统性失败**：

## 关键发现
- **overall_success_rate = 0.0% (0/200)** ，两 seed 完全一致
- **每个 task 的 20 个 rollout 全部在 step 0 抛 `torch.AcceleratorError: CUDA error: out of memory`**
- 失败位置：`pi05_wrapper.py:163` 在 `torch.flip(img, dims=[2, 3])` 处 OOM
- 触发位置：`pi05_wrapper.preprocess_obs → _preprocess_image`（第一次图像预处理）
- 没有 W&B run（脚本未启用）
- `trigger_rate` 无法计算（adaptive gating 还没机会触发就崩了）
- exit_code = 0（脚本"正常"完成，但每个 rollout 都被异常吞掉）

## 失败原因推断
seed 43/44 分别用 cuda:4 / cuda:5 在 cqa1-32758 上**并行运行**。PI05 模型加载阶段成功（说明每张卡至少能容下权重），但首次 forward 时即 OOM——很可能是同卡上有其他进程占用，或 K=2 采样 + PI05 双 expert 推理峰值超出剩余显存。

## 建议下一步
1. 用 `nvidia-smi` 排查 cqa1-32758 cuda:4/5 是否有其他进程占显存
2. 改为顺序运行（不并行）或换到空闲 GPU 重跑
3. 这两个 run 的 conclusion=negative 仅作为状态标记；**真实的 adaptive vs VLA-only 对比尚未获得**，需要 rerun

---
