# research experiment failure analysis

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_experiment_failure_analysis_20260515T114729_result.json`
- **Structured JSON:** [`d72401f1c86172b1eec9.json`](../../sessions/d7/d72401f1c86172b1eec9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文档已生成并注册。核心发现：

**50 个实验，3 个成功（6%），GPU 有效利用率仅 14%。**

失败分布：
- **Infrastructure 40%**（磁盘满、Ray OOM、cgroup 限制、cron 误报）
- **Algorithm Design 23%**（sparse 冷启动、reward gaming、full-history 退化）
- **Format/Environment 23%**（SFT/RAGEN 格式不匹配是单一最大教训）
- **Hyperparameters 11%**（LR/KL 的可行窗口极窄）
- **Framework 9%**（RAGEN 结构性限制 + verl-agent 容器不兼容）

最关键的已证伪路线：**RAGEN 全历史 GRPO 3/3 退化**，根因是 context 爆炸而非超参。exp026 的 step-independent rollout 是目前唯一未被证伪的 RL 路线。

---
