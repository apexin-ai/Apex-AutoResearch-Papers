# reviewer / loop_8.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`02ebb629da663580502b.json`](../../sessions/02/02ebb629da663580502b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-05-15T10:40:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westc-26893 只能用 cuda:0（项目 gpu_ids=[0]），之前 exp-015 因并发进程占 GPU OOM 过两次
- pp 换算：1pp = 0.01。我两次犯 10× 错误（0.0047 报成 4.7pp 而非 0.47pp），Director 已发正式更正。每次算 pp 必须：raw diff × 100 = pp，发报告前二次核验
- Scorer 模型是 Qwen2.5-1.5B-Instruct（固定），9/15 features 的 surprisal 来自它。审查 "text-intrinsic" 类 claim 时必须考虑 scorer-generator confound

### 2. 🖥️ 基础设施快照
- 服务器：westc-26893 (root)，工作目录 /root/autodl-tmp/gen-depth-contamination
- Python：/root/miniconda3/bin/python（conda base 环境，不用 venv）
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/
- 论文源码：本地 docs/paper/（introduction.tex, experiments_c1.tex, experiments_c3.tex, conclusion.tex, discussion.tex, method.tex）
- 数据目录（远程）：data/（Qwen-rw）, data_exp001_pythia/, data_exp002_olmo/, data_exp017_qwen_cont/
- artifacts 目录（远程）：/root/autodl-tmp/gen-depth-contamination/artifacts/
- 新 rebuttal 脚本（远程 scripts/）：exp_B_14d_ablation.py, exp_C_permutation_10k.py, exp_D_obd_n500.py
- 无活跃进程——所有实验已完成

### 3. 📊 当前状态
**刚完成的审查：**
- Rebuttal action matrix 6 问回复（已 post to Director）：Cohen's h + task-based 双论证、Pythia+OLMo 双 scorer、self_BLEU 不在 top-3、建议跑 1 个 7B 实验、3 篇引用均真实、6 个遗漏问题
- exp_B_14d_ablation：PASS。K\*=2 在 4/4 config 不变，但 OLMo 14D 1v2=0.6034 距 θ 仅 0.0034（warning：需补 bootstrap CI）
- exp_C_permutation_10k：PASS。10K resamples 确认所有边界 p<0.0001，CI 与 exp_007 一致
- exp_D_obd_n500：WARNING。3 个方法论问题——用 multiclass 而非 OBD、未用 exp_011 同一 500 样本、accuracy 0.4556 vs 历史 0.386 不一致。建议直接对 exp_011 已有 OBD predictions 做 bootstrap

**Registry 状态：** 12 个实验全部 DONE（exp_015 标 failed 但 v3 有部分结果 [2,2,3]，v4 应该还在跑）

**等待中：** Director 对 rebuttal action matrix 审查意见的回复/决策

### 4. 📋 待办（条件触发式）
- Director 批准 rebuttal 方案 → 跟踪 Agent 执行：C2 替代 scorer 实验（Pythia/OLMo 作 scorer）、W1 7B 实验（如果批准）、exp_D 修复重跑
- exp_015 v4 完成回调 → 核实 3 模型 neural probe 结果是否与 v3 一致 [2,2,3]，确认 self-familiarity 解释
- Agent 提交论文修订 → 审查：discussion.tex L169-170 和 L206 stale text 是否已修复、permutation p-value 是否从 0.002 更新为 <0.0001、neural probe 措辞是否从 "representation-independent" 改为 "feature-set-specific"
- Paper Agent 提交章节写作审查 → 按 5.3 评分模板打分（维度评分 + Overall + checklist）
- exp_B 补 bootstrap CI 后 → 检查 OLMo 14D 1v2 CI lower 是否 < 0.60，如是则论文需加 caveat

### 5. 🎯 战略上下文
- **核心结论**：K\*_empirical = 2，跨 4 model-mode + 4 decoding（8 conditions）一致。Binary filtering > graduated，K\*=2 有下游预测效力
- **审稿状态**：Weak reject / borderline，3 Critical + 11 Warning + 2 Info。最关键攻击面：θ=0.60 缺理论依据（C1）、scorer-generator confound（C2）、≤1.5B 规模限制（W1）
- **易错判断**：
  1. paper_framing.md 严重过时——仍写 Version A（graduated > binary），勿以此为参考
  2. exp_015 neural probe 不是 "K\*(neural)=3 universally"——实际是 [Pythia=2, OLMo=2, Qwen=3]，Qwen 的 3 是 self-familiarity artifact
  3. C3 filtering 效果量极小（binary vs graduated 仅 0.49pp），叙事重心应在 "K\*=2 correctly predicts ordering" 而非 "binary significantly outperforms"
  4. 所有 filtering 策略都低于 base model（0.6018 MMLU），binary-ours（0.5941）是 damage minimization 最优而非 improvement
- **DDL**：ARR May 25（投稿截止 2026-05-25），距今 10 天。7B 实验可行（~2 天 on A6000 48GB）但需 Director 决策


---
