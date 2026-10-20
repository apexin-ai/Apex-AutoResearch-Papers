# run wnut lora merge pilot

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_wnut_lora_merge_pilot_20260514T133121_result.json`
- **Structured JSON:** [`2528cad99943723f8f73.json`](../../sessions/25/2528cad99943723f8f73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

## WNUT-17 LoRA Merge + Pilot 结果

**Step 1: LoRA Merge** — 成功
- Merged model: `/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-merged/` (19GB, 4 shards)

**Step 2: Pilot Inference** — 完成，Verdict: **FAIL**

| 指标 | 值 |
|------|-----|
| greedy F1 | 0.525 |
| oracle F1 | 0.664 |
| headroom | 0.139 |
| ρ(SJ, F1) full | 0.082 |
| ρ(SJ, F1) cond | **0.275** |
| ρ(FK, F1) cond | 0.164 |
| ρ(logprob, F1) cond | **0.352** |
| sample F1=0 % | **53.7%** |

关键发现：
- **Logprob baseline 在 conditional 上强于结构一致性**（0.352 vs 0.275），structural_beats_surface=false
- **53.7% samples F1=0**，远超 30% 阈值，脚本建议 T=0.7 重跑
- 46% gold-empty instances（598/1287），WNUT-17 大量句子无实体
- WNUT-17 上模型表现明显弱于 SciERC（greedy F1 0.525 vs 0.663）

---
