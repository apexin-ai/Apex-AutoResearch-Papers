# exp mvp results check

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_mvp-results-check_20260512T114051_result.json`
- **Structured JSON:** [`b1718a47841fa63cd698.json`](../../sessions/b1/b1718a47841fa63cd698.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### 1. 当前进程：**运行中**
- PID: 75855, 已运行 ~6 分钟
- 当前阶段: **Phase 1 — Uncalibrated baseline**
- 进度: 已启动 task 0-3（共 20 个 task），约完成 2 个
- 最新日志时间: 19:41:55，持续有 LLM 调用

### 2. 已完成 task 结果（Phase 1 进行中）
| Task | 状态 | Reward | 说明 |
|------|------|--------|------|
| task 0 | ✅ | 1.0 | cancel_pending_order，成功完成 |
| task 1 | ❌ | 0.0 | exchange_delivered_order_items，被转到 human agent |

### 3. 之前 Quick Test 的结果（mvp_results.json，19:35 生成）

这是之前 quick test 跑 3 个 task 的结果（非当前全量实验）：

| Condition | question_rate | politeness_rate | task_completion | num_traces |
|-----------|--------------|-----------------|-----------------|------------|
| uncalibrated_baseline | 0.65 ± 0.15 | 0.45 ± 0.05 | 33.3% | 2 |
| aave_target | 0.74 ± 0.05 | 0.66 ± 0.12 | 0.0% | 3 |

### 4. Quick Test H-Gate 评估

| Gate | 结果 | 详情 |
|------|------|------|
| **H1** | **PASS** ✅ | question_rate=0.65 > 0.15 阈值, politeness_rate=0.45 > 0.30 阈值 |
| **H2** | **FAIL** ❌ | aave_target 校准后偏差反而更大：question_improvement=-16.2%, politeness_improvement=-82.2%（需 >30%） |
| **H3** | **FAIL** ❌ | aave_target task_completion=0.0%，baseline=33.3%，未达到 80% 保持率 |

### 5. 预估时间
- Phase 1 (20 tasks): task 0-1 约耗时 2 分钟/task，20 个 task 预计 ~30-40 分钟
- 全部 Phase（baseline + 各 calibration condition）: 预计总计 **1-2 小时**

### 6. 初步分析
Quick test 暴露的核心问题：calibration prompt 不仅没有让 agent 行为向目标靠近（H2 FAIL），还严重损害了 task completion（H3 FAIL，从 33% 降到 0%）。当前全量实验（20 tasks）将给出更可靠的统计量。建议等全量实验完成后再做最终判断。

---
