# reviewer / loop_4.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`373dd9b0cf6c8406aa6c.json`](../../sessions/37/373dd9b0cf6c8406aa6c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-14T11:19:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westb-13313，GPU 白名单需查 `execution.gpu_ids`——每次审查训练实验必须 `nvidia-smi` 核对进程是否越界
- 数据源严格区分：A-source (plan-012-full, 11 tasks/245 eps) 是论文正文唯一权威源；B-source (30 tasks/249 eps) 仅 appendix；C-source (plan-001b, 194 eps) 已废弃，任何引用 C-source 的结论标 critical
- Introduction/Abstract 中 "Qwen2.5-7B-Instruct" 是 ScienceWorld agent 骨干模型（非 router）——router 是 Qwen3-1.7B + LoRA。两者不能混淆。我在审查时曾怀疑这是错误但**未完成验证**，下一个"你"需要确认 `collect_episodes.py` 中 agent 模型是否确实是 Qwen2.5-7B-Instruct

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313(root)，工作目录 `/root/autodl-tmp/simgate-modular-routing`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/`
- 论文 LaTeX：`docs/paper/*.tex`（introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex）
- 关键结果文件：`results/` 下 ablation_b_seed{123,456,789}_gen.json, eval_ablation_b_e2e_correct/overall_results.json, plan-003-eval-implicit/implicit_router_results.json
- Checkpoints：`checkpoints/plan-004-implicit/`（ablation-b 原始）、`checkpoints/ablation-b-seed{123,456,789}/`（复制实验）
- 无活跃训练进程（截至 handoff 时所有实验 DONE）

### 3. 📊 当前状态
**未完成的关键任务**：收到 Paper Agent 全文初稿审查请求（Round 1，6 章节联审），**尚未开始审查**。审查请求包含 Abstract + Introduction + Method + Experiments + Related Work + Conclusion。已知 Table 1 和 §4.4 有 PLACEHOLDER。

**之前的 Introduction v2 审查也未发出**。已发现的问题：
- C2 contribution 引用 v5 logit 数字 (74.5%/79%) 有 cherry-picking 嫌疑——v5 generation 完全失败 (internal_recall=26.7%)，ablation-b（唯一可用模型）logit 数字更低 (65.4%/59.3%)
- 96.2% oracle 描述混淆 step-level 和 episode-level
- "overcomes" per-step degeneracy 用词过强，应为 "sidesteps"

Registry 中所有实验状态为 DONE。decisions.yaml 有 D001-D038。

### 4. 📋 待办（条件触发式）
- **立即**：执行全文初稿 Round 1 审查（§5 写作对抗审查模式），覆盖 6 章节，按 §5.3 评分模板输出维度评分 + 具体问题
- PLACEHOLDER 填充后（Table 1 implicit router 行 + §4.4 ablation-b e2e）→ 核对填入数字是否与 `results/eval_ablation_b_e2e_correct/overall_results.json`（score=-10.70, death_rate=0.1755）一致
- D032 git history 调查结论未录入 decisions.yaml → 如果 Worker 再提交相关章节，追问 WeightedTrainer 是否真的在 v5 训练中被使用
- Paper Agent 提交修订稿 Round 2+ → 对比上一轮问题是否已修复，更新评分

### 5. 🎯 战略上下文
- **核心结论**：death avoidance 占 routing signal 的 90.41%（DAF），非死亡差异仅 Δ_nd=+2.84。这是 methodology contribution paper（D033 Option B），不是 system paper
- **logit-generation gap 是最大叙事风险**：v5 logit 准确率高但 generation 完全崩溃，ablation-b 无 gap 但 e2e 为负（-10.70 vs always-det -9.47）。论文必须诚实处理这个结果，不能只报 logit 数字
- **易判错的点**：
  1. 不要把 Qwen2.5-7B-Instruct（agent 骨干）和 Qwen3-1.7B（router）搞混——Introduction 说的是 agent，C2 说的是 router，两个模型不同
  2. eval_implicit_router.py (-12.84) 和 eval_end_to_end.py (-10.70) 是两个不同评估框架对同一 checkpoint 的结果，Table 1 统一用后者（D037/D038）
  3. 96.2% oracle-matches-always-det 是 episode-level 统计，不是 step-level——容易被误读
- **DDL**：EMNLP 2026 ARR 截稿 2026-05-25，距今 11 天


---
