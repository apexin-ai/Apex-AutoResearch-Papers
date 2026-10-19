# director / loop_5.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`7ec8c8fe90299cb973d6.json`](../../sessions/7e/7ec8c8fe90299cb973d6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-14T16:16:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 bjb1-42106 的 cuda:0 和 cuda:1（项目配置 gpu_ids 白名单）
- m2_full_qwen registry 状态卡在 ANALYZING（cron 误触发），状态机不允许回退到 RUNNING。实际 cuda:0 在跑训练。report.md / 资源监控显示 cuda:0 空闲是 false alarm——不要因此把卡分给别的实验
- s42 runs 必须用 3 epochs（D026），s43/s44 用 2 epochs + early-stopping-patience=2（D027）
- plot_neg_difficulty 输出是合成数据占位图（文件名带 _placeholder），禁止直接入稿

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-42106 (connect.bjb1.seetacloud.com)，工作目录 /root/structfuse-context（代码）+ /root/structfuse（训练脚本）
- Python：/root/miniconda3/bin/python（aml-train 镜像，conda base 环境）
- 模型：Qwen2.5-Coder-3B /root/autodl-tmp/structfuse/models/qwen2.5-coder-3b-instruct，StarCoder2-3B /root/autodl-tmp/structfuse/models/starcoder2-3b
- 数据：/root/autodl-tmp/structfuse/full_m2_training_data/（训练 jsonl），/root/autodl-tmp/structfuse/checkpoints/（checkpoint 输出）
- HF cache：/root/autodl-tmp/.hf_cache
- 活跃 tmux sessions（6 个）：
  - m2_qwen_s43: Qwen s43+s44 主训练（PID 337267 bash wrapper → PID 337271 python）
  - qwen_s42_watcher: 等 s43+s44 完成后自动触发 embedding_s42 + dataflow_s42 补跑
  - m2_starcoder_s43: StarCoder s43+s44 等待启动（PID 309679 watcher 监控 76627）
  - starcoder_s42_watcher: 等 s43+s44 完成后自动触发补跑
  - 旧 StarCoder wrapper（PID 74122，random_s42 在跑，PID 76627）
  - m1_reextract_v2: 后台 CodeQL 提取（CPU，71/82 groups）

### 3. 📊 当前状态
刚完成：ROADMAP 全量更新（Reviewer PASS）、s42 补跑链式部署（Reviewer PASS）、新颖性自查（Manager 要求，已回复 A 群）、Discussion 草稿 + 文献对比 plan_017（Reviewer WARNING 已修复）、neg_difficulty 可视化（placeholder）

正在跑：
- m2_full_qwen: random_s42 DONE (R@1=0.5527), random_s43 RUNNING @step~1000, 全 9 runs ETA ~May 19
- m2_full_starcoder: random_s42 RUNNING @step~3700/4242 (~87%), 全 9 runs ETA ~May 20
- m1_reextract_v2: 71/82 groups，~12h 剩余

等待中的 Agent 回调：
- plan_015 dynamic mining 实验设计文档（CPU Worker 进行中）
- ROADMAP 更新已完成
- Dream dream_20260514T075732 仍在 reviewing 阶段，完成后会注入 session

### 4. 📋 待办（条件触发式）
- M2 Qwen 全 9 runs 完成 (~May 19) → 立即跑 m2_stat_analysis.py 统计检验；若 embedding>random p<0.05 → Claim 1 confirmed；若 dataflow>random p<0.05 for Qwen → Claim 2 保持 conditional claim；否则 → 降为 observation（D028）
- M2 StarCoder 全 9 runs 完成 (~May 20) → 跑统计检验 + 跨编码器交互分析
- M2 任一编码器完成 → 立即启动 plan_003 SWE-bench eval（脚本+repo 就绪）+ plan_004 RepoBench-R eval（脚本就绪）并行
- plan_003 完成 → plan_016 Bootstrap CI（0 GPU）
- GPU 空出 → plan_014 Temperature ablation（Dream reviewer 要求，Claim 2 唯一独立支撑，P1）
- Dream 报告到达 → 按 dream-report-action skill 逐条处理
- plan_015 设计文档完成 → 审核方案，M2 后安排 GPU 执行

### 5. 🎯 战略上下文
- 核心决策链：D017（真 embedding mining 有效）→ D019/D020（full M2 go/no-go 框架）→ D024（framing 适配 pilot 结果）→ D026/D027（epoch 缩减+early stopping）→ D028（Claim 2 降级待定，等 M2 统计结果）
- Claim 2 是论文最薄弱环节：n=2 encoders 的交互效应无统计功效。Reviewer 建议降为 "observation + mechanistic hypothesis"。最终决定等 M2 full 结果
- StarCoder pilot negative 不影响 Claim 1（embedding>random 两编码器一致），只影响 Claim 2 dataflow conditional benefit
- 新颖性自查结论：核心贡献组合新颖（纠正 CoCoHaNeRe + dataflow 训练负样本 + 表征饱和机制），但需补引 AAAI 2025 uncertainty paper、ICLR 2025 representation geometry paper、EACL 2026 survey 等 6 篇
- 易错点：registry 显示 m2_full_qwen 状态 ANALYZING + cuda:0 空闲，实际在跑。不要因此重新分配 cuda:0
- 时间线紧但可行：M2 ~May 19-20 → eval ~May 20-22 → 统计+framing ~May 22-23 → 写作 ~May 23-25 → ARR May 25


---
