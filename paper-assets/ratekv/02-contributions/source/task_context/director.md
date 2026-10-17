---
loop: 6
reason: max_messages
updated: '2026-05-15T14:31:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目绑定服务器 westd-37397，只能用 cuda:0 / cuda:1（2×RTX PRO 6000 Blackwell 98GB）
- Llama-3.1-8B concentration=0.34, t1/t5=0.71 是实验实测值，**绝对不能改**。Paper Agent 刚完成紧急撤回（从错误的 0.57/0.85 恢复），全文已验证无残留
- 论文 .tex 真源在本地 `projects/ratekv/docs/paper/`，不在远程服务器。改论文只改本地，远程只跑实验
- ARR May 25, 2026 DDL（距今 10 天），审稿分数 R1 2.5/5, R2 2/5 → Weak Reject，目标是补实验+二审翻盘

### 2. 🖥️ 基础设施快照
- 服务器：westd-37397 (connect.westd.seetacloud.com)，账号 root
- 工作目录：/root/ratekv
- GPU：cuda:0 + cuda:1，均空闲（0% util, 0MB used）
- 飞书：A群 oc_e886d722cc0b64fdb553f7bb0b99816c，C群（审稿）oc_ec66209ede0ea4e3bda924778c210d8e
- 论文本地路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/`
- 活跃进程：无（GPU 全空）

### 3. 📊 当前状态
刚处理完 Paper Agent 紧急撤回（Llama 0.57→0.34 revert，5处修改全部验证通过，编译 PASS）。

已派 Agent 并行推进待处理实验（消息已入队）：
- **mistral_hires_bf16_2bitonly_v3** — Mistral-7B hires bf16 2-bit profiling v3 → cuda:0
- **qwen_hires_constrained_d049** — Qwen hires constrained → cuda:1
- 剩余待处理：qwen25-hires-profiling, cross_domain_calibration_v2, greedy_constrained_ablation

Agent 队列深度 1（刚发的指令），等待 Agent 开始执行。

### 4. 📋 待办
- Agent 回复确认实验启动 → 验证两张卡都在跑，确认 plan_id 关联
- mistral/qwen 实验完成 → 立即接力 cross_domain_calibration_v2 + greedy_constrained_ablation 占满 GPU
- 全部 5 个实验完成 → Paper Agent 批量 Patch 写入新数据 → 重新提交二审（submit_paper_to_review, recommended_review_mode="continue"）
- 收到审稿报告 → Read review-report-action.skill.md，按 Holistic Pass + Per-Comment Action Matrix 处理

### 5. 🎯 战略上下文
- 核心 story：KV cache 量化中，不同 attention head 的 bit 分配应该 rate-adaptive（MCKP solver），而非 uniform。Spread 型模型（如 Qwen）收益大，Spike 型（如 Llama）收益小——这是 feature 不是 bug
- 一审 Weak Reject 主因：跨模型验证不足 + baseline 对比缺 KIVI。当前策略是补 Mistral/Qwen14B/KIVI baseline 实验后二审
- Dream best case 4.5/6 Borderline Accept，说明补完实验后有翻盘空间
- 易错点：Paper Agent Patch 写入新数据时容易引入数值错误（刚发生过），patch 后必须 grep 验证所有数值一致性
- 决策日志 60 条，provenance 覆盖率 49/49，实验 87 个（成功 47）
