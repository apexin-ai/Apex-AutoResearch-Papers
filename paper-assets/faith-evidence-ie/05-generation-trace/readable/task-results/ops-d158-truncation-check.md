# ops d158 truncation check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d158_truncation_check_20260524T092058_result.json`
- **Structured JSON:** [`3539fad2a11a95c8c630.json`](../../sessions/35/3539fad2a11a95c8c630.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

**s42/s43 共享同一份生成数据**（两者的 RSFT 训练都使用 `rsft_scored_1_7b` / `rsft_scored_1_7b_k1`，源自同一个 SFT adapter `sft_output_qwen3_1_7b_bf16`，只是训练 seed 不同）。

| Seed | Truncation Rate | 来源 |
|------|----------------|------|
| **s42** | **12.1%** (2920/24216) | `rsft_scored_1_7b/rsft_report.json` truncation_analysis |
| **s43** | **12.1%**（同上） | 与 s42 共享生成数据 |
| **s44** | **19.2%**（前 100 docs）/ ~20.2%（当前 302/1496） | `d158_1_7b_rsft_s44_generate.log` + JSONL 直接统计 |

**s44 truncation rate 显著高于 s42/s43**（19-20% vs 12.1%，相对增幅 ~60%）。原因是 s44 使用了不同的 SFT adapter（`sft_output_qwen3_1_7b_bf16_seed44`），该模型倾向生成更长的输出。

**是否需要干预：** s44 的 19-20% 不在 s42/s43 的类似范围内（偏高约 8 个百分点）。truncation 的负面影响已在 s42 的 report 中量化：被截断样本的 mean F1 = 0.4389 vs 未截断的 0.6132（差距 0.1743）。s44 更高的 truncation rate 意味着更多低质量候选进入筛选池。建议 Director 决定是否需要增大 `max_new_tokens`（当前默认 1024）或接受该水平。

---
