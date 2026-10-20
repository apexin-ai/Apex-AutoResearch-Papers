# ops step20 metrics check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_step20-metrics-check_20260514T112748_result.json`
- **Structured JSON:** [`78fb8ae2ba00023e7301.json`](../../sessions/78/78fb8ae2ba00023e7301.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐了。以下是完整分析。

---

## Step 5/10/15/20 Metrics 趋势

| Step | loss | f1_reward | format_reward | ced_reward | reward(total) | KL | clip_ratio |
|------|------|-----------|---------------|------------|---------------|----|----|
| 5 | **286,572,390** | 0.0208 | 0.1023 | 0.1227 | 0.2458 | **3.77e9** | 0.00122 |
| 10 | 0.3427 | 0.0068 | 0.1382 | 0.1393 | 0.2843 | 4.80 | 0.00113 |
| 15 | **21,925,201,510** | 0.0109 | 0.1724 | 0.2320 | 0.4153 | **3.40e11** | 0.00090 |
| 20 | **202,007,821** | 0.0063 | 0.1969 | 0.3046 | 0.5078 | 0.0963 | 0.00087 |

## 分析

### 1. 奇偶尖刺模式

**部分延续，部分变化：**
- Step 5 (奇) 和 15 (奇)：loss/KL 都是巨大尖刺，符合预期模式
- Step 10 (偶)：完全正常（loss=0.34, KL=4.8），符合预期
- **Step 20 (偶)：KL 正常（0.096），但 loss 仍然异常高（202M）**

这说明：`num_iterations=2` 的第二个 iteration（偶数 step）KL 始终正常，但 loss 从 step 10 的 0.34 恶化到 step 20 的 202M。loss 尖刺可能正在扩散到偶数步。

### 2. f1_reward 趋势

**持续下降**：0.0208 → 0.0068 → 0.0109 → 0.0063。模型几乎没在学习 F1 匹配。

### 3. reward(total) 趋势

**稳步上升**：0.246 → 0.284 → 0.415 → 0.508。但这主要靠 **ced_reward 拉动**（0.12 → 0.14 → 0.23 → 0.30）和 **format_reward 缓慢提升**（0.10 → 0.14 → 0.17 → 0.20）。f1_reward 贡献几乎为零。

### 4. checkpoint-20

**已生成**，时间 2026-05-14 19:27，位于 `/root/autodl-tmp/grpo_s3_r2/checkpoint-20/`。

### 5. 进程状态

PID 39556 仍在运行（elapsed 30:23）。注意日志中 step 18 处出现 `PID 39555 Killed`——这是外层 `timeout` wrapper 被 kill，但训练进程本身存活并继续到 step 20+。

### 关键风险

loss 在偶数步（20）也开始异常高（202M），说明不稳定性正在恶化。如果 step 25（奇数步）loss 再次爆炸（预计比 step 15 的 219 亿更大），训练可能完全发散。

---
