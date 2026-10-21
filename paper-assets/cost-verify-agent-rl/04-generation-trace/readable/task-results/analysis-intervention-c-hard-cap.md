# analysis intervention c hard cap

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_intervention-c-hard-cap_20260521T222357_result.json`
- **Structured JSON:** [`8bba3c2ad27c3e1aaa90.json`](../../sessions/8b/8bba3c2ad27c3e1aaa90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**Conclusion: NEGATIVE**（部分成功——cap 有效但训练仍退化）

### Step 7 关键指标
| 指标 | Intervention C (hard cap) | Seed 7 (无干预) |
|------|:---:|:---:|
| total_resp_len | **7170** | **11569** (爆炸) |
| train_success | 15.6% | ~0% |
| val_success | 9.38% | — |
| KL loss | 0.020 (飙升) | — |

### 与 Seed 7 无干预对比
- Hard cap **成功阻止了 response inflation**：total_resp_len 7170 vs 11569，per-turn 始终 <400 tokens
- 但 **success 仍崩溃**：从 step 4 的 54.7% 降到 step 7 的 15.6%，且 KL loss 飙升 4x
- 崩溃模式不同：baseline 是 response inflation collapse，intervention 是 KL-driven collapse

### 一句话总结
Hard cap 证明了 response inflation 是症状而非根因——物理限制 response length 后，训练不稳定性通过 KL divergence spike 以另一种形式表现，三种干预方案（len_penalty / high_kl / hard_cap）均未能根治问题。

报告已注册：`art_20260521_c3e110`

---
