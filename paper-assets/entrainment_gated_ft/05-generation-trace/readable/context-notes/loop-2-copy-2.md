# agent / loop_2.md

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`d3794febf74e992e1a78.json`](../../sessions/d3/d3794febf74e992e1a78.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: idle_timeout
updated: '2026-05-22T01:27:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westb-48145:cuda:0（gpu_ids 白名单仅此一张）
- 所有 fla 模型评估必须用 `run_lmeval_clean.py`（它注入 `allow_neg_eigval=True`，用其他 wrapper 会导致 GDN acc 偏低 ~3.3pp）
- D009 禁止 post-hoc 统计技巧：不能做 2-benchmark Bonferroni、不能做 ρ<0 子集校正
- 论文 framing 已锁定 "task-specific convergence"（LAMBADA only），不能 claim "general convergence"
- D017 sprint：May 25 ARR 截止，剩 3 天，新实验需 Director 批准
- RetNet-pure 1.3B logsamples 数据异常（全部 acc=0），cross-scale Jaccard 不可用

### 2. 🖥️ 基础设施快照
- 服务器：westb-48145，工作目录 `/root/entrainment_gated_ft/`
- Python：`/root/miniconda3/bin/python`，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 1.3B 模型：`/root/autodl-tmp/models_1.3b/`（GDN/RetNet/HGRN2 × 5 ratios + Transformer baseline，共 16）
- 340M 模型：`/root/autodl-tmp/models/`（GDN/RetNet/HGRN2 × 5 ratios + partial，共 ~16）
- 评估输出：`/root/entrainment_gated_ft/lm_eval_clean/`（按 benchmark 子目录组织）
- 分析脚本：`/root/entrainment_gated_ft/analysis/`
- 活跃进程：W3 Worker 正在 cuda:0 上跑 WinoGrande+PIQA 全模型评估（12/30 完成，~30min 剩余）
- 活跃 Worker：`worker_analysis_w3-format-confound-eval_20260521T082626`（turn 38，Monitor 中）
- Cron：无活跃 cron（已 reconcile）

### 3. 📊 当前状态
本轮完成：
- exp-boolq-hellaswag-eval 从 PREPARING 补填 hypothesis/parent/spec 后推进到 DONE(success)。4-benchmark spectrum 已入 registry：HellaSwag(α=0.10) < ARC-Easy(α=0.21) < LAMBADA(α=0.30) < BoolQ(α=0.49)
- 已向 Director 汇报 session 重启状态 + exp 关闭 + W3 进展 + Worker 池不足问题

Registry 非 DONE 实验：
- `w3-winogrande-piqa-eval` — PREPARING，W3 reviewer concern 的 WinoGrande/PIQA per-example α+Jaccard 实验，Worker 正在执行评估
- `exp-005` — PREPARING/killed（Wang zoo 无额外架构）
- `exp-003-p2v2` — PREPARING/killed（HGRN2 monkey-patch 问题）

等待中：
- W3 Worker 回调（`worker_analysis_w3-format-confound-eval_20260521T082626`）→ 拿到 WinoGrande/PIQA metrics
- Director 回复：确认 Paper Agent 写作任务是否需要 Agent 侧 spawn Worker 推进

### 4. 📋 待办
- W3 Worker 回调到达 → 读 metrics，更新 w3-winogrande-piqa-eval registry（补 hypothesis: "WinoGrande/PIQA per-example multiplicity 分析验证 format confound 不影响 multiplicity 发现"，parent=exp-011），转 DONE，汇报 Director
- W3 结果 α 与已有 4-benchmark spectrum 一致 → 更新 spectrum 为 6-benchmark，强化 "multiplicity is universal" claim
- W3 结果异常（如 α≈0 或 Jaccard 无显著性）→ 汇报 Director，可能需要排查评估脚本或 format 适配问题
- Director 回复需要 spawn Paper Agent Worker → 按指示铺写作任务
- Worker 池 < 2 → 确认 Director 指示后立即 spawn CPU Worker（文献/写作/分析）

### 5. 🎯 战略上下文
- **核心叙事**：Hybrid architectures 中 attention 产生 task-specific aggregate convergence（仅 LAMBADA）+ task-general per-example predictive multiplicity（LAMBADA α~0.30 + ARC-Easy α~0.21 + HellaSwag α~0.10 + BoolQ α~0.49）。两者 decoupled，不是 co-evolution
- **决策链**：D008（decoupling）→ D009（BCa CI 统计策略）→ D015（ARC-Easy 扩展）→ D017（May 25 sprint）→ D018（4-benchmark spectrum）→ D019（Round 5 Action Matrix 直接执行）
- **Round 5 审稿 7 个 issue**：W1(seed confound) W2(convergence prominence) W3(format confound) W4(novelty) W5(page limit) W6(refs) W7-W9(minor)。W3 是唯一需要新 GPU 实验的，其余由 Paper Agent 处理
- **易错点**：
  1. W3 的 WinoGrande/PIQA 是 per-example multiplicity 分析（α+Jaccard），不是 aggregate convergence 分析——不要混淆
  2. 统计报告必须附原始数值（ρ=X, p=Y），"majority"/"most" 必须有计数
  3. exp-boolq-hellaswag-eval 的 BoolQ GDN h24-1 acc=0.489（近随机）是真实模型表现，不是 eval bug
  4. w3-winogrande-piqa-eval 的 registry 状态仍是 PREPARING，Worker 回调后需要正确走状态机（需要 spec 含 checkpoint_source + eval_data 才能转 RUNNING）


---
