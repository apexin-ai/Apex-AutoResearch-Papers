# analysis exp007

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp007_20260514T025245_result.json`
- **Structured JSON:** [`1b0499f97cd9f1bf56ea.json`](../../sessions/1b/1b0499f97cd9f1bf56ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp007 分析结论：**FAILED**

### 双重失败

1. **基础设施崩溃**：step 10/30 时 `/tmp` 磁盘满（Ray session 文件占满 30GB 根分区），fast_downward 无法复制 .so 文件。无 checkpoint 保存。

2. **学习信号不足**：即使完成的 10 步中，关键指标无上升趋势：

| 指标 | Dryrun 基线 | Step 10 (最终) | Phase A 标准 |
|------|------------|---------------|-------------|
| action_is_valid | 5.4% | 8.4% | >10% (FAIL) |
| success_rate | - | 6.3% | ≥76% (PASS) |
| manager_invalid_action | 6.5% | 1.6% | <50% ✓ |

### 核心发现

- **Parser fix 有效**：manager_invalid_action 从 exp003 的 95% 降到 <3%
- **但解决格式问题后暴露语义问题**：动作格式正确但在 ALFWorld 中语义无效（action_is_valid 仅 4-12%）
- pg_loss 非零（有梯度），但 reward 过于稀疏（大部分轨迹 reward=0），GRPO 无法有效学习

报告已写入 `artifacts/exp007/report/exp007_analysis.md`，registry 已更新为 `conclusion: failed`。

---
