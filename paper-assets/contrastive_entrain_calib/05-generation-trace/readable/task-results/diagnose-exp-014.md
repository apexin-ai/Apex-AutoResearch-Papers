# diagnose exp 014

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-014_20260518T180356_result.json`
- **Structured JSON:** [`417ba47bbf86cf9f8f88.json`](../../sessions/41/417ba47bbf86cf9f8f88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 结论

**EXIT_CODE=127 只是表象**，实际有两个问题叠加：

1. **环境未激活**: `deepspeed` 在 `/root/miniconda3/bin/deepspeed`，原始命令缺少 `source /root/miniconda3/bin/activate`

2. **GPU 分配冲突**: `deepspeed --num_gpus 2` 会**忽略** `CUDA_VISIBLE_DEVICES=1,2`，强制使用 GPU 0,1。GPU 0 被 exp-004 占用 21.8GB，导致 GRPO 训练初始化时 OOM 崩溃

## 正确的重试命令

```bash
source /root/miniconda3/bin/activate && cd /root/contrastive_entrain_calib/training && deepspeed --include localhost:1,2 run_exp014_continuous_probe.py
```

关键改动：
- 加 `source activate` 解决 PATH 问题
- 用 `--include localhost:1,2` 替代 `--num_gpus 2`，精确指定空闲 GPU

报告已保存到 `artifacts/exp-014/diagnosis.md`。

---
