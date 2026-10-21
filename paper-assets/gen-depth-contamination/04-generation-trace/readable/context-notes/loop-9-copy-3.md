# reviewer / loop_9.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`c86bc1ee7b6903eaf530.json`](../../sessions/c8/c86bc1ee7b6903eaf530.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-15T15:07:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:0**（gpu_ids=[0]），westc-26893 上只有 1 张 RTX 4090D 24GB
- exp-004（Qwen2.5-7B）正在占用 cuda:0，不可启动其他 GPU 任务直到完成
- K* 定义必须用 **CI lower bound ≥ θ**（D033），不是 mean AUC。之前图脚本用 mean AUC 导致 critical 被打回过
- Holm-Bonferroni 修复后 MMLU 显著对数是 **8/15**（非旧值 10/15），论文中 4 处已标记需改但可能尚未全部改完
- exp-004 用的是 Qwen2.5-7B **BASE**（非 Instruct），D032 决策确认不重启

### 2. 🖥️ 基础设施快照
- 服务器：**westc-26893(root)**，工作目录 `/root/autodl-tmp/gen-depth-contamination`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型缓存：`/root/autodl-tmp/.hf_cache/`（Qwen2.5-7B 14.5GB, Qwen2.5-1.5B-Instruct, Pythia-1.4B, OLMo-1B）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/`
- 论文：`docs/paper/`（本地），远程也有残留旧版——**论文真源在本地**
- 活跃进程：exp-004 生成脚本 `run_exp004_qwen7b_depth.py`（nohup，日志 `exp004_run.log`，在 depth 1 ~80%，~6.4s/batch）

### 3. 📊 当前状态
**刚完成**：批量审查 6 项积压（K* θ 图 CI 修复 ×3 轮、exp-004/exp-012 分析脚本、appendix layout）+ EXP-E Holm-Bonferroni 修复审查 + ROADMAP 审查 + Claim 强度评估。

**Registry**：
- `exp_004_7b_crossscale`：**RUNNING**，depth 1 ~80%，ETA ~05-16 06:00 UTC
- `exp_012_binary_confidence`：**PREPARING**，排队等 exp-004 完成后启动

**无等待中的 Worker 回调或 Director 决策。**

### 4. 📋 待办（条件触发式）
- **exp-004 完成通知到达** → 立即用 `ssh_read_only` 读 `artifacts/exp004_7b_analysis.json`，核验：(1) K* 是否 =2，(2) pairwise AUC 与 1.5B baseline 对比，(3) paired difference test 是否显著。如果 K*≠2，**立即 critical** 通知 Director 调整 universality claim
- **exp-012 完成通知到达** → 核验 PPL-as-classifier 的 pairwise AUC 是否低于 OBD-15D（负面结果预期），hardcoded baselines 已验证与 registry 一致
- **Paper Agent 提交章节审查** → 按 §5 模板评分，重点检查 4 处 "10/15→8/15" 是否已更新
- **论文全文 submit_paper_to_review 触发** → 做全文一致性审查（数字、引用、图表）

### 5. 🎯 战略上下文
- **核心结论**：K*=2 across 8 conditions at ≤1.5B scale，binary-ours filtering 最优
- **2+1 claim 结构**：C1'（K* characterization + universality）+ C3（filtering application）+ supporting analysis（D012）
- **Claim 校准已评估**：当前 "characterization" + "suggesting universality" 是证据上限，**不应升级**为 "universal law"。理由：cross-scorer K*=1 反例 + neural probe K*=3 model-dependence + ≤1.5B scale limitation
- **exp-004 是决定性实验**：7B K*=2 → universality 叙事大幅加固；7B K*≠2 → 需要调整 claim scope。在结果出来前任何 claim 升级都 premature
- **易踩的坑**：(1) 论文真源在本地 `docs/paper/`，远程有残留旧版，审查 "worker 未修改" 前必须两边都读；(2) ci_half 字典是 Panel A 误差棒用的装饰值，K*(θ) 计算必须用 `ci_lower` 字典（已修复但容易回滚）；(3) pp 单位：1pp = 0.01，历史上犯过 10× 错误


---
