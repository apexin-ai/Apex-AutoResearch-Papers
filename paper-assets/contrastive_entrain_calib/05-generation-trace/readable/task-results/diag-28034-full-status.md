# diag 28034 full status

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_28034-full-status_20260522T233024_result.json`
- **Structured JSON:** [`c9a2f2b2b364bacf8424.json`](../../sessions/c9/c9a2f2b2b364bacf8424.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

原始3个eval（gs8 ckpt-500 verify, reduced-lora ckpt-1500, reduced-lora ckpt-2000）**没有留下任何结果文件或日志**。它们的PID已经不存在，且在服务器上找不到对应的output。

这是这台服务器（28034→westd-29046）的实际情况，注意服务器编号不同——有可能那3个eval跑在另一台机器上（编号28034），而当前连接的是 westd-29046。

以下是当前 westd-29046 的完整状态：

---

```
GPU状态:
GPU0: 训练 exp003_gs8_r3only (PID 516696, 7h56m) — step 1040/8000 (13%), ~25s/step
GPU1: 训练 exp004_act_baseline_s2 resume (PID 494017, 12h41m) — step 7010/8000 (87.6%), ~90s/10step
GPU2: 无 (此服务器只有2张GPU)
GPU3: 无

当前训练进度:
exp003_gs8_r3only:    1040/8000 (13%), 预计还需 ~48h
exp004_act_s2_resume: 7010/8000 (87.6%), 预计还需 ~2.5h，最新 ckpt=7000

已完成的 Eval 结果 (exp003 seed2 D027 preset eval):
exp003-s2-ckpt4000: SYCONScore=0.1430, ToF=0.0773, NoF=0.9448
exp003-s2-ckpt7500: SYCONScore=0.1241, ToF=0.0663, NoF=0.9724
exp003-s2-ckpt8000: SYCONScore=0.1240, ToF=0.0663, NoF=0.9613
  (所有 eval 用 seed2 checkpoint, 数据=calibration_v2_1_expanded.jsonl, n=362)

原始3个eval (gs8 ckpt-500 verify / reduced-lora ckpt-1500 / reduced-lora ckpt-2000):
  ❌ PID 131250/136668/137176 均不存在
  ❌ 无对应结果JSON、无日志文件
  → 可能跑在另一台服务器上，或进程被kill后未保存结果

Checkpoint 清单:
exp003_r3only_seed1: ckpt 500~8000 (每500步)
exp003_r3only_seed2: ckpt 500~8000 (每500步)
exp-004-act-baseline-s2: ckpt 2000~7000 (每500步, 仍在产出)
exp003_gs8_r3only: ckpt 500, 1000 (仍在产出)
```

---
