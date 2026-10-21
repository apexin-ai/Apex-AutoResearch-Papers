# director / loop_13.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_13.md`
- **Structured JSON:** [`5d6da47b5438c8482a48.json`](../../sessions/5d/5d6da47b5438c8482a48.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_messages
updated: '2026-05-21T02:44:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb2-40593 cuda:0, bjb1-18228 cuda:0-3, bjb1-32546 cuda:0-5, bjb2-28827 cuda:0-5。严禁使用白名单外 GPU
- 每 GPU 只能跑 1 个 LIBERO eval 进程（M034: 双进程导致 rollout 动态显存增长→OOM kill，无 traceback）
- Cron 报 failed 时 **必须先 ssh_read_only `ps -p PID` + 检查 JSON 是否完整**，不验证不改 registry（M035: 已 4 次误标活跃实验为 failed）
- Adaptive K 必须是核心贡献（用户硬要求），固定 K=10 是 analysis baseline
- Plan A 代码 hardcode K=2，永远不扩展到 K=10。argmin-to-centroid（不是 sample mean）
- OpenVLA CRM 实验线已 CLOSED (D093, 0% SR)，不再追加

### 2. 🖥️ 基础设施快照
- **bjb2-40593** (1×4090): connect.bjb2.seetacloud.com, /root/acr-vla-conformal-refinement, conda base
- **bjb1-18228** (4×4090): connect.bjb1.seetacloud.com, 同上路径, conda base
- **bjb1-32546** (6×4090): 同上, conda base. python3 需 symlink `/usr/local/bin/python`
- **bjb2-28827** (6×4090): connect.bjb2.seetacloud.com, 同上. python3 同样需 symlink
- CRM checkpoint: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`
- SmolVLA: 自动从 HF 加载 (~5.7GB VRAM)
- π0.5: `lerobot/pi05_libero_finetuned` 已下载到 bjb2-40593 (~8.7GB VRAM), wrapper 在 `src/pi05_wrapper.py`
- 活跃进程: bjb2-40593 PID 802639 (π0.5 baseline eval, ~2-3h), bjb1-18228/32546/28827 多个 norm sweep eval
- 论文: `projects/acr-vla-conformal-refinement/paper/main.tex`, Paper Agent session 活跃

### 3. 📊 当前状态
**π0.5 baseline eval 运行中** (bjb2-40593, LIBERO-Object, seed42, 10 tasks × 20 rollouts, 预计完成时间 ~03:30 UTC)。Task 1 alphabet_soup = 0%，需更多 task 数据。归一化风险待观察 (MEAN_STD vs QUANTILES)。

**Norm sweep 运行中** (~13-16 GPU): seed66×3 (bjb1-18228), seed71-75 (bjb2-28827, seed71 ~77% done), bjb1-32546 双实验批次。我刚发了指令让 Agent 填 3 个新空闲 GPU (seed67)。

**Registry 需修正**: seed60(killed→success,15%), seed65(failed→success,14%), seed56(RUNNING→DONE,15%), seed66×3(failed→RUNNING)。已发指令给 Agent。

**Paper Agent**: Plan A 整合完成 (Abstract/Intro/Table 1/§4.3/Conclusion), "80% fewer VLA forward passes" 修正完成, trigger rate 诚实度已加, 主体 8 页。

### 4. 📋 待办
- π0.5 baseline eval 完成 → 检查 SR。若 >50%: 检查 action diversity (K=2 L2 distance)，若 stochastic → precompute features (2048D) → 训练 projection layer (Linear 2048→960, 复用现有 CRM) → Plan A eval。若 SR 异常低: 优先查归一化 (MEAN_STD vs QUANTILES)
- Norm sweep seed 完成 → 收集结果更新 norm sweep 表。当前: ε=0.03 mean~14.3% (seeds: 13,15,15,...), ε=0.05 mean~14% (14,16,15,...), ε=0.1 mean~17% (19,15,...)
- Norm sweep GPU 释放 → 重定向到 π0.5 多 seed eval 或 Plan A π0.5 eval
- 用户未回复 threshold calibration 两个方向（1: 强调 K=2 efficiency, 2: recalibrate Pareto sweep）→ 等用户回复，不主动选
- Paper Agent 完成后 → 考虑 submit_paper_to_review 提交新一轮审稿

### 5. 🎯 战略上下文
**CoRL 2026 DDL 2026-05-29 (7 天)**。核心方法 Plan A: K=2 batched → L2 uncertainty → selective CRM, Object 18.3%±2.1%, Spatial 35.0%±1.0%。

**π0.5 是 DDL 前最关键实验** — 同时解决 M1 (narrow scope, 标题说 "VLAs" 复数但只测了 SmolVLA) 和 R2-W1-new (11% absolute SR 太低)。如果 π0.5 baseline 72% + CRM 有效，论文从 weak accept 提升到 borderline accept 以上。

**决策链**: D092 Plan A GO → D093 OpenVLA CLOSED → D094 Plan A Spatial → D095 π0.5/π 实验线 → D096 π0.5 适配 GO

**易错点**:
- Plan A 的 uncertainty metric (flatten-L2 30D) 和 Adaptive K 的 (per-step-mean-L2 7D) 不同，阈值不可互换 (ratio ~2.77×)
- Cron 系统性误报：eval 脚本不写 sentinel/W&B → cron 总报 failed。必须 SSH 验证
- bjb1-18228/32546 的 python3 不在 PATH，需要 symlink 或 conda activate
- π0.5 CRM 不能直接迁移 (obs_dim 2048 vs 960)，需 projection layer


---
