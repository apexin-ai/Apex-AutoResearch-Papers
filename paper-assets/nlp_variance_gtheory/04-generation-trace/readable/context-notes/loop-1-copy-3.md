# reviewer / loop_1.md

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`f688ef8c2132d8879514.json`](../../sessions/f6/f688ef8c2132d8879514.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-21T06:08:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-32570:{0,1,2,3}，4 张 RTX PRO 6000 Blackwell (96GB)。越界即 CRITICAL。
- Qwen 推理正在跑（PID 91484/91486/91488/91490，GPU 0-3），不要 kill 或抢占。
- REML 结果 `converged: false`（100 iter），论文引用前必须用 `--max-iter 500` 重跑确认收敛。
- 对比表引用不平衡数据数值时核对原始 JSON，Worker 报告中曾出现错误值（seed×item_id 写成 0.5% 实际 2.5%，model main 写成 3.1% 实际 0.2%）。

### 2. 🖥️ 基础设施快照
- 服务器：westd-32570，工作目录 `/root/nlp_variance_gtheory`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型缓存：`/root/autodl-tmp/.hf_cache/`（Qwen3-8B 正在从此加载）
- 数据：`/root/nlp_variance_gtheory/data/mmlu_items_exp001.json`（200 MMLU items）
- 结果目录：`/root/nlp_variance_gtheory/results/`
  - `exp001_llama/` — Llama-3.1-8B 完成 (4×64,800 = 259,200)
  - `exp001_gemma/` + `exp001_gemma_fp32/` — Gemma-2-9B 完成
  - `exp001_mistral/` — Mistral-7B 完成 (4×64,800 = 259,200)
  - `exp001_qwen/` — Qwen3-8B 进行中（shards 已生成，推理刚启动）
  - `analysis/` — 所有 G-study JSON 结果
- 活跃进程：Qwen 推理 PID 91484-91490（auto_start_qwen.sh 链式启动，13:31:42 CST）
- 本地 artifacts：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/`

### 3. 📊 当前状态
**刚完成的审查**：
1. G_item 修正计算 (cross_model_g_coefficients.json) — PASS，G_item=0.707 验证通过
2. Dataset B 平衡 G-study (dataset_b_gstudy.json) — WARNING，对比表数据有误+混淆变量
3. Dataset A 三模型 G-study (dataset_a_gstudy.json) — PASS，G_item=0.777 验证通过
4. REML 实现 (cross_model_reml.json) — WARNING，未收敛+重要推论（Henderson I 偏差很小）
5. Mistral 完成确认 — PASS，259,200 条全部完整
6. Qwen 自动链式启动确认 — 进行中

**未发 review 的**：无积压。所有已完成 Worker 均已审查并 post 给 Director。

**等待中**：
- Qwen 推理完成通知
- 可能的 REML 重跑（--max-iter 500）Worker
- 可能的 Dataset A G-study 在平衡数据上的重跑

### 4. 📋 待办
- Qwen 推理完成 → 独立核实 shard 行数（期望 4×64,800=259,200）+ GPU 设备合规 + 准确率合理性
- 4 模型 G-study 结果出来 → 核实 D-study 预测（之前预测 4-5 模型 G_item≈0.83+）是否兑现
- REML 重跑结果 → 确认收敛 + 对比 100-iter 估计是否有实质变化
- 论文章节提交审查 → 切换到审查模式 B，加载 paper-quality-lessons skill，按 5.1-5.2 维度审
- exp-001 registry 条目 → 如果仍缺失，再次提醒 Director（已提醒多次）

### 5. 🎯 战略上下文
**核心结论链**：
1. 单模型 item_id 主导方差（61.1%），G=0.611
2. 跨模型 model×item_id 交互是第二大方差源（26-32%），说明 item 难度是 model-specific 的
3. D-study 证明 n_models 是提升跨模型信度最有效的杠杆（3 模型 G≥0.78，5 模型 G≥0.84）
4. REML 验证 Henderson I 在本数据集上偏差很小——平衡 vs 不平衡的差异主要来自设计差异（温度/精度水平不同），不是估计方法偏差

**易判断错的事**：
- Dataset B (G=0.866) vs 不平衡 (G=0.707) 的差异**不是**平衡修正效果——REML 已证明 Henderson I 偏差 <0.5pp。差异来自去掉 temp=0.0 和减少 precision 水平。论文中不能将 Dataset B 的高 G 归因于"消除估计偏差"。
- G_condition (tau=fixed facets) 和 G_item (tau=item_id) 是完全不同的指标，不可并排比较。之前 Worker 曾犯过"G 从 0.611 暴跌至 0.073"的混淆。
- Worker 报告中的对比表可能有手动输入的错误数值——必须回查原始 JSON 交叉验证。


---
