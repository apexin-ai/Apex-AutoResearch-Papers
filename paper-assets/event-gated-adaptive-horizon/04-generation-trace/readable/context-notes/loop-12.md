# director / loop_12.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_12.md`
- **Structured JSON:** [`a7cfca18c121f0bda8a1.json`](../../sessions/a7/a7cfca18c121f0bda8a1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_messages
updated: '2026-05-25T14:30:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb1-45299 cuda:0/1, westd-19154 cuda:0/1，共 4 张，严禁用其他卡
- ICML 2026 DDL 5/29，数据锁定 5/27——剩 2 天锁数据，任何新实验必须能在 5/27 前出结果
- CIVO scope 已精确化为 "multi-joint locomotion"（D149），不要再用 "DMC locomotion" 的旧表述
- D146 已正式撤回 PegInsertion 混合机制 claim，不要重提
- exp_079 frozen dt_emb walker 被 killed（不是 negative），plan_015 尚未有效完成

### 2. 🖥️ 基础设施快照
- **bjb1-45299**: connect.bjb1.seetacloud.com, RTX PRO 6000 96GB ×2, 工作目录 /root/autodl-tmp/event-gated-adaptive-horizon
- **westd-19154**: connect.westd.seetacloud.com, 工作目录同上
- Python: /root/miniconda3/bin/python（conda base 环境，不用 venv）
- 磁盘充裕：bjb1 399G/439G, westd 816G/879G
- W&B 未配置，无 HF cache 依赖
- 审稿 chat_id: oc_dd4a07a509df7e5f9a31d65f776059bc（Round 5 审稿中）

### 3. 📊 当前状态
4 GPU 满载运行：
- exp_080_008e_v3_walker_s1 (bjb1 cuda:1) — Walker mitigation seed=1，plan_014
- exp_081_008e_v3_walker_s2 (bjb1 cuda:0) — Walker mitigation seed=2，plan_014
- exp_082_cheetah_no_dt_emb_s0 (westd cuda:0) — Cheetah causal control dt_embed_dim=0，plan_022
- exp_083_cheetah_baseline_s1 (westd cuda:1) — Cheetah baseline seed=1，plan_020，刚提交

刚收到 Reviewer PASS 报告确认 exp_077/078 Cheetah 对：
- exp_077 baseline: eval=448.1, 健康基线
- exp_078 CIVO trigger: peak NVE 3.1×, CIVO 确认跨环境成立。注意 Cheetah 有部分自校正（eval 从 26 恢复到 119.5=baseline 27%），分类时需明确标准

Agent 启动了 LOCO-CV（n=56 leave-one-config-out 阈值验证）和 ROADMAP 刷新 Worker，尚未回调。

### 4. 📋 待办
- exp_080/081 完成 → 分析 Walker mitigation 3-seed 统计，更新论文 C6 claim
- exp_082 完成 → 与 exp_078 构成因果对，确认 trained dt_emb 是 Cheetah CIVO 必要条件
- exp_083 完成 → 与 exp_077 构成 Cheetah baseline 2-seed 校准
- LOCO-CV Worker 回调 → 结果写入 appendix（阈值稳健性验证）
- Round 5 审稿报告回来 → 按 review-report-action skill 处理，必须先 Holistic Pass 再逐条 Action Matrix
- 所有实验完成 + 审稿反馈整合 → 5/27 数据锁定 → 5/29 提交

### 5. 🎯 战略上下文
- 核心 story：DreamerV3 中 trained dt_embedding 驱动 CIVO，是 multi-joint locomotion 特异性现象，frozen/removed dt_emb 可阻止
- 159 个实验（80 success），论文 7 页 + appendix，ICML 模板，Round 5 审稿中
- Cheetah 扩展刚确认 CIVO 跨环境（exp_078 NVE 3.1×），但 Cheetah 有部分自校正特征——论文当前说 "6/7 sustained collapse, 1/7 self-correcting"，加入 Cheetah 数据后需更新这个统计
- exp_079 frozen dt_emb 被 killed（plan_015），2×2 ablation 矩阵（trained/frozen × exposed/unexposed）缺这一格，但时间紧可能无法重跑
- 15 条 rebuttal Q&A 已完成
- 易错点：不要混淆 Walker 的 CIVO（持续崩溃）和 Cheetah 的 CIVO（部分自校正）——分类标准需统一


---
