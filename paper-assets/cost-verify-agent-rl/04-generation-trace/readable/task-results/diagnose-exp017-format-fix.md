# diagnose exp017 format fix

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp017-format-fix_20260514T163832_result.json`
- **Structured JSON:** [`35baf86a5ee9c737eddd.json`](../../sessions/35/35baf86a5ee9c737eddd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### format_ok=75% 根因

**不是 SFT 数据格式问题。** 20 个 eval episode 中：
- 15 个正常运行，format_ok=**100%**
- 5 个（EP 7/12/16/17/18）在 step 1 crash，format_ok=0% → 因 vLLM context length overflow（>8192 tokens）

75% = 15/20，是二元分布，不是渐进退化。

### action_is_valid=63.8% 根因

**PDDL planner 生成 `move X to Y`，ALFWorld 有效动作是 `put X in/on Y`。**

| 数据集 | `put` | `move` | `close` |
|--------|-------|--------|---------|
| exp008 | 1200 | 0 | 0 |
| exp017 | **0** | **2279** | 3608 |

模型从未学过正确的 `put` 动作。额外的 3608 个 `close` 动作增加了 trajectory 长度（mean 27.1 vs 20.1 msgs），间接加剧 context overflow。

### 修复完成

脚本 `/root/cost-verify-agent-rl/scripts/fix_expert_sft_format.py` 已将所有 `move OBJ to RECEP` → `put OBJ in/on RECEP`（同时修 `&lt;answer>` 和 `&lt;think>` Suggestion）。

| 文件 | 修复数 | 残留 move |
|------|--------|----------|
| train.jsonl (2460条, 32110 msgs) | 2279 answer + 2279 think | 0 |
| val.jsonl (129条, 1667 msgs) | 113 + 113 | 0 |

输出：`/root/autodl-tmp/expert_sft_v2/expert_sft_train.jsonl` 和 `expert_sft_val.jsonl`

诊断报告：`/root/cost-verify-agent-rl/artifacts/diag_exp017_format.md`

---
