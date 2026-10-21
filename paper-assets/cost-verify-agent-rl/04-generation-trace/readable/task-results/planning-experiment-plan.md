# planning experiment plan

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_planning_experiment_plan_20260515T194910_result.json`
- **Structured JSON:** [`bd9719beddd61b943ac6.json`](../../sessions/bd/bd9719beddd61b943ac6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/_project/report/experiment_plan.yaml`，17 个实验条目：

| Phase | 数量 | GPU-h | 内容 |
|-------|------|-------|------|
| A | 3 | ~504 | exp027 续训 + 扩展训练 + 3-seed 复现 |
| B | 3 | ~424 | action-change 分析 + B-IAVR 训练 + 3-seed |
| C | 7 | ~566 | no-verify / random-p / confidence-threshold ablation + entropy 控制分析 + causal intervention + reward 对比 + alpha/beta sweep |
| D | 2 | ~28 | ARES 复现 + head-to-head 对比 |

关键设计点：
- **Critical path**: plan_001 → 002 → 005 → 006/012/015
- **Minimum viable paper**: 11 个实验 ~534 GPU-h（去掉 multi-seed 和 P2 项）
- 所有 5 个 reviewer concerns 均有对应实验覆盖，RC3（action change = noise）最厚——4 个实验从统计控制和因果干预两个角度防御

---
