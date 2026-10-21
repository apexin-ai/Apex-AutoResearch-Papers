# research failure taxonomy

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_failure_taxonomy_20260515T160527_result.json`
- **Structured JSON:** [`37425d7c673dd286fc97.json`](../../sessions/37/37425d7c673dd286fc97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

**总量**: 51 个实验，46 个已有结论（3 成功、5 负向、38 失败/终止）。

**4 个失败类别**:
1. **工程类** (24 个, 63%) — 磁盘满、AutoDL 容器限制、错误入口点、版本不兼容、cron 误判
2. **GRPO 训练不稳定** (9 个, 24%) — 零梯度死锁、死亡螺旋、RAGEN full-history entropy collapse
3. **SFT 格式/数据** (4 个, 11%) — 训练数据与推理框架格式不匹配
4. **奖励设计** (3 个, 8%) — format penalty 梯度劫持、dense reward gaming

**最重要的 3 个 pattern**:
1. **RAGEN full-history 是 GRPO 退化的结构性根因** — 3/3 RAGEN GRPO 一致退化，切换 step-independent 后 2 步即突破 (exp026 train 32.81%)
2. **Sparse reward + GRPO 无安全 LR 区间** — 三个量级均失败 (1e-6/5e-7/1e-7)，根因是 base success 太低
3. **AutoDL 容器硬限制不可绕过** — pids.max=20480 直接杀死 verl-agent 方案，6 次尝试 10+ GPU-h 空转

文档已写入 `artifacts/analysis/failure_taxonomy.md` 并注册 (art_20260515_5d3d32)。

---
