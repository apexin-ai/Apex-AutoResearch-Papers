# audit trace llama rsft s42

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_trace-llama-rsft-s42_20260524T053125_result.json`
- **Structured JSON:** [`d78c17320d324a197aac.json`](../../sessions/d7/d78c17320d324a197aac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集完毕。以下是完整汇总。

---

## LLaMA-3.1-8B RSFT s42 所有 eval 输出

| # | 目录 | ign_f1 | rel_f1 | evi_f1 | max_new_tokens | no_evidence | checkpoint | 时间 |
|---|------|--------|--------|--------|---------------|-------------|------------|------|
| 1 | `plan_006_llama_rsft_r3_eval` | **55.63** | 56.74 | 82.55 | 1024 | false | `rsft_output_llama_3_1_8b_r3/checkpoint-3312` (**k=3**) | May 17 19:05 |
| 2 | `d102_llama_k1_s42` | **57.14** | 58.39 | 82.38 | 1024 | false | `rsft_output_llama_3_1_8b_k1` (**k=1**) | May 18 18:52 |
| 3 | `eval_llama_rsft_s42_no_evidence` | 55.26 | 56.66 | 0.03 | 1024 | true | `rsft_output_llama_3_1_8b_k1` (k=1) | May 20 08:57 |
| 4 | `eval_llama_rsft_s42_with_evidence_2048` | 57.74 | 58.92 | 82.22 | 2048 | false | `rsft_output_llama_3_1_8b_k1` (k=1) | May 21 15:03 |
| 5 | `eval_llama_rsft_s42_no_evi_2048` | 55.59 | 57.03 | 0.07 | 2048 | true | `rsft_output_llama_3_1_8b_k1` (k=1) | May 21 22:01 |

## 结论

- **Registry 55.63** → 来自 `plan_006_llama_rsft_r3_eval`（May 17）。使用的是旧的 **k=3** RSFT 模型 (`rsft_output_llama_3_1_8b_r3/checkpoint-3312`)。

- **Paper 57.14** → 来自 `d102_llama_k1_s42`（May 18）。使用的是方法论修正后的 **k=1** RSFT 模型 (`rsft_output_llama_3_1_8b_k1`)。

**差异根因**：不是同一个模型的不同 eval 配置，而是**两个不同的 RSFT 模型**。d102 的 registry hypothesis 明确写道："D102 方法论修正：LLaMA-8B RSFT 从 k=3 改为 k=1（与论文声明和 4B canonical 一致）"。即 d102 将 LLaMA RSFT 从 k=3 修正为 k=1 以匹配论文方法论声明，产生了新的 57.14 结果，但 registry 的 ign_f1 字段仍指向旧的 plan_006 (k=3) 的 55.63，**未更新为 d102 (k=1) 的 57.14**。

**Paper 57.14 是正确值**（k=1，与论文声明的方法论一致）。Registry 的 55.63 是过时值，应更新。

---
