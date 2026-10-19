# ssh kill oom experiments 28034

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-oom-experiments-28034_20260522T163920_result.json`
- **Structured JSON:** [`e02667417ae21f13ea95.json`](../../sessions/e0/e02667417ae21f13ea95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

```
exp-003-s3 (PID 24760): KILLED ✓ (SIGTERM 成功)
exp-003-len512: NOT_FOUND — 无匹配进程，无对应 tmux session
exp-004-reduced-lora: NOT_FOUND — 无匹配进程
```

**注意：服务器是 westd-29046（2x ~98GB GPU），不是 28034 RTX 5090。** 当前实际运行的实验：

| 进程 | PID | GPU | 说明 |
|------|-----|-----|------|
| exp-003-gs8 (`run_exp003_gs8_r3only.py`) | 516696 | cuda:0 | 训练中，345% CPU |
| exp-003-eval-s2-ckpt7500 | 517336 | cuda:0 | eval，178% CPU |
| exp-003-eval-s2-ckpt8000 | 517417 | cuda:1 | eval，201% CPU |
| exp-004-s2 (`run_exp004s2_act_resume.py`, 从 ckpt-2000 恢复) | 494017 | cuda:1 | 训练中，96% CPU |

**GPU 状态：**
```
GPU 0: 55140 / 97887 MiB, 99% util  (exp-003-gs8 + eval-ckpt7500)
GPU 1: 40222 / 97887 MiB, 100% util (exp-004-s2 + eval-ckpt8000)
```

服务器上没有 "reduced-lora" 或 "len512" 相关实验。exp-004 实际跑的是 `exp-004-s2 act_resume`，不是 reduced-lora。需要确认是否要操作这些实验？

---
