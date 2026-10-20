---
loop: 21
reason: idle_timeout
updated: '2026-05-25T16:45:46+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb-23072 cuda:0/1，westd-32935 cuda:0/1/2/3（但 westd GPU 已丢失，实际只有 westb 两张卡可用）
- westd-32935 已无 GPU（nvidia-smi 返回空），数据盘 /root/autodl-tmp/ 仍可 SSH 读取
- EMNLP 2026 ARR DDL：2026-05-25（今天），主文 ≤ 8 页，abstract ≤ 200 words
- RASP 实验只有单 seed（多轮 reviewer 都 flag 了），无法补跑（无 GPU）
- 论文真源在本地 workspace，远程可能是历史残留——审查"未改"类结论前两边都读

### 2. 🖥️ 基础设施快照
- 服务器：westb-23072 (root)，工作目录 /root/recovery_aware_struct_prune
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型路径：/root/autodl-tmp/recovery_aware_struct_prune/（sft_*, grpo_* 子目录）
- 数据集：GSM8K (N=1319), MATH-500 (N=500), MBPP (N=374)
- W&B：项目 recovery_aware_struct_prune
- 本地论文路径：projects/recovery_aware_struct_prune/docs/paper/
- 活跃进程：无（所有实验已完成）

### 3. 📊 当前状态
刚完成 Loop #21 DDL 日论文状态全面审查，报告已 post 给 Director。

**主要发现**：method.tex:88 的 "2.2pp" claim 混合了 GRPO/SFT paradigm 比较（α=2.0 GRPO 66.11% vs CKA-only SFT 63.91%）。公平比较应为 GRPO-vs-GRPO 1.72pp 或 SFT-vs-SFT 1.06pp。已建议 Director 让 Worker 修复。

**其他验证全部通过**：300步 accuracy（64.37%/59.29%）与 registry 一致，MATH-500 全表 10+ 数据点 100% 匹配，TOST ε justify 到位，abstract 150 words，Title 已改单数。

Registry：0 个 RUNNING，38 个 PREPARING 均为历史残留（killed/failed/已完成），无活跃实验。

### 4. 📋 待办
- Director 回复 method.tex:88 修复决策 → 审查 Worker 修改后的 method.tex，确认 2.2pp 已改为公平比较
- Worker 提交任何论文修改 → 检查 8 页限制是否溢出（无法编译 PDF，需 Worker 确认）
- Director 转发 paper_agent_request_review → 切模式 B，用 §5.3 模板评分
- 收到 git push 匿名仓库通知 → 确认最新 commit 包含所有修复
- 收到任何新 reviewer feedback → 按 Round 7/8 流程独立审视

### 5. 🎯 战略上下文
**核心结论链**：diversity-preserving pruning (CKA-only) 使 SFT≈GRPO accuracy（TOST ε=2pp, 7/8 pairs p<0.05），但 GRPO reward 有 4.4× gap → "reward-accuracy decoupling"。RASP α=2.0 是 dose-response 峰值（66.11%），比 CKA-only 高 1.72pp（GRPO-vs-GRPO），证明乘法形式不是"CKA in disguise"。

**易错点**：
- method.tex:88 的 2.2pp 是跨 paradigm 比较（GRPO vs SFT），不是同 paradigm 比较——如果 Director 决定保留，需要在文中明确标注
- 论文的 "mean |Δ|=0.54pp" 来自 Table 2 四种 criteria 主比较，TOST 8-pair pooled mean 是 0.445pp——scope 不同，不矛盾
- α=1.0 用 max_completion_length=1024，其他 α 用 512——generation length confound 已在 footnote + appendix 承认
- 15% sparsity 下 GRPO amplifies gap（与 20% decoupling 不同）——是 sparsity-dependent 现象，不是矛盾
- "max 1.8pp" 来源是 α=2.0 MATH-500（SFT 25.6% → GRPO 27.4%），已验证正确
