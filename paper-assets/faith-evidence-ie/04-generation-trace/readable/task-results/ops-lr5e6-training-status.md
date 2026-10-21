# ops lr5e6 training status

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_lr5e6_training_status_20260514T221718_result.json`
- **Structured JSON:** [`8609d71664cf4ee3344b.json`](../../sessions/86/8609d71664cf4ee3344b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 1. Checkpoints

| Checkpoint | 状态 | 保存时间 |
|---|---|---|
| checkpoint-20 | ✓ | 04:17 |
| checkpoint-40 | ✓ | 04:54 |
| checkpoint-60 | ✓ | 05:33 |
| checkpoint-80 | ✓ (新) | 06:10 |

4 个 checkpoint 全部存在，checkpoint-80 是新增的。

### 2. ckpt-40 eval (PID 101842)

- **状态**: ALIVE，已运行 ~53 分钟
- **说明**: 这是第二次尝试 (r2)，第一次被 SIGTERM 杀死 (exit -15)
- r2 输出目录 `/root/autodl-tmp/eval_results/lr5e6_r1_ckpt40/checkpoint-40/` 目前为空（仍在推理中）
- 第一次尝试的速度约 93-122s/batch，共 62 batches ≈ 103 分钟总推理时间
- **估计进度**: ~50% (53min / ~103min)，预计还需 ~50 分钟完成

### 3. 当前训练 step

**Step 84 / 200 (42%)**，PID 90080 运行 2h37m，ETA ~3h22m

### 4. 训练指标 (step 40–80)

| Step | loss | format_reward | f1_reward | ced_reward | kl | total_reward |
|------|------|---------------|-----------|------------|------|------------|
| 40 | 0.0229 | 0.201 | 0.0381 | 0.0786 | 0.006 | 0.318 |
| 45 | 0.0405 | 0.138 | 0.0 | 0.0 | 0.011 | 0.138 |
| 50 | 0.0857 | 0.225 | 0.0087 | 0.0113 | 0.008 | 0.245 |
| 55 | 0.0449 | 0.198 | 0.0378 | 0.0278 | 0.095 | 0.264 |
| 60 | 0.0411 | 0.208 | 0.0094 | 0.0059 | 0.145 | 0.223 |
| 65 | 0.1777 | 0.212 | 0.0421 | 0.0447 | **10.3** | 0.299 |
| 70 | 0.0493 | 0.216 | 0.0050 | 0.0078 | 0.012 | 0.228 |
| 75 | 0.0224 | 0.219 | 0.0043 | 0.0158 | 0.007 | 0.239 |
| 80 | 0.0463 | 0.249 | 0.0161 | 0.0178 | 0.009 | 0.283 |

### 关键观察

- **KL 二次飙升**: step 65 KL=10.3（step 5 曾爆到 2.4e9），但 step 70 立即恢复到 0.012，恢复速度快
- **format_reward 稳步上升**: 0.138→0.249，趋势正面
- **f1_reward 波动大**: 0.0→0.042 之间剧烈震荡，step 40 和 65 是局部峰值
- **ced_reward 同样不稳定**: step 40 达到峰值 0.079，后续回落到 0.005-0.045
- **总 reward**: 0.138–0.318 区间波动，step 40 最优 (0.318)，step 80 有回升趋势 (0.283)

---
