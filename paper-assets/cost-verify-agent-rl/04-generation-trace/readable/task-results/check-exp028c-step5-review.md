# check exp028c step5 review

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp028c_step5_review_20260516T023032_result.json`
- **Structured JSON:** [`b31591169512cb44ea52.json`](../../sessions/b3/b31591169512cb44ea52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W&B history 返回空（可能尚未同步完毕），但日志数据完整。以下是汇总。

## exp028c_selfguide_recipe 状态报告

### 基本状态
- **进程**: PID 824675 存活，运行 4h53m
- **GPU**: cuda:0 97% (19.3/97.9 GB), cuda:1 100% (19.3/97.9 GB) — 正常工作中
- **当前进度**: Step 4 rollout 进行中，Step 5 val 尚未开始

### 趋势表

| Step | Type | Success | Pass@8 | KL Loss | Entropy | Valid | Grad Norm | Score Mean | Step Time |
|------|------|---------|--------|---------|---------|-------|-----------|------------|-----------|
| 0 | val | **6.25%** | - | - | - | 74.5% | - | 0.119 | (included in step 1) |
| 1 | train | 13.28% | 37.5% | 0.0128 | 0.2634 | 76.4% | 16.88 | 0.843 | 54 min |
| 2 | train | **6.25%** | 25.0% | **0.1706** | 0.2470 | 83.2% | 17.30 | 0.274 | 52 min |
| 3 | train | 15.63% | **68.75%** | 0.1118 | 0.2488 | 85.9% | 12.57 | 0.661 | 46 min |
| 4 | train | (running) | - | - | - | - | - | - | >2h13m |
| 5 | val | (pending) | - | - | - | - | - | - | - |

### 关键观察

1. **Step 4 异常慢**: Step 1-3 每步 46-54 min，Step 4 已运行 >2h13m（~2.5x 正常时长）。GPU 利用率正常（97-100%），最新日志时间戳 10:22 仍有 anchor_obs 输出，说明进程未 hang，但 rollout 显著变慢。可能原因：模型学到了更长的探索轨迹（max_turn=50）。

2. **Success 趋势不稳定**: 6.25% → 13.28% → **6.25%** → 15.63%。Step 2 出现大幅回落后 step 3 恢复，但振荡明显。

3. **KL 走势**: 0.013 → **0.171** → 0.112。Step 2 KL 飙升 13x，step 3 有所回落但仍高于 step 1。KL 并未在 step 2 后持续下降，而是从峰值回退了约 35%。

4. **Entropy**: 0.263 → 0.247 → 0.249。轻微下降后稳定在 ~0.25，**未出现 collapse**（远高于 0.1 阈值）。

5. **action_is_valid 持续改善**: 74.5% → 76.4% → 83.2% → 85.9%，这是最稳定的正面信号。

6. **Pass@8 跳升**: 37.5% → 25% → **68.75%**。Step 3 pass@8 大幅提升，说明模型在多次采样中能力增强，但 pass@1（success）仍低。

### Step 5 val 预计时间

- Step 4 已运行 >2h13m，rollout 仍在进行。如果 step 4 在接下来 30-60 min 完成，step 5 val eval 大约再需 30-60 min。
- **乐观估计**: ~1.5h 后可见 step 5 val 结果（约 12:00）
- **保守估计**: ~2.5h 后（约 13:00），取决于 step 4 rollout 何时结束

### MVP 判定

目前 train success 在 6-16% 波动，val baseline 是 6.25%。考虑到 train pass@8 在 step 3 达到 68.75%，模型有探索能力但 greedy 策略尚弱。**Step 5 val 结果是关键**——如果 val success 仍 <20%，按标准为 fail。

---
