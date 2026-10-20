# analysis s42 taxonomy rerun current classify

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_s42-taxonomy-rerun-current-classify_20260515T170612_result.json`
- **Structured JSON:** [`af6207019f6bee0148ae.json`](../../sessions/af/af6207019f6bee0148ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新成功。plan016-extended-1000-s42 条目已存在（我初始搜索的过滤方式有误），metrics 已更新。

## 结果汇总

### s42 1000 步 taxonomy（当前版本 classify_h7.py）

| 类别 | 数量 | 比例 |
|------|------|------|
| Proved | 96 | 96% |
| H7a (text-match tautology) | 0 | 0% |
| H7b (obfuscated tautology) | 0 | 0% |
| H1 (conclusion in premises) | **96** | **100%** |
| H8 (conjunction collapse) | 0 | 0% |
| **Genuine** | **0** | **0%** |

旧版 classify_h7 给出 genuine=7 是因为 H1 检测不够全面（不是因为缺少 H8 —— H8 在 s42 1000 步中本来就是 0）。当前版本识别出全部 96 个 proved proof 都是 H1（结论嵌入在前提中），genuine 归零。

### 三 seed pooled genuine（1000 步 exec-only）

| Seed | n_proved | H7 | H1 | H8 | Genuine | Rate |
|------|----------|-----|-----|-----|---------|------|
| s42 | 96 | 0 | 96 | 0 | 0 | 0% |
| s43 | 90 | 90 | 0 | 0 | 0 | 0% |
| s44 | 100 | 0 | 85 | 15 | 3 | 3% |

**Pooled: 1.0% ± 1.7%** — 与 D090 完全一致，不再矛盾。

---
