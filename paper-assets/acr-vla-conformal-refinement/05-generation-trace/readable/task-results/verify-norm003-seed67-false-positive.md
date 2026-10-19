# verify norm003 seed67 false positive

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_norm003-seed67-false-positive_20260521T050523_result.json`
- **Structured JSON:** [`f79ae83bd328034f1d31.json`](../../sessions/f7/f79ae83bd328034f1d31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 总结

**是否 false positive**: 是。Cron 误判（项目脚本不写 sentinel/W&B 的已知问题）。

**证据**：
- Log `/root/autodl-tmp/logs/norm003_seed67.log` 末尾显示：
  - `Overall success rate (crm_obs_only): 14.0% (14/100)`
  - `[eval] Results saved to logs/eval_object_crm_obs_only_norm0.03_seed67.json`
- Output JSON 完整：10 task × 10 rollouts = 100 全跑完

**SR 值**: overall_success_rate = **0.14** (14/100)

**Registry 修正**: ✅ conclusion: failed → success（metrics 已存在，无需补录）

---
