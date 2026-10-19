# code l2 ablation prep

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_l2-ablation-prep_20260523T151054_result.json`
- **Structured JSON:** [`d3ade9007022fa70abe4.json`](../../sessions/d3/d3ade9007022fa70abe4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出汇总：

### 1. 脚本路径
- `/root/contrastive_entrain_calib/train/run_l2_ablation_lambda0.sh` — λ=0 (Simple SFT)
- `/root/contrastive_entrain_calib/train/run_l2_ablation_lambda05.sh` — λ=0.5

### 2. 与 ACT 原始脚本的 diff
两个 shell wrapper 都调用同一个 `training/run_exp004s2_act.py`，仅覆盖两个参数：

| 参数 | ACT (原始) | λ=0 | λ=0.5 |
|------|-----------|-----|-------|
| `--lambda-l2` | 0.1 | **0.0** | **0.5** |
| `--output-dir` | `outputs/exp-004-act-baseline-s2` | `outputs/exp004_l2_lambda0` | `outputs/exp004_l2_lambda05` |

其余超参完全相同：LoRA r=64 α=128, 7 modules, lr=5e-5, grad_accum=16, max_steps=8000, save_steps=500, seed=43。

### 3. 预计训练时间
dry-run 1 step ≈ 10s，grad_accum=16，每 step = 16 micro-steps。8000 steps × 10s ≈ **22 小时/每个实验**。

### 4. Dry-run 验证
- λ=0: `total=2.4728 = sft(2.4728) + 0.0×l2(2.6144)` — L2 项归零，纯 SFT
- λ=0.5: `total=3.7800 = sft(2.4728) + 0.5×l2(2.6144)` — 数值正确

启动方式：
```bash
# GPU 释放后
CUDA_VISIBLE_DEVICES=0 bash /root/contrastive_entrain_calib/train/run_l2_ablation_lambda0.sh
CUDA_VISIBLE_DEVICES=1 bash /root/contrastive_entrain_calib/train/run_l2_ablation_lambda05.sh
```

---
