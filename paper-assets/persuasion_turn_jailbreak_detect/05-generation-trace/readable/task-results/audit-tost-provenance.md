# audit tost provenance

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_tost-provenance_20260525T202512_result.json`
- **Structured JSON:** [`4541747b2d6888f7f2b6.json`](../../sessions/45/4541747b2d6888f7f2b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完毕。以下是完整追溯结果。

---

## 结论：d=0.44 来源已确认

**d=0.440 来自 exp41_tost_10seed，于 2026-05-22T03:27–03:53 执行，数据真实存在且可验证。**

---

## 完整追溯链

| 层级 | 文件/位置 | 内容 |
|------|-----------|------|
| 论文 | `docs/paper/appendix.tex:325` | `ActorAttack & .183 & 0.440 & --` |
| 本地 summary | `artifacts/exp41_tost_10seed/data/exp41_tost_10seed_summary.txt` | `AA OOD: p=0.183, NOT EQUIV, Cohen d=0.440` |
| 本地 checkpoint | `checkpoints/exp41_tost_10seed_DONE_20260522T035353.json` | `tost_AA.cohens_d: 0.44` |
| 服务器结果 | `/root/.../results/exp41_tost_10seed_analysis.json` | `cohens_d: 0.4397329954223104` |
| 服务器脚本 | `/root/.../scripts/exp41_tost_10seed.py` | 完整训练+TOST计算代码 |

---

## 实验机制

exp41 的做法：
1. 从 exp39 继承 **前 5 seeds** (42, 123, 456, 789, 1000) 的 F1 值（hardcoded 在脚本的 `PRIOR_F1` dict 中）
2. 新训练 **5 seeds** (2024, 2025, 2026, 314, 628)，每个 seed 训练 9-class 和 scrambled 两个模型
3. 合并 10 seeds 的 F1 值跑 paired TOST

### 关键数值（服务器验证）

**AA OOD F1 (10 seeds)**:
- 9-class: `[0.990, 0.935, 0.990, 0.972, 0.972, 1.000, 0.981, 1.000, 0.981, 0.972]`
- Scrambled: `[0.891, 0.990, 0.971, 0.990, 0.990, 0.981, 1.000, 0.990, 0.833, 0.858]`
- Mean diff: 0.0297 (≈3pp)
- Cohen's d: **0.4397** → 四舍五入 0.440

---

## 为什么早期审计说"只有 5-seed"

- `tost_equivalence.json`（exp11 时代）：5 seeds, AA d=0.092
- `exp39_tost_analysis.json`：5 seeds, AA d=0.084
- **exp41 是后续补跑** (2026-05-22)，训练 5 个新 seed 并合并为 10 seeds

`data_audit_report.md` 中的 "UNVERIFIABLE" 结论是在 **exp41 运行之前**写的。后来 `audit_experiments.md` 已更新标注为 ✓。

---

## 5-seed → 10-seed 的 d 值变化原因

5-seed 时 AA Cohen's d ≈ 0.08（效应极小），但 10-seed 时 d=0.44（中等效应）。原因是新增 5 seeds 中有两个极端值：
- **seed 314**: scrambled AA = 0.833（远低于 9-class 的 0.981）
- **seed 628**: scrambled AA = 0.858（远低于 9-class 的 0.972）

这两个 seed 的 scrambled 模型在 AA 上表现异常差，拉大了整体 mean diff 并放大了 effect size。

---

## 总结

| 问题 | 答案 |
|------|------|
| d=0.44 来自哪里？ | exp41_tost_10seed (2026-05-22) |
| 10-seed 数据是否存在？ | **是**，服务器上有完整 JSON（含逐 seed F1 值） |
| 为什么之前审计找不到？ | 审计在 exp41 运行之前；exp41 是补跑实验 |
| 数据是否可信？ | 脚本逻辑清晰，10 个 F1 值可独立验证，Cohen's d 计算正确 |

---
