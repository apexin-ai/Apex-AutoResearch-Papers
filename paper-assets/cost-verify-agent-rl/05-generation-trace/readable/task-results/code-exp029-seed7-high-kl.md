# code exp029 seed7 high kl

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp029_seed7_high_kl_20260521T161623_result.json`
- **Structured JSON:** [`5ee5523c3f34fbbac75a.json`](../../sessions/5e/5ee5523c3f34fbbac75a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程 324855 正在运行。

```
GPU 确认: bjb1 cuda:0,1 已释放 → 已占用
配置:
  文件: /root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp029_seed7_high_kl.yaml
  关键修改: kl_loss_coef=0.1 (原 0.01), seed.train=999, seed.val=333, total_steps=7
  其他参数: train_batch=128 (16×8), optimizer_offload=false, save_freq=5, max_ckpt_keep=2 — 与 seed 系列一致
提交:
  PID: 324855
  tmux session: exp029_seed7_high_kl
  日志: ~/runs/cost-verify-agent-rl/exp029_seed7_high_kl.log
  W&B: 启动中，project=cost-verify-agent-rl, run_name=exp029-seed7-high-kl
```

磁盘注意：数据盘仅剩 15G（95%），7 步 + keep=2 够用但偏紧，训练中建议留意。

---
