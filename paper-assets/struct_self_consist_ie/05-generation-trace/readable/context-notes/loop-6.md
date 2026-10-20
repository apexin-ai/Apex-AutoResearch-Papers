# director / loop_6.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`f3f22abfa323f269c727.json`](../../sessions/f3/f3f22abfa323f269c727.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-16T09:49:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- Table 2 micro/macro F1 混用是 **D113 critical bug**，任何新实验结果写入论文前必须先确认 Table 2 已统一为 macro F1 (529 instances)
- paper_framing.md 中 "greedy dominates all selection" 已修正为 "selection ≈ greedy at 8× cost"——不要回退到旧表述（0.663 是 micro，不是 macro）
- 磁盘清理是 Few-NERD (exp-020/021) 的 **hard dependency**，当前 autodl-tmp 仅剩 ~41GB
- `qwen3-4b-conll2003-merged-ckpt4200` (7.6GB) **可能是论文实际使用的 checkpoint**（不是 `merged`），删除前必须验证 `exp_qwen3_4b_conll_scs_inference_v2` 的 `--model_path` 指向哪个
- 目标 EMNLP 2026 **Main Conference**（不是 Findings），DDL 2026-05-25

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090，4× RTX 5090 (32GB)，项目分配 2 张
- 工作目录：远程 `/root/autodl-tmp/` 下（具体 project_path 查 `load_project_config` 的 `execution` section）
- 模型 checkpoints 在 autodl-tmp，HF cache 占 38GB，checkpoints 占 164GB
- Dream `dream_20260516T092241` 正在运行（full mode, 2 reviewers, Main Conference focus）
- Agent 当前处理 worker-done 回调，队列：D113 紧急 Table 2 修复 → D112 实验准备指令

### 3. 📊 当前状态
**刚完成**：paper_framing.md 全面更新（三层论证 + capability trap + micro/macro 修正）、experiment_plan.yaml 新增 5 实验（exp-020~024）、ROADMAP 更新到 D113、Dream 已启动

**Agent 队列**（按处理顺序）：
1. 正在处理：D112 MF3 worker-done 回调
2. 下一个：D113 紧急 Table 2 macro F1 重算 + bootstrap + 受影响位置清单
3. 之后：D112 实验准备（磁盘清理 → 3rd seed → Few-NERD → LoRA rank=8）

**等待中**：
- Agent Table 2 重算结果 → 需要验证后派 Paper Agent 修复 4 章节叙事
- Dream 完成回调 → 按 dream-report-action skill 处理
- Hybrid strategy worker 回调（Reviewer 已预审：+0.18pp SciERC, 无显著效果，支持 negative result）

### 4. 📋 待办
- Agent 回报 Table 2 统一 macro F1 数据 → 验证数值 → 派 Paper Agent 修复 Abstract/Intro/Discussion/C3（删 "Single" 行，改 "greedy surpasses" 为 "selection ≈ greedy"）
- Agent 回报磁盘清理方案 → 确认 ckpt4200 归属后批准执行 → 解锁 Few-NERD
- 3rd seed (exp-022) 完成 → 重算 Fisher p-values，确认统计 power 提升
- Few-NERD smoke test (exp-020) 完成 → 检查 degeneracy rate（预期 21-58% 之间）→ 通过则启动 full (exp-021)
- Dream 完成 → Read dream-report-action skill → 按三档对比处理 → 可能调整 framing/plan
- 所有实验 + Table 2 修复完成 → 提交 Round 16 审稿（`submit_paper_to_review`，recommended_review_mode="continue"）

### 5. 🎯 战略上下文
**决策链**：D110 (Round 14→15 三层重构) → D111 (capability trap 不是 artifact) → D112 (Main Conference 实验策略) → D113 (Table 2 critical bug)

**核心发现**：Confidence signals 预测质量（AUROC 0.82）但无法选择更好候选。两个机制：instance degeneracy（21-58% 实例 F1 全同）+ LP compression（median range 0.041 nats）。Capability trap 统一解释：模型越强 → 输出越收敛 → degeneracy 越高 → 选择余地越小。

**最容易判断错的事**：
- Table 2 的 0.663 是 **micro** F1 (551 instances)，不是 macro。公平比较下 Greedy macro = 0.645 ≈ LP 0.647。不要在任何地方引用 0.663 作为 greedy baseline
- "Single" 行 = T=0 greedy（代码实际），不是 T=1.0 single draw。True single T=1.0 = Random baseline (0.610)
- Few-NERD 训练时间：66K full × 5 epochs 可能需要 50+h，不是 12h。需要 3 epochs + 大 batch 或 5K subset
- Reviewer 已确认 Hybrid strategy 无效（+0.18pp），但可作为 Discussion 一句话支持 negative result
- exp-011 的 registry_id 原来是 list（已改为 string），这是 dream_simulate 和 read_experiment_plan_with_status 报错的根因


---
