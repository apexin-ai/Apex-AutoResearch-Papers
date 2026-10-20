# exp conf2 subset

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_conf2-subset_20260514T184004_result.json`
- **Structured JSON:** [`4aa68488a36d39e3ffe8.json`](../../sessions/4a/4aa68488a36d39e3ffe8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果：

## conf2-subset 实验结果

**实验设计**：用 probe-002 的 split（确保相同 test set），训练时只保留 conf>=2 的 10769 个 windows（28.2%），测试在完整 8101 个 windows 上。

**背景**：OB LF 没有内部置信度字段，"confidence" 是 MV 整体置信度（3 个 LF 中多少个一致）。采用 Alternative 解读。

| 配置 | test set | macro_f1 | f1_stag | f1_prog |
|------|----------|----------|---------|---------|
| probe-002 (全量训练) | full 8101 | **0.8468** | 0.7772 | 0.9165 |
| **conf2-subset** (本实验) | full 8101 | 0.7875 | 0.7051 | 0.8699 |
| probe_001 (conf>=2 训练+测试) | conf>=2 1824 | 0.9055 | 0.8593 | 0.9518 |
| **conf2-subset** (本实验) | conf>=2 2206 | **0.9281** | 0.9017 | 0.9546 |

**结论：negative**
- 在完整 test set 上 **-5.9pp** (0.7875 vs 0.8468)：移除 72% 训练数据（noisy conf=1）导致模型对 conf=1 测试窗口泛化能力下降
- 在 conf>=2 子集上 **+2.3pp** (0.9281 vs 0.9055)：高质量训练数据确实提升了高置信度窗口的判别精度
- 核心 tradeoff：**数据质量 vs 数据量**。conf=1 虽然噪声大，但提供了模型学习模糊情况的样本

---
