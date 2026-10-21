# deploy exp014 dryrun v2 probe fix

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_exp014-dryrun-v2-probe-fix_20260518T175030_result.json`
- **Structured JSON:** [`66aaca534c6f11b89226.json`](../../sessions/66/66aaca534c6f11b89226.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

max_steps=8000 和 OUTPUT_DIR 已恢复，deepspeed 和 report_to 保留。

---

## Dry-run v2 结果汇总

### 1. Probe 训练（重新训练，含归一化）
- **Accuracy: 0.9945** (目标 >0.95 ✓)
- **AUROC: 0.9999** (目标 >0.99 ✓)
- vs exp-001 direction AUROC delta: +0.1729

### 2. R1 分布（修复验证 ✓）
R1 **不再恒为 1.0**，有正常的分布和区分度：

| Step | Rank | R1 mean | R1 std | R1 min | R1 max |
|------|------|---------|--------|--------|--------|
| 0 | 0 | 0.7920 | 0.3720 | 0.0961 | 1.0000 |
| 0 | 1 | 0.5044 | 0.4855 | 0.0000 | 0.9999 |
| 1 | 0 | 0.2936 | - | - | - |
| 1 | 1 | 0.5978 | - | - | - |

R1 mean 范围 [0.29, 0.79]，有明显 variance，归一化修复生效。

### 3. R3 分布
- Step 0: R3 mean = 0.25 ~ 0.62
- Step 1: R3 mean = 0.51 ~ 0.87
- 范围符合预期 ✓

### 4. VRAM
- GPU 1 (cuda:1): **25,596 MiB / 32,607 MiB** (78%)
- GPU 2 (cuda:2): **22,306 MiB / 32,607 MiB** (68%)
- 在 32GB 限制内 ✓

### 5. Dry-run: **PASS** ✓
- 2 steps 完成，~20.5s/step
- train_loss = -0.0027
- combined reward mean = 0.56
- 无报错

---
