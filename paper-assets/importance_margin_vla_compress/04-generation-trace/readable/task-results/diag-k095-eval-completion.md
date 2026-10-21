# diag k095 eval completion

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_k095_eval_completion_20260518T131921_result.json`
- **Structured JSON:** [`f914bf30a5456cba16c6.json`](../../sessions/f9/f914bf30a5456cba16c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 实验结果：eval_smolvla_random_prune_k095

**Overall SR: 0.00% (0/500)**，Wilson 95% CI: [0.0000, 0.0076]

**Per-task SR（全部 0%）：**

| Task | Description | SR |
|------|-------------|-----|
| T0 | pick up alphabet soup | 0% |
| T1 | pick up cream cheese | 0% |
| T2 | pick up salad dressing | 0% |
| T3 | pick up bbq sauce | 0% |
| T4 | pick up ketchup | 0% |
| T5 | pick up tomato sauce | 0% |
| T6 | pick up butter | 0% |
| T7 | pick up milk | 0% |
| T8 | pick up chocolate pudding | 0% |
| T9 | pick up orange juice | 0% |

**Conclusion: success** — hypothesis 完全验证。仅移除 7/128 tokens（5%）即导致 0% SR，证实了极端 cliff-edge 现象：SmolVLA 对 random token removal 的敏感度极高，即使最小幅度的随机剪枝也会完全摧毁 action generation。

**Registry: DONE (success)，Cron 已清除。**

---
