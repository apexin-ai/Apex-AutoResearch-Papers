# diagnose 8b rsft seed audit

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_8b-rsft-seed-audit_20260522T212728_result.json`
- **Structured JSON:** [`b649b2143d23cd631330.json`](../../sessions/b6/b649b2143d23cd631330.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论明确，**Reviewer 的担忧不成立**。

## 8B RSFT seed 数量确认

### Qwen3-8B RSFT — 3 个 seed，全部有 adapter + eval 结果

| Seed | Registry Key | ign_f1 | evi_f1 | edcr |
|------|-------------|--------|--------|------|
| s42 | `plan_006_qwen3_8b_rsft_eval` | 0.5433 | 0.8052 | 0.6377 |
| s43 | `d102_8b_rsft_k1_s43` | 0.5471 | 0.8180 | 0.6094 |
| s44 | `plan019_8b_rsft_s44_eval` | 0.5451 | 0.8145 | 0.6233 |

### Llama-3.1-8B RSFT — 3 个 seed，全部有 adapter + eval 结果

| Seed | Registry Key | ign_f1 | evi_f1 | edcr |
|------|-------------|--------|--------|------|
| s42 | `eval_llama_rsft_s42_with_evidence_2048` | 0.5774 | 0.8222 | 0.6143 |
| s43 | `eval_llama_rsft_k1_s43` | 0.5662 | 0.8287 | 0.5783 |
| s44 | `llama_rsft_s44_pipeline` | 0.5587 | 0.8328 | 0.5829 |

### 8B SFT baseline — 同样 3 个 seed

服务器上确认 adapter 存在：
- Qwen3-8B: `sft_output_qwen3_8b_bf16` (s42), `_s43`, `_s44`
- Llama-3.1-8B: `sft_output_llama_3_1_8b` (s42), `_s43`, `_s44`

### 结论

两个 8B 模型的 RSFT 和 SFT 都有 **3 个 seed（s42/s43/s44）**，adapter 文件完整，eval 指标齐全。N=3 的 std 虽然不理想但符合 NLP 领域惯例，17× 方差压缩 claim 在统计上可报告。无需补跑。

---
