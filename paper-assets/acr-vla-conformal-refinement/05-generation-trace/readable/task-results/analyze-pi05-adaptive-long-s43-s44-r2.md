# analyze pi05 adaptive long s43 s44 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_pi05-adaptive-long-s43-s44-r2_20260526T101751_result.json`
- **Structured JSON:** [`51386907c2064fe7107d.json`](../../sessions/51/51386907c2064fe7107d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**两个实验完全失败，原因是 CUDA OOM。**

## 实验 1: pi05-adaptive-long-s43-cqa1-r2
```
exp_id: pi05-adaptive-long-s43-cqa1-r2
overall_success_rate: 0.0% (0/200)
trigger_rate: N/A (每个 rollout 在 step 0 就 OOM，未执行任何 action)
per_task_rates: 全部 10 个 task 均为 0% (0/20)
wandb_run_id: 无 (日志中未出现 wandb 相关信息)
status: FAILED — CUDA OOM
```

## 实验 2: pi05-adaptive-long-s44-cqa1-r2
```
exp_id: pi05-adaptive-long-s44-cqa1-r2
overall_success_rate: 0.0% (0/200)
trigger_rate: N/A (同上)
per_task_rates: 全部 10 个 task 均为 0% (0/20)
wandb_run_id: 无
status: FAILED — CUDA OOM
```

## 根因分析

两个实验从第一个 rollout 的 **step 0** 开始就全程 OOM（s43 日志中有 316 次 "CUDA error" 记录）。OOM 发生在 `pi05_wrapper.py:163` 的 `torch.flip()` — 即图像预处理阶段，模型推理都没有开始。

这说明 π0.5 模型加载后 GPU 显存已经接近满了，`adaptive_conformal_crm` 模式（需要额外采样 K=2 次）在预处理时就溢出。两个实验分别跑在 cuda:4 和 cuda:5 上，说明这两张卡的可用显存不足。

**结论：这两个实验的结果无效，不能用于与 baseline (57.2%) 对比。需要排查 GPU 显存占用或换更大显存的卡重跑。**

---
