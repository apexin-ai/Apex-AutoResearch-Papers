# investigate 4b evidence tax source

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_4b_evidence_tax_source_20260518T134827_result.json`
- **Structured JSON:** [`8d481ad8b4bd009b6d5f.json`](../../sessions/8d/8d481ad8b4bd009b6d5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the complete picture. Here's the analysis:

---

## 调查结果

### 三组独立的 4B SFT eval 结果

| 来源 | Evidence ign_f1 | No-evi ign_f1 | Tax | 协议 |
|---|---|---|---|---|
| **v1 buggy** (sft_baseline_noquant/metrics.json) | **41.06%** (ign=f1 bug) | — | — | merged model, bs=16 |
| **v2 fixed** (sft_baseline_noquant/metrics_v2.json + sft_no_evidence/metrics_v2.json) | **40.36%** | **47.36%** | **7.00pp** | merged model, bs=16 |
| **D076 reeval** (sft_baseline_d076_reeval + sft_no_evidence_noquant) | **39.74%** | **47.21%** | **7.47pp** | base+adapter, bs=4 |

### 41.06% 的来源

- **文件**: `sft_baseline_noquant/metrics.json` (v1)
- **Config**: model_path=`/root/autodl-tmp/sft_output` (merged model), batch_size=16, seed=42, quantize=false
- **Bug**: ign_f1 == f1 == 0.4106 — evaluator.py 的 Ign-F1 计算有 bug（train_facts 未按 doc_id 过滤），导致 ign_f1 = f1
- v2 修正后该 eval 的真实 ign_f1 = **40.36%**

### "39.86%" — **不存在于任何 metrics 文件中**

搜遍了 `/root/autodl-tmp/eval_results/` 和本地 artifacts 目录，"39.86" 未出现在任何 SFT baseline 的 metrics 文件中。最接近的值是：
- **39.74%** — `sft_baseline_d076_reeval/metrics.json`（D076 protocol, base+adapter, bs=4）
- **40.36%** — `sft_baseline_noquant/metrics_v2.json`（merged model, bs=16, 修正后）

任务描述中的 "39.86%" 可能是 39.74% 的误记，或是 47.36 - 7.5 = 39.86 的反推。

### 差异根因

两个维度的差异叠加：

1. **Ign-F1 计算 bug**：v1 metrics.json 的 ign_f1 没有排除 train triples（ign_f1=f1），v2 修正后 40.36% → 降幅 0.70pp
2. **Eval 协议不同**：merged model (bs=16) vs base+adapter (bs=4) 产生不同的生成行为（merged: f1=41.06, adapter: f1=40.49）

### memory.md 中 "6.15pp" 的来源

混用了两个不同协议的 buggy 值：
- sft_baseline_noquant v1 ign_f1 = 41.06%（buggy, merged model）
- sft_no_evidence_noquant ign_f1 = 47.21%（correct, base+adapter）
- 47.21 - 41.06 = 6.15pp — **跨协议比较 + 使用 buggy 值，无效**

### 论文当前 canonical 值

`paper_metrics_corrected.md` 和 `paper_main_tables_draft.md` 统一使用 **v2 fixed metrics**：
- Evidence: **40.36%**（sft_baseline_noquant/metrics_v2.json）
- No-evidence: **47.36%**（sft_no_evidence/metrics_v2.json）
- Tax: **7.00pp**

### 推荐

论文应使用 **40.36% / 47.36% / tax 7.00pp**（v2 corrected, merged model, 与 paper_metrics_corrected.md 一致）。

如果 RSFT 对比实验全部遵循 D076 protocol（base+adapter, bs=4），那么 SFT baseline 也应对齐为 **39.74% / 47.21% / tax 7.47pp**。当前 D076 paired t-test 已使用 39.74% 作为 baseline。

memory.md 中的 "6.15pp" 需要修正为 7.00pp（v2）或 7.47pp（D076）。

---
