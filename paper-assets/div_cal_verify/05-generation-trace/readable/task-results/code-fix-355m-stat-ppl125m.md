# code fix 355m stat ppl125m

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_355m_stat_ppl125m_20260514T100752_result.json`
- **Structured JSON:** [`205086fa3c3acac3ef0d.json`](../../sessions/20/205086fa3c3acac3ef0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项修复全部完成，脚本运行正常。

### 结果汇总

**修复 1: PPL_125M 数据补全** — 已添加 3 条 seed=456 条目（rgds=66.22, uncurated=44.69, external_only=43.90）。

**修复 2: external_only 目录命名一致性** — 确认匹配：
- `results_medium_external/external_only/`
- `results_medium_external_seed123/external_only/`
- `results_medium_external_seed456/external_only/`

代码中 `dir_suffix="external"` + `subdir="external_only"` 与实际目录结构完全一致。

**修复 3: Cohen's d** — 无需改代码，确认。

### dry-run 结果

脚本无报错，完整执行。Asymmetric Gap Test 使用 n=2 common seeds（因为 355M 侧 rgds/random_50 的 seed=456 实验尚未完成），输出正常：

| 对比 | 125M gap | 355M gap | 变化 |
|------|----------|----------|------|
| RGDS vs Random-50 | +35.85 | +15.15 | 缩小 57.7% |
| RGDS vs Uncurated | +30.11 | -2.81 | 缩小 109.3%（反转） |
| RGDS vs External | +30.74 | +7.90 | 缩小 74.3% |

当前 common_seeds 仍为 n=2（受限于 355M 侧 rgds/random_50 缺 seed=456 数据）。待这两个实验完成后，Asymmetric Gap Test 将自动使用 n=3 seeds。

---
