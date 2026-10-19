# monitor acib v4 step1000

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_acib_v4_step1000_20260516T011631_result.json`
- **Structured JSON:** [`203b5aee67fcdfd70a40.json`](../../sessions/20/203b5aee67fcdfd70a40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据到 step 1300 了。完整报告：

## Step 800–1300 指标趋势

| Step | task_loss | ib_loss | β | scorer_mean | scorer_std |
|------|-----------|---------|-------|-------------|------------|
| 800 | 0.0793 | 0.0134 | 0.0000 | 0.859 | 0.010 |
| 900 | 0.0808 | 0.0132 | 0.0000 | 0.859 | 0.009 |
| **1000** | **0.0742** | **0.0174** | **0.0000** | **0.871** | **0.008** |
| 1100 | 0.0587 | 0.0114 | 0.0010 | 0.855 | 0.008 |
| 1200 | 0.0885 | 0.0017 | 0.0020 | 0.828 | 0.010 |
| 1300 | 0.1064 | 0.0011 | 0.0030 | 0.824 | 0.009 |

## 判断

**scorer_std = 0.008 at step 1000 → 需要干预（< 0.01）。**

β 开始生效后（step 1100–1300）的表现：

1. **scorer_std 没有恢复分化**：β 从 0 涨到 0.003 后，std 仍在 0.008–0.010 徘徊，没有上升趋势。在 step 1200 微弹到 0.010 后立刻回落到 0.009。

2. **scorer_mean 在下降**：0.871 → 0.824。β 确实在压低整体保留率，但方式是**均匀压低所有 token 的 score**，而不是选择性过滤。

3. **ib_loss 急剧下降**：0.0174 → 0.0011。aggregate rate KL 约束太容易满足——scorer 只需统一降低 mean 就能达标，不需要分化。

4. **task_loss 恶化**：0.0742 → 0.1064。均匀压低保留率导致有用信息也被丢弃。

## 核心问题

v4 的 aggregate rate KL 约束的是 **mean 保留率**，scorer 发现最省力的策略是做一个近常数函数、只调整整体水平。这个约束形式缺乏对 **per-token 方差** 的激励，所以 β 再怎么涨也无法恢复分化——它只会让 scorer 继续均匀压低 mean，同时 task_loss 持续恶化。

---
