# code exp post rl launch

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-post-rl-launch_20260521T035625_result.json`
- **Structured JSON:** [`517858d3bc15b33ffbc0.json`](../../sessions/51/517858d3bc15b33ffbc0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SFT 训练正常运行在 GPU 2（83% utilization, 19869 MiB）。

**汇总：**
- 模型：Qwen2.5-7B-Instruct（7.6B params, QLoRA 4-bit, trainable 0.13%）
- 数据：7106 SFT samples（5000 alpaca + 2106 MMLU 15% contamination）
- 配置：3 epochs, batch=4, grad_accum=4, lr=2e-4, 1335 total steps
- 速度：~1.06 it/s，预计 ~21 分钟完成
- GPU：cuda:2, 19869 MiB
- 日志：`~/runs/irt_personfit_contam/exp-post-rl.log`

修复记录：删除了 `train_sft.py`/`train_grpo.py`/`eval_lz.py` 中的 `os.environ["CUDA_VISIBLE_DEVICES"]` 覆盖，避免与 `submit_training_job` 框架冲突。

SFT 完成后需接续 GRPO 阶段 + eval_lz.py 评估。

---
