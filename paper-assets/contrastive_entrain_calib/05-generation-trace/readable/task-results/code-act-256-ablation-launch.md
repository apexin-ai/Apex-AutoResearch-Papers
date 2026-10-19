# code act 256 ablation launch

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_act-256-ablation-launch_20260525T073612_result.json`
- **Structured JSON:** [`05e9b6c6f2237383a2ae.json`](../../sessions/05/05e9b6c6f2237383a2ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已稳定运行。第一个 logging 点（step 10）需要 160 个 micro-batch，预计约 10 分钟才会出现。

**ACT-256 ablation 已成功启动：**

| 配置项 | 值 |
|--------|-----|
| exp_id | exp-act-256 |
| GPU | cuda:1 (PID 13276) |
| 数据 | 256 行 / 128 对 |
| LoRA | r=64, alpha=64, qkvo, dropout=0 (匹配 GRPO) |
| 训练步数 | 8000 |
| lr | 5e-5, warmup=200 |
| lambda_l2 | 0.1 |
| grad_accum | 16 |
| 输出目录 | /root/autodl-tmp/checkpoints/act_256_ablation/ |
| 日志 | /root/runs/contrastive_entrain_calib/exp-act-256.log |
| tmux | exp_act_256 |

cuda:0 上的 seed4 eval 不受影响。

---
