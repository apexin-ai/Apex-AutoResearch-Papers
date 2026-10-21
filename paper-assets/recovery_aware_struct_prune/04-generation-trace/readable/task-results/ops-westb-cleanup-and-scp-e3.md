# ops westb cleanup and scp e3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_cleanup_and_scp_e3_20260518T154118_result.json`
- **Structured JSON:** [`040fc137b0bcae9c1a0d.json`](../../sessions/04/040fc137b0bcae9c1a0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

## 清理
已删除: pruned_gradient_20 (12G), pruned_magnitude_20 (12G)
释放空间: ~24G (7.7G → 31G)

## SCP
- pruned_standard_20: 成功, 12G (westd → westb 直推)
- pruned_rasp_20: 成功, 12G (westd → westb 直推)

## 5 模型验证
全部就位: **yes**
- Dense (DeepSeek-R1-Distill-Qwen-7B) ✓
- pruned_cka_only_20 ✓
- pruned_standard_20 ✓
- pruned_random_20 ✓
- pruned_rasp_20 ✓

## GPU 状态
- cuda:0: 运行中 — `grpo_cka_only_20_1p5b` step 93/100 (约 3h 运行，还剩 ~13min)
- cuda:1: 运行中 — `grpo_rasp_20_1p5b` step 68/100 (约 36min 运行，还剩 ~17min)

另外 `grpo_standard_1p5b_100steps` 已完成 (EXIT_CODE=0)。

## 磁盘
传输后: 243G used / 7.7G avail (250G total) — 两个 12G 模型传入填满了释放的空间，符合预期。

---
