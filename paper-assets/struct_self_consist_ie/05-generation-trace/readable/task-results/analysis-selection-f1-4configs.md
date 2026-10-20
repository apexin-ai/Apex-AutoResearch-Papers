# analysis selection f1 4configs

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_selection_f1_4configs_20260515T030701_result.json`
- **Structured JSON:** [`7cf214b85a23791a90b5.json`](../../sessions/7c/7cf214b85a23791a90b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 格式正确，数值合理。所有 5 个 JSON 文件已保存到 `/root/autodl-tmp/struct_self_consist_ie/output/review_round2/`。

汇总结果：

| Config | N | Greedy | Oracle | SJ | FK | EM | LP | VC |
|--------|---|--------|--------|-----|-----|-----|-----|-----|
| llama_scierc_n8 | 529 | .6460 | .7780 | .6433 | .6386 | .6343 | **.6518** | .6332 |
| llama_scierc_n16 | 529 | .6445 | .8062 | .6494 | .6492 | .6395 | .6462 | .6402 |
| qwen_conll_n8 | 2756 | .9079 | .9483 | .8990 | .8926 | .8975 | .8974 | .8948 |
| llama_conll_n8 | 2756 | .9242 | .9426 | .9237 | .9245 | .9244 | .9244 | .9233 |

关键发现：
- **LLaMA SciERC N=8**: 只有 logprob 略优于 greedy (+0.006, p=0.39 不显著)；voting_conf 显著差于 greedy (p=0.03)
- **LLaMA SciERC N=16**: SJ/FK 略优于 greedy (+0.005) 但均不显著
- **Qwen CoNLL N=8**: 所有 signal 都**显著差于 greedy** (p<0.001)，greedy 已经很强 (0.908)
- **LLaMA CoNLL N=8**: 所有 signal 与 greedy 几乎无差异 (|Δ|<0.001)，greedy 更强 (0.924)

总体：在这 4 个配置上，没有 signal 能可靠地超过 greedy baseline 做 sample selection。Oracle-greedy gap 虽大（SciERC ~13pt），但现有 signal 无法利用。

---
