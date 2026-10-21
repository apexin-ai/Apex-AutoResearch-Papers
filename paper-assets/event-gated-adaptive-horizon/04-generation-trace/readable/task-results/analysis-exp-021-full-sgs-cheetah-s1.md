# analysis exp 021 full sgs cheetah s1

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_021_full_sgs_cheetah_s1_20260517T224736_result.json`
- **Structured JSON:** [`4c07ee366951313f2dec.json`](../../sessions/4c/4c07ee366951313f2dec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**exp_021 结果：PARTIAL NEGATIVE**

| 指标 | 值 |
|------|-----|
| eval_return_final | 221.5 (baseline的38.7%) |
| NVE_peak | 9.94 @ step 45K |
| civo | True (transient, self-correcting) |
| NVE_sustained (55K-105K) | 0.338 |

关键发现：
1. Full-SGS **未能阻止** Cheetah 的 CIVO spike（NVE=9.94 @ 45K, eval collapse 到 4.6）
2. 但 SGS 使得 agent **恢复**了（vs 010b 永久 collapse），最终 221.5 vs 010b 的 51.7
3. 与 Walker (018, NVE_peak=0.72) 对比，**跨环境一致性未确认**——SGS 在 Walker 完全有效，在 Cheetah 仅部分有效
4. actor_grad_norm 全程极低 (0.0-0.1)，SGS 可能过度阻断梯度导致学习受限

报告已注册: `art_20260517_24b7c0`

---
