# ssh harvest and gpu check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_harvest_and_gpu_check_20260522T095831_result.json`
- **Structured JSON:** [`be8aa3cead6aba515baa.json`](../../sessions/be/be8aa3cead6aba515baa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收齐。

## GPU 状态
| 服务器 | cuda:0 | cuda:1 | cuda:2 | cuda:3 |
|--------|--------|--------|--------|--------|
| autodl-5090 | 空闲 | 空闲 | 空闲 | 空闲 |
| autodl-5090-c | 空闲 | **忙** (30079/32607 MiB) | 空闲 | **忙** (29785/32607 MiB) |

autodl-5090-c GPU1 跑 `fewnerd_pretrained_n16_s42`，GPU3 跑 `fewnerd_pretrained_n32_s42`。

## 实验结果

| exp_id | 状态 | greedy_f1 | mv_strict_f1 | mv_delta_pp | oracle_f1 | degen% |
|--------|------|-----------|-------------|-------------|-----------|--------|
| conll_pretrained_n64_s42 | **完成** | 0.6005 | 0.6316 | **+3.11** | 0.7703 | 14.3% |
| fewnerd_n32_s42 | **完成** | 0.7914 | 0.7818 | **-0.96** | 0.9305 | 1.4% |
| fewnerd_pretrained_n32_s42 | **运行中** 35% (422k/1.2M) | — | — | — | — | — |
| fewnerd_pretrained_n16_s42 | **运行中** 54% (327k/602k) | — | — | — | — | — |

### 要点
- **conll_pretrained_n64**: MV 带来 +3.11pp 增益，degeneracy 14.3%，oracle headroom 大（77%），结构化 SC 有效
- **fewnerd_n32 (finetuned)**: MV 反而降了 0.96pp，degeneracy 极低 (1.4%)——finetuned 模型在 fewnerd 上 greedy 已经很强 (79.1%)，一致性投票没帮助
- **两个 pretrained fewnerd 实验**预计还需 ~10h (n32) 和 ~4h (n16) 完成

---
