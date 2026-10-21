# code fix confound abs r

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-confound-abs-r_20260522T171054_result.json`
- **Structured JSON:** [`0144ac7e7c25fcce802d.json`](../../sessions/01/0144ac7e7c25fcce802d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成，重跑成功。

### 修改内容

4 行阈值判断改为绝对值：

| 行号 | 修复前 | 修复后 |
|------|--------|--------|
| 164 | `if r < -0.7:` | `if abs(r) > 0.7:` |
| 166 | `elif r <= -0.5:` | `elif abs(r) > 0.5:` |
| 303 | `if mean_r < -0.7:` | `if abs(mean_r) > 0.7:` |
| 305 | `elif mean_r <= -0.5:` | `elif abs(mean_r) > 0.5:` |

### 重跑结果

| Condition | r | Verdict |
|-----------|---|---------|
| arc_challenge×position_bias | +0.916 | SEVERE |
| arc_challenge×score_manipulation | +0.908 | SEVERE |
| arc_challenge×prompt_injection | +0.888 | SEVERE |
| arc_challenge×verbosity_bias | +0.790 | SEVERE |
| arc_challenge×sycophancy | +0.764 | SEVERE |
| arc_challenge×authority_bias | +0.732 | SEVERE |
| mmlu×score_manipulation | +0.820 | SEVERE |
| mmlu×prompt_injection | +0.656 | MODERATE |
| mmlu×position_bias | +0.633 | MODERATE |
| mmlu×authority_bias | +0.595 | MODERATE |
| mmlu×verbosity_bias | +0.355 | BROKEN |
| mmlu×sycophancy | +0.348 | BROKEN |

**Overall: mean |r| = 0.701, verdict = CONFOUND_SEVERE**

修复前这些正向高 r 值（如 arc_challenge×prompt_injection 的 r=+0.888）全部被误判为 CONFOUND_BROKEN，现在正确归类为 SEVERE。arc_challenge 全部 6 个 condition 都是 SEVERE，说明 K_eff 与 eta_max 的正向共线性非常强。

---
