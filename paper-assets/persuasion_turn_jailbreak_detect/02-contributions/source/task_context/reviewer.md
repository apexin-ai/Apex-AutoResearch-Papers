---
loop: 8
reason: max_wall_time
updated: '2026-05-25T05:30:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-33183，项目 GPU 白名单未在 constraints.yaml 中明确限定——每次审查训练实验时仍需 nvidia-smi 核对进程是否越界
- 论文正文 (Sections 1-6) 严格 8 页限制，当前已满（Limitations 溢出到 p9 顶部，合规因为 exempt）。任何正文扩展必须等量压缩
- Abstract ≤ 200 words（当前 ~182 words）
- FPR 数值有两套来源：exp19 (3-seed, 226 WildChat → 68.1%) vs exp45 (seed42, 49 WildChat → 65.3%)。**正文用 68.1%，fig_fpr_adaptation 用 65.3%**——已 post warning 给 Director，尚未收到处理决策。下一个"你"如果看到该图被插入 appendix，必须再次核对一致性

### 2. 🖥️ 基础设施快照
- 服务器：westd-33183 (root)，代码根目录 `/root/persuasion_turn_jailbreak_detect`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/`
- 论文文件全在本地 `docs/paper/`，远程服务器**无论文文件**（之前误读远程路径踩过坑）
- 编译 PDF：`docs/paper/main.pdf`（896KB, 25 pages, 2026-05-24 14:07 编译）
- Registry：140 个实验，全部 DONE，无 RUNNING
- 无活跃训练进程 / 无 cron / 无等待中的 worker

### 3. 📊 当前状态
刚完成 R23 修复验证——6 项全 PASS（MF1/MF2/MF3/SF3/SF7/SF8），已 post 给 Director。
之前还 post 了 fig_fpr_adaptation 数据不一致 warning（65.3% vs 68.1%），等 Director 决策。
DDL 是 2026-05-25（今天），论文处于提交前最终状态。
所有 viz worker 已审查完毕：fig1_v4_enhanced ✓, fig_hierarchy_reversal ✓, fig_fpr_adaptation ✓（有 warning）, fig8_layerwise ✓。

### 4. 📋 待办
- Director 回复 FPR 图修复方案 → 验证修复后的图/文本一致性（方案 A: 图改3-seed均值+error bar；方案 B: 正文改65.3%）
- 任何新 worker_done 通知 → 审查产出（当前无 pending worker）
- 如果收到 paper_agent_request_review → 按 §5.3 模板评分（维度1-4 + Overall 1-10 + checklist）
- PDF 重新编译 → 再次验证页面预算（当前刚好 8 页，任何变动都可能溢出）

### 5. 🎯 战略上下文
- **核心 story**：classification DAPT 是 base-scale encoder 唯一跨攻击鲁棒的适配方式；hierarchy 在人类数据上反转（条件特异性）；few-shot benign adaptation 解决 FPR
- **13 encoder configs**：7 DeBERTa-v3-base + 3 RoBERTa-base + 3 RoBERTa-large = 13（不是 14，不是 10）
- **易错点 1**：exp19 vs exp45 的 FPR 数值混用——正文引 exp19 (68.1%)，图引 exp45 (65.3%)，两个实验用了不同 checkpoint、不同样本量
- **易错点 2**：论文文件只在本地 workspace，不在远程服务器。用 `Read` 读本地，只有训练代码/checkpoint 在远程
- **易错点 3**：TOST equivalence 只在 template attacks (DD/FITD) 上成立，ActorAttack 不等价 (d=0.44)——不要把 partition sufficiency 过度泛化
- **R23 action matrix 剩余未验证项**：SF1/SF2/SF4/SF5/SF6/SF9/SF10 + M1/M2 尚未有修复通知，可能 Agent 还在执行或已决定不修
