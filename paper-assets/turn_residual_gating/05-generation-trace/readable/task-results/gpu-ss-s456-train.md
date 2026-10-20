# gpu ss s456 train

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_ss_s456_train_20260523T034232_result.json`
- **Structured JSON:** [`873dcb7c48dad4207c32.json`](../../sessions/87/873dcb7c48dad4207c32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**d048_ss_s456 训练已在运行中，无需手动启动。**

**训练状态：**
- 由 `queue_runner` → `d048_remaining_queue.sh` → `d048_ss_s456.sh` 自动调度，10:55 启动
- 当前进度：Epoch 0, Step 2850（SS ratio 逐步爬升中，当前 ~0.119）
- GPU：96% utilization, 53.1 GB 显存占用
- Gate mean ~0.95，训练正常

**d048_final_ar 评测结果（已完成）：**
- `results/d048_final_ar/` 包含 6 个模型的 AR n=50 评测：base, lo, pcgrad, ss, tg, ug（均为 s42）
- `d048_summary_ci_wilcoxon.json` 汇总统计已生成
- `results/d048_ar_n50_existing/` 有 4 个模型的旧版评测结果

**结论：GPU 繁忙，SS s456 已自动开跑，不需要任何操作。**

---
