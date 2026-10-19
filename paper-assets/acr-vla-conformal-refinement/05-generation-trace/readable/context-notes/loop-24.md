# director / loop_24.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_24.md`
- **Structured JSON:** [`6669ea65b773749e1295.json`](../../sessions/66/6669ea65b773749e1295.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 24
reason: max_messages
updated: '2026-05-26T19:14:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb2-40593 已掉线，不要尝试连接，等用户确认实例状态
- bjb1-18228 之前报告 pi05 376 missing_keys——已确认是正常行为（`_fix_vision_tower_keys`），不是 bug，SR 正常
- cqa1 Long Adaptive r2 的 0% SR JSON 是 OOM 导致的 artifact，绝不能引用。只用 r3 或 bjb1-32546 hedge run 的数据
- π0.5 correction_norm 恒定 0.200（max cap）是真实现象不是 bug，是论文核心发现之一
- DDL：**2026-05-28 20:00 北京时间**，用户明确要求所有实验必须结束

### 2. 🖥️ 基础设施快照
- **bjb1-18228** (4×4090): 上次部署 SmolVLA τ-sweep，可能已完成需收割
- **bjb1-32546** (6×4090): Long Adaptive s43/s44 hedge run (cuda:0/1) + D149 CRM 验证 (cuda:2-5)，可能已完成
- **bjb2-28827** (6×4090): π0.5 τ-sweep (spatial/goal/long s42, τ=0.15/0.35)，部分已完成
- **bjb2-24035** (1×4090D): SmolVLA τ-sweep Object s42 部署中
- **cqa1-32758** (6×4090D): Long Adaptive s43/s44 r3 (cuda:4/5)，30+ min 前 8/10 tasks done，应已完成
- **westd-49937** (6×RTX PRO 6000): Object CRM+Adaptive paired validation，上次 6/6 跑满，可能已完成
- 代码路径: 各服务器 `/root/acr-vla-conformal-refinement/`
- 本地 artifacts: `projects/acr-vla-conformal-refinement/artifacts/` 含 trigger_rate_scatter_data.csv（已有 SmolVLA 数据，π0.5 数据需从 bjb2-28827 JSON 提取补充）

### 3. 📊 当前状态
**Table 2 (π0.5)**: 11/12 cells 完成，仅缺 **Long Adaptive s43/s44**（双线运行中：cqa1 r3 + bjb1-32546 hedge）。

已完成数据：
| Suite | VLA-only | CRM K=2 | Adaptive K=2 |
|-------|----------|---------|--------------|
| Spatial | 98.0±0.5% | 96.8±0.3% | 97.2±0.8% |
| Goal | 96.7±1.0% | 83.5±1.3% | 88.5±1.7% |
| Object | 99.7% (Blackwell) | 88.0±1.0% | 86.2±1.6% |
| Long | 95.0±0.9% | 78.0±3.5% | **TBD** (s42=80.5%) |

**τ-sweep**: Spatial 完成 (τ=0.15/0.25/0.35), Goal τ=0.15 完成 (92%), Goal τ=0.35 + Long τ=0.15/0.35 运行中。

**关键发现已收集**: trigger rate 交叉表 (4 suite × 2 model) + correction_norm 饱和对比。

Agent session 已 idle 16h，需要 RESET 后立即收割 + 部署。大量 GPU 可能已空闲。

### 4. 📋 待办
- Long Adaptive s43/s44 cqa1 r3 或 bjb1-32546 hedge 完成 → 收割数据，Table 2 收官，汇报用户
- Table 2 全部完成 → 更新 ROADMAP + report.md + 通知 Paper Agent 启动/更新写作（D166 narrative）
- τ-sweep 全部完成 → 汇总 τ sensitivity 表格，确认 τ=0.25 非 cherry-picked
- westd paired validation 完成 → 确认跨服务器数据一致性
- scatter_data.csv 缺 π0.5 数据 → 从 bjb2-28827 JSON 提取补充
- 空闲 GPU > 0 → 部署 K=2 VLA-only Object 消融（Reviewer 建议）或其他补充实验
- bjb2-40593 用户回复 → 确认移除或恢复连接
- 实验全部结束 → 考虑启动 Paper Agent 写作流水线（D166 framing 已定稿待 Reviewer 最终确认）

### 5. 🎯 战略上下文
- **D165→D166 决策链**: MC1 从 "Adaptive ≥ CRM on ALL suites" 调整为 "恢复比例 ∝ CRM 危害"。Object Adaptive < CRM 不是弱点而是正面证据（VLA 近天花板时 K=2 noise 抵消恢复）。Reviewer 条件通过，要求论文双维度呈现（trigger rate + correction norm）
- **三层叙事**: (1) gating 自适应 suite 难度 (2) gating 自适应模型能力 (3) correction_norm 饱和解释跨 VLA 退化差异
- **易错点**: Object VLA-only 数据有多源（bjb1-32546 99.7% Blackwell vs 4090），Table 2 主表应用同一 GPU 类型的数据。Goal VLA-only 选了 May24 数据 96.7±1.0%（非 May22 r4 的 97.8%）
- **ROADMAP 已 12h 未更新**，新 session 优先更新
- **Paper Agent 尚未启动 D166 叙事更新**——Table 2 完成后立即通知


---
