---
loop: 18
reason: idle_timeout
updated: '2026-05-25T18:56:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-19828 只有 **1 张 GPU (cuda:0)**，report.md 历史残留写 "cuda:0, cuda:1" 是错的，cuda:1 不存在（曾导致 c2_s43 v1 CPU fallback 事故）
- 5-method 分析**必须用 run_5method_analysis_d102.py**（排除 mauve, threshold=true_3sigma_d105, n_perm=5000），不能用旧脚本（M063 硬约束）
- 所有训练命令必须包含 `export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com`
- FPR 基准数字：PermG 6.7% (4/60, CI [1.8%, 16.2%], 10 seeds)，K≥3 FPR 10.0% (6/60)——论文中 8 个位置引用，不可写错

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828(root)，工作目录 /root/autodl-tmp/distrib_canary_collapse
- Python：/root/miniconda3/bin/python（conda base 环境，不是 venv）
- HF cache：/root/autodl-tmp/.hf_cache
- 数据：data/wikitext103_5k
- 论文：本地 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/
- C2-s42 已完成：results/c2_opt13b/a050_s42_fp32/（EXIT_CODE=0, all_metrics.json + 5method 分析完成）
- C2-s43 目录已创建但尚未启动训练：results/c2_opt13b/a050_s43_fp32/
- 当前无活跃训练进程（c2_s42 刚结束，GPU 空闲）

### 3. 📊 当前状态
**刚完成**：
- C2-s42 (OPT-1.3B α=0.50 s42) 实验完成 + D102 分析审查。**结果：PermG 0/8 forward（negative）**。Entropy 先降后升（非单调），detection boundary α_c 在 OPT-1.3B 上 > 0.50。
- SF4 离散化熵 Granger 检验审查（bins_5_equal_freq 0/7, ≥15 bins 恢复 7/7）
- R16 审稿逐条方案独立审查（7 个关键判断已回复 Director）
- R16 Patch P0-P7 Mode B 对抗审查（1 critical: experiments.tex:14 节标题 "Sharp" 未改 "Steep"；2 warning）
- 4-method κ 分析审查（移除 NaiveXCor 后 κ 反降 0.187→0.167，但分析用了 8 pairs 非 D102 6 pairs 基准）

**等待中**：
- Director 决策：C2-s43 是否仍需运行（s42 已 negative，s43 能否改变定性结论存疑）
- Director 决策：R16-W1 追加 seeds 方案选择（方案A ~11 GPU-hours vs 方案C limitation 加强）
- Paper Agent 修复 experiments.tex:14 "Sharp→Steep" + appendix 3 处 "sharp" 残留
- Paper Agent 修复 discussion.tex:15 "fully recovered at ≥15 bins (7/7)" → "6--7/7"

### 4. 📋 待办
- **C2-s43 launch 通知到达** → 验证 CUDA_VISIBLE_DEVICES=0 + HF_HOME + 脚本参数
- **Worker 提交 OPT-1.3B α=0.50 论文更新** → 审查 §4.5 措辞是否 honest（不能 overclaim、不能 hide negative）
- **R16-W1 追加 seeds 实验开始** → 监控 GPU 使用、验证 α 值和 seed 正确
- **Paper Agent 提交 "Sharp→Steep" 修复** → 确认 experiments.tex:14, appendix:552/581/599 全部替换
- **4-method κ 分析用 D102 基准重新跑** → 验证 FPR 数字与论文一致（当前 5.0% vs 论文 10.0% 有差异）
- **如果 OPT-1.3B 结果需要 negative framing** → 加载 negative-framing-review.skill.md 四维度审查

### 5. 🎯 战略上下文
- **D130 reframe**：C1=detection onset characterization（R16 后进一步弱化为 "empirical characterization"），C2=landscape，C3=toolkit（降级为 "supports reproducible analysis"），C4=applications
- **R16 审稿给 3.0 Findings**，升 3.5 条件：更多 seeds（最关键）+ framing 弱化 + cross-arch intermediate-α + C4 domain。C2-s42 negative 意味着 cross-arch 条件未满足
- **最容易判断错的事**：OPT-1.3B α=0.50 PermG=0/8 不是"方法失败"或"论文崩塌"——它是 **detection boundary architecture-dependent** 的证据，strengthens limitations 中 "Pythia-family-only" 的诚实性。不要建议 hide 这个结果或包装成正面发现
- **易踩坑**：论文中 "sharp" 已全局替换为 "steep"，但 experiments.tex 节标题和 appendix 有 3 处遗漏——这是上一轮 patch review 的 critical finding，确认是否已修
- **α=0.50 seed 数据极少**：Pythia-410M 仅 3 seeds (42/43/44)，OPT-1.3B 仅 1 seed (42)。这是 R16-W1 reviewer 反复攻击的最大软肋
- **discussion.tex MMCT "marginal improvement" vs "does not outperform" 张力**：已 flag 两轮但仍未修——limitations.tex:13 说 "marginal improvement"，但 K≥3 FPR (10.0%) > PermG standalone (6.7%)，实际无 improvement
