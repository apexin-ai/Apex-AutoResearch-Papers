# reviewer / loop_19.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_19.md`
- **Structured JSON:** [`6b836b5b1d2ab1c8bb60.json`](../../sessions/6b/6b836b5b1d2ab1c8bb60.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: max_wall_time
updated: '2026-05-21T01:24:52+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb2-40593=cuda:0; bjb1-18228=cuda:0-3; bjb1-32546=cuda:0-5; bjb2-28827=cuda:0-5
- Cron 系统存在 tmux exit 误报 bug（30+ 次），实验标 "failed" 前**必须 SSH 验证 JSON 是否存在**，不可信 cron conclusion
- Registry 中 conclusion="failed" 的实验可能实际成功（norm01-seed48=18%, norm02-seed43-r3=16% 等已确认被误标），核实前不引用
- π0.5 实验线在 bjb2-40593 上，该服务器只有 1 块 GPU，不可与 norm sweep 争抢

### 2. 🖥️ 基础设施快照
**服务器配置：**
- bjb2-40593: 1×24GB GPU, `/root/acr-vla-conformal-refinement`, python=/root/miniconda3/bin/python
- bjb1-18228: 4×24GB GPU, `/root/acr-vla-conformal-refinement`, python=python（系统）
- bjb1-32546: 6×24GB GPU, `/root/acr-vla-conformal-refinement`, python symlink `/usr/local/bin/python` → miniconda3（修复于 00:30 UTC）
- bjb2-28827: 6×24GB GPU, `/root/acr-vla-conformal-refinement`, python3=/root/miniconda3/bin/python3

**关键路径：**
- CRM checkpoint: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt` (所有服务器)
- SmolVLA: `/root/autodl-tmp/models/smolvla_libero/` (所有服务器)
- π0.5 模型: `/root/autodl-tmp/models/pi05_libero_finetuned/` (仅 bjb2-40593)
- 日志: `/root/autodl-tmp/logs/` (bjb1-32546, bjb2-28827) 或项目内 `logs/` (bjb1-18228)
- JSON 结果: `/root/acr-vla-conformal-refinement/logs/eval_*.json`

**活跃进程 (截至 01:25 UTC)：**
- bjb2-40593: 空（π0.5 待评估代码同步）
- bjb1-18228: 1 进程 (PID 622484, norm005-seed65, cuda:1)
- bjb1-32546: 9 进程（4 GPU 双实验：seed51-r3/seed64@cuda:0, seed52-r3/seed65@cuda:1, seed62-r2/seed64@cuda:3, seed63-r2/seed65@cuda:4; seed64@cuda:5）
- bjb2-28827: 6 进程（seed71-75 on cuda:0-4, old PID 890017 on cuda:5）

### 3. 📊 当前状态
**刚做完：** 发了报告 #43（GPU 回落至 13/17，bjb1-18228 3 GPU 空闲 35 min，bjb2-40593 π0.5 代码未同步）。本 session 共发 15 份报告 (#29-#43)。

**RUNNING 实验 (~18-20)：** 全部是 norm sweep (ε=0.03/0.05/0.1)。seed 范围 51-75。分布在 bjb1-32546 (9 进程)、bjb2-28827 (6 进程)、bjb1-18228 (1 进程)。

**Norm sweep 已验证累计结果：**
- ε=0.03: 15.1% ± 1.2% (n=7, seeds 42-46,56,59)
- ε=0.05: 14.0% ± 1.4% (n=10, seeds 42-45,47-50,55,58)
- ε=0.1: 15.4% ± 3.0% (n=9, seeds 42-44,50-54,57) — 方差异常高
- ε=0.2: 17.2% ± 1.8% (n=12) — LOCKED

**等待中：**
- π0.5 代码同步到 bjb2-40593 + baseline eval 启动
- bjb1-18228 GPU 0/2/3 回填
- bjb1-32546 双实验批次完成（~1-2h 估计）
- Director 对报告 #43 (GPU 空窗模式) 的响应

### 4. 📋 待办（条件触发式）
- bjb1-32546 双实验完成 → 验证 JSON SR 值，更新 norm sweep 累计表，检查是否有 GPU 空闲未回填
- bjb2-28827 seed71-75 完成 → 同上，特别关注 ε=0.1 方差是否收敛
- π0.5 baseline eval 启动 → SSH 验证 evaluate_pi05.py 存在、进程在 cuda:0、参数正确
- π0.5 baseline eval 完成 → 验证 SR，核查 action diversity（flow-matching 应有 diversity，若无则如 OpenVLA 一样是 applicability boundary）
- Norm sweep 全 ε n≥10 → 编译最终统计表发给 Director，重点标注 ε=0.05 是否仍低于 14.3%、ε=0.1 方差是否可接受
- 收到章节审查请求 → 先检查 Agent 是否读过 red-section skill，再按模式 B 五维度审
- Cron on_failed 通知 → 先 SSH 查 JSON 是否存在，存在则忽略（误报概率 >90%）

### 5. 🎯 战略上下文
**核心叙事：** "Correction Over Selection" — CRM correction（修正残差）是提升机制，不是 selection（从 K 候选中选最好的）。Plan A (K=2 + selective CRM) 用 80% 更少 VLA forward 达到同等或更好性能。

**决策链关键节点：**
- D092: Plan A GO — Object 18.3%±2.1%, Spatial 35.0%±1.0%
- D093: OpenVLA CRM 0% — CLOSED, applicability boundary
- D095: π0.5/π 新实验线 — 用户硬要求，验证方法泛化到第二个 VLA backbone

**最容易判断错的事：**
1. **Plan A ≠ Adaptive K**。Plan A 用 `adaptive_conformal_crm` mode（flatten-L2 30D, trigger_rate=84%），Adaptive K 用 `adaptive_k` mode（per-step-mean-L2 7D×5, trigger_rate=22.6%）。两者 threshold τ=0.074855 相同但 uncertainty scale 差 2.77×。不可混淆。
2. **Cron "failed" ≠ 实验失败**。tmux session 替换触发 EXIT_CODE 文件 → cron 误判。必须 SSH 查 JSON。Agent 因此部署了大量不必要的 r2 rerun，浪费 GPU。
3. **ε=0.05 是 norm sweep 最低点** (14.0%)，不是 ε=0.03。paper_framing 声称 "14.3-17.6% all ε" 需修正下界。
4. **Random Selection baseline 已完成** — Object ~10.7% ≈ VLA-only 11.0%，Spatial ~29.3% ≈ VLA-only 29.3%。这是 Claim 1 最强证据，确认 CRM scoring（非 sampling diversity）是提升来源。
5. **GPU 空窗反复出现**：实验完成 → cron 误报 → diagnose worker → 不部署。关注 bjb1-18228 和 bjb2-40593 是否恢复。


---
