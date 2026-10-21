# agent / loop_12.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_12.md`
- **Structured JSON:** [`5816a06cf83507d220b1.json`](../../sessions/58/5816a06cf83507d220b1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: idle_timeout
updated: '2026-05-16T04:12:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-5090 上 cuda:0/1/2/3，不得用其他服务器的 GPU（历史服务器 autodl-4x5090, gpu-5090-4x-2 已过期）
- **论文 ρ 值只能来自 gold-filtered 管道**（`rho_audit.py` 或 bootstrap CI 脚本），禁止直接引用 registry metrics（report.json 的 EM/VC 值与分析脚本存在系统性差异，D066 已确认）
- SciERC 数据集 **551 全集为 canonical**（无选择偏差），529 交集仅作参考不进论文
- exp_012 是唯一 max_tokens=512 的实验，voting_conf ρ 虚高——论文数据必须来自 _rerun_1024 或本身就用 1024 的实验
- 20% gold-empty 实例曾导致 FK ρ 膨胀 0.48→0.81、SJ ρ 压低——**永远排除 gold-empty**

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090（别名 bjb1-21071），4× RTX 5090 32GB，**全部空闲**
- 工作目录：`/root/autodl-tmp/struct_self_consist_ie/`
- Python：`/root/miniconda3/bin/python`，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 网络加速：`source /etc/network_turbo`（pip/HF 前必须执行）
- 基座模型：`/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`
- ft merged checkpoint：`checkpoints/qwen3-8b-scierc-merged-v2/`
- Canonical 分析数据：`artifacts/analysis_unified_rho.json`
- 活跃进程：无（0 running workers, 0 active crons, 0 tmux sessions）

### 3. 📊 当前状态
全部 107 个实验已完成（success 60 / negative 23 / failed 4 / killed 20）。无 RUNNING/PREPARING 实验。

**刚完成的最后一批**（2026-05-16）：
- `exp_llama3b_scierc_ablation` — success, LLaMA 3.2-3B cross-family gap 确认，2 family × 2 scale 矩阵完整
- `exp_verbalized_confidence` — negative（有价值），overconfident 8.58/10，强化 compression-is-general 论点
- `exp_freeform_conll_4seed` — success, LP 压缩跨数据集确认（median=0.058）

**当前关键路径**：Paper Agent 正在整合这 3 组实验数据进论文 → Round 10 审稿 → Final polish → 提交（DDL: 2026-05-25, 9 天）。Round 9 审稿 19 issues 中 15 resolved, 4 in_progress（orphan bib + 3 minor formatting）。

无等待中的 Worker 回调 / Cron / Director 决策。

### 4. 📋 待办（条件触发式）
- Paper Agent 整合完成 → 提交 Round 10 审稿（continue mode）
- Round 10 审稿反馈到达 → 按 issue 分派 Worker 处理，预计 1-2d
- Round 10 要求补充实验 → autodl-5090 4 卡待命，可立即启动
- DDL 前 2 天（2026-05-23）→ final polish + 格式检查 + reference-audit
- 如果 Paper Agent 未在今天内完成整合 → 升级给 Director

### 5. 🎯 战略上下文
**核心结论**：universal correlation-selection gap——结构一致性信号（SJ/FK/VC）与质量高度相关但选择效果差，LP 相关弱但选择效果最稳定。Controlled ablation（free-form + VerbConf + temperature + scale）证明 score compression 是 model/task intrinsic，非 decoding artifact。

**决策链关键节点**：
- D066: LLaMA fresh rerun，修正了 σ 5× 增大的 seed 变异
- D098: 4B scale ablation 完成，gap 与 model capacity 无关
- D100: Table 4 SciERC 8B 统一为 v2 checkpoint
- D103: 撤回 D102，Table 4 CoNLL 4B 原值确认正确

**易踩的坑**：
- 不要把 registry metrics 的 EM/VC 值直接写进论文（LLaMA 数据 report.json 与分析脚本有系统差异）
- RE 上所有结构信号 selection F1 低于 greedy，这是 feature 不是 bug——强化 gap-is-universal 论点
- Verbalized confidence 是 negative 但已被 paper_framing 吸收为 "compression is general" 的证据，不需要 framing 调整
- Round 9 的 "by construction" reframe 是核心叙事策略——instance-level failure 不是 weakness 而是 definitional consequence


---
