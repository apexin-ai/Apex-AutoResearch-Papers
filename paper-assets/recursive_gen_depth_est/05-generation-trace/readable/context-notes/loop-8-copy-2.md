# agent / loop_8.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_8.md`
- **Structured JSON:** [`84f16935d77d68d8da5d.json`](../../sessions/84/84f16935d77d68d8da5d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: idle_timeout
updated: '2026-05-15T15:48:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**gpu-6000pro-2 cuda:0, cuda:1** 仅此两卡，禁用其他设备
- **z-score 恢复 LR d1v2 AUC 的 claim 已证伪** (D021)：论文中必须删除/修改此声明。LR z-score 实验结果：GPT-2 XL 0.50→0.24, OLMo 0.50→0.19，与 framing 声称完全相反
- **EDD 不得写"EDD=4 across all models"**：正确措辞是"连续 AUC 衰减曲线 + d3v4 clusters near 0.75 + d4v5 uniformly <0.70"。Pythia p=0.001 显著，OLMo p=0.091 边际，GPT-2 XL p=0.505 不显著 (D027)
- **Baseline 叙事**：RF ≈ CORAL ≈ DivEye 统计不可区分 (bootstrap p>0.05 Bonferroni)，不得写"RF best" (D022/D023)
- **DCOL 方向已永久关闭** (D018)：6 版迭代全败，只能写 negative analysis section
- submit_on_allocated 的 command 必须用 `bash -c "..."` 包裹（tmux 跑 /bin/sh），脚本内 GPU 一律 `cuda:0`

### 2. 🖥️ 基础设施快照
- **服务器**: gpu-6000pro-2（本地机，非 AutoDL）
- **工作目录**: `/root/autodl-tmp/recursive_gen_depth_est`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- **模型路径**: 各模型 LoRA checkpoint 在 `/root/autodl-tmp/recursive_gen_depth_est/models/` 下（Pythia-1.4B / GPT-2 XL / OLMo-1B）
- **数据路径**: `/root/autodl-tmp/recursive_gen_depth_est/data/`（pythia_nucleus095 / pythia_temp09 / pythia_topk50 / gpt2xl_* / olmo_*，每 cell 5000 samples × 4 depths = 20000）
- **Artifacts**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/`
- **活跃进程**: 无（两卡空闲）
- **Cron**: 无活跃 cron
- **Workers**: 无运行中 worker

### 3. 📊 当前状态
Phase 1 全部完成（46 个实验：24 success / 3 negative / 6 failed / 其余 killed）。**项目处于 Phase 2 写作阶段**，DDL EMNLP ARR May 25（剩 10 天）。

两卡完全空闲，无 RUNNING 实验。两个 PENDING 实验等待 Director 审批：
- **zeroshot_llm_500_001** (PENDING): 零样本 LLM 样本量从 200→500 缩窄 CI (R1-W4)
- **temp07_pilot_pythia_001** (PENDING): τ=0.7 temperature pilot 验证 d1v2 inversion 是否在 τ<0.9 也出现 (R2-W3)

无等待中的 Worker 回调或 Cron。上一轮 session 完成了 N2 双 backbone 实验（DeBERTa 58.3% / RoBERTa 59.5% 均远低于 RF 78.2%）和 feature overlap 分析（Spearman ρ=-0.484），以及全部 EDD 跨模型验证。

### 4. 📋 待办（条件触发式）
- **Director 审批 zeroshot_llm_500_001** → spawn worker 在 cuda:0 跑 500-sample zero-shot eval
- **Director 审批 temp07_pilot_pythia_001** → spawn worker 在 cuda:1 跑 Pythia τ=0.7 数据生成+评估
- **写作启动**（可立即开始，不等审批）→ spawn paper worker 按 memory.md §D 写作顺序执行：
  - 第一批：§4 EDD 公式定义(R1-N1) + §3 Benchmark Construction(W5) + Bibliography 扩充(R2-N2) + 术语一致性(R2-W2)
  - 第二批：§4 Atlas analysis(D024/D027) + §5 Results baseline 重构(D022/D023) + per-class recall 表(W6)
  - 第三批：§5 End-to-end baseline 对比(R1-N3, 数据已就绪) + §6 Discussion(D015/D014)
  - 第四批：§1 Intro + Abstract + Limitations 调整 + orphan bib 清理
- **4 张必需图**(Dream D002 硬约束) → 与第二批写作并行，spawn worker 用 draw-paper-figure skill 生成：AUC decay curve / feature trajectory / confusion matrix / Atlas heatmap
- **两个 PENDING 审批超过 24h 无响应** → 向 Director 催促，DDL 紧迫不能等

### 5. 🎯 战略上下文
**核心结论链**: 19 个统计特征 (p90_ppl, var_surprisal 等) 的手工特征 + 简单分类器 (RF) 能以 70-85% 准确率估计递归生成深度。端到端 PLM (DeBERTa/RoBERTa ~59%) 大幅落后 (-19pp)，因为 PLM 表征与手工特征关注文本的不同层面 (Spearman ρ=-0.484)。深度退化信号在 depth-4 饱和 (EDD=4)，跨模型方向一致但统计强度分层。

**易错点**:
- 不要把 6-class pairwise AUC 与 4-class 直比（决策边界稀释，见 D019/D020）
- Cross-strategy LOO temp09 d1v2 反转是 covariate shift 而非 bug（temp09 depth N ≈ 其他策略 depth N+1）
- 3-class acc < 4-class 是结构性的（排除了最易分的 d0），不是异常
- **两卡空闲 = 失职**——Phase 2 写作期间应同时跑补充实验（两个 PENDING + 可能的制图任务）
- DDL 只剩 10 天，写作是关键路径，不要等所有补充实验跑完才开始写


---
