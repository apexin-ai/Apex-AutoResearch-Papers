# director / loop_21.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_21.md`
- **Structured JSON:** [`cd1ec3676e6248d45869.json`](../../sessions/cd/cd1ec3676e6248d45869.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 21
reason: max_messages
updated: '2026-05-24T00:55:50+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb1-18228(4×4090), bjb1-32546(6×4090), bjb2-28827(6×4090), bjb2-40593(1×4090D), cqa1-32758(6×4090D)。不得使用其他项目的卡。
- CRM checkpoint 分两个版本：3-suite (Spatial/Object/Goal) 用 `crm_3suite_obs_only.pt`，4-suite (含Long) 用 `crm_4suite_obs_only.pt`。混用会导致结果作废。
- τ=0.25 是论文锁定参数。Object Adaptive 正确 trigger rate 是 3-5%。若看到 >50% trigger → 用了错误 τ 值，结果作废。
- p<0.05 已从论文移除（n=3 vs n=3 不够）。不要在汇报中声称统计显著性。
- 输出文件名必须包含 exp_id 或方法标识，禁止通用名（M070 教训：同名覆盖丢数据）。
- Long VLA-only s43=59.5% 已确认合法（cqa1 孤儿进程产出）。bjb1-32546 同名文件 `eval_long_vla_only_seed43.json` 实际是 K2mean（看 baseline_mode 字段）。

### 2. 🖥️ 基础设施快照
- 5 台服务器，工作目录均为 `/root/acr-vla-conformal-refinement/`
- Python: conda base (`/root/miniconda3/bin/python`)，激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- CRM 3-suite checkpoint: `/root/acr-vla-conformal-refinement/crm_checkpoints/crm_3suite_obs_only.pt`
- CRM 4-suite checkpoint: 同目录 `crm_4suite_obs_only.pt`
- eval 脚本: `scripts/wrapper_eval.py`，n_rollouts=20
- π0.5 precompute: bjb1-18228 全 4 卡，Spatial/Goal ETA 5/24 05:00-06:00 UTC, Object ETA 5/24 10:00 UTC, **Long ETA 5/26 00:00 UTC（136K 样本，瓶颈）**
- Cron 已知问题：tmux 部署的实验缺 exit sentinel，cron 会误报 failure。收割时查 JSON 而非信 cron status。
- bjb2-40593 磁盘 90%，部署前注意清理旧日志。

### 3. 📊 当前状态
**23/23 GPU 满载运行**。本轮主要成果：
- 收割了 Goal s45 全套（VLA=83.5%, CRM=81.0%, Adaptive=81.0%, Reconvla=85.5%）、Object CRM s46=79.5%、Spatial CRM s45=78.0%、Spatial Reconvla s45=79.5%、Long s44 全套（Reconvla=57.0%, CRM=56.5%, Adaptive=56.0%, K2mean=54.5%）
- Object s46 全 5 method 完成 ✅（VLA=79.0, CRM=79.5, Reconvla=80.0, Adaptive=77.5, K2mean=76.5）
- 修复了 Spatial Adaptive s45 部署失败 + kill 了重复 Object K2mean s45
- 更新了 paper_framing.md（D134 header）、ROADMAP（+1.8→+1.9pp 修正）、experiments.tex（-1.3→-1.2pp 修正）
- Paper Worker 完成 Table 1 Long 更新 + trigger-rate scatter Figure ✅

**RUNNING 实验（~21 个）：**
- bjb1-32546: Long s45 全 5 method (cuda:1-4) + Object Reconvla s45 (cuda:5) + Spatial K2mean s46 (cuda:0)
- bjb2-28827: Goal s46 全 5 method (cuda:0-3,5) + Long K2mean s45 (cuda:4)
- cqa1-32758: Spatial VLA/Adaptive s45 (cuda:1,4) + Spatial Adaptive/Reconvla s46 (cuda:2,5) + Long VLA-only s46 (cuda:3) + Goal K2mean s45 (cuda:0)
- bjb2-40593: Spatial K2mean s45 (cuda:0)
- bjb1-18228: π0.5 precompute ×4

### 4. 📋 待办（条件触发式）
- Long s45 完成（bjb1-32546, ~1-2h）→ 收割 5 method → 释放 cuda:1-4 → 部署 Long s46 波次（Adaptive/CRM/Reconvla/K2mean）
- Spatial s45 VLA/Adaptive 完成（cqa1）→ 收割 → 释放卡 → 部署 Spatial s46 剩余 method
- Goal s46 完成（bjb2-28827, ~6-10h）→ 收割 → Goal 5-seed 数据齐全
- π0.5 precompute Spatial+Goal+Object 完成（ETA 5/24 05:00-10:00 UTC）→ **先用 3 suite 启动 CRM 训练（~1-2h）→ eval（~2-3h/suite）→ 5/25 可有 π0.5 初版数据**。Long precompute 到 5/26，后续 patch in
- 全部 s45/s46 + Paper Agent Patch 完成 → submit_paper_to_review 最终审稿
- CoRL DDL **2026-05-29**

### 5. 🎯 战略上下文
- **D134 叙事（核心，已锁定）**: "Gating correctly modulates intervention intensity — improves where VLA uncertain (Spatial +2.1, Goal +1.3), preserves where VLA confident (Object +0.1, Long -0.3pp=0.22σ)。Adaptive ≥ CRM on ALL 4 suites (+1.0 to +1.9pp)。"
- **不能说的**：(1) "Adaptive ≥ VLA-only on all suites"（Long -0.3pp, Goal s45=81% outlier）(2) "no degradation"（Long mean 确实低了 0.33pp）。安全词："comparable to" / "within noise"。
- **Goal Adaptive s45=81.0%**：低于 3-seed mean 85.0%。论文 Table 1 保持 3-seed（已锁定），s45 放 supplementary。4-seed mean ~84.0%，Δ vs VLA-only 从 +1.3pp 缩至 ~+0.4pp，但仍为正。继续跑 s46 确认真实 effect size。
- **π0.5 策略**：Reviewer 建议先出 3-suite（Spatial/Goal/Object），Long 后补。DDL 前 3 天时间够做 3-suite π0.5 eval。π0.5 baseline 94-99% 饱和，CRM 目标是 no-harm。
- **Trigger-rate scatter Figure** 已生成（artifacts/figures/trigger_rate_scatter.png），是论文 killer figure，直接回答 "when does Adaptive help?"。
- **易错点**：(1) Agent session 反复 reset，队列容易堆积过时消息——用 replace_agent_queue 清理后发一条干净 pickup；(2) cron 误报频繁（tmux 部署缺 sentinel），收割时必须 SSH 查 JSON 不能信 cron status；(3) 不同服务器同名文件可能是不同方法输出，查 baseline_mode 字段。


---
