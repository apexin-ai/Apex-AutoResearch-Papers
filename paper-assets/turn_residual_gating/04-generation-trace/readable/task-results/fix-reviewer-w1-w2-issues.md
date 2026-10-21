# fix reviewer w1 w2 issues

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_reviewer_w1_w2_issues_20260525T204337_result.json`
- **Structured JSON:** [`cabaebc4e2a59d87fd1a.json`](../../sessions/ca/cabaebc4e2a59d87fd1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修正完成。总结：

**W1** — crossmodel 表 SS 行统一用 s42：TF 0.502, AR 0.347, Gap 1.4×；caption 标注 seed 42。

**W2** — perseed TG 表 caption 增加 N=50 协议下的 AR GAR (0.064/0.055) 和 gap (7.9×/9.1×) 说明，解释与主表的协议差异。

**INFO-1** — 已由 W1 修正覆盖（crossmodel TF 0.498→0.502）。

**INFO-2** — cost 表 Uniform Gate 时间 6.0→6.1h。

**连锁更新** — 正文/附录中 SS gap 从 ~1.2× 改为 ~1.3×（3-seed mean），涉及 introduction/experiments/analysis/conclusion/appendix 共 11 处；experiments.tex 的 TF GAR 同步更新为 0.517±0.032；llama-vs-qwen-ss 对比表的 Qwen TF/gap/compression 一并修正。

---
