# director / loop_13.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_13.md`
- **Structured JSON:** [`d79bb6ebf00038e98d41.json`](../../sessions/d7/d79bb6ebf00038e98d41.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_messages
updated: '2026-05-27T04:10:24+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-10894 cuda:0-3 + westd-34685 cuda:0-3，共 8 卡，不得使用其他服务器/GPU
- Detach+LN 数据：v1 checkpoint (detach_ln_s3, CAR=0.765) 不得标为 v2 使用。梯度分析 Detach LN 条件必须等 v2 checkpoint 完成
- D067 决策：Table 1 Detach+LN 标 $^\star$ 省略 ΔCAR（方案 A），不得用 v2 n=1 值替换，等 v2 多 seed 到位再统一更新
- 论文 interaction narrative 不要基于混合 v1/v2 数据做 claim

### 2. 🖥️ 基础设施快照
- **westd-34685** (connect.westd.seetacloud.com): 4× RTX PRO 6000 98GB, /root/occsafe_vla, 磁盘 2% used (819GB 可用)
- **westd-10894** (connect.westd.seetacloud.com): 4× RTX PRO 6000 98GB, /root/occsafe_vla, 磁盘 50% (425GB 可用)
- 梯度分析脚本：run_gradient_analysis_v2.py, compare_gradient_conditions.py, plot_gradient_analysis_v2.py（已多次验证就绪）
- eval 命令文档：artifact eval_commands_batch3.md + batch_eval.sh（已验证）
- Cron：9 个训练监控 cron 曾活跃（但 Agent 连续 5 次 idle 16h，cron 回调未能唤醒 Agent）

### 3. 📊 当前状态
**我（Director）没有执行任何工作**——只做了决策和指令下发。Agent 连续 5 次 reset 后 idle 16h（累计 ~80h），所有指令未被执行。

**训练**（最后确认状态 ~03:40 UTC May 27，距今可能已 80h+）：
- 34685: detach_ln_v2_s1_35 (Cell4 s43), detach_ln_s4 (Cell4 n=5 s46), ablation_occ_detach_s4 (Cell3 n=5 s46), mvp_occ_s4 (Cell1 n=5 s46) — 当时 22-30%，ETA ~12:30-13:21 UTC May 27
- 10894: full_occ_ln_v2_s1c_r2 (Cell2 s43), full_occ_ln_v2_s2_r2 (Cell2 s44), detach_ln_v2_s0c_r2 (Cell4 s42), full_occ_ln_v2_s0d (Cell2 s42) — 当时 14-22%，ETA ~13:39-14:21 UTC May 27

**训练几乎确定已完成**，但 eval、梯度分析、论文修复全未执行。

**CoRL DDL May 28 12:00 UTC 已过**。已通知用户，等用户确认后续安排。

### 4. 📋 待办
- 新 session 启动 → **立即 SSH 两台服务器确认训练完成状态**（不要做 prep，直接 ssh_read_only nvidia-smi + ls checkpoints）
- 训练已完成 → 并行 3 个 Worker：(A) 8 实验 eval, (B) 4-5 条件 v2 梯度分析, (C) D067 论文文本修复
- D067 论文修复清单：Table 1 Detach+LN 加 $^\star$ + ΔCAR→---; caption 改; results.tex L9/L45 修正; Table 2/Figure 2 caption 修正 n 数; appendix.tex L69 删 v1 统计
- 梯度分析 condition_name 用空格不用下划线（Reviewer 后来说 fuzzy matching 能处理，但用空格更安全）
- eval + 梯度分析完成 → ANOVA + Table 1 更新 + 论文最终修订
- 用户回复 DDL 安排 → 按新 DDL 调整节奏

### 5. 🎯 战略上下文
- **核心 claim**：gradient flow 是损害源，detach 后 aux head 无害（≈ Vanilla）。Vanilla n=3 = 0.745±0.024; Detach BN 0.767 ≈ Vanilla (p=0.28 NS); Full OCC BN 0.725 < Vanilla
- **v1 机制证据已推翻**（D056/D057）：gradient collapse + CKA degradation 是 bug 产物。当前可用机制证据：梯度正交性 (cosine≈0) + 方差不对称。v2 梯度分析是重建机制证据的关键
- **最易判断错的事**：v1/v2 数据边界。Table 1/Table 2 中 Detach+LN 和 Random OCC 是 v1 数据，其余是 v2。LN cells 的 n 数不统一（Full OCC+LN n=1 v2, Detach+LN n=3 v1）。不要混用做 interaction 比较
- **M078 教训**：不要依赖 cron 回调唤醒 Agent，关键路径 ETA 后应主动发 urgent_message
- D066 核心修订已完成（R1-R4 baseline fix, F1-F7 hedging/LN rationale）
- PREPARING: full_occ_ln_s4 (Cell 2 n=5 s46) 等 GPU


---
