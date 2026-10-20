# director / loop_7.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_7.md`
- **Structured JSON:** [`ad868ef6942ec34ddefc.json`](../../sessions/ad/ad868ef6942ec34ddefc.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-16T20:17:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 bjb1-45299 的 cuda:0 / cuda:1（2×RTX PRO 6000 96GB）
- ManiSkill3 环境需要 resolve_physical_device() 而非 CUDA_VISIBLE_DEVICES stash（SAPIEN 要求移除 CVD）
- submit_training_job 注入 CVD 后逻辑设备变 cuda:0，训练脚本用 --device cuda:0 而非物理 GPU ID
- exp_018 (原版) 已作废（D065）——gate_enabled=false 导致 full_sgs 空操作。论文中所有 018 数据已替换为 018v2
- NVE baseline 定义：exp_001 seed 1 的 v/e trajectory。论文中 NVE = ve_ratio / baseline_ve
- 008e_v3_s2 �� NVE false positive（Pathway B, 非 CIVO）— 不归为 CIVO 失败
- Bootstrap CI 中 full_sgs 条件只含 018v2（不含已作废的 018），no_dt_emb 不含 020（020 是 vanilla_baseline 条件）

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299 (connect.bjb1.seetacloud.com)，root 用户
- 工作目录：/root/autodl-tmp/event-gated-adaptive-horizon
- Python：/root/miniconda3/bin/python（conda base 环境）
- 论文源码：本地 projects/event-gated-adaptive-horizon/docs/paper/sections/*.tex
- 审稿群：review_chat_id = oc_dd4a07a509df7e5f9a31d65f776059bc
- 活跃进程：018_full_sgs_s2 (cuda:0, PID 612876, ~15K/105K), cuda:1 刚完成 008f_s3（空闲，待提交 019a ManiSkill）
- D1 seed 脚本已就绪：scripts/exp_008d_civo_trigger_s2.sh, scripts/exp_018_full_sgs_s2.sh

### 3. 📊 当前状态
本轮完成了大量工作：
- 018v2 Full-SGS 确认消除 CIVO（NVE≤1.66× peak, eval=448.3=49% baseline, D067/D068）
- 010b Cheetah 跨环境验证（NVE 14.59×, D066）
- 020 C6 Pathway B 控制确认（vanilla s2 stable 837 vs trained dt_emb s2 collapsed 137, D069）
- 008f_s3 no_dt_emb seed 3 完成（n=3 闭合，0/3 CIVO）
- 论文 8 页主体达标（CoRL 模板），所有 claim 修正完成
- Bootstrap CIs 完成并修正（full_sgs n=1, no_dt_emb n=3, cross_env 7/8）
- 梯度正反馈机制发现（008d obs 25→93% vs 018v2 11→24%）
- Dream dream_20260516T172011 应该已完成但回调未收到，需检查

RUNNING：exp_018_full_sgs_s2 (cuda:0, ~2-3h remaining)
空闲：cuda:1（Agent 在准备 019a ManiSkill 重新提交）
Paper Agent 最后指令：恢复 abstract "(Walker Walk)" 标注

### 4. 📋 待办
- 018_full_sgs_s2 完成 → 分析 NVE（如<1.5× 且无 collapse → SGS n=2 闭合，论文 reproducibility 补强）→ 提交 008d_s2 到 cuda:0
- cuda:1 空闲 → 提交 019a_v2 PickCube baseline（ManiSkill3，用户要求）→ 完成后 019b CIVO trigger
- dream_20260516T172011 结果 → 读 dream-report-action skill → 执行行动项
- 018_s2 + 008f_s3 完成后 → 更新 bootstrap CI → 如 SGS n=2 CI 不跨零 → 论文加 "statistically significant" 语言
- 所有实验完成 → 提交论文给 Review Director（submit_paper_to_review���

### 5. 🎯 战略上下文
核心因果链：trained dt_emb → obs decoder gradient 正反馈（25%→93%）→ CIVO (NVE>1.5×) → collapse。Full-SGS 阻断反馈环路（obs 保持 11-24%）→ NVE peak 1.66×（transient, 非 sustained）→ 无崩溃。

**最容易判断错的事：**
1. 018v2 的 NVE peak 是 1.66×（35K+ window），不是 4.01×（25K pre-threshold noise）——论文和 CI 都应用 35K+ 窗口值
2. "substantially mitigates" 不是 "completely eliminates"——018v2 有 transient exceedances，CIVO 定义已精化为 sustained escalation + collapse
3. Reviewer 最大攻击面是 SGS n=1（018v2 单 seed）——018_full_sgs_s2 正在跑就是为了补这个
4. 论文 abstract 的 "(Walker Walk)" 是正确的（n=8 分类全是 Walker），不要改成 "primarily Walker Walk"
5. ManiSkill3 是用户 (吴俊豪 5/15) 明确要求的——不能因 reset 再丢
6. Dream 的旧版本（D064 基于错误 018）结果打折扣；新 dream (dream_20260516T172011) 基于真实数据，其结果才有参考价值


---
