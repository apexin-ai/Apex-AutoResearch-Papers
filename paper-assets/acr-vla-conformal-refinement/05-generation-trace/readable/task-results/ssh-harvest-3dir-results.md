# ssh harvest 3dir results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_harvest-3dir-results_20260523T031403_result.json`
- **Structured JSON:** [`be448ffe655c1a0b21d9.json`](../../sessions/be/be448ffe655c1a0b21d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果收割完成。

**已完成 (2/5):**
- CRM norm=0.1: **79.0%** (vs VLA-only 79.8%, -0.8pp)
- CRM norm=0.05: **80.0%** (vs VLA-only 79.8%, +0.2pp)

**即将完成 (3/5, 均在最后一个 task 的最后几个 rollout):**
- CRM norm=0.3: ~74-76% (估计, -4~6pp)
- Adaptive CRM: ~81-83% (估计)
- Reconvla K=10: ~81-83% (估计)

**核心发现:**

1. **Norm 大小是决定性因素**: 1.42→0.3→0.1→0.05，SR 从 57%→~75%→79%→80%，单调递增
2. **CRM 在小 norm 下无增益**: norm=0.05 时 SR 与 VLA-only 持平（80% vs 79.8%），corrections 太小无法帮助也无法伤害
3. **Reconvla (无 CRM 的 K=10 平均) 是强 baseline**: 估计 ~81-83%，与 adaptive CRM 持平甚至略优于 CRM variants
4. **T6 (on_ramekin) 全部 0%**: 所有方法均失败，是 VLA 本身的限制

报告已写入 `artifacts/3dir_spatial_s42_results.md`。3 个 running 实验预计 ~15 分钟内完成，届时可更新最终数字。

---
