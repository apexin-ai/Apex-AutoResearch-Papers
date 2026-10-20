---
loop: 1
reason: max_messages
updated: '2026-05-17T10:39:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: bjb2-23165 cuda:0, cuda:1 only。之前 C1 regen 因未设 CUDA_VISIBLE_DEVICES=0 跑到 cuda:1 OOM (M001)
- ArmoRM 8B 与训练模型不能同时在 GPU 上: pipeline.py 已修复 (del model + empty_cache after scoring)，新脚本必须遵守 (M002)
- 论文核心 Vendi/Quality 指标用原始 registry 数据，C1 regen 仅用于 format 分析（regen 因 sampling randomness 与原始 ±1% 不同）
- C7 registry 值需更新: 当前 107.81/107.83/107.86，真值 108.08/107.85/108.13（已指示 Agent 修但未确认完成）

### 2. 🖥️ 基础设施快照
- 服务器: bjb2-23165 (connect.bjb2.seetacloud.com), root
- 工作目录: /root/autodl-tmp/carr/
- 模型: /root/autodl-tmp/models/Qwen3-0___6B (训练), ArmoRM-Llama3-8B-v0___1 (scoring), all-MiniLM-L6-v2 (embedding)
- 数据: UltraFeedback 2200 条 (2000 train / 200 eval), HF_DATASETS_OFFLINE=1
- 论文目录: projects/collapse_aware_reward_rebalancing/docs/paper/ (sections/, figures/)
- 活跃进程: C1 regen v2 可能刚完成 (cuda:0), K=16 已完成 (cuda:1 空闲)
- Paper Agent session 活跃, 正在做 Figure 4 (format collapse)

### 3. 📊 当前状态
**论文初稿 8/8 sections 完成**, 全部通过 Reviewer 审查。K=16 数据已 patch 进论文。

- Figures: Fig1 (pipeline) 待产出, Fig2 (Vendi trajectory 含 C8) ✓, Fig3 (direction reversal) ✓, Fig4 (format collapse) Paper Agent worker 运行中
- C1 regen v2: 3 代全部完成, format 分析数据已就绪但 format_metrics_unified.md 尚未产出
- K=16: DONE, Vendi -0.19%, 确认 Outline A
- 所有 GPU 实验已完成, cuda:0 和 cuda:1 均空闲
- References.bib: 15 条, LoRA 重复已修, Qwen3 已加
- Paper Agent 队列: Table 1 caption 修正 + Figure 4 生成

### 4. 📋 待办
- C1 format 分析 Worker 完成 → 产出 format_metrics_unified.md (C1 vs C5 同-K=4 对比) → 决定是否替换 analysis.tex 中 C2(K=8) vs C5(K=4) 的表格
- Figure 4 完成 → Figure 1 (pipeline) 产出 → 所有 figures 就绪
- 所有 figures 就绪 → 全文 consistency check + proofread → 编译 PDF
- 编译通过 → submit_paper_to_review 提交审稿 → 根据反馈迭代
- cuda:0/cuda:1 空闲 → 如果论文需要补充实验（如 C1 K=4 format 数据 C2 selected responses 重算），可即时安排
- Format metrics 数值不一致问题: 论文所有 format metrics 应基于 selected responses (2000/gen)，不是 candidates pool

### 5. 🎯 战略上下文
- **核心结论**: Reward-based curation 不导致 semantic diversity collapse (8/8 configs FAIL)。但 format/template homogenization 真实存在且 Vendi Score 盲区。LoRA 下 3.4pp gap 是 capacity artifact，Full-FT 下方向反转 (+0.63pp)
- **决策链**: D001(MVP设计) → D004(P1 FAIL) → D006(P1 重定义) → D007(LoRA artifact) → D008(LR诊断) → D009(5/5证伪) → D010(C→D pipeline) → D011(Direction C FAIL, CARR 99.3% overlap) → D012(K=16 FAIL, Outline A确认)
- **论文 framing**: "Collapse is real but mischaracterized" — semantic 稳定, format 坍缩, metric blind spot
- **易错点**: (1) 不要混淆 C1 regen 指标与原始 C1 registry 指标 (2) Format metrics 要统一 population (selected responses not candidates) (3) analysis.tex 当前用 C2(K=8) vs C5(K=4) 对比有 K 差异 confound，C1 regen 数据出来后应换为同-K 对比 (4) placeholder_ 前缀 bib keys 提交前最好清理
- **目标**: EMNLP 2026 ARR, DDL 2026-05-25 (~7天), 进度健康
