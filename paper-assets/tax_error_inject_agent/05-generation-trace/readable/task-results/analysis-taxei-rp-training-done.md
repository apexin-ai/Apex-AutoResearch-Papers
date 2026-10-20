# analysis taxei rp training done

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_taxei-rp-training-done_20260516T060627_result.json`
- **Structured JSON:** [`133e992c7c2750dc2e51.json`](../../sessions/13/133e992c7c2750dc2e51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。汇总如下：

## v4-taxei-rp-s42
- **状态**: 成功 (EXIT_CODE=0)
- **最终 train_loss**: 0.3847 (overall avg)
- **Epoch loss**: E1=0.419 → E2=0.327 → E3=0.226
- **训练时间**: 3h 46m 40s (13600s)
- **Checkpoint**: `/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s42/v0-20260516-101703/checkpoint-5415`
- **异常**: 无

## v4-taxei-rp-s123
- **状态**: 成功 (EXIT_CODE=0)
- **最终 train_loss**: 0.3852 (overall avg)
- **Epoch loss**: E1=0.474 → E2=0.334 → E3=0.221
- **训练时间**: 3h 46m 30s (13590s)
- **Checkpoint**: `/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s123/v0-20260516-101708/checkpoint-5415`
- **异常**: 无

## v4-taxei-rp-s1
- **状态**: 成功 (EXIT_CODE=0)
- **最终 train_loss**: 0.3853 (overall avg)
- **Epoch loss**: E1=0.441 → E2=0.356 → E3=0.243
- **训练时间**: 3h 46m 18s (13578s)
- **Checkpoint**: `/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s1/v0-20260516-101834/checkpoint-5415`
- **异常**: 无

## v4-taxei-rp-s0 (进行中)
- **进度**: 99.2% (5372/5415)
- **当前 loss**: ~0.25 (windowed)
- **预计剩余**: ~2 min

---

**Cross-seed 一致性**: 3 个 seed 的 overall train_loss 非常接近 (0.3847 / 0.3852 / 0.3853)，训练时间也几乎相同 (~3h46m)，loss 曲线趋势一致 (E1 ~0.44 → E2 ~0.34 → E3 ~0.23)。每个 seed 均保存了 3 个 checkpoint (step 1805/3610/5415)。s0 即将完成。

---
