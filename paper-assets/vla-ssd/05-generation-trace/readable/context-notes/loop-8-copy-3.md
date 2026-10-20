# reviewer / loop_8.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`d058ba4470772fa6f362.json`](../../sessions/d0/d058ba4470772fa6f362.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-05-17T17:04:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1（westd-19183）。越界立即 CRITICAL。
- Reviewer 只读：不执行实验、不修改文件、不直接回 Paper Agent。唯一输出渠道 `reviewer_post_to_director`。
- 论文本地路径 `projects/vla-ssd/docs/paper/`，训练代码/结果在远程 `/root/vla-ssd/` 和 `/root/autodl-tmp/vla-ssd/`。断言"未修改"前必须两边都读。
- Abstract 说 "21–24 heads" 但 Table 2 写 25/32 —— 已报 warning，等 Agent 修复。不要在下次审查中漏掉这个。

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183，2× NVIDIA RTX PRO 6000 Black (98GB each)
- 远程代码：`/root/vla-ssd/`，结果：`/root/autodl-tmp/vla-ssd/results/`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/`
- 论文：`docs/paper/main.tex`（已编译 PDF 存在于同目录）
- Python：`/root/miniconda3/bin/python3.12`
- 活跃进程：**无**。两块 GPU 均空闲（0% util, 0 MiB）。无 tmux session 运行中。
- Registry 中 `l1_head_ablation` 仍标 RUNNING 但实际已完成，需 Agent 改为 DONE。

### 3. 📊 当前状态
**刚完成**：论文压缩后全文完整性审查（5 维度），发现 2 个 warning：
1. Ablation 段落缺 5 demos/task 标注（审稿人会困惑为什么 L1 R²=0.256 远低于主实验）
2. Abstract "21–24 heads" vs Table 2 "25/32" 数字不一致

**Ablation 实验链已全部审完**（v1 label bug CRITICAL → v2 fix → v3 all-32 → diagnostic → action probe → bootstrap CI），所有报告已通过 `reviewer_post_to_director` 发送。

**等待中**：
- Paper Agent 修复上述 2 个 warning
- Round 3 内审提交（需用户审批）
- Round 3 审稿结果（预计 May 18-20 返回）

### 4. 📋 待办
- Paper Agent 提交修改后的论文 → 检查 "21–25" 是否统一、5 demos 是否标注
- Director 触发 Round 3 审查请求 → 执行 §5 章节对抗审查（评分模板 + checklist）
- Round 3 审稿结果返回 → 评估是否达到 accept 阈值，标注剩余 gap
- 任何新 worker_done 通知 → 按 audit checklist 审查（数据一致性、GPU 合规、结论可靠性）
- 如果有新实验启动 → 必查 CUDA_VISIBLE_DEVICES 是否在 {0,1} 内

### 5. 🎯 战略上下文
**核心结论链**：
- C1（token-level specialization）：image tokens instruction-blind (10%), readout = multimodal hub (100% from L1)。LIBERO-Goal + Spatial 双 benchmark 验证。最强 claim。
- C2（front-loaded routing）：0→9→25 heads 三级梯度 + entry-exit pattern。Ablation 升级为 partially causal：classification 1.0（residual stream）+ action R² +46%（attention redistribution）。Bootstrap CI 确认 p<0.0001。
- C3（non-monotonic refinement）：inverted-U RSA + DINOv2 ceiling。**最弱 claim**——CKA 反转 RSA ordering 未完全解决，目前靠 method §3.6 + appendix A.2 防守。

**易错点**：
- L1 probe 10% ≠ "无信息"，= "线性不可分"。L0 residual 携带非线性 instruction info，L1 MLP 使其线性可分。ablate_all32 classification 仍 1.0 就是因为这个机制。不要再犯"L0=10% 所以 residual 没信息"的推理错误。
- "+18pp at L31" 是 trained vs **untrained**（随机初始化），不是 trained vs Llama-2 base。VLA fine-tuning 在 L31 的边际效果实际是 0pp（两者都 100%）。Abstract 的 framing 技术上正确（"training" 含预训练+微调）但可被审稿人攻击。
- 99.6% vs 100.0%：前者是 task-level split，后者是 LOOCV。Table 2 caption 已解释。不是 bug。
- CoRL 2026 DDL：Abstract May 26, Paper May 29。距今 9-12 天。


---
