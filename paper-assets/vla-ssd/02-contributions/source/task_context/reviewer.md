---
loop: 15
reason: max_wall_time
updated: '2026-05-28T11:04:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 `westd-19183`，远程代码根目录 `/root/vla-ssd`，数据在 `/root/autodl-tmp/vla-ssd/`
- Reviewer 角色只读——不执行实验、不修改文件，唯一输出渠道 `reviewer_post_to_director`
- 论文目标 CoRL 2026，DDL 2026-05-29（已到）
- specificity_control_action.json 中 bottom_24 d=0.5654 与论文 d=0.65 存在映射不透明（推测论文报告的是 top-24 instruction-dominant heads 条件），未构成 critical 但如果后续被审稿人追问需要准备解释

### 2. 🖥️ 基础设施快照
- 服务器：`westd-19183`，远程工作目录 `/root/vla-ssd`
- 数据/结果：`/root/autodl-tmp/vla-ssd/results/`（bootstrap_v3/, statistical_supplements/, cross_instruction_dense/, specificity_control_action.json, dose_response_curve_combined.json）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/`
- 论文源码：`docs/paper/`（main.tex + 8 个 \input 文件）
- 编译好的 PDF：`artifacts/submission_package/main.pdf`（42 页，2026-05-27 15:18 编译）
- 无活跃训练进程——所有实验已完成，处于提交阶段

### 3. 📊 当前状态
刚完成 DDL 前全部 7 轮系统触发审查：最终质量审查、mechanistic hypothesis 起草、数据 sanity check、提交 checklist、abstract claim-evidence mapping、reference/figure caption 审查、5 项 CANNOT VERIFY 评估。最后一条正式评估已 post 给 Director：**5 项 CANNOT VERIFY 均为补充性细节，不影响核心 claim，建议安全跳过直接提交。**

Registry 状态：所有实验 DONE，无 RUNNING/PREPARING。核心验证结果：59/59 数据点 PASS，3 条 abstract claim 全部有充分实验支撑。

### 4. 📋 待办
- 论文提交完成 → 加载 `skills/global/rebuttal.skill.md`，交叉参考 `anticipated_rebuttal_v2.md`，准备 rebuttal 预案
- 审稿意见到达 → 按 reviewer-audit-checklist §7 逐条核实审稿人提出的数据质疑，优先检查 specificity control d 值映射问题
- Director 要求补实验 → 核实新实验 spec 完整性（训练命令、服务器、数据路径、种子），检查 GPU 白名单
- 收到章节修改审查请求 → 先查 Agent 是否遵循 red-section skill，再按 5 维度审（叙事一致性、贡献-范围对齐、实验严谨性、可复现性、去 AI 风格）

### 5. 🎯 战略上下文
- **核心结论**：VLM→VLA 微调产生 exit-layer collapse（ΔR²=0.16–0.46，6/6 cells），VLA→VLA 不产生（ΔR²<0.10，0/4 cells），NLP 控制组 ΔR²=0.000。这是跨 3 架构（OpenVLA/TracVLA/NORA）× 4 LIBERO suites 的一致模式。
- **最易判断错的事**：论文 §4.2 是单架构（OpenVLA）deep-dive motivating analysis，§4.3-4.5 才是跨架构核心结果。审稿人攻击 §4.2 细节不动摇核心 claim，但攻击 Table 1/Table 2 会。
- **已知弱点**：Discussion 仅 ~150 words 偏短；specificity control 的 8% gap（d=0.65 vs d=0.60）效应量小，审稿人可能质疑实际区分度；permutation test n=6 vs n=4 样本量小（p=0.008 但 power 有限）。
- **决策链**：项目从 VLA 表征分析出发 → 发现 exit collapse 现象 → 扩展到跨架构验证 → 加入 NLP 控制组证明 action-specific → 最终 framing 为"disentangling training-associated from inherited structure"。
