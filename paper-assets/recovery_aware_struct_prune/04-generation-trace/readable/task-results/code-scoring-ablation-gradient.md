# code scoring ablation gradient

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scoring_ablation_gradient_20260517T073242_result.json`
- **Structured JSON:** [`ca4250de725eaace74da.json`](../../sessions/ca/ca4250de725eaace74da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在情况清楚了。

## 当前状态

**cuda:0 占用 (63GB/98GB, 99% util):**
| Session | 进程 | 进度 | ETA |
|---------|------|------|-----|
| multiseed_serial | eval sft_standard_20 seed=456 [4/4] | 17% (34/200) | ~14 min |
| scoring_ablation_v2 | magnitude SFT (149/1870 steps) | 8% | ~52 min |

**cuda:1 占用 (18GB/98GB, 91% util):**
| Session | 进程 | 备注 |
|---------|------|------|
| eval_unstructured_20 | eval unstructured (1319 samples) | 已跑 ~2h |

**Gradient 前置条件:**
- `importance_scores.pt` ✅ 存在 (18KB)
- `pruned_gradient_20/` ❌ 不存在（需要先 prune）

## 问题

`scoring_ablation_v2` 正在跑完整的 4-method 循环 (magnitude → gradient → random → cka_only)，有 `set -e`。当前卡在 magnitude SFT 上：
- 如果 magnitude SFT 成功：还需 ~52 min SFT + eval，然后才轮到 gradient（总计 ~1h+）
- 如果 magnitude SFT 崩溃（如你所说"已死"）：`set -e` 会终止整个脚本，gradient 永远不会启动

**要立即启动 gradient，需要 kill 掉 scoring_ablation_v2 中的 magnitude SFT（PID 689115）释放 cuda:0。**multiseed eval 14 min 后也会自行结束。

是否 kill magnitude SFT 直接跳到 gradient？

---
