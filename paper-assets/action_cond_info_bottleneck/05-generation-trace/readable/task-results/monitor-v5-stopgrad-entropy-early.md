# monitor v5 stopgrad entropy early

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v5_stopgrad_entropy_early_20260516T020954_result.json`
- **Structured JSON:** [`6b18d2b23ed5f9e2083d.json`](../../sessions/6b/6b18d2b23ed5f9e2083d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已采到 step 100-900 全部数据。整理对比分析。

## 训练状态

- **PID 694348 存活，运行 20分19秒**
- GPU1: 93% 利用率, 16256 MiB / 24GB（与 GPU0 baseline 进程无冲突，两张卡独立）
- 训练速度 ~0.8-0.9 steps/s，已到 step 900

## 配置确认
hidden=64, α=0.01, β=0.01, β_warmup=1000, mode=soft, top_k=0.8, diversity_λ=0.1, **λ_ent=0.1**, lr=1e-4, batch=64, seed=42

## Step 100/200/500 对比（v5_stopgrad_entropy vs v5_div_reg）

| Step | 指标 | v5_stopgrad_entropy | v5_div_reg | 差异 |
|------|------|---------------------|------------|------|
| 100 | scorer_mean | **0.026** | 0.656 | **-0.630** |
| 100 | scorer_std | **0.061** | 0.188 | **-0.127** |
| 100 | task_loss | **0.419** | 0.046 | **+0.373** |
| 200 | scorer_mean | **0.018** | 0.637 | **-0.619** |
| 200 | scorer_std | **0.100** | 0.297 | **-0.197** |
| 200 | task_loss | **0.436** | 0.064 | **+0.372** |
| 500 | scorer_mean | **0.016** | 0.594 | **-0.578** |
| 500 | scorer_std | **0.102** | 0.379 | **-0.277** |
| 500 | task_loss | **0.337** | 0.064 | **+0.273** |

## 关键发现

1. **预测反了——entropy reg 推 p→0，不是 binary 化**
   - scorer_mean 从 0.026 一路降到 0.016，即所有维度都被推向"关闭"
   - scorer_std 反而更**低**（0.061→0.102），不是更高
   - entropy 项 H(p) 在 p 趋近 0 或 1 时都会减小，**当前优化路径选了 p→0**（trivial 解）

2. **stop-grad 阻断 task→scorer 信号确认**
   - task_loss 比 v5_div_reg 高 8-10 倍（0.34 vs 0.046）
   - scorer 不再为 task 服务，纯由 div_loss + ent_loss 驱动
   - div_loss 持续为负（-0.05 → -0.13），diversity reg 在工作但被 entropy 拉去推 mean→0

3. **ent_loss 单调下降**（0.091 → 0.024）符合预期，但代价是 scorer 坍缩到全 0
   - 这是 **information bottleneck 的 trivial 失败模式**：scorer 直接关掉所有维度，task 信息全部丢失

4. **β=0.0 阶段（前 1000 step）就已坍缩**
   - β warmup 还没生效，IB 项尚未介入，仅 div+ent 就把 scorer 推垮了
   - λ_ent=0.1 + 当前 ent loss 形式（应该是 -H 或 H(p)→0）选择了崩塌路径

## 结论
**v5_stopgrad_entropy 早期已显示 trivial collapse**（scorer→0），与 v5_div_reg（mean 收敛到 0.6，std 上升）轨迹完全相反。entropy reg 当前实现把所有维度推向关闭而非 binary 化，需要审查 ent loss 公式或加 mean 约束。

---
