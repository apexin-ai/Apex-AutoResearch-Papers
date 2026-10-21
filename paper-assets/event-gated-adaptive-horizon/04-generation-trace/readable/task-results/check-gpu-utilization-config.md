# check gpu utilization config

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu-utilization-config_20260525T002803_result.json`
- **Structured JSON:** [`61fe328922d18c9aaffb.json`](../../sessions/61/61fe328922d18c9aaffb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，汇总如下：

---

## GPU 利用率诊断结果

### 1. 各实验配置与状态

| 实验 | 服务器 | GPU | batch_size | batch_length | 显存占用 | GPU利用率 | FPS |
|------|--------|-----|-----------|-------------|---------|----------|-----|
| exp_060 (Cartpole baseline) | bjb1-45299 | RTX PRO 6000 (96GB) cuda:0 | **16** | **64** | 5.2GB / 96GB (5.4%) | 9% | ~10.8 |
| exp_061 (Cartpole CIVO) | bjb1-45299 | RTX PRO 6000 (96GB) cuda:1 | **16** | **64** | 2.8GB / 96GB (2.9%) | 21% | ~8.1 |
| exp_062 (Cartpole control) | bjb1-40020 | RTX 4090 (24GB) cuda:0 | **16** | **64** | 3.6GB / 24GB (14.5%) | 16% | ~8.1 |
| exp_066 (Walker fidelity) | bjb1-40020 | RTX 4090 (24GB) cuda:1 | **16** | **64** | 2.5GB / 24GB (10.3%) | 1% | ~7.8 |

所有实验都使用 configs.yaml 的默认值 `batch_size=16, batch_length=64`，没有命令行覆盖。

### 2. 诊断结论

GPU 利用率低是**预期行为**，原因：

- **模型很小**：~16.4M 参数（model_opt），纯 MLP encoder/decoder（Cartpole obs 只有 5 维 proprio，Walker 24 维）
- **无 CNN**：所有实验 `Encoder CNN shapes: {}`，计算量极小
- **DreamerV3 训练循环瓶颈在 CPU 侧**（env step / data loading），不在 GPU
- batch_size=16 × batch_length=64 = 1024 tokens/batch，对现代 GPU 来说微不足道

### 3. 是否建议加大 batch_size？

**不建议修改**，理由：

1. **可比性优先**：之前所有 Walker/Cheetah 实验（exp_008-059）都用默认 batch_size=16。修改会导致 Cartpole 实验与它们不可比，论文中无法直接对比
2. **batch_size 影响学习动态**：DreamerV3 中 batch_size 不只是吞吐量参数，它影响 world model 梯度估计的方差和 imagination horizon 的有效覆盖率。加大 batch_size 可能改变收敛行为
3. **瓶颈不在 GPU**：FPS 8-11 说明瓶颈在 env interaction（DMC MuJoCo step）和数据 IO，加大 batch 不会显著提速
4. **96GB GPU 跑 Cartpole 本身就是大材小用**——这是实验调度的问题，不是 batch 参数的问题

如果将来要提高 GPU 利用率，正确做法是在同一张卡上跑多个 seed（用不同 `CUDA_VISIBLE_DEVICES` 分配即可，但 bjb1-45299 的 96GB 卡完全可以同时跑 4-6 个 Cartpole 进程共享一张卡）。

---
