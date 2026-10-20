# agent / loop_6.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_6.md`
- **Structured JSON:** [`fa527e59d9449e39e063.json`](../../sessions/fa/fa527e59d9449e39e063.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: idle_timeout
updated: '2026-05-14T22:50:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westd-16980 的 cuda:0 和 cuda:1（gpu_ids=[0,1]），其他设备号/服务器绝对不碰
- F1 计算必须用 **all_set** method（OOV predictions 算入 denominator），之前用 recognized_set 被 Reviewer 打回过（D012/D013）
- checker 版本必须是 **fixed_20260514_v2 (strip + alias + unique_et)**，v1 有 ET triple-counting bug（D011）
- submit_training_job 命令必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，裸 python3 会 command not found（phase2_scierc_full_s1 踩过两次）
- 论文数字必须从 registry metrics 追溯，不可凭记忆写

### 2. 🖥️ 基础设施快照
- 服务器：westd-16980，account: root，项目路径 /root/schema_semantic_constrained_ie
- Python：/root/miniconda3/bin/python3（通过 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base` 激活）
- 模型：Qwen3-8B → /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B；Llama-3.1-8B-Instruct → /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct
- 数据：SciERC → data/processed_data/test.json (551 docs)；DocRED → data/docred/dev.json (998 docs)
- 约束文件：SciERC → ontology_constraints.json；DocRED → data/docred/ontology_constraints_docred.json
- 输出目录：outputs/（所有 .jsonl 结果文件）
- 活跃进程：llama_docred_full_s1 (PID 194295, tmux session, cuda:0)，已运行约 5 小时
- W&B：未使用（本项目用本地 checker 评估，不走 W&B）

### 3. 📊 当前状态
**刚做完**：收到 llama_docred_unconstrained 完成回调（CRON → ANALYZING），已派 Worker `analysis:llama_docred_unconstrained` 去 SSH 读日志 + 跑 checker 获取 metrics。同时派了 `check:llama_docred_full_s1_progress` 查进度。

**两个 Worker 回调未到**：
1. `worker_analysis_llama_docred_unconstrained_20260514T194008` — 分析 Llama DocRED unconstrained 的 violation + F1 指标
2. `worker_check_llama_docred_full_s1_progress_20260514T194059` — 检查 Llama DocRED full_s1 进度/ETA

**Registry 状态**：
- `llama_docred_unconstrained` — ANALYZING，等 Worker 返回 metrics 后推到 DONE
- `llama_docred_full_s1` — RUNNING on cuda:0 (PID 194295)，DocRED 998 docs + Llama + full_s1 约束，预计总时长 ~5-6h
- 其余 18 个实验全部 DONE（17 success + 1 killed）

**cuda:1 空闲**——llama_docred_unconstrained 跑完释放了，目前无新 GPU 实验可排。

### 4. 📋 待办（条件触发式）
- Worker `analysis:llama_docred_unconstrained` 回调 → 用返回的 metrics 调 `update_registry(status=DONE, conclusion=success/negative, metrics=...)` + 设 checkpoint_path/log_path → 对比 Qwen3-8B DocRED unconstrained（DR 18.5%, R-F1 7.74%）→ 更新 report.md → 向 Director 汇报
- Worker `check:llama_docred_full_s1_progress` 回调 → 确认进度正常，估算 ETA，记录到 notes
- `llama_docred_full_s1` CRON 完成回调 → 派 Worker 分析（同上流程）→ 与 Qwen3-8B DocRED full_s1（DR 10.19%, R-F1 8.23%）对比 → 这是 cross-model 验证最后一个数据点
- **两个 Llama DocRED 都 DONE 后** → 派 Worker 写 §5 Cross-model 子节（Llama vs Qwen 在两个数据集上的 violation + F1 对比表）→ 这是 ROADMAP 里的近期任务
- **所有实验完成后** → Discussion 段落补充（低 F1 实际意义、CF severity、fallback frequency、post-hoc 对比）→ May 19 内部稿目标

### 5. 🎯 战略上下文
**核心结论**：OntoCoDec（grammar + semantic 两层约束解码）近完全消除 LLM IE 的本体违规，F1 中性到正向（SciERC neutral p=0.58, DocRED +0.50pp p<0.001）。

**决策链关键节点**：
- D012: Bootstrap CI 确认 SciERC F1 neutral, DocRED F1 显著提升
- D013: Post-hoc baseline framing = 不争 F1，多维对比（recall/coverage/operational）
- D011: ET 计数 v1→v2 修复（去重），所有实验已用 v2 重跑
- D007: S2 降级为架构 ablation，S1 为主推策略

**易错点**：
- Llama IE 质量显著弱于 Qwen（SciERC R-F1 2.54% vs 8.36%），但约束合规性反而更好（Llama DR 0.08% vs Qwen 0.93%）——这不是 bug，是 Llama 保守提取的特性，论文应 claim "model-agnostic compliance" 而非 "model-agnostic F1"
- DocRED grammar_only DR 反而上升（18.46→26.17%）——grammar 强制 valid relation name 后 entity type 与新 relation domain/range 不匹配加剧，恰好证明 semantic 层必要性。这是审稿必问点，已有 framing 准备
- CF (cross-field consistency) violations 在 constrained 模式下反而升高（特别是 Llama），这是 checker 设计问题而非方法缺陷——Discussion 段落需要解释
- cuda:1 当前空闲，但没有新 GPU 实验要跑——如果 Director 问为什么空着，答案是"Llama cross-model 矩阵的最后一格在 cuda:0 跑，全部实验已覆盖"


---
