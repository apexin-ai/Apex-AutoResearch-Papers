# diag exp014 speed check step30

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp014-speed-check-step30_20260518T184140_result.json`
- **Structured JSON:** [`0f3d9d7c21b5db2b9215.json`](../../sessions/0f/0f3d9d7c21b5db2b9215.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-014 训练速度诊断报告

### 1. Step 20-30 速度

| Step 范围 | 平均 step time | 趋势 |
|-----------|--------------|------|
| 20-30 | **~20.0 s/step** | 稳定（±1s 波动，无加速/减速趋势） |

logged `step_time`: step 20 = 19.66s, step 30 = 19.90s

### 2. GPU 利用率与显存

| GPU | 显存使用 | GPU 利用率 |
|-----|---------|-----------|
| GPU 1 | 31400 / 32607 MiB (96.3%) | 0-100% 交替 |
| GPU 2 | 30638 / 32607 MiB (94.0%) | 0-100% 交替 |

GPU 利用率呈**脉冲模式**（100% → 0% → 96%），是 GRPO 训练的典型特征：generation 阶段满载 → reward 计算间隙 → 梯度更新。CPU 空闲率 98%，不是瓶颈。无 NCCL 异常日志。

### 3. 77s/step 的原因

**误读 tqdm 累计平均值。** 实际情况：

- Step 1 耗时 **447s**（包含 CUDA kernel 编译、DeepSpeed 初始化等一次性 warmup）
- Step 2 起实际每步就是 **~20s**
- tqdm 在 step 4 时显示累计平均 77.69 s/it，这是被 step 1 的 447s 严重拉高的结果
- **不存在 3.7× 速度差距**，稳态速度 ≈ dry-run 速度（20.5s）

关于 grad_accum=16 的疑问：GRPO 的 step 定义包含了完整的 generation + multi-sample forward/backward，grad_accum 影响的是 micro-batch 拆分方式而非总计算量翻倍，所以与 dry-run 速度接近是合理的。

### 4. 结论

**无需干预。** 训练速度正常，~20s/step 在 2×V100-32G DeepSpeed ZeRO-2 上合理。预估总时长 ≈ 8000 × 20s ≈ 44.4 小时。

---
