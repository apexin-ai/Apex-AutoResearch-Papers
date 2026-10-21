# director / loop_17.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_17.md`
- **Structured JSON:** [`789fe5f9cc41a01770de.json`](../../sessions/78/789fe5f9cc41a01770de.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: max_messages
updated: '2026-05-22T18:15:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- **Method paper 定位**（用户最高权限指令）— 不是 analysis paper，CRM + Adaptive K 必须是核心贡献
- **Adaptive K 必须是核心贡献** — 禁止固定 K 暴力多推理（用户明确指令）
- **Wrapper pipeline 一致性** — D122/D123: precompute 和 eval 都必须用 SmolVLAWrapper（不是 lerobot native），保证分布一致。Native precompute 已停止
- **π0.5 必须用 n_action_steps=10**（官方设定）
- **bjb2-28827 有 36 分钟进程超时** — Long suite 任务（~58min）禁止在此服务器运行，必须用 bjb1
- **CRM r4 训练 PID 322367 (bjb1-32546:cuda:3) 不要动** — cron 多次误报将其标为 failed，实际正常运行。Registry 用 r5 continuation 跟踪
- **2-model paper (D124)** — OFT 已放弃，锁定 SmolVLA + π0.5

### 2. 🖥️ 基础设施快照
- **bjb1-18228** (4×4090): `/root/acr-vla-conformal-refinement/`
- **bjb1-32546** (6×4090): `/root/acr-vla-conformal-refinement/`
- **bjb2-28827** (6×4090): `/root/acr-vla-conformal-refinement/`，有 36min 超时限制
- **bjb2-40593** (1×4090D): 已释放（D124 放弃 OFT）
- SmolVLA checkpoint: `lerobot/smolvla_libero` (v2)，π0.5 用 openpi 官方
- SmolVLA precompute cache: `/root/autodl-tmp/crm_cache_smolvla_k10/`（object/spatial/goal 完成，long 正在跑）
- π0.5 precompute cache: `/root/autodl-tmp/crm_cache_v5/`（4 suite 完成）
- 活跃进程:
  - SmolVLA CRM 3-suite training: bjb2-28827:cuda:0, PID 344463, tmux `train-crm-smolvla-3suite-v1`, **ETA ~07:30 UTC May 23**
  - CRM r4/r5 unified (π0.5): bjb1-32546:cuda:3, PID 322367, **ETA ~07:00-15:30 UTC May 23**（Reviewer 说 epoch 16/50 ~13h）
  - SmolVLA Long precompute (wrapper): bjb1-18228:cuda:2, ~50min（可能已完成）
  - SmolVLA Long 3-seed baseline: bjb1-32546:cuda:0-2, ~25min（可能已完成）

### 3. 📊 当前状态
刚完成：D123 停止 native precompute、D124 放弃 OFT、π0.5 Long seed42 rerun 确认 94.0%、GPU 5 rogue 进程清理、Reviewer critical registry 修复指令已发。

Registry RUNNING: `train-crm-unified-4suite-r5`（π0.5 CRM），`train-crm-smolvla-3suite-v1`（SmolVLA CRM）。

等待：Agent 确认 r5 registry 状态正确 + SmolVLA Long precompute/baseline 结果回调 + 两个 CRM 训练完成后的 eval 部署。

### 4. 📋 待办（条件触发式）
- **SmolVLA CRM 训练完成**（~07:30 UTC May 23）→ 立即部署 3-suite ACR-VLA eval（Object+Spatial+Goal, adaptive_conformal_crm mode, seeds 42/43/44, wrapper pipeline）。Eval 命令模板已由 Agent 准备好。这是论文主要正面结果
- **CRM r4/r5 训练完成**（~07:00-15:30 UTC May 23）→ 部署 π0.5 4-suite ACR-VLA eval（adaptive mode, 3 seeds）。预期 no-harm（≥95%）
- **SmolVLA Long precompute 完成** → 确认 long/ 数据在 crm_cache_smolvla_k10/，如果 3-suite CRM 效果好，考虑训练 4-suite CRM
- **SmolVLA Long 3-seed baseline 完成** → 记录 mean±std，更新 ROADMAP SmolVLA baseline 表
- **SmolVLA CRM eval 结果出来** → 如果 3-suite 全部 positive（>baseline），立即启动 paper writing（director_post_to_paper_agent）
- **π0.5 CRM eval 显示退化** → 必须用 adaptive 模式（always-correct 已知有害 ~20pp 退化），检查是否正确配置了 adaptive_conformal_crm 而非 acr_vla

### 5. 🎯 战略上下文
- **核心 story**: SmolVLA（15.7-66.5% baseline）是 CRM 主要验证模型（有改进空间），π0.5（95-99%）是 no-harm 验证。CoRL DDL 2026-05-29，≤7 天
- **决策链**: D117(正确baseline先行) → D118(π0.5饱和) → D119/D120(lerobot官方代码) → D122(wrapper数据先行) → D123(停native) → D124(放弃OFT,2-model)
- **最易判断错的事**: CRM r4/r5 registry 混乱 — r4 被 cron 误标 failed 但训练正常，r5 是 continuation entry 跟踪同一 PID。不要因为 r4=failed 就重启训练
- **always-correct vs adaptive**: π0.5 上 acr_vla（always-correct）模式导致 ~20pp 退化（~80% vs 99.3%），论文必须用 adaptive_conformal_crm 模式（选择性纠正）。这是 Adaptive K 贡献的核心验证点
- **M055/M057 教训**: wrapper 有 image flip bug 导致与 lerobot 官方 eval 分布不一致，但 D122 决定 wrapper 内部一致即可。GPU 5 出现过进程自动重启幽灵，kill 后要验证不再复活


---
