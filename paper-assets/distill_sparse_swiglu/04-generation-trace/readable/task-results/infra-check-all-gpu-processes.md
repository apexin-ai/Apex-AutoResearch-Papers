# infra check all gpu processes

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check_all_gpu_processes_20260518T005046_result.json`
- **Structured JSON:** [`71afe8b2c964df6c83e0.json`](../../sessions/71/71afe8b2c964df6c83e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-34887
- cuda:0: **空闲** (0MiB / 0% util)
- cuda:1: **空闲** (0MiB / 0% util)
- 最近 log 文件 (2h内):
  - `qwen14b_kl30_uniform_eval_4task.log` — **失败**: `RuntimeError: Cannot send a request, as the client has been closed.` (HuggingFace Hub httpx 客户端问题)
  - `qwen14b_teal30_uniform_eval_4task.log` — **同样失败**: 相同的 RuntimeError
  - `qwen14b_kl30_uniform_eval.log` / `qwen14b_teal30_uniform_eval.log` — 也在最近修改列表中

## westd-41718
- cuda:0: **KL 30% 训练 seed=123** (PID 34700, 67560MiB, 100% util, 运行 23h33m)
  - `train.py --loss_type kl_normalized --seed 123 --sparsity_target 0.3 --num_steps 1000`
  - 进度: **Step 610/1000**, loss≈0.147, sparsity≈0.281, constraint=0
- cuda:1: **KL 30% 训练 seed=456** (PID 35045, 67560MiB, 100% util, 运行 23h02m)
  - `train.py --loss_type kl_normalized --seed 456 --sparsity_target 0.3 --num_steps 1000`
  - 进度: **Step 600/1000**, loss≈0.148, sparsity≈0.293, constraint=0
- 最近 log 文件: wandb offline logs + `download_data.log`

## 发现 & 建议
1. **westd-34887 完全空闲** — 14B 4-task eval 两个任务都因 HuggingFace Hub httpx client 关闭错误崩溃，无进程存活。需要排查 HF Hub 网络/认证问题后重跑。
2. **westd-41718 两个训练正常运行** — seed 123 和 456 的 KL 30% 8B 训练都在 ~60% 进度，loss 已收敛到 0.14-0.18 区间，sparsity 稳定在 28-30% 附近。按当前速度（~610 steps / 23.5h），预计还需 ~15h 完成 1000 steps，之后会自动进入 Phase 2 eval。
3. **之前报告的 PID 33894/33988 已不存在** — 当前实际 PID 为 34700 (s123) 和 35045 (s456)，是后续重新启动的进程。

---
