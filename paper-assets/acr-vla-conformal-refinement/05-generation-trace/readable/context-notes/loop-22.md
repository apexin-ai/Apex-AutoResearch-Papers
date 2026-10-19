# director / loop_22.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_22.md`
- **Structured JSON:** [`0349ac1a2c86b0e5cd21.json`](../../sessions/03/0349ac1a2c86b0e5cd21.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 22
reason: max_messages
updated: '2026-05-25T17:40:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- 方法固定 K=2 + gating（evaluate.py adaptive_conformal_crm 硬编码 K=2，--K 参数无效）。所有 Adaptive 实验必须 `--K 2 --conformal_threshold 0.25`
- GPU 只能用项目已分配的 5 台服务器：bjb1-18228(4卡), bjb1-32546(6卡), bjb2-28827(6卡), bjb2-40593(1卡), cqa1-32758(6卡)
- π0.5 Adaptive 已修复 OOM（evaluate.py 加了 gc.collect+empty_cache），修复版已同步全部 5 台。修复前的旧 evaluate.py 不能用于 π0.5 Adaptive
- Worker auth 系统性故障未恢复，所有 SSH 操作需直接 Bash SSH（ssh_read_only / ssh_execute）
- D149 Table 1 seed 方案锁定：Spatial s47/s48/s49，Goal/Object/Long s42/s43/s44。不要用其他 seed

### 2. 🖥️ 基础设施快照
- **bjb1-18228** (4 GPU 4090): connect.bjb1.seetacloud.com, /root/acr-vla-conformal-refinement
- **bjb1-32546** (6 GPU 4090): connect.bjb1.seetacloud.com, /root/acr-vla-conformal-refinement
- **bjb2-28827** (6 GPU 4090): connect.bjb2.seetacloud.com, /root/acr-vla-conformal-refinement
- **bjb2-40593** (1 GPU 4090): connect.bjb2.seetacloud.com, /root/acr-vla-conformal-refinement
- **cqa1-32758** (6 GPU 4090): connect.cqa1.seetacloud.com, /root/acr-vla-conformal-refinement
- Python: conda base（aml-train 镜像），`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- CRM checkpoints: SmolVLA ~/crm_checkpoints/obs_only_4suite_unified/; π0.5 ~/crm_checkpoints/crm_pi05_unified_3suite/
- 论文源码: 本地 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/
- 最后审计时 GPU 8/23 在用（实验完成后大量空闲未重新部署）

### 3. 📊 当前状态
刚发了 URGENT 指令让 Agent 做全服务器审计 + harvest + 重新部署。之前因 RESET_BOTH 流程卡住（WRITE HANDOFF 未到达）导致系统停摆 ~1h，GPU 从 23/23 掉到 8/23。

**关键实验状态（大概率已完成待 harvest）**：
- π0.5 Adaptive Goal s42 全量（cqa1 cuda:0）— trigger_rate=22.6%（dry-run），全量 10-task SR 未知，这是 MC3 叙事关键数据
- CRM Spatial s47 re-run（bjb1-32546）— 原值 52% 异常，task 1 re-run = 95%，应已完成
- SmolVLA Adaptive Long s42/s43/s44（bjb2-28827）— Table 1 最后缺口
- SmolVLA CRM Wave 1 剩余（bjb1-32546 6 GPU）— Goal s43/s44, Object s42/s43/s44, Spatial s48
- π0.5 CRM（cqa1 5 GPU）— Goal s42/43/44, Spatial s42/43

**Table 1 填充度**：发 handoff 前 9/12 完成，Long Adaptive + 部分 CRM 在跑

### 4. 📋 待办
- Agent 回复全服务器审计 → harvest 所有已完成实验 → 更新 Table 1 D149 数据
- π0.5 Adaptive Goal 全量 SR 出来 → 如果 Δ≈0 或正向 → MC3 "cross-VLA compatible" 成立，post_to_reviewer 确认叙事；如果 Δ<-10pp → MC3 降级为 limitation，π0.5 不进 Table 2
- Table 1 SmolVLA 12/12 填满 → 更新 ROADMAP → director_post_to_paper_agent 写最新摘要
- CRM Wave 2（Long s42/s43/s44）如未完成 → 部署到空闲 GPU
- π0.5 VLA-only Goal/Object 未部署 → CRM 完成后释放 GPU 部署
- 所有数据齐全 → Paper Agent 写摘要 + submit_paper_to_review

### 5. 🎯 战略上下文
- **CoRL 2026 DDL 2026-05-29**（≤4 天）。Method paper，核心贡献 = K=2 + CRM + Adaptive gating
- **Claim 策略 (D146/D150)**：Spatial 做 magnitude claim (p<0.05, n=8)；Goal/Object/Long 做 mechanism claim（trigger rate ↔ Δ 单调正相关）
- **π0.5 trigger_rate 22.6%** 已被 Reviewer 确认为 info 级（τ=0.25 适配），但全量 SR 未出。Reviewer 注意到 π0.5 trigger 比 SmolVLA 高 2.7×（可能 action diversity 差异），全量数据出来后需检查
- **易错**：(1) 不要把 dry-run 单 task SR=65% 当全量推断（Reviewer 已标记不可引用）；(2) Object Adaptive ≈ VLA-only (Δ≈0) 是预期结果（trigger 4%），不是 bug；(3) CRM always-on 在 Object/Long 上有害（-1.2pp/-2.2pp），这是 Adaptive gating 必要性的核心证据
- **M093 教训**：大模型 Adaptive 部署前必须做 dry-run 验证显存，π0.5 3.6B + K=2 在 4090 24GB 上 margin 只有 ~10GB


---
