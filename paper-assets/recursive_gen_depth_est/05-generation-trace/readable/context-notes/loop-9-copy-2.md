# agent / loop_9.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_9.md`
- **Structured JSON:** [`24ec1f5a6f24157a6609.json`](../../sessions/24/24ec1f5a6f24157a6609.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: idle_timeout
updated: '2026-05-15T18:55:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 gpu-6000pro-2 的 cuda:0 和 cuda:1（config 白名单 gpu_ids=[0,1]）
- DDL: EMNLP ARR May 25 — 剩余 10 天，Phase 2 写作 + 审稿修改 + 提交
- 三个模型的种子语料都是 Wikipedia subset，不是 OpenWebText/Dolma/WebText — 之前 Worker 写 method section 时搞错过，method.tex 原文正确不需要改
- DCOL 已死（v1-v6 全失败），论文 framing 已转 Plan A：Atlas/EDD primary，不要再尝试 DCOL
- feat_ablation_v1 在 registry 中 RUNNING 但无 PID/tmux/cron — 实际计算由 Worker 在 SSH 上执行，不是 submit_training_job 提交的

### 2. 🖥️ 基础设施快照
- 服务器：gpu-6000pro-2，工作目录 /root/autodl-tmp/recursive_gen_depth_est
- Python：需探测确认（可能是 conda 或系统 Python，前一个 session 未留路径记录）
- 模型数据：9 cell feature files (JSONL)，每 cell 5000 samples，共 20000 per model-strategy
- W&B：无活跃 run（Phase 1 实验全部完成）
- 活跃 Worker：`worker_exp_feature_ablation_9cell_harvest_20260515T184719`（status=running, turn=11, 正在 ssh_read_only 收集 9 cell feature ablation 结果）
- 活跃 Cron：无（reconcile 返回 0）
- GPU：两卡均空闲，可用于补充实验

### 3. 📊 当前状态
Phase 1 全部完成（50 实验，26 success / 3 negative / 6 failed / 13 killed）。Phase 2 写作刚启动。

正在进行：
- **feat_ablation_v1** (RUNNING)：R3-N2 reviewer 要求的 feature ablation study（top-k ablation, per-category ablation, forward selection, VIF, correlation matrix），Worker 正在从 9 个 cell 收割结果
- **feature_ablation_9cell** (PREPARING/failed)：准备阶段失败，feat_ablation_v1 是其替代

等待中：
- Worker 回调 → 收到后需更新 registry + report.md + 将 ablation 结果纳入论文 Section 5
- 审稿修改大量待处理（见下方待办）

### 4. 📋 待办（条件触发式）
- Worker feature_ablation 回调完成 → 更新 feat_ablation_v1 registry (metrics/conclusion) → 将结果写入 paper Section 5.4 或新建 ablation subsection
- Ablation 结果就绪 → 派 Paper Agent Worker 批量处理 Warning 级审稿修改：R1-N1 EDD 公式修正 / W3 LoRA 引用 / W5 无条件生成文本 / W6 per-class recall 纳入 / R2-N2 文献补充 / R2-W2 术语统一 / R2-W4 Limitations 位置 / R2-W6 orphan bib 清理
- Paper Agent 完成 → 派 Reviewer Worker 对抗迭代（max 5 rounds）
- May 23 前 → 最终 polish + bibliography audit + 提交 ARR

### 5. 🎯 战略上下文
**核心结论链**：
- D011: Plan A 激活（Atlas/EDD primary，DCOL 全线失败退出）
- D024/D027: EDD 叙事从硬阈值转向连续 AUC 衰减曲线，d3v4 borderline 透明报告
- D022: RF ≈ CORAL ≈ DivEye 统计不可区分，核心贡献在特征发现而非分类器
- D028: Cross-strategy normalization 不可修复（z-score 不救 d1v2 AUC），这是结构性偏移不是 scale 差异
- N2 双 backbone 结论：DeBERTa 58.3% / RoBERTa 59.5% 均远低于 RF 78.2%，Spearman ρ=-0.484 负相关 → representation bias 而非训练不足

**易踩坑**：
- τ=0.9 的 d1v2 反转（GPT-2 XL 0.13, OLMo 0.25）是 covariate shift 不是 bug — 论文需要正面讨论而非回避
- EDD=4 三模型一致性声明已降级（D027）：Pythia 显著 p=0.001，OLMo 边际 — 不要写 "all three models show significant EDD=4"
- 6-class 不能用 RF 多分类 AUC，必须用 binary pairwise classifier（决策边界稀释问题）
- Worker 写的 method section artifact 里种子数据描述有误，不可直接合并


---
