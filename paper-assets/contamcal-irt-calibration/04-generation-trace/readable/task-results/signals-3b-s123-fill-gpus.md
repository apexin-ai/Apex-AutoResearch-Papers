# signals 3B s123 fill gpus

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_signals_3B_s123_fill_gpus_20260516T143113_result.json`
- **Structured JSON:** [`1c153b98cd57cab7b7e9.json`](../../sessions/1c/1c153b98cd57cab7b7e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实际情况与预期不符，3B s123 signals 全部已完成或正在完成中：**

| GPU | 状态 | 正在跑什么 |
|-----|------|-----------|
| cuda:0 | 忙（6.5GB） | d000_s123_a32 最后一个任务 `s4×mmlu`（PID 780943） |
| cuda:1 | 忙（1.6GB） | 0.5B-Instruct signals `s4×mmlu`（PID 780591） |
| cuda:2 | **空闲** | — |
| cuda:3 | **空闲** | — |

**3B s123 Signals 完成度：**

| Condition | Status | 备注 |
|-----------|--------|------|
| d000_s123 | 8/9 done, 最后 1 个正在 cuda:0 跑 | 缺 `s4_selfcritique_mmlu`，正在运行 |
| d005_s123 | ✅ 全部完成 | 9 signals + 3 merged |
| d025_s123 | ✅ 全部完成 | 9 signals + 3 merged |
| d100_s123 | ✅ 已完成 | 之前报 success |

**结论**：无需再提交任何 3B s123 signal 任务。所有 3B s123 都已完成或即将完成。

只有 **cuda:2 和 cuda:3 空闲**。需要你决定分配什么任务：
- 0.5B/1.5B s123 signals 也全部在 output dir 中（已完成）
- cuda:1 上的 0.5B-Instruct 是唯一还在跑的 signal 任务
- 可选任务：3B instruct eval 重试、Llama-3.2-3B signals、或其他

需要指示 cuda:2/3 跑什么。

---
