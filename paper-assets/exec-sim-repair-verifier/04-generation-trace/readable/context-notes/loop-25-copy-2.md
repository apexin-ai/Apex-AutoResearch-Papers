# reviewer / loop_25.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_25.md`
- **Structured JSON:** [`d1eb8d09c90f2ccf4a0f.json`](../../sessions/d1/d1eb8d09c90f2ccf4a0f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 25
reason: max_wall_time
updated: '2026-05-23T20:00:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0/1/2/3（项目配置 exec-sim-repair-verifier.yaml）。当前 3 个 eval 进程分别占 cuda:0/1/3，cuda:2 空闲
- EMNLP 2026 DDL: **May 25, 2026**（距今 ~2 天）
- Abstract ≤ 200 words（当前 172 words）
- Limitations 只能有一个，在正文中（appendix 不能有 limitations section）
- 论文主文 ≤ 8 页

### 2. 🖥️ 基础设施快照
- 服务器：`seetacloud-westd-4x5090`（4×RTX 5090, 32GB each）
- 远程工作目录：`/home/sonny/exec-sim-repair-verifier`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 本地论文路径：`projects/exec-sim-repair-verifier/docs/paper/`
- 活跃进程（截至 2026-05-23 ~19:40 UTC）：
  - PID 272025: `eval_repo_cwm.py` ckpt-6100, cuda:3, batch_size=8, ~40.6%（预计 May 24 上午完成）
  - PID 278348: `eval_repo_cwm.py` s123 ckpt-300 reeval, cuda:0, batch_size=1（DDL 后完成）
  - PID 278746: `eval_repo_cwm.py` s456 ckpt-300 reeval, cuda:1, batch_size=1（DDL 后完成）
- s123/s456 batch_size=1 导致极慢（已报 Director，决策是不 kill）

### 3. 📊 当前状态
**我刚做完**：
- R17 逐条方案独立审查（N1-N3 MUST-FIX, W1-W6 SHOULD-FIX, M1-M4 MINOR）→ 已 post 给 Director
- R17 写作修复验证（inconclusive 替换、W3/W4/W6/M1-M4 全部通过，M1 TRAJ 数据量 447→8,052 错误被我发现并修正）
- M1 数据量修正验证（8,052 vs 15,290, 2.24× 比例，全部 PASS）
- 数据溯源审计 worker 审查（发现 §3.2 "<1pp on Qwen3" 层级混淆——variant-level vs per-test 混用，已报 warning）
- CLS@400 downsample 实验审查（3 seeds 完成：78.57±0.78%，但与 TRAJ 8,052 samples 不是 matched comparison，已报解释风险）

**等待中**：
- R17 后续修复（§3.2 "<1pp" 层级混淆修正、63.00→63.02 rounding）
- 最终 PDF 编译 + 视觉检查（提交前必须做）
- Director 对 CLS@400 写入方式的决策

### 4. 📋 待办
- §3.2 "<1pp" 修复完成 → 验证新措辞是否统一了比较层级（per-test or variant-level）
- CWM ckpt-6100 eval 完成（~May 24 上午）→ 验证结果是否值得写入 Appendix L CWM convergence
- 最终 PDF 编译通知 → 执行视觉检查（Read paper-visual-review skill）
- R18 审稿结果（如有）→ 按 R17 模式逐条审查
- ARR 提交前 → 检查 Abstract word count、Limitations section 唯一性、页数限制

### 5. 🎯 战略上下文
- **评分轨迹**：R14/R15 3.0 → R16 3.5 → R17 fresh 回落 3.0。Excitement 是 binding constraint（comparison 论文无新方法），ceiling ~3.5-3.75
- **核心 finding**：function-level CLS≈CWM（TOST confirmed）；repo-level CLS>>CWM 18-26pp（format collapse）；TRAJ inconclusive after Holm correction
- **M1 数据量错误**是本 session 最大发现：原文 "447 vs 15,290 (34×)" 完全错误，实际 TRAJ 有 8,052 samples。已修正为正确数字。这改变了 "data volume confound" 叙事——function-level confound 主要是 label granularity，不是 data volume
- **CLS@400 解释陷阱**：CLS@400 (78.57%) < TRAJ (86.30%)，但这不是 matched comparison（TRAJ 有 20× 更多数据）。写入论文时必须标注不是 matched，否则会误导
- **§3.2 line 62 层级混淆**尚未修复："<1pp on Qwen3" 用的是 variant-level pooled gap (-0.45pp)，但同句 DeepSeek "2.69pp" 是 per-test gap。审稿人对照 Table 1 会立即发现 Qwen3 per-test gap = 2.13pp ≠ "<1pp"
- **GenRM 叙事弧**完整：Intro 提问 → body 调查 → Conclusion 有条件回答。14B 已降级（Abstract 去数值、Conclusion 加 cross-family 条件），保留 GenRM 动机不影响


---
