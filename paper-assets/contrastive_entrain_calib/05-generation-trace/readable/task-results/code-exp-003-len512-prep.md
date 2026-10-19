# code exp 003 len512 prep

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-003-len512-prep_20260522T235826_result.json`
- **Structured JSON:** [`0c40e02e2d6a61f6b0b3.json`](../../sessions/0c/0c40e02e2d6a61f6b0b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已就绪，语法验证通过。

```
脚本路径: /root/contrastive_entrain_calib/training/run_exp003_len512_r3only.py
关键参数变化: max_completion_length 256→512
其余参数: 与 exp-003 完全一致
  - r1=0, r2=0, r3=1.0 (R3-only)
  - num_generations=2, beta=0.04, temperature=0.7
  - lr=5e-5, warmup=100, cosine scheduler
  - LoRA r=64, alpha=64, targets=[q,v,k,o_proj]
  - max_steps=8000, save_steps=500, seed=42
  - report_to="none" (无 wandb)

显存预估: 可行
  - GPU: NVIDIA RTX PRO 6000 Blackwell, 96GB/卡
  - exp-003 (len=256) 在 cuda:0 占用 ~38GB
  - len=512 主要增加 generation 阶段 KV cache（batch=1, group=2, 额外 256 tokens）
  - KV cache 增量约 2-4GB（Qwen3-8B, GQA, bf16）
  - 预估峰值 ~42-45GB，96GB 完全够用

启动命令（待 cuda:1 释放后执行）:
CUDA_VISIBLE_DEVICES=1 nohup python /root/contrastive_entrain_calib/training/run_exp003_len512_r3only.py \
  > /root/contrastive_entrain_calib/logs/exp003_len512.log 2>&1 &

状态: 代码就绪，待 cuda:1 释放后启动
```

---
