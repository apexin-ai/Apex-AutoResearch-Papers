---
loop: 18
reason: idle_timeout
updated: '2026-05-21T05:16:50+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：gpu-6000pro-2 的 cuda:0, cuda:1（westd-48862 已确认可安全关闭，数据已迁移完毕）
- gpu-6000pro-2 的 SSH config name 是 `autodl-rtx6000`（不是 `gpu-6000pro-2`）
- Reference model 固定 Pythia-1.4B；Pythia pipeline 结果标 †（self-reference 4-11pp advantage）
- EMNLP 2026 main text 严格 8 页限制，当前刚好卡在 8 页边界（§6 Discussion 结束于 page 8，Limitations 起于 page 9）——任何主文修改都要验证不溢出
- 论文处于 review 模式（`\usepackage[review]{acl}`, `\author{Anonymous}`），投稿前不要改

### 2. 🖥️ 基础设施快照
- **保留服务器**：gpu-6000pro-2 (autodl-rtx6000), connect.westb.seetacloud.com:52439
  - 工作目录：/root/autodl-tmp/recursive_gen_depth_est/（20G, 含 checkpoints 18G）
  - Python：/root/miniconda3/bin/python（conda base 环境）
  - /root/autodl-tmp/models/ 90G（预下载模型）
  - GPU：nvidia-smi 报 1 张卡 97887 MiB (~96GB)，异常状态（100% util, 0 MiB used, 无进程）——可能需要用户重启实例
- **已关闭**：westd-48862 (connect.westd.seetacloud.com:48862)，数据已全量迁移到 gpu-6000pro-2，逐目录验证通过
- **活跃进程**：无。无 RUNNING 实验，无活跃 cron
- 论文源码：本地 `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/`
- Registry：139 个实验，全部 DONE

### 3. 📊 当前状态
刚完成三批投稿准备工作：

**已完成**：
1. 论文最终写作修改（Round A FAIL/NOTE 修复 + Round B 15 项微调，含 C1/W1-W8/MR1-3/M1-M2，全部编译通过，8 页限制满足）
2. Supplementary README 创建并注册（art_20260520_4d199e）
3. Camera-ready checklist 预检全通过（anonymization, figures, no TODOs）
4. Limitations 28 个数字溯源完成（3 个 ⚠️ 仅在 conclusion.tex 出现，registry 可追溯但 appendix 无对应文本）
5. 数据迁移 westd-48862 → gpu-6000pro-2 完成并验证（0 缺失文件）
6. GPU 状态检查：gpu-6000pro-2 无用户进程，GPU 状态异常待用户处理

**等待中**：无 Worker / Cron / 审批待处理

### 4. 📋 待办（条件触发式）
- Director 确认 westd-48862 已关闭 → 从 project config 移除该服务器条目
- Director 决定是否补充 appendix 中缺失的 3 个数字（53.7% ref-free, 73.7% ensembling, +16.4/+8.0pp per-model recovery）→ 派 Worker 在 section_appendix.tex B.10/B.19 补文
- Director 确认 M5 author order（alemohammad2024_mad, guo2024_biscope, hosmer2000 的作者排序）→ 派 Worker WebSearch 确认正确顺序并修 references.bib
- GPU 异常状态（100% util + 0 MiB + 无进程）→ 建议用户重启 gpu-6000pro-2 实例
- 投稿指令到达 → 确认 review mode 开启、匿名、编译无 warning，打包 main.pdf + supplementary

### 5. 🎯 战略上下文
- 论文核心 narrative：recursive generation depth 是可估计的 ordinal classification 问题，perplexity tail features（p90_ppl, var_surprisal）是跨模型/策略一致的 depth fingerprint
- 关键数字锚点：in-distribution 68.9-85.9%（d1-d3: 58.9-81.5%），cross-model 66.4%（d1-d3: 55.4%），cross-strategy 59.1%（d1-d3: 45.9%），14B EDD=0（confounded）
- 最容易判断错的事：(1) 不要把 4-class accuracy 当核心指标——d0 recall >97% 严重膨胀 headline，d1-d3 balanced accuracy 才是真实信号；(2) Pythia 结果有 self-reference advantage（†标记），跨 cell 比较需 caveat；(3) cross-strategy transfer 的 d1/d2 boundary inversion 是已知 limitation，不是 bug
- 论文状态：写作基本完成，处于投稿前最后检查阶段。所有实验已跑完，无新实验计划
