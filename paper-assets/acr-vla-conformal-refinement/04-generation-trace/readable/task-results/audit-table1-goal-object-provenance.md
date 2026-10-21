# audit table1 goal object provenance

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_table1-goal-object-provenance_20260525T015038_result.json`
- **Structured JSON:** [`7ac9392cfc529dbf57a0.json`](../../sessions/7a/7ac9392cfc529dbf57a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Audit complete. Here's the full report:

---

## Table 1 Goal + Object 全量溯源审计报告

### Goal Suite — 3 seeds: s42, s43, s44

```
[Goal] [VLA-only] seeds=[s42,s43,s44] = 83.7±1.3%
  s42: SR=83.5%, server=bjb2-28827, nr=20, bm=single, mtime=2026-05-23 17:31 ✓
  s43: SR=82.5%, server=bjb1-32546, nr=20, bm=single, mtime=2026-05-23 21:34 ✓
  s44: SR=85.0%, server=bjb1-32546, nr=20, bm=single, mtime=2026-05-24 00:34 ✓
  重算: mean=83.7%, std=1.3% → Table 1: 83.7±1.3% ✓

[Goal] [CRM] seeds=[s42,s43,s44] = 83.7±1.8%
  s42: SR=85.5%, server=bjb2-28827, nr=20, bm=single, mtime=2026-05-23 14:23 ✓
  s43: SR=82.0%, server=bjb1-32546, nr=20, bm=single, mtime=2026-05-23 18:36 ✓
  s44: SR=83.5%, server=bjb2-28827, nr=20, bm=single, mtime=2026-05-23 20:31 ✓
  重算: mean=83.7%, std=1.8% → Table 1: 83.7±1.8% ✓

[Goal] [Adaptive] seeds=[s42,s43,s44] = 85.0±1.3%
  s42: SR=84.0%, server=bjb2-28827, nr=20, bm=single, mtime=2026-05-23 16:52 ✓
  s43: SR=84.5%, server=bjb1-32546, nr=20, bm=single, mtime=2026-05-23 18:38 ✓
  s44: SR=86.5%, server=bjb1-32546, nr=20, bm=single, mtime=2026-05-23 19:00 ✓
  重算: mean=85.0%, std=1.3% → Table 1: 85.0±1.3% ✓
```

### Object Suite — CRM 3 seeds (s42-s44), VLA-only/Adaptive 5 seeds (s42-s46)

```
[Object] [VLA-only] seeds=[s42,s43,s44,s45,s46] = 77.7±1.3%
  s42: SR=79.0%, server=bjb1-32546, nr=20, bm=single, mtime=2026-05-25 06:41 ⚠️
  s43: SR=77.0%, server=bjb2-28827, nr=20, bm=single, mtime=2026-05-23 14:57 ✓
  s44: SR=77.5%, server=bjb2-28827, nr=20, bm=single, mtime=2026-05-23 14:57 ✓
  s45: SR=76.0%, server=bjb2-28827, nr=20, bm=single, mtime=2026-05-24 04:12 ✓
  s46: SR=79.0%, server=bjb1-32546, nr=20, bm=single, mtime=2026-05-24 03:40 ✓
  重算: mean=77.7%, std=1.3% → Table 1: 77.7±1.3% ✓

[Object] [CRM] seeds=[s42,s43,s44] = 76.5±2.3%
  s42: SR=77.0%, server=bjb1-32546, nr=20, bm=single, mtime=2026-05-23 14:31 ✓
  s43: SR=78.5%, server=bjb1-32546, nr=20, bm=single, mtime=2026-05-23 19:02 ✓
  s44: SR=74.0%, server=bjb1-32546, nr=20, bm=single, mtime=2026-05-23 22:05 ✓
  重算: mean=76.5%, std=2.3% → Table 1: 76.5±2.3% ✓

[Object] [Adaptive] seeds=[s42,s43,s44,s45,s46] = 77.8±2.1%
  s42: SR=81.0%, server=bjb2-28827, nr=20, bm=single, mtime=2026-05-23 17:57 ✓
  s43: SR=77.5%, server=bjb1-32546, nr=20, bm=single, mtime=2026-05-23 19:08 ✓
  s44: SR=75.0%, server=bjb1-32546, nr=20, bm=single, mtime=2026-05-23 22:02 ✓
  s45: SR=78.0%, server=bjb2-28827, nr=20, bm=single, mtime=2026-05-24 04:10 ✓
  s46: SR=77.5%, server=bjb2-28827, nr=20, bm=single, mtime=2026-05-24 04:09 ✓
  重算: mean=77.8%, std=2.1% → Table 1: 77.8±2.1% ✓
```

### Issues

**1. [CRITICAL] Object VLA-only s42 溯源断裂**
- bjb2-28827 上的 s42 文件 `bm=mean`（错误），SR=79.5%
- bjb1-32546 上的 s42 文件 `bm=single`（正确），SR=79.0%，但 **mtime=2026-05-25**（今天）
- 8-seed table（2026-05-24 20:10 生成）显示 Object VLA s42 = "—"（当时不存在）
- Table 1 使用 79.0% 仅匹配今天创建的 bjb1-32546 文件
- D133（2026-05-23 14:26）就引用了 VLA-only 3-seed=77.8%±1.0，暗示 s42=79.0% 的原始文件可能已被覆写

**2. [WARNING] VLA-only 文件 baseline_mode=mean 污染**（不影响 Table 1，但影响 8-seed 扩展）
- bjb2-28827: `eval_object_vla_only_seed42.json`（bm=mean）
- bjb2-28827: `eval_goal_vla_only_seed47.json`（bm=mean）
- bjb2-40593: `eval_goal_vla_only_seed42.json`（bm=mean，SR=85.5%）
- cqa1-32758: `eval_object_vla_only_seed44/45/46.json`（全部 bm=mean）

**3. [WARNING] 跨服务器 SR 不一致**（同 seed，不同 SR，1-2.5pp 差异）
- Goal VLA s42: bjb2-28827=83.5% vs cqa1-32758=82.0%（Δ=1.5pp）
- Goal VLA s43: bjb1-32546=82.5% vs cqa1-32758=83.5%（Δ=1.0pp）
- Object VLA s46: bjb1-32546=79.0% vs cqa1-32758=76.5%(bm=mean)（Δ=2.5pp）
- 部分差异因 bm=mean vs single 导致，部分可能是服务器环境差异

**4. [INFO] Adaptive s47 文件名不一致**：bjb2-28827 上为 `eval_goal_adaptive_conformal_crm_tau0.25_seed47.json`（缺 norm0.2），不影响 Table 1（仅用 s42-s44）

### 结论

**6/6 Table 1 条目数值验证通过**：mean/std 重算完全匹配，n_rollouts=20，baseline_mode=single。

**1 个溯源缺陷**：Object VLA-only s42 的正确文件（bm=single）今天才创建。原始数据源不可追溯——可能是 bjb2-28827 上被覆写的旧文件。数值本身（79.0%）通过了交叉验证（D133 引用的 3-seed mean 与此一致）。

---
