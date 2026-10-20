# analysis random s42 taxonomy verify

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_random-s42-taxonomy-verify_20260515T141559_result.json`
- **Structured JSON:** [`c90c1d89b21e16be539d.json`](../../sessions/c9/c90c1d89b21e16be539d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证结果汇总：

**Registry genuine=23 确认一致。** 79 个 proved 样本分解如下：

| 类别 | 数量 | 说明 |
|------|------|------|
| H7 (tautological P→P) | **0** | 无单前提自证 |
| H1 (exact match) | **56** | 结论完全等于某个前提（registry 定义） |
| H8 (conjunction collapse) | **3** | idx 51, 65, 82 — 结论是前提的 top-level 合取 |
| H1-near (substring) | **8** | 结论是某前提的子串或反之（不完全等于但文本包含） |
| Genuine (strict) | **12** | 真正需要推理的证明 |

**H8 + H1-near + genuine = 3 + 8 + 12 = 23 = registry 的 genuine 数字。** Registry 用 exact string match 定义 H1，不区分 H8，所以 23 实际包含了 11 个半trivial 样本（3 H8 + 8 H1-near）。严格 genuine 只有 **12**。

注意 H1-near 的两种子类型：
- **conc_in_prem** (5 个): 结论是某前提的子表达式（如 `racehorse(detroit_city)` vs `(racehorse(detroit_city))`，仅差外层括号）
- **prem_in_conc** (3 个): 某前提是结论的子表达式（结论是合取但未被 H8 捕获，因为只有部分 conjunct 匹配前提）

---
