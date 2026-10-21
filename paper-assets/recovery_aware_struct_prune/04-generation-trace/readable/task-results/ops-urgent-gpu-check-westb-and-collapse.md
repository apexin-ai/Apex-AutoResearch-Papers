# ops urgent gpu check westb and collapse

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_gpu_check_westb_and_collapse_20260517T182000_result.json`
- **Structured JSON:** [`e76ab84928d060a62ec5.json`](../../sessions/e7/e76ab84928d060a62ec5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 核查 + GRPO 训练动态报告

### GPU 状态 (westb-23072)

| GPU | 实验 | PID | 进度 | Memory | Temp | Util |
|-----|------|-----|------|--------|------|------|
| cuda:0 | grpo_cka_only_20 | 725232 | **30/100** | 73549/97887 MiB | 81°C | 100% |
| cuda:1 | grpo_random_20 | 719684 | **38/100** | 73165/97887 MiB | 82°C | 100% |

两个实验均在运行，未完成。~7 min/step，预计还需 **7-8 小时**完成。

---

### Collapse 动态表

**grpo_cka_only_20 (CKA-pruned → SFT → GRPO):**

| Step | Reward | Reward_std | frac_zero_std | Loss | Grad_norm | Entropy | KL | Mean_len | Clip_ratio |
|------|--------|------------|---------------|------|-----------|---------|---------|----------|------------|
| 10 | **0.253** | 0.387 | 0.175 | 0.039 | 1.891 | 0.083 | 0.00121 | 500.5 | 0.40 |
| 20 | **0.218** | 0.360 | 0.200 | 0.150 | 1.250 | 0.075 | 0.00123 | 515.7 | 0.40 |
| 30 | **0.250** | 0.390 | 0.200 | -0.021 | 1.102 | 0.097 | 0.00167 | 443.7 | 0.32 |

**grpo_random_20 (Random-pruned → SFT → GRPO):**

| Step | Reward | Reward_std | frac_zero_std | Loss | Grad_norm | Entropy | KL | Mean_len | Clip_ratio |
|------|--------|------------|---------------|------|-----------|---------|---------|----------|------------|
| 10 | **0.161** | 0.309 | 0.300 | -0.021 | 3.750 | 0.231 | 0.00418 | 341.5 | 0.16 |
| 20 | **0.142** | 0.280 | 0.325 | -0.037 | **8.625** | 0.228 | 0.00470 | 387.1 | 0.21 |
| 30 | **0.166** | 0.347 | 0.325 | 0.003 | 3.672 | 0.235 | 0.00459 | 433.9 | 0.24 |

---

### 当前判断

**均未 collapse**，但两者差异显著：

1. **Reward**: CKA 稳定在 ~0.22-0.25，Random 在 ~0.14-0.17，CKA 领先约 **50-60%**
2. **frac_zero_std**: CKA 0.175→0.20（低位稳定），Random 0.30→0.325（偏高但未恶化）。Random 的 30%+ zero-std 意味着接近 1/3 的 batch 完全无 reward 方差，是 collapse 的前兆信号
3. **Grad_norm**: CKA 持续下降（1.9→1.1，健康）；Random step 20 飙到 **8.625**（异常 spike），虽然 step 30 回落到 3.7，但仍是 CKA 的 3 倍
4. **KL**: Random 的 KL（~0.0045）是 CKA（~0.0015）的 **3 倍**，说明 random-pruned 模型偏离 ref policy 更快
5. **Entropy**: Random (~0.23) >> CKA (~0.08)，看似 random 更"多样"，但结合低 reward 和高 frac_zero_std，这更可能是"乱猜"而非有效探索
6. **RewardDesertCallback**: patience=50 步，最早 step 50 才会触发。Random 的 frac_zero_std=0.325 如果继续升高，可能在 step 50-70 之间被终止

**结论**: 30 步数据尚早定论，但 CKA-pruned 模型的 GRPO 训练显著更稳定。需要等到 step 50-60 才能判断 Random 是否会真正 collapse。

---
