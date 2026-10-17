---
loop: 2
reason: idle_timeout
updated: '2026-05-25T06:13:31+00:00'
---

### 1. 🔴 硬约束 / 红线
- 论文已于 2026-05-25 提交 EMNLP 2026 ARR，OpenReview 由运维人工完成。**任何对 `docs/paper/` 的修改不会影响已提交版本**，仅用于 rebuttal/camera-ready 准备
- GPU 白名单：westb-29275 的 gpu_ids 需查 `get_project_status` 确认，上一轮全部备弹完成后已通知 Manager GPU 可全局调度，**当前可能已被重新分配给其他项目**
- 匿名仓库已 push（commit 1c90d33），rebuttal 前不要再 push 任何内容到匿名仓库
- GPT-5.4 替换 GPT-4o 已被 NO-GO（D081），不要重新讨论此决策

### 2. 🖥️ 基础设施快照
- 服务器：westb-29275，4×RTX PRO 6000 96GB
- 工作目录 / Python 路径 / conda env：**需下一轮 SSH 探查确认**（本 session 未连接服务器）
- 论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/`
- 活跃进程：无。全部实验已完成，无 RUNNING 实验，reconcile_crons 返回 0 条
- Cron：无活跃 cron

### 3. 📊 当前状态
刚完成 Figure 2 DAG 字体加深（Director 追加要求）：修改 `sections/method.tex` TikZ 代码，将所有节点标签、sub-labels、箭头注释、× 标记从淡色改为深色（#2C3E50/#333333/#C0392B）。编译通过，视觉确认。已向 Director 汇报。

Registry 状态：58 个实验，成功 41 / 负向 13 / 失败 0。全部 DONE，无 RUNNING/PREPARING。

等待中：无 Worker 回调、无 Cron、无 Director 决策待处理。

### 4. 📋 待办
- 审稿结果回来（预计 4-6 周）→ 读 reviewer comments → 制定 rebuttal 策略 → 用已完成的 4 个备弹实验数据回应
- Director 要求重新分配 GPU → 确认 gpu_ids 白名单是否已变更
- 如需 camera-ready 修改 → Figure 2 深色版已就绪在本地，需同步到匿名仓库（需 Director 批准时机）
- **rebuttal 备弹已全部就绪**：formality_scaled_n300、formality_llama_rewriter、llama70b_crossbench、GPT-5.4 NO-GO

### 5. 🎯 战略上下文
- 核心发现：LLM judge 对 style 有 **Likert Blindspot**——BT pairwise 检测到显著偏好，但 Likert 评分 ATE 不显著（effect size 极小）。这是 CSD 方法的核心贡献
- Score trajectory: R1: 2.5 → R17: 3.5，目标 4.0 (Conference)
- 备弹逻辑链：(1) 跨 judge 验证（Llama-70B 复现 Qwen3 pattern）(2) 跨 benchmark 验证（AlpacaEval + MT-Bench）(3) 跨 rewriter 验证（Llama rewriter 排除 rewriter artifact）(4) 大样本验证（n=355 确认结构性 attenuation）
- 易错点：llama70b_crossbench 的 Likert 在大效应下**变显著了**（d=0.21-0.30），这不是矛盾——恰好证明 Blindspot 是 effect-size gradient 现象，小效应被 Likert 吞掉，大效应保留。**不要把这个结果解读为否定 Blindspot**
- D078: construct divergence adjudication 已决策为 non-essential，不需要额外实验
