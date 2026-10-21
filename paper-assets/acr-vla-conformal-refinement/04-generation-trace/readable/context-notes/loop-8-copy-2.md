# agent / loop_8.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_8.md`
- **Structured JSON:** [`4dbc44209bd39b0ecb5f.json`](../../sessions/4d/4dbc44209bd39b0ecb5f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: idle_timeout
updated: '2026-05-15T09:39:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb1-18228 GPU 白名单: cuda:0,1,2,3（4× RTX 4090）
- bjb1-32546 GPU 白名单: cuda:0,1,2,3,4,5（6× RTX 4090）
- bjb2-28827 GPU 白名单: cuda:0,1,2,3,4,5（6× RTX 4090）
- bjb2-40593 GPU 白名单: cuda:0（1× RTX 4090 D）
- per-DOF claim 在 spatial 上已死（D027: perdof = argmin = 42.9% on T0-T6，0pp delta）。不要再基于 spatial perdof 做任何 positive claim
- eval-acr-spatial-v4-default/small/obs-only/scalar 的 r1 版本被误杀（D026 kill 指令在 Director 撤销前已执行），r2/r3 是重启版本，合并结果时要从 parent 拿已完成 tasks + restart 拿剩余 tasks
- Object eval perdof 前 2 tasks 均 0%（⚠️），不要提前声称 perdof 在 object 上有效

### 2. 🖥️ 基础设施快照
- **bjb1-18228**: 工作目录 `/root/projects/acr-vla-conformal-refinement`，Python `/root/miniconda3/bin/python`，conda base env
- **bjb1-32546**: 同上路径结构，conda base
- **bjb2-28827**: 同上路径结构，conda base
- **bjb2-40593**: 同上路径结构，conda base
- 模型/数据: `/root/autodl-tmp/` 下（各服务器），HF cache `/root/autodl-tmp/.hf_cache`
- 日志统一在 `~/runs/acr-vla-conformal-refinement/` 下
- 活跃进程（reconcile_crons 确认 16 个 RUNNING）:
  - bjb1-18228: PID 311881 (scalar-r2, cuda:1), 312150 (small-r2/perdof, cuda:2), 312420 (obs-only-r3, cuda:3)，cuda:0 刚释放（argmin-r2 完成）
  - bjb1-32546: PID 9659 (reconvla-object, cuda:0), 11116 (perdof-object, cuda:1?), 13797 (obs-only-object, cuda:2), 14003 (scalar-object, cuda:3), 44270 (obs-only-norm02, cuda:4), 18808 (vla-mean-object, cuda:5)
  - bjb2-28827: 6 个 magnitude sweep 进程 (PID 13185-15190, cuda:0-5)
  - bjb2-40593: PID 227434 (obsonly-norm003-b2, cuda:0)

### 3. 📊 当前状态
**刚做完**: 收到 eval-argmin-only-spatial-r2 (argmin baseline T9 重启) 完成回调，已派 Worker `worker_analysis_eval-argmin-only-spatial-r2_20260515T063659` 读日志分析 T9 结果。Worker 尚未返回。

**Parent 数据已提取**: T0-T8 共 33/90 (36.7%)，T9 结果待 Worker 返回。

**RUNNING 实验 (16个)**:
- bjb1-18228 (3/4 GPU): spatial 重启三路 — scalar-r2 (T3起), perdof-r2/small-r2 (T7起), obs-only-r3 (T6起)。cuda:0 刚空出
- bjb1-32546 (6/6 GPU): object 六路 — reconvla, perdof, obs-only, scalar, obs-only-norm02, vla-mean
- bjb2-28827 (6/6 GPU): magnitude sweep — perdof norm 0.03/0.05/0.2/0.3 + obs-only norm 0.05/0.2
- bjb2-40593 (1/1 GPU): obs-only norm 0.03 重提交

**PREPARING (15个)**: eval-acr-object-v4-default, eval-acr-object-v4-scalar-b2, eval-acr-object-v4-obs-only-b2, eval-object-v6-full, eval-reconvla-spatial-v1, precompute-v4-shard0/1/2, eval-spatial-v4-full, precompute-v3-shard2 等

**等待中**:
- Worker 回调: `worker_analysis_eval-argmin-only-spatial-r2_20260515T063659`（分析 argmin T9 日志）
- 16 个 RUNNING 实验的 cron 监控回调
- bjb1-18228 cuda:0 空闲，Worker 回调后应考虑部署新实验

### 4. 📋 待办（条件触发式）
- Worker `analysis_eval-argmin-only-spatial-r2` 返回 → 合并 T0-T9 总成绩 → update_registry(DONE) + 更新 report.md + 汇报 Director（含资源行：cuda:0 空闲）
- bjb1-18228 cuda:0 空闲 → 从 PREPARING 列表选实验部署（优先 eval-reconvla-spatial-v1 或其他 spatial 补充实验）
- bjb1-18228 spatial 三路重启全部完成 → 合并 10-task 完整 matched comparison（argmin vs perdof vs obs_only vs scalar）→ 最终 framing 裁决
- bjb2-28827 magnitude sweep 完成 → norm 敏感性曲线 → perdof claim 最终裁决
- bjb1-32546 object eval 完成 → cross-benchmark validation → 如果 obs_only > perdof across benchmarks → 论文转向 "learned correction"
- 如果项目存活条件 3（obs_only CRM +5pp stable）成立 → 更新 paper_framing.md 转向 "learned correction" narrative → 启动 Paper Agent CoRL 初稿
- 全部四个存活条件均失败 → 汇报 Director 项目 dead

### 5. 🎯 战略上下文
**核心决策链**: D018(输入归一化修复) → D019(magnitude control 必要) → D020(obs_only val_loss 最优) → D022/D023(CoRL 降为单 Claim) → D025(52.5% perdof 数据纠错) → D027(perdof=argmin=42.9% on matched T0-T6, per-DOF claim killed on spatial)

**项目生死线**: 四个存活条件中，前两个（perdof spatial, perdof object）初步趋势均不利。第三个（obs_only CRM）是最可能的存活路径：spatial T0-T5 obs_only 40% > perdof/argmin 35%，magnitude sweep 每个 norm 下 obs_only >= perdof。但目前都只有 2 tasks 数据，需要 5+ tasks 才能定论。

**易错点**:
- 合并 restart 实验结果时，必须从 parent 拿已完成 tasks + restart 拿剩余 tasks，不能只看 restart 的 partial 结果
- ROADMAP 里的 per-task 表是 D027 之前的快照，部分 task 数据来自被 kill 的 r1 版本，r2/r3 重启后的新数据以 r2/r3 日志为准
- Magnitude sweep 仅有 T0/T1 数据（2 tasks），不要过早下结论
- CoRL abstract DDL ~May 26（11 天），时间极紧，所有分析应以"能否写出 positive paper"为导向
- 论文方向很可能转向 obs_only CRM（"learned correction without per-DOF conformal"），但需要 Director 最终裁决，不要自行修改 paper_framing.md


---
