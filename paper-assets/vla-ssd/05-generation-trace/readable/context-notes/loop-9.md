# director / loop_9.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_9.md`
- **Structured JSON:** [`317fd44415968fa32713.json`](../../sessions/31/317fd44415968fa32713.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_messages
updated: '2026-05-23T23:52:45+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-19183 的 cuda:0 和 cuda:1（`execution.gpu_ids`）
- 远程代码路径 `/root/vla-ssd`，模型/数据在 `/root/autodl-tmp/`
- 论文 LaTeX 真源在**本地** `projects/vla-ssd/docs/paper/`，不是远程
- TracVLA reference 是 **Phi-3-Vision**（不是 Phi-3-Instruct），全文已统一，不要改回去
- 图表中 "Random Init" 和 "Reference" 是两个不同概念——Random Init = 随机初始化(0/32 heads)，Reference = OXE-pretrained 或 base VLM。M020 教训：禁止 blanket 术语替换
- CoRL 2026 DDL: Abstract 5/26, Paper 5/29, 正文 8 页限制

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183 (connect.westd.seetacloud.com), user=root
- 远程工作目录：`/root/vla-ssd`
- GPU：2× (cuda:0, cuda:1)，磁盘 816G/879G 可用
- 模型 checkpoint：`/root/autodl-tmp/vla-ssd/checkpoints/`（OpenVLA/TracVLA/NORA，全是最终权重，无中间 checkpoint）
- 实验结果：`/root/autodl-tmp/vla-ssd/results/`
- 本地论文目录：`projects/vla-ssd/docs/paper/`（main.tex + figures/）
- 本地产出：`projects/vla-ssd/artifacts/`
- 无 conda env，无 wandb，无 git config
- 活跃进程：1 个 Worker `worker_run_phi3_nlp_control_20260523T231450` 在 cuda:0 运行 Phi-3-mini-instruct NLP control 实验（下载模型中，预计还需 1-2h）

### 3. 📊 当前状态
**刚完成**：PI 第二轮 14 项结构性改版（图表重排序、Abstract 替换、多章节重写、全局 Untrained→Reference 清理）+ 3 个 CRITICAL 修复（TracVLA L1 方向矛盾、Random Init 误标、CF bar 空白）+ final polish（em-dash、Table 2 歧义、label 统一）+ Significance 提升写作（Diagnostic Implications 段 + Conclusion actionable takeaway）

**正在运行**：
- `phi3_nlp_control` PREPARING — Phi-3-mini-instruct per-layer action probe（第二个 NLP control，加强 VLA-specificity 证据）
- cuda:1 空闲 — 中间 checkpoint 检查已完成，结论是全部模型只有最终权重，training dynamics 分析不可行

**等待中**：
- phi3_nlp_control Worker 完成回调
- 用户审批 fresh review（`apr_20260523T212915_qx6t` pending）—— 内部 Reviewer 已完成 fresh review（Overall 6/10），外部审稿团队等用户点审批卡
- Reviewer 的 Significance 提升方向评估回复（可能已回但未注入我的 session）

**论文当前状态**：编译通过，0 critical warnings，正文 8 页，最新 PDF 已上传用户（`vla-ssd_final_polished_2026-05-23.pdf`）

### 4. 📋 待办
- phi3_nlp_control 完成 → 如果 ΔR²≈0 确认 VLA-specificity → 派 Paper Agent 加入 appendix 作为第二 NLP control 证据 + 更新 experiments.tex 提及 "two NLP controls"
- phi3_nlp_control 完成 → ΔR² 显著 > 0 → CRITICAL 发现，需要重新评估 VLA-specificity claim
- 用户审批 fresh review → review 启动 → 收到审稿报告后按 review-report-action skill 处理
- Reviewer Significance 评估回复到达 → 消化建议，决定是否有额外可执行项
- 用户新反馈 → 按指令执行修改
- Abstract DDL 5/26 临近 → 提醒用户准备 abstract 提交

### 5. 🎯 战略上下文
- 论文核心：R² exit collapse 在 VLM→VLA 转换时出现（6/6, Δ=0.156-0.455），VLA→VLA 不出现（0/4, Δ=0.033-0.086）。CF sensitivity d≥0.45。L1 attention 是 backbone inherited，不是训练创造的。
- Significance 2/4 是最大短板。已加 Diagnostic Implications 段。Phi-3 NLP control 加强 Soundness。如果 Reviewer 有更好建议要认真考虑。
- 易错点：paper_framing.md 中 RC3 已标注 "NO LONGER APPLICABLE"（旧 RSA 阶段的 5-demo concern），不要重新启动相关实验
- 易错点：CF 数据有复杂历史——M019 错误数据文件教训。正确数据源是 `libero_{suite}/counterfactual_combined.json`（finetuned model），不是 `counterfactual_10tasks/`（base model）
- 易错点：论文图文件名已全部更新（fig_overview, fig_r2_collapse, fig_counterfactual_bar, fig_l1_attention, fig_claim_evidence），旧文件（fig_teaser, fig_cross_arch_l1）仍在 figures/ 目录但未引用，提交前需清理
- 运维审计已回复：westd-19183 归类 B（保留），预计 5/29 后可释放


---
