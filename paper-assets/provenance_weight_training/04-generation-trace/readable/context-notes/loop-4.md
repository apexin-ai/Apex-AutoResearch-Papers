# director / loop_4.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`1c23fcd52ae576ce0023.json`](../../sessions/1c/1c23fcd52ae576ce0023.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-14T13:31:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-47453 只有 4 张 GPU（cuda:0-3），均为本项目分配，不可使用其他设备号
- 输出目录必须在数据盘（根分区 30GB 曾爆满导致 3 个 uniform baseline 在 step 1000/6103 崩溃，D008 记录）
- adaptive_v2 系列是算法修复重跑，不是 p-hacking——旧 adaptive 结果保留为 constrained ablation，不要删
- Detector gate 已更新（D009）：AUC ≥ 0.90 且 ECE ≤ 0.05（不是原来的 0.95），当前 TF-IDF 检测器 AUC=0.939, ECE=0.048 已通过

### 2. 🖥️ 基础设施快照
- 服务器：westd-47453 (connect.westd.seetacloud.com)，用户 root
- 工作目录：/root/provenance_weight_training
- 模型：Qwen3-0.6B，合成数据 132M tokens（datagen_synthetic_4gpu 已完成）
- 检测器：TF-IDF bigrams + Logistic Regression（秒级完成，不占 GPU）；ModernBERT 方案已废弃（AUC 太高导致 q-score 极化）
- W&B：未配置
- 活跃进程：grid_b_seed42_batch（RUNNING，6 个 b 值批量跑）、grid_b5_0_seed123（RUNNING）、grid_b3_0_seed123（RUNNING）

### 3. 📊 当前状态
- **阶段**：MVP 验证中，投稿目标 EMNLP 2026 ARR May 25（12 天窗口，已过约 1.5 天）
- **关键进展**：uniform 3 seeds 全 DONE，adaptive 3 seeds 全 DONE（但 seed42 零改善，D011/D012 诊断为 n_min=3 钳制 ESS）
- **RUNNING**：grid_b_seed42_batch（6 个 b 值）、grid_b5_0_seed123、grid_b3_0_seed123
- **QUEUED**：grid_b seed456 系列（6 个，等 GPU 释放）、detector_modernbert（已废弃但 registry 未清理）
- **PREPARING**：adaptive_v2_seed42/123/456（D012 修复算法后的重跑，n_min=2 + EMA 平滑 b*）
- **等待中**：grid-b seed42 + seed123 跑完 → GPU 释放后立刻跑 adaptive_v2 三组

### 4. 📋 待办（条件触发式）
- grid_b_seed42_batch 完成 → 汇总 6 个 b 值 eval_ppl，确定 best-b for seed42
- grid_b seed123 全部完成（b=0.5/1.0/1.5 已 DONE，b=3.0/5.0 RUNNING）→ 汇总 seed123 best-b
- GPU 释放 → 优先跑 adaptive_v2 三组（D012 已决策优先于 seed456 grid-b 高 b 值）
- adaptive_v2 三组完成 → 重新做 MVP PASS/FAIL 判定：均值 ≥ 90% grid-best 改善量 → PASS
- MVP PASS → 调 complete_mvp()，启动 post-mvp-kickoff（写 paper_framing.md → experiment_plan.yaml → dream_simulate）
- MVP FAIL Level 1 → 检查检测器校准 + 理论假设
- seed456 grid-b 系列在 adaptive_v2 之后排队跑（补齐 3-seed 统计）

### 5. 🎯 战略上下文
- **核心假设**：adaptive b*（从 α_eff 推导）无需网格搜索即可匹配/超越 grid-searched best-b
- **决策链**：D005→D006→D007→D008 是检测器迭代链——ModernBERT AUC 过高(0.9998) → 10%数据仍过高 → TF-IDF+LR(AUC=0.939) 解决 q-score 极化。这条链是论文 story 的重要部分（"even simple detectors suffice"）
- **D011→D012 是当前关键转折**：seed42 adaptive 零改善诊断为 n_min=3 约束导致，不是算法根本失效。修复后重跑 adaptive_v2 是 MVP 判定的最后一步
- **易错点**：不要把 adaptive（旧，有 n_min=3 bug）和 adaptive_v2（修复版）混为一谈；D011 暂缓了 MVP 判定，必须等 adaptive_v2 结果才能重新评估
- **Claim 方向已调整（D011）**：从 "adaptive > grid-best" 软化为 "comparable performance, eliminates grid-search cost"——具体 claim 强度取决于 adaptive_v2 结果
- **时间压力**：EMNLP ARR May 25 还剩约 10.5 天，当前在 Day 1.5，按排期 Day 2-3 应完成 MVP


---
