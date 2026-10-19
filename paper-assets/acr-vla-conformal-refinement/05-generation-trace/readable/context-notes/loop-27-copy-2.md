# agent / loop_27.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_27.md`
- **Structured JSON:** [`f84cd723c57d145eacfa.json`](../../sessions/f8/f84cd723c57d145eacfa.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 27
reason: idle_timeout
updated: '2026-05-26T10:06:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**（29卡）：bjb1-18228 cuda:0-3, bjb1-32546 cuda:0-5, bjb2-28827 cuda:0-5, cqa1-32758 cuda:0-5, westd-49937 cuda:0-5, bjb2-24035 cuda:0。白名单外的 GPU 一律不碰，Director 指令也要 push back
- **westd-49937 是 RTX PRO 6000 (Blackwell)**，与 4090 集群存在 ~3pp 系统性偏差（D158）。Table 2 数据必须 same-server paired，westd 数据不能和 4090 直接比
- **evaluate.py 必须用 a594db5 版本**（D163）。所有补跑用旧代码确保 Table 1/2 一致性，不要拉新 commit
- **cqa1-32758 并发 ≤6 个 π0.5 进程**，超过必 OOM。cqa1 上部署 π0.5 前需确认 gemma-2b-tokenizer 完整（之前缺 tokenizer.model 导致崩溃）
- **CoRL 2026 DDL = 2026-05-29**，距今 3 天，一切以论文提交为最高优先级

### 2. 🖥️ 基础设施快照
- **项目路径（所有服务器）**: `/root/acr-vla-conformal-refinement`
- **服务器集群**:
  - bjb1-18228 (4×4090) — SmolVLA + π0.5 eval
  - bjb1-32546 (6×4090) — π0.5 CRM K=2 Object/Goal eval（无 .git，不能回溯版本）
  - bjb2-28827 (6×4090, 1TB RAM) — π0.5 CRM/Adaptive Spatial eval，可跑 6 个 π0.5 同时
  - cqa1-32758 (6×4090D) — π0.5 Adaptive Object/Long + CRM Long eval
  - westd-49937 (6×RTX PRO 6000) — ⚠️ Blackwell 偏差，VLA-only baseline 补跑
  - bjb2-24035 (1×4090D) — 状态待确认
- **CRM checkpoint**: SmolVLA → `.../crm_smolvla_3suite_v1/crm_best.pt`; π0.5 → `.../crm_pi05_unified_3suite/crm_best.pt`
- **Python**: 各服务器 `/root/miniconda3/bin/python`（conda base，不用 venv）
- **活跃 cron 监控**: 10 个（reconcile 确认全部 still running）
  - bjb1-18228: pi05-adaptive-goal-s43-bjb1-18228 (pid=42110)
  - bjb2-28827: pi05-crm-k2-spatial-s42/s43/s44-bjb2-r2 (pid=334539/334906/335268), pi05-adaptive-spatial-s42/s43/s44-bjb2-r2 (pid=335649/336003/刚创建)
  - cqa1-32758: pi05-crm-k2-long-s44-cqa1, pi05-adaptive-object-s42-cqa1, pi05-adaptive-goal-s42-cqa1

### 3. 📊 当前状态
**π0.5 Table 2 数据收集是当前唯一焦点**——DDL 前 3 天，需完成 4 suite × 3 mode × 3 seed = 36 cells。

**RUNNING（18 个实验，24 GPU 活跃）**:
- bjb2-28827 (6/6 GPU): CRM K=2 Spatial s42/43/44 + Adaptive Spatial s42/43/44
- bjb1-32546 (6/6 GPU): CRM K=2 Goal s42/43/44 + Object s42/43/44
- cqa1-32758 (3-6/6 GPU): CRM K=2 Long s44 + Adaptive Goal s42, Object s42, Long s43/s44, Object s44
- bjb1-18228 (1/4 GPU): Adaptive Goal s43

**PREPARING（177 个，大量是早期残留或排队）**:
- 有意义的待部署: pi05-crm-k2-long-s43-r2, pi05-crm-k2-long-s42-r2 (QUEUED), westd VLA-only baseline 补跑

**已完成数据（memory.md）**: π0.5 VLA-only 全 4 suite ✅, CRM K=2 Spatial/Goal/Object ✅, CRM Long ⏳, Adaptive Spatial/Goal/Object/Long 大部分 ⏳

**Worker 池: 0 个运行中**。Paper Agent 已激活但本轮 session 无活跃 Worker。

**等待中**: 所有 18 个 RUNNING 实验的 cron 回调；Paper Agent 写作流水线 Steps 2-5；Director 综合指令的 P0-P3 执行。

### 4. 📋 待办（条件触发式）
- π0.5 CRM/Adaptive Spatial (bjb2-28827) 完成 → 更新 memory.md Table 2 数据，与 VLA-only 97.8% 对比
- π0.5 CRM Goal/Object (bjb1-32546) 完成 → 确认 CRM 退化幅度（已知 Goal -11.7pp, Object -11.3pp from s42 data）
- π0.5 Adaptive Long/Object/Goal (cqa1) 完成 → 补全 Table 2 Adaptive 列，判断 Adaptive 是否缓解 CRM 退化
- **所有 Table 2 cells 就绪** → spawn Worker 写 Table 2 + Discussion/Analysis section + Appendix；spawn Worker 填 paper_provenance.yaml T002
- westd VLA-only baseline 需 same-server paired → 确认 westd 是否还需要跑（如果 4090 集群数据足够则跳过）
- **P0 空闲 GPU 部署**: bjb1-18228 cuda:0/1/2 空闲 + cqa1 空闲卡 → 部署 pi05-crm-k2-long-s42/s43 或 Adaptive 剩余 seeds
- Paper Agent 写作完成 → submit_paper_to_review 最终审稿
- **DDL -1 day (05-28)** → 全部实验必须 DONE，Paper Agent 必须完成所有 section，提交前 reference-audit + paper-visual-review

### 5. 🎯 战略上下文
**核心叙事（D146/D150/D159）**: ACR-VLA 是 Method paper，CRM + Adaptive K 为核心贡献。3 个 Claims:
- MC1 (Consistency): Adaptive ≥ CRM on ALL 4 suites（gating 消除 CRM 退化）。n=3 p≈0.27 n.s.，附录保留 8-seed paired p=0.017
- MC2 (Mechanism): trigger_rate ↔ Δ 单调正相关
- MC3 (Cross-VLA): π0.5 负向 → 改为"模型能力依赖性分析"（D155 reframe），不 claim cross-model generalization

**Table 1 SmolVLA 已锁定** (36/36 cells)。关键 pattern: CRM always-on 在 Object/Long 有害，Adaptive gating 必要。

**π0.5 已知结论**: VLA-only 极强(94-99%)，CRM K=2 在 Goal/Object 导致 -11pp 退化，Adaptive 略好但仍负向。这符合 D155 reframe 预期——不需要 π0.5 positive，只需系统性数据支撑"模型能力依赖性"分析。

**最容易判断错的事**:
1. **不要期望 π0.5 positive results**——π0.5 baseline 饱和，CRM/Adaptive 预期均为 no-harm 或 slightly harmful，这是论文叙事设计的一部分（分析贡献而非 claim 跨模型泛化）
2. **PREPARING 里 177 个实验大量是早期残留**，不要盲目部署——只关注当前 Table 2 需要的 cells
3. **bjb1-32546 无 .git**——不能在上面做代码修改或版本回溯
4. **monitor "失败" 经常是误判**（π0.5 eval 每个 4-6h，monitor 5 次无信号就判 dead）——收到 failed 回调先 SSH 检查进程是否真的死了
5. **Spatial 数据有历史修正**（D159: 78.7±0.3→79.3±0.8），Table 1 Spatial VLA-only 用 79.3±0.8


---
