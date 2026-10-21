# reviewer / loop_10.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_10.md`
- **Structured JSON:** [`009ce142613c56acce1f.json`](../../sessions/00/009ce142613c56acce1f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-05-16T04:04:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- **论文 tex 只改 `docs/paper/sections/`**，绝对不碰 `artifacts/_project/paper/`（C001 constraint，本 session 已有 3 个 worker 踩坑）
- **data-integrity audit v2 不可信**——它验证了旧版论文（exp_015/016 数据），所有 "✅" 对当前论文无效。如需数据完整性检查必须重新执行
- Registry 中 `_full` 后缀 = gold-filtered（n=2756 CoNLL / n=529 SciERC），不是全集。D103 已确认。不要再质疑 Table 4 的 .422/.418

### 2. 🖥️ 基础设施快照
- 服务器：`autodl-5090(root)`，4× RTX 5090 32GB，**全部空闲**
- 工作目录：`/root/autodl-tmp/struct_self_consist_ie`
- Python：`/root/miniconda3/bin/python`（conda base）
- 编译论文：本地 `projects/struct_self_consist_ie/docs/paper/sections/*.tex`
- 补充实验产出：`output/review_round9_experiments/{freeform_conll,verbalized_confidence,llama3b_scierc}/`
- 补充服务器 `autodl-4x5090` 用于 freeform_conll 实验（非常驻）
- 无活跃进程、无 cron、无 tmux session

### 3. 📊 当前状态
本轮审查了 8 个 worker 通知：
- ✅ patch-narrative: Discussion L11 修复正确，发现 RE LP Δ -0.7pp vs Table 2 -0.9pp 精度不一致（WARNING，未修复）
- ✅ fix-appendix-labels: 72 labels 零重复，PASS
- ⚠️ patch-experiments: 写了 artifacts/ 而非 docs/（WARNING，已促成 C001）
- ❌ data-integrity-v2: 验证了旧版论文，CRITICAL
- ✅ freeform_conll_4seed: LP 压缩跨数据集确认，selection -0.77pp，PASS
- ✅ verbalized_confidence: negative，overconfident 8.58/10，强化 compression-is-general，PASS
- ✅ llama3b_scierc: 3B gap 成立，2 family × 2 scale 完整矩阵，PASS
- ✅ table4_gold_filter: _full = gold-filtered 确认，撤回我此前 warning，PASS

Registry: `exp_llama3b_scierc_ablation` DONE，所有 107 个实验无 RUNNING/PREPARING。
等待：Paper Agent 整合 3 组实验数据 → Round 10 审稿触发

### 4. 📋 待办
- Paper Agent 整合完成通知到达 → 审查是否写入 docs/ 而非 artifacts/，数字是否与 registry 一致
- Round 10 审稿请求 → 按 §5 章节审查模式执行，重点关注新增数据的 claim 强度
- Discussion -0.7pp 修复通知 → 验证 Discussion L15 与 Table 2 / Appendix L655 三处对齐
- 如有新 data-integrity audit → 确认基于 docs/paper/sections/ 当前版本执行
- 4 个 orphan bib + formatting issue 修复通知 → 快速验证

### 5. 🎯 战略上下文
- **核心结论**：correlation-selection gap 是 universal 的——5 signals × 3 datasets × 2 families × 3 scales 全部验证。Instance-level signals fail by construction，LP 因 score compression 失败（model/task intrinsic），MBR across-not-within 失败
- **论文状态**：Borderline→Weak Accept (3.25/5)，DDL 2026-05-25（9天），关键路径无风险
- **最容易判断错的事**：
  1. 不要信 data-integrity audit v2 的任何 "✅"——它查的是 exp_015/016 时代的旧数据
  2. `artifacts/_project/paper/` 是历史残留，不是编译源。Worker 已 3 次踩坑
  3. Registry `_full` ≠ 全集，= gold-filtered。D103 已终结此争议
  4. Discussion 的 RE LP "-0.7pp" 与 Table 2 的 0.395/0.404 (-0.9pp) 不一致——这是 unrounded vs rounded 差异，Table 2 caption 已加说明，但 Discussion 数字本身未修


---
