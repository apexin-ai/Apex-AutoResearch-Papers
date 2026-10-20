# director / loop_5.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`02ec8f1f122ecc04e35d.json`](../../sessions/02/02ec8f1f122ecc04e35d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-14T17:13:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westd-47453 的 cuda:0-3（4× RTX 6000 Pro 96G），不可用其他服务器的 GPU
- 输出目录必须在数据盘（根分区 30GB，D008 教训），模型/数据/checkpoint 放 /root/autodl-tmp/ 或数据盘
- adaptive_fix 实验（3 seeds）是 MVP 关键路径，GPU 释放后优先级高于 grid-b seed456 系列
- 不要比较 v1 adaptive（n_min=3）和 v2 adaptive（n_min=2）作为单变量实验——D016 确认存在混淆变量风险

### 2. 🖥️ 基础设施快照
- 服务器：westd-47453 (connect.westd.seetacloud.com)，用户 root
- 工作目录：/root/provenance_weight_training
- Git：未配置（远程可能无 git history，D016 调查需注意）
- W&B：未配置
- 数据：132M tokens 合成数据已生成（datagen_synthetic_4gpu DONE）
- 检测器：TF-IDF bigrams + LR（AUC=0.939, ECE=0.048）
- 活跃进程：adaptive_fix_seed42/seed123/seed456 三组在跑（具体 PID/tmux 需 Agent 确认）

### 3. 📊 当前状态
**刚处理完**：Reviewer 的 b*=20.0 硬上限影响评估报告，记录 D015（ceiling hit 不阻塞 MVP）和 D016（v1→v2 混淆变量）。

**RUNNING**：adaptive_fix_seed42/123/456（D012 修复版，n_min=2）— MVP 判定依赖这三组结果
**QUEUED**：grid_b seed456 全 6 值、detector_modernbert（已废弃但未清理）
**PREPARING**：adaptive_v2_seed42/123/456（可能与 adaptive_fix 重复，需确认是否同一组）

**Agent 状态**：正在处理 method draft 修正的 worker 回调，队列中有 D016 调查任务（检查 alpha_eff.py git history 确认变更范围）。

### 4. 📋 待办
- Agent 完成 D016 调查 → 如果确认 early return 是 D012 新增：更新 method draft 描述 v2 为"修正版算法"而非"仅 n_min 调整"；如果 early return 本就存在：记录确认，无需改叙述
- adaptive_fix 三组完成 → 汇总 eval_ppl，与 uniform baseline（17.69/17.69/17.70）和 grid-best 比较，执行 MVP PASS/FAIL 判定（均值 ≥ 90% grid-best 改善量 → PASS）
- MVP PASS → 立即启动 post-mvp-kickoff（paper_framing.md → experiment_plan.yaml → dream_simulate → update_roadmap），按 skill 流程不跳步
- MVP FAIL → 评估是否需要第三轮算法修正或软化 claim 到"comparable + no grid search"
- GPU 空出 → 排 grid-b seed456 补齐 3-seed 统计

### 5. 🎯 战略上下文
**核心假设**：用检测器置信度估计 α_eff(b)，推导理论最优 b*，替代启发式 grid search。Claim 已软化为"comparable performance, eliminates grid-search cost"（D011）。

**决策链关键节点**：D005-D008 检测器迭代（ModernBERT → TF-IDF+LR）→ D009 gate 降至 AUC≥0.90 → D011 seed42 零改善暂缓 MVP → D012 修复 n_min=2 → D013 新颖性风险（Drayson et al. EMNLP 2025 用同一公式）→ D014 framing 精炼 Path B → D015 b_max ceiling 不阻塞 → D016 v1/v2 混淆变量

**最容易判断错的事**：
1. adaptive_v2 和 adaptive_fix 可能是同一批实验的不同命名，进 session 后先对 registry 确认，不要重复提交
2. ~78% batch 用 b=0 不是 bug——是 adaptive 方法的正面特性（"只在需要时干预"），论文应正面呈现
3. 投稿目标 EMNLP 2026 ARR May 25，Day 2/12，时间紧但 AI 团队速度足够——不要降级目标
4. D013 新颖性风险（Drayson et al.）尚未完全解决，post-MVP 需要明确差异化 story


---
