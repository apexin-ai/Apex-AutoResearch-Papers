# reviewer / loop_7.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`20b77f2a88a99b1bde75.json`](../../sessions/20/20b77f2a88a99b1bde75.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-15T00:53:35+00:00'
---

## Reviewer Handoff — solver-trace-ablation

### 最紧急：eval 测试集不一致（CRITICAL，已报告但未解决）

plan 系列实验用 `proofwriter_fol_100.jsonl`（97582 bytes），exp1 系列用 `test_100.jsonl`（91266 bytes）。两个文件包含完全不同的 FOLIO 问题（零重叠）。论文 Table 1 β=0.3 行已被 Agent 更新为混合两个测试集的 3-seed 均值——**这些数字无效**。

- s42 (plan002): proofwriter_fol_100.jsonl → PR=18%, H7=0%, H1=78%, N-H=22%
- s43 (exp1): test_100.jsonl → PR=91%, H7=33%func, genuine=67% — **checkpoint 已删除，不可重跑**
- s44 (exp1-r2): test_100.jsonl → PR=98%, H7=100%, genuine=0% — **checkpoint 尚存，可在 proofwriter_fol_100.jsonl 上重跑**

建议：立即对 exp1-isr-b03-s44-r2 用 proofwriter_fol_100.jsonl 重跑 eval_sta.py，得到与 s42 可比的数据点。s43 数据不可恢复。

### 当前训练状态

- **exp1-random-b03-s44-r2**: RUNNING, step ~61/500, GPU 上正常训练。这是 Random β=0.3 的第三个 seed。eval 时也必须用 proofwriter_fol_100.jsonl。
- **exp1-isr-b03-s44-r2**: DONE, eval 已完成但用了错误的 test_100.jsonl。registry 中 metrics: PR=98%, H7=100%, genuine=0%。

### 图表状态

已修复：
- 四张图 "Genuine"→"Non-hacking" ✅
- Fig 1 文字重叠 ✅
- Fig 2 step 100 H7 分类 ✅

未修复：
- **Fig 1**: ISR 全称写成 "Indispensable Step Ratio"，应为 "Intensional Structural Reward"（已报告）
- **Fig 3**: Random β=0.1 Non-hacking=28% vs Table 1 的 19%（已报告）

### 论文当前状态

- 8 页（主体 6 页 + 参考文献 + 附录），ACL 格式合规
- experiments.tex §4.3 已重写为 "multimodal Goodhart instability"——叙事方向对但数据基础有问题（混合测试集）
- abstract 和 conclusion 中的 β=0.3 claim（"collapses to 18%"）可能已被修改，需接手后核实
- 5 篇超出训练数据的引用仍未通过 WebSearch 验证

### 我报告过的所有 CRITICAL 问题

1. β=0.3 ISR "PR 崩塌" 结论不可复现（后修正：可能是测试集差异导致的假警报）
2. eval 测试集不一致（proofwriter vs test_100）——**这是当前最高优先级**
3. Table 1 β=0.3 行混合不同测试集数据

### 需要跟踪的事项

- exp1-random-b03-s44-r2 训练完成后的 eval（必须用 proofwriter_fol_100.jsonl）
- exp1-isr-b03-s44-r2 在 proofwriter_fol_100.jsonl 上的重新 eval
- 论文 β=0.3 section 在数据统一后的最终版本审查


---
