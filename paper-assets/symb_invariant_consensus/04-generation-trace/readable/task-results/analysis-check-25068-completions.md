# analysis check 25068 completions

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_check-25068-completions_20260519T194104_result.json`
- **Structured JSON:** [`0457f7475a757bbe2505.json`](../../sessions/04/0457f7475a757bbe2505.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

| 实验 | 状态 | SC | Method | Δ | n |
|------|------|-----|--------|------|-----|
| exp-073b Qwen7B×LogiQA s456 | ✅ 完成 | 69.5% | SICA 71.5% | **+2.0pp** | 200 |
| exp-074 ICG×FOLIO | ✅ 完成 | 53.9% | ICG 52.0% | **-2.0pp** | 204 |
| exp-076 Debate×FOLIO | 🔄 运行中 | 59.6% | Debate 38.3% | -21.3pp | 141/204 (69%) |
| exp-075b Contrastive×FOLIO | 🔄 运行中 | 62.8% | Contrastive 46.9% | -15.9pp | 113/204 (55%) |

**GPU 空闲状态**：
- cuda:0 (exp-074) — vllm 还在跑但实验已完成，可释放
- cuda:1 (exp-073b) — 同上，可释放
- cuda:2 (exp-075b) — 占用中
- cuda:3 (exp-076) — 占用中

**要点**：
- exp-073b tie-breaker 结果：+2.0pp，与 exp-070 (+2.5pp) 方向一致，3 seeds 中 2/3 正向 → SICA 在 Qwen7B×LogiQA 上有微弱但一致的增益
- exp-074 ICG 方法 negative：独立约束生成反而比 SC 低 2pp，确认 trace-independent 约束不优于 trace-sourced
- exp-076 Debate 和 exp-075b Contrastive 中间结果都大幅 negative（-21pp、-16pp），预期最终也是 negative

---
