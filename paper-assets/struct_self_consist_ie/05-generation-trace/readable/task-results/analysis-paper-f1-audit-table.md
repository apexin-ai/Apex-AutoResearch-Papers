# analysis paper f1 audit table

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper_f1_audit_table_20260518T215058_result.json`
- **Structured JSON:** [`c8e262c1e19ad4734de4.json`](../../sessions/c8/c8e262c1e19ad4734de4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已保存（313 行）。结果汇总：

**24/24 论文位置全部 verified，0 missing。**

| Paper Location | Model | Greedy | Oracle | Headroom | Degen% | Old→New Delta |
|---|---|---|---|---|---|---|
| 4B SciERC | Qwen3-4B | 0.6622 | 0.7925 | 13.03pp | 10.4% | +0.85pp |
| 4B CoNLL | Qwen3-4B | 0.9236 | 0.9394 | 1.58pp | — | -0.13pp |
| rank=8 SciERC | Qwen3-8B r8 | 0.6397 | 0.7998 | 16.01pp | — | +0.61pp |
| N=32 SciERC | Qwen3-8B | 0.6397 | 0.8396 | 19.99pp | — | +0.16pp |
| N=16 SciERC seed42 | Qwen3-8B | 0.6442 | 0.8194 | 17.52pp | — | +0.44pp |
| FewNERD N=8 seed42 | Qwen3-8B | 0.7478 | 0.8719 | 12.41pp | — | N/A |
| FewNERD N=16 | Qwen3-8B | 0.7478 | 0.9020 | 15.42pp | 7.1% | N/A |
| LLaMA SciERC s42/123/456 | LLaMA3.1-8B | 0.645-0.646 | 0.763-0.775 | 11.7-12.9pp | 25-27% | -0.3~-0.5pp |
| LLaMA CoNLL s42/123/456 | LLaMA3.1-8B | 0.924 | 0.948-0.949 | 2.4-2.6pp | 86-87% | -0.04~-0.11pp |
| CoNLL Qwen s42/123/456 | Qwen3-8B | 0.907 | 0.957-0.959 | 5.0-5.2pp | 47-55% | -0.48~+0.18pp |
| 3-epoch SciERC | Qwen3-8B | 0.6501 | 0.7998 | 14.97pp | — | +0.52pp |
| 10-epoch SciERC | Qwen3-8B | 0.6467 | 0.7331 | 8.64pp | — | -0.68pp |
| T=0.5/0.8/1.2 SciERC | Qwen3-8B | 0.643-0.649 | 0.740-0.789 | 9.1-14.6pp | 15-41% | -0.28~+0.06pp |
| SciERC canonical seed42 | Qwen3-8B | 0.6439 | 0.7758 | 13.19pp | 17.8% | -0.17pp |
| SciERC seed123/456 | Qwen3-8B | 0.644 | 0.817-0.823 | 17.3-17.9pp | — | +0.44~+0.58pp |

关键发现：
- unified 与 old oracle 的 delta 绝大多数在 ±0.6pp 以内，数值一致性良好
- 退化率最高的是 LLaMA CoNLL（86-87%）和 4B CoNLL（90.6%）
- 产出文件：`output/paper_f1_audit/paper_f1_audit_table.json`

---
