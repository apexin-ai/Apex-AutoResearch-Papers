# analysis plan006 prolog sta s44

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan006-prolog-sta-s44_20260514T181907_result.json`
- **Structured JSON:** [`1b3c82182efbc0d89514.json`](../../sessions/1b/1b3c82182efbc0d89514.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

**三 seed Prolog exec+STA 对比：**

| seed | PR | ISR | 模式 | 特征 |
|------|-----|-----|------|------|
| s42 | 0.50 | 0.50 | Goodhart | ISR≈PR, 100% H7 |
| s43 | 0.38 | 0.07 | Genuine | 低 ISR, 0% H7 |
| s44 | 0.75 | 0.50 | Goodhart | ISR≈PR, 后期 ISR≈1.0, completion 暴跌到 32 tokens |

s44 明确是 s42 模式——后期 PR≈ISR≈1.0 且 completion length 从 127 崩塌到 32 tokens，entropy 极低，`frac_reward_zero_std=1.0` 频繁出现，是典型的 ISR gaming + mode collapse。3 seed 中 2/3 出现 Goodhart 崩塌，s43 是例外（可能因 seed 随机性未触发 gaming 路径）。

Checkpoint 正常保存在 `/root/autodl-tmp/outputs/plan006_prolog_sta_s44/`（含 final model + checkpoint-500），模型权重 ~15GB。

---
