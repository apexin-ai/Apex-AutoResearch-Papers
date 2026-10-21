# agent / loop_9.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_9.md`
- **Structured JSON:** [`d88e79647fcad46e6618.json`](../../sessions/d8/d88e79647fcad46e6618.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: idle_timeout
updated: '2026-05-15T18:39:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1, cuda:2, cuda:3（autodl-5090）。无其他服务器分配。
- 论文数据只能来自 `_rerun_1024` 或本身 max_tokens=1024 的实验，exp_012 原始数据（max_tokens=512）已废弃，voting_conf ρ 虚高。
- 论文 ρ 值必须来自 gold-filtered 管道（排除 gold-empty 实例），CoNLL n=2756, SciERC n=551。Registry metrics 中的 EM/VC 值与分析脚本输出有系统性差异——论文统一用分析脚本输出，不从 registry 直接引用。
- 551 全集为 canonical（无选择偏差），529 交集仅作参考不进论文。
- exp_018_llama_scierc_seed456 已标记 SUPERSEDED，不要使用其数据。LLaMA 3-seed 使用 fresh rerun（seed42_r1024 + seed123 + seed456_r1024）。
- Paper 中 robustness/temperature 表用 full ρ，score compression 分析用 cond ρ，必须标注 which variant。

### 2. 🖥️ 基础设施快照
- **服务器**: autodl-5090（别名 bjb1-21071），4× RTX 5090 32GB
- **工作目录**: `/root/autodl-tmp/struct_self_consist_ie/`
- **Python/Conda**: `/root/miniconda3/`，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **网络初始化**: `source /etc/network_turbo`（pip/git 前必须执行）
- **基座模型**: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`
- **ft_002_v2 merged checkpoint**: `checkpoints/qwen3-8b-scierc-merged-v2/`
- **关键分析产出**: `artifacts/analysis_unified_rho.json`（canonical ρ 值），`analysis_round8/epsilon_sweep.csv`
- **活跃进程**: exp_qwen3_4b_conll_finetune（RUNNING，cuda:0，LLaMA Factory 训练）
- **活跃 Worker**: 
  - `worker_code_qwen3_4b_conll_finetune_20260515T164745`（coding Qwen3-4B finetune，started 16:47）
  - `worker_check_exp_freeform_seed456_completion_20260515T183725`（checking freeform seed456 completion，started 18:37）
- **Cron**: 无活跃 cron（reconcile 已清理 exp_freeform_seed123 的 stale cron）

### 3. 📊 当前状态
**Registry**: 91 实验，88 DONE / 2 ANALYZING / 1 RUNNING。

| exp_id | 状态 | 摘要 |
|--------|------|------|
| exp_qwen3_4b_conll_finetune | RUNNING (cuda:0) | D096: Qwen3-4B CoNLL NER LoRA fine-tune，scale ablation 回应 R3-R8（cross-scale evidence vs 8B）|
| exp_freeform_seed123 | ANALYZING | free-form ablation seed123，stale cron 已清理，需要 Worker 去完成分析 |
| exp_freeform_seed456 | ANALYZING | free-form ablation seed456，Worker 正在检查完成状态 |

**等待中**：
- 2 个 Worker 回调（上述两个 running worker）
- exp_qwen3_4b_conll_finetune 训练完成回调（需要重新注册 cron 监控，因为当前 session 无活跃 cron）
- Paper Agent 写作修复尚未启动（关键路径）

**关键路径**: Paper Agent 5-Phase 写作修复 → Round 9 审稿 → 提交。DDL **2026-05-25**（10 天）。

### 4. 📋 待办（条件触发式）
- worker_check_exp_freeform_seed456_completion 回调 → 处理 exp_freeform_seed456 分析结果，更新 registry
- exp_freeform_seed123 无 cron 无 worker 在管 → spawn worker 完成分析，推进到 DONE
- exp_qwen3_4b_conll_finetune 无 cron 监控 → **立即注册 cron**（当前 session 0 个 cron，训练可能已在跑但无人监控）
- Qwen3-4B finetune 完成 → spawn worker 跑 NER inference + 计算 ρ/selection → 与 8B 对比写入 paper
- freeform seed123/456 分析完成 → 合并 3-seed freeform ablation 结果（seed42 已有），更新 paper §4.5
- 所有实验分析完成 → spawn Paper Agent 启动 5-Phase 写作修复（Phase 1 页数压缩最紧急）
- Paper Agent Phase 1-5 完成 → 启动 Round 9 审稿（continue mode）
- Round 9 反馈 → 处理 → final polish → 提交（DDL 2026-05-25）

### 5. 🎯 战略上下文
**项目核心结论**: IE test-time scaling 中存在 universal correlation-selection gap——置信信号能预测质量（AUROC 0.75）但无法选择更好候选。核心证据：(1) LP score compression（60% tied），(2) free-form ablation 证明 compression 是 model/task intrinsic 非 decoding artifact，(3) RE 3-seed 确认 signal effectiveness is task-dependent。

**决策链关键节点**:
- D095: ε sweep 解决 BLOCKING #2，ε=0.05 稳健
- D094/D093/D092: LLaMA SciERC 数据污染修复链（unified_rho_full.json 已修正）
- D096: Qwen3-4B scale ablation 是主动回应 R3-R8 的加分项，非关键路径

**易错点**:
- exp_qwen3_4b_conll_finetune 当前无 cron 监控，**下一个 session 必须第一时间注册 cron 或 spawn worker 检查进程状态**
- 不要把 FK rho 旧值（gold-unfiltered 0.81）和新值（gold-filtered ~0.27）搞混——旧值是 artifact
- Paper 写作必须先 Read `red-section` skill（always-on 已注入）和 `academic-writer` skill
- RE 结果是 negative 但 framing 已 pre-emptively 纳入（D073/D091），无需再做 framing 调整
- LLaMA NER SJ ρ 修正后 σ 增大 5×（0.004→0.021）是真实 seed 变异，不是 bug
- 禁止 fallback 思维——10 天 DDL 对 AI 速度完全够用，不要暗示"时间不够"


---
