# reviewer / loop_20.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_20.md`
- **Structured JSON:** [`67a01de4e013ab0feef1.json`](../../sessions/67/67a01de4e013ab0feef1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 20
reason: max_wall_time
updated: '2026-05-25T08:28:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb-23072 cuda:0/1，westd-32935 cuda:0/1/2/3（但 westd GPU 已丢失，实际只有 westb 两张卡可用）
- westd-32935 已无 GPU（nvidia-smi 返回空），但数据盘 /root/autodl-tmp/ 仍可 SSH 读取
- 关键备份已从 westd 迁移到 westb-23072:/root/autodl-tmp/backups/
- EMNLP 2026 ARR DDL：2026-05-25（今天），主文 ≤ 8 页，abstract ≤ 200 words
- RASP 实验只有单 seed（Round 7/8 reviewer 都 flag 了），无法补跑（无 GPU）

### 2. 🖥️ 基础设施快照
- 服务器：westb-23072 (root)，工作目录 /root/recovery_aware_struct_prune
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型路径：/root/autodl-tmp/recovery_aware_struct_prune/（sft_*, grpo_* 子目录）
- 数据集：GSM8K (N=1319), MATH-500 (N=500)
- W&B：项目 recovery_aware_struct_prune
- 匿名仓库：最新 commit f76b29d（含 PaperBanana fig1 重绘）
- 活跃进程：无（所有实验已完成，DDL 前只剩写作修复）
- 本地论文路径：projects/recovery_aware_struct_prune/docs/paper/

### 3. 📊 当前状态
**刚完成**：Round 8 reviewer feedback 独立审查 + TOST 等价性检验审查（PASS），两份报告已 post 给 Director。

**Registry**：无 RUNNING/PREPARING 实验。462 条记录全部 DONE/killed/failed。

**等待中**：Director 可能派 Worker 执行 Round 8 写作修复（Title 改单数、Discussion 扩充、RASP 叙事修正、300步 accuracy 补入 Appendix、TOST ε justify、补 2 篇引用）。我需审查这些 Worker 产出。

### 4. 📋 待办
- Worker 提交 Title/Discussion/Method 修改 → 审查 8 页限制是否溢出（上次 conclusion 多 3 行就超页）
- Worker 补 Appendix E 300 步 accuracy 数字 → 验证 64.37%（CKA-only）和 59.29%（Standard）与 registry 一致
- Worker 修 RASP 叙事 → 确认"α=2.0 比 CKA-only 高 2.2pp"的反驳论据被使用
- Director 转发任何新 reviewer feedback → 按 Round 7/8 相同流程独立审视
- 如收到 paper_agent_request_review → 切换到模式 B，用 §5.3 模板评分

### 5. 🎯 战略上下文
**核心结论链**：diversity-preserving pruning (CKA-only) 使 SFT≈GRPO accuracy（TOST ε=2pp, 7/8 pairs p<0.05），但 GRPO reward 有 4.4× gap → "reward-accuracy decoupling"。RASP α=2.0 是 dose-response 峰值（66.11%），比 CKA-only 高 2.2pp，证明乘法形式不是"CKA in disguise"。

**易错点**：
- 论文的 "mean |Δ|=0.54pp" 来自 Table 2 四种 criteria 主比较，TOST 8-pair pooled mean 是 0.445pp——scope 不同，不矛盾，别当 bug 报
- α=1.0 用 max_completion_length=1024，其他 α 用 512——这个 generation length confound 是 Round 7 MF1，reviewer 反复 flag，但论文已在 footnote + appendix 承认，无 GPU 无法补实验
- 15% sparsity 下 GRPO amplifies gap（与 20% decoupling 不同）——这是 sparsity-dependent 现象，不是矛盾，应框架为 phase transition
- westd 的数据可能是历史残留版本，论文真源在本地 workspace，审查"未修改"类结论前两边都读


---
