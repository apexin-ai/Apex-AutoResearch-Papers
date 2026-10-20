---
loop: 2
reason: max_messages
updated: '2026-05-13T23:04:36+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0 和 cuda:1（seetacloud-westb-2xpro6000 双卡 RTX 6000 Pro）
- 模型路径必须用本地绝对路径 `/root/autodl-tmp/models/Qwen/Qwen3.5-9B`，不能用 HuggingFace hub 名
- 训练脚本必须用 Jinja2 变量注入 `{%- set enable_thinking = false -%}` 禁用 thinking mode，不能用 `.replace()` hack（D006 教训）
- kill 训练进程时必须 `ps aux | grep train_grpo` 找实际 python PID，不能只 kill submit_training_job 返回的 bash wrapper PID（D1 v2/v3 同目录写入事故教训）
- eval 必须用修复后代码：enable_thinking=False + skip_special_tokens=False + max_new_tokens=1024
- relation type 映射：DyGIE++ 大写 → schema Mixed-case（DYGIEPP_TO_SCHEMA_REL_TYPE in data_utils.py）

### 2. 🖥️ 基础设施快照
- 服务器：seetacloud-westb-2xpro6000（connect.westb.seetacloud.com）+ westb-23072 备用
- 工作目录：`/root/schema-conform-ie-training/code/`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：`/root/autodl-tmp/models/Qwen/Qwen3.5-9B`（base）
- 训练输出：`/root/autodl-tmp/output/` 下 formal_A/, formal_B/, formal_D1_v4/, formal_D2_phase1/, formal_D2_phase2/, formal_A_continued/
- 数据集：SciERC（训练 1861 samples）, CrossNER politics/science（zero-shot eval）
- HF cache：`/root/autodl-tmp/.hf_cache`
- 活跃进程：**刚派了 Agent 检查，状态待确认**——eval_B_v3 (PID 110498, cuda:1) 和 eval_A_continued (cuda:0) 可能已完成
- Cron：eval_A_v3 的 cron 可能仍在，需确认清理

### 3. 📊 当前状态
刚批准 RESET_BOTH，写 handoff 中。最后一个动作是派 Agent 检查所有 eval 进程状态（GPU 利用率报低，eval 可能已完成）。

Registry 状态：
- eval_B_v3: RUNNING（可能已完成，PID 110498）
- eval_A_continued_ckpt400: RUNNING（可能已完成，PID 114668）
- eval_A_continued_final: 应在 ckpt400 后串行启动（同一 tmux session）
- exp_007_a_continued: DONE(success)，训练 500/500 完成
- 其他 11 个实验均 DONE(success)

等待中：Agent 收到检查指令（om_x100b6f647a17bca8c36ab65bd0478c1），应很快回复 eval 结果。

### 4. 📋 待办
- Agent 回复 eval 结果 → 编译八组对比表，做 MVP 最终判定（pass criteria: CrossNER entity_f1 ≥ baseline+2pp 且 A-continued ckpt400 < D2 ckpt400 证明 conformance reward 有增量价值）
- MVP PASS → complete_mvp() → 进入 research 阶段 → 执行 post-mvp-kickoff skill（写 paper_framing.md → experiment_plan.yaml → dream_simulate → update_roadmap）
- MVP FAIL（A-continued ≈ D2）→ conformance reward 无增量价值，需 pivot 或加强 reward 设计
- eval_B_v3 结果出 → 补全 B 的修复后 relation_f1 对比数据

### 5. 🎯 战略上下文
- 核心假设：GRPO + decomposed schema-conformance rewards 教模型学 schema 验证过程（非 schema 知识），实现 zero-shot IE 迁移
- 关键决策链：D006（thinking mode Jinja2 fix，最大突破）→ D008（relation type case fix）→ D010（Reviewer CONDITIONAL PASS，要求 A-continued ablation）→ D011（A relation_f1=0.181 基线修正，叙事调整）
- D2 curriculum learning（Phase1 F1-only 500步 → Phase2 F1+conformance 500步）是当前最佳方案：CrossNER entity_f1 比 A 高 +3.2pp/+3.6pp
- **最易判断错的事**：A-continued vs D2 的对比必须用 ckpt400（900 effective steps）对齐，不能用 D2 final（1000步）vs A-continued ckpt400（900步）
- **叙事调整**：修复后 A 的 relation_f1=0.181（非 0），不能再说"首次实现 non-zero relation extraction"，改为"提升 +5.7pp"
- D1 v4 relation_f1 最高（0.2913）但 CrossNER 结构退化，不适合做主推方案
- 目标：EMNLP 2026 ARR May 25 提交
