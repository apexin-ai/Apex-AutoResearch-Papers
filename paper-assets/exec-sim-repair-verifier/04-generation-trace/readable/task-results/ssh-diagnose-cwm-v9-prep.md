# ssh diagnose cwm v9 prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose-cwm-v9-prep_20260512T211046_result.json`
- **Structured JSON:** [`04d5258f44c63e4b33cb.json`](../../sessions/04/04d5258f44c63e4b33cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 环境状态 (seetacloud-westd-4x5090)

| 项目 | 状态 |
|------|------|
| 训练代码 | ✓ `/home/sonny/exec-sim-repair-verifier/train_repo_cwm.py` |
| 模型 | ✓ `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B` |
| Python 环境 | ✓ torch=2.11.0+cu128, transformers=5.8.0, peft=0.19.1 |
| GPU | 4x RTX 5090 (32GB), **全部空闲** (0MiB used) |
| 磁盘 | `/root/autodl-tmp` 144GB 可用 |
| SSH 账户 | 必须用 `root`（`sonny` 账户不存在于 SSH 工具中）|

### 问题分析

原始错误：`save_steps=100` 不是 `eval_steps=500` 的整数倍。

**关键问题：`--eval_steps` 不是 CLI 参数。** `eval_steps` 在第 268 行硬编码为 `500`：

```python
ta = {
    ...
    "eval_steps": 500,
    "save_steps": args.save_steps,  # CLI 传入，默认 100
    ...
}
```

argparse 只定义了 `--save_steps`，没有 `--eval_steps`。直接加 `--eval_steps 100` 会报 `unrecognized arguments` 错误。

### 修复方案（二选一）

**方案 A**（不改代码）：传 `--save_steps 500`，使 save_steps=500 成为 eval_steps=500 的整数倍。

**方案 B**（改代码）：给 `train_repo_cwm.py` 加 `--eval_steps` 参数，然后命令行传 `--eval_steps 100 --save_steps 100`。

### 其他注意

- `--device cuda:3` 在 argparse 中定义但代码中从未使用 `args.device`。Trainer 默认用 GPU 0。需通过 `CUDA_VISIBLE_DEVICES` 控制 GPU。
- 分配的 GPU 是 cuda:2 和 cuda:3，单卡训练选一个即可。

### 准备好的训练命令

**方案 A（不改代码，推荐最快启动）：**

```bash
cd /home/sonny/exec-sim-repair-verifier && \
CUDA_VISIBLE_DEVICES=2 python3 train_repo_cwm.py \
  --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B \
  --output_dir /root/autodl-tmp/checkpoints_repo_cwm_v9/ \
  --no_wandb \
  --save_steps 500
```

**方案 B（改代码后，eval 更频繁）：**

需先在 `train_repo_cwm.py` 中：
1. 添加 argparse 参数：`p.add_argument("--eval_steps", type=int, default=500)`
2. 修改 ta 字典：`"eval_steps": args.eval_steps,`

然后：
```bash
cd /home/sonny/exec-sim-repair-verifier && \
CUDA_VISIBLE_DEVICES=2 python3 train_repo_cwm.py \
  --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B \
  --output_dir /root/autodl-tmp/checkpoints_repo_cwm_v9/ \
  --no_wandb \
  --save_steps 100 \
  --eval_steps 100
```

---

请确认选哪个方案，我来执行代码修改（如选 B）或直接准备提交命令。

---
