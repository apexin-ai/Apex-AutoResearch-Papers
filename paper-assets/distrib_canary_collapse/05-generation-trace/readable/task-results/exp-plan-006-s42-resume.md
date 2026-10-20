# exp plan 006 s42 resume

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_plan_006_s42_resume_20260515T115307_result.json`
- **Structured JSON:** [`0dadff5b1e145083e2d3.json`](../../sessions/0d/0dadff5b1e145083e2d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验成功启动，模型已加载到 cuda，gen_18 正在生成合成数据。

**总结**：

- **恢复方案**：方案 B — 写 `resume_plan006_s42.py` wrapper 脚本，import 原始 `iterative_train.py` 的核心函数，从 gen_17/checkpoint 加载模型恢复
- **清理**：已删除空的 gen_18 目录
- **实验状态**：`plan_006_s42_resume` 已提交 RUNNING，tmux session 运行中，PID=114844
- **日志**：`~/runs/distrib_canary_collapse/plan_006_s42_resume.log`
- **超时**：6h，预计 3 代 × ~35min + metrics ≈ 2-2.5h 完成
- **注意**：right-padding warning 是 Pythia generate 时的标准 warning，原始实验也有，不影响结果

---
