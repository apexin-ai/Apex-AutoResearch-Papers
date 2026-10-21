# agent / loop_1.md

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`bc3aa6cd7fafc1151069.json`](../../sessions/bc/bc3aa6cd7fafc1151069.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: idle_timeout
updated: '2026-05-21T08:51:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westb-48145:cuda:0（gpu_ids 白名单仅此一张）
- 所有 fla 模型评估必须用 `run_lmeval_clean.py`（它注入 `allow_neg_eigval=True`，用其他 wrapper 会导致 GDN acc 偏低 ~3.3pp）
- D009 禁止 post-hoc 统计技巧：不能做 2-benchmark Bonferroni、不能做 ρ<0 子集校正
- 论文 framing 已锁定 "task-specific convergence"（LAMBADA only），不能 claim "general convergence"
- D017 sprint：May 25 ARR 截止，纯写作冲刺，新实验需 Director 批准
- Confidence margin 分析（within-category control）已写入论文 §4.3，GDN 用 h12-1（1.3B h3-1 不可用）

### 2. 🖥️ 基础设施快照
- 服务器：westb-48145，工作目录 `/root/entrainment_gated_ft/`
- Python：`/root/miniconda3/bin/python`，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 1.3B 模型：`/root/autodl-tmp/models_1.3b/`（GDN/RetNet/HGRN2 × 5 ratios + Transformer baseline，共 16）
- 340M 模型：`/root/autodl-tmp/models/`（GDN/RetNet/HGRN2 × 5 ratios + partial，共 ~16）
- 评估输出：`/root/entrainment_gated_ft/lm_eval_clean/`（按 benchmark 子目录组织）
- 分析脚本：`/root/entrainment_gated_ft/analysis/`
- 活跃进程：无。GPU 空闲
- 活跃 Worker：`worker_analysis_exp-boolq-hellaswag-eval_20260520T124927`（刚 spawn，分析 BoolQ/HellaSwag 结果）
- Cron：已 reconcile，无活跃 cron

### 3. 📊 当前状态
收到 `exp-boolq-hellaswag-eval` 完成 cron 回调（进程正常退出）。刚 spawn Worker 去 SSH 读日志提取 metrics，**Worker 尚未返回**。

Registry 状态：
- `exp-boolq-hellaswag-eval` — PREPARING（cron 已转 ANALYZING 但 registry 未同步），跑了 `run_boolq_hellaswag_all.sh`，BoolQ+HellaSwag 全模型评估。**缺 hypothesis 和 parent 字段，需补填后才能转 DONE**
- `exp-005` — PREPARING/killed（Wang zoo 无额外架构，已终止）
- `exp-003-p2v2` — PREPARING/killed（HGRN2 monkey-patch 问题，已终止）
- 其余 16 个实验全 DONE

等待中：
- Worker `worker_analysis_exp-boolq-hellaswag-eval_20260520T124927` 回调 → 拿到 metrics 后更新 registry、汇报 Director
- D017 sprint 写作任务（W-CHECKLIST / W-OVERCLAIM / W-GENERAL / W-GDN / R3-POWER / Q1 / Q5 / W-ZOO / Author Response）— 需 Paper Agent 执行

### 4. 📋 待办
- Worker 回调到达 → 读 metrics，补 hypothesis（推荐：parent=exp-011，hypothesis="BoolQ 和 HellaSwag 的 per-example evaluation 数据用于扩展 multiplicity 分析到更多 benchmark"），更新 registry 到 DONE，汇报 Director
- 如果 BoolQ/HellaSwag 有 log_samples per-example 数据 → 可做 Jaccard/multiplicity 分析（类似 exp-015 对 ARC-Easy 的分析），但需 Director 批准（D017 锁定写作冲刺）
- D017 写作任务未完成 → 汇报 Director 后确认 Paper Agent 是否需要继续推进
- GPU 空闲 → D017 期间无需算力，但若 Director 指示新实验，westb-48145:cuda:0 可用

### 5. 🎯 战略上下文
- **核心叙事**：Hybrid architectures 中 attention 产生 task-specific aggregate convergence（仅 LAMBADA）+ task-general per-example predictive multiplicity（LAMBADA α~0.30 + ARC-Easy α~0.21）。两者 decoupled，不是 co-evolution
- **决策链关键节点**：D008（decoupling 叙事）→ D009（W1 统计策略，BCa CI 主导）→ D015（ARC-Easy 扩展 multiplicity）→ D017（May 25 deadline sprint）
- **易错点**：
  1. 不要把 BoolQ/HellaSwag aggregate 结果当新发现——exp-011 已做过且 negative。本次实验的价值在于是否有 per-example log_samples 数据可做 multiplicity 分析
  2. 统计报告必须附原始数值（ρ=X, p=Y），"majority"/"most" 必须有计数（Director 硬约束）
  3. RetNet-pure 1.3B logsamples 数据异常（全部 acc=0），cross-scale Jaccard 不可用——不要尝试用这个数据
  4. exp-boolq-hellaswag-eval 的 registry 状态仍是 PREPARING，需要先正确更新（可能需要补 spec 字段才能转 RUNNING → DONE）


---
