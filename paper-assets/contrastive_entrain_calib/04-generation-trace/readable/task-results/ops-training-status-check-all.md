# ops training status check all

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_training-status-check-all_20260519T081532_result.json`
- **Structured JSON:** [`ee2ca1c6dadf313d7e4a.json`](../../sessions/ee/ee2ca1c6dadf313d7e4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 实验状态报告 (2026-05-19 16:16 UTC)

### 1. exp002v2-recalib
```
exp_id:             exp002v2-recalib (DC-GRPO cosine + recalibration)
server/GPU:         westd-29046 / GPU 0 (66.9/97.9 GiB)
current_step:       741 / 8000
ETA:                ~52h → May 21 ~20:30 UTC
key_metrics (近 20 步):
  R1 mean:          -0.06 ~ +0.01 (围绕 0 波动，信号极弱)
  R2 mean:          -0.02 ~ +0.01
  R3 mean:          0.43 ~ 0.88
  combined mean:    0.32 ~ 0.65
  loss:             0.014 ~ 0.037
  grad_norm:        0.19 ~ 0.88
  entropy:          0.18 ~ 0.40
  step_time:        ~25s/step
anomalies:          ⚠️ R1 仍然接近 0，未见改善趋势。GPU util 显示 0%（可能在 step 间 idle）
```

### 2. exp-003
```
exp_id:             exp-003 (R3-only GRPO baseline)
server/GPU:         westd-29046 / GPU 1 (38.2/97.9 GiB, 69% util)
current_step:       1894 / 8000
ETA:                ~49h → May 21 ~17:20 UTC (tqdm 估计)
key_metrics (近 20 步):
  R3 mean:          0.25 ~ 0.87 (高方差)
  combined mean:    = R3 (R3-only)
  step_time:        ~28-47s/step (波动较大)
anomalies:          R3 波动大但属正常范围；WARNING "d_syc not loaded" 每步都出现（expected for R3-only）
```

### 3. exp-004
```
exp_id:             exp-004 (ACT baseline)
server/GPU:         westd-28034 / GPU 0 (21.8/32.6 GiB, 43% util)
current_step:       6390 / 8000
ETA:                ~4.4h → May 19 ~20:40 UTC ← 今晚完成！
key_metrics (近 50 步):
  SFT loss:         0.0000 (自 step ~850 起归零，严重过拟合)
  L2 loss:          0.001 ~ 0.0014 (缓慢上升趋势)
  total loss:       0.0001
  lr:               1.03e-05 (衰减中)
  step_time:        ~9.8s/step (每 10 步 log)
anomalies:          ⚠️ SFT loss 早已归零 → 模型过拟合。L2 近期有微弱上升趋势。
                    ✅ 今晚完成，GPU 0 可交给 exp-002v3
```

### 4. exp-008v3
```
exp_id:             exp-008v3 (Binary Probe GRPO, DeepSpeed)
server/GPU:         westd-28034 / GPU 1+2 (31.4+30.6 / 32.6 GiB, 97%+86% util)
current_step:       291 / 8000
ETA:                ~41h → May 21 ~09:30 UTC
key_metrics (近 10 步):
  R1 mean:          0.375 ~ 1.0 ← 🔥 Binary Probe R1 远强于 exp002v2 的连续 R1！
  R2 mean:          0.0
  R3 mean:          0.19 ~ 0.81
  combined mean:    0.38 ~ 0.75
  loss:             0.001
  grad_norm:        0.112
  entropy:          1.31
  step_time:        ~19.4s/step
anomalies:          每步输出两次 reward（两个 DeepSpeed rank 各报一次），正常行为。
                    仍在编译 torch._inductor workers（刚启动 1.5h），正在产出有效训练步。
```

### 额外发现
- **westd-28034 GPU 3** 正在跑 `vanilla_baseline_eval`（sycon_bench 评估），不影响上述实验。

### 关键结论
1. **exp-004 今晚完成**（~20:40 UTC），GPU 0 可释放给 exp-002v3
2. **exp-008v3 的 Binary Probe R1 (0.375-1.0) 远优于 exp002v2 的连续 R1 (~0)**，验证了 binary probe 方案的信号传递优势
3. exp002v2 的 R1 信号仍无改善趋势，recalibration 未能解决连续 R1 弱信号问题

---
