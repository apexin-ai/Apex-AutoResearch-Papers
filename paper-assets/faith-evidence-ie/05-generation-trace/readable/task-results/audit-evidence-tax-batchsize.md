# audit evidence tax batchsize

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_evidence-tax-batchsize_20260523T143541_result.json`
- **Structured JSON:** [`778acdcb2e44359bc672.json`](../../sessions/77/778acdcb2e44359bc672.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。以下是完整审计报告。

---

## 审计项 4: Evidence Tax 数值追溯

### 逐项验证

```
[PASS] 1.7B s42 | 论文 tax=-5.43pp | with-evi=0.2933 (源:test_eval_1_7b_rsft_s42) | no-evi=0.2390 (源:test_eval_1_7b_rsft_s42_no_evi) | 计算 tax=0.2390-0.2933=-5.44pp | Δ=0.01pp 四舍五入差异
```

```
[PASS] 4B s42 | 论文 tax=+1.51pp | with-evi=0.2501 (源:test_eval_4b_rsft_s42_v2) | no-evi=0.2652 (源:test_eval_4b_rsft_s42_no_evi) | 计算 tax=0.2652-0.2501=+1.51pp
[PASS] 4B s43 | 论文 tax=+1.99pp | with-evi=0.2503 (源:test_eval_4b_rsft_s43_with_evi) | no-evi=0.2702 (源:test_eval_4b_rsft_s43_no_evi) | 计算 tax=0.2702-0.2503=+1.99pp
[PASS] 4B s44 | 论文 tax=+1.46pp | with-evi=0.2525 (源:test_eval_4b_rsft_s44_with_evi) | no-evi=0.2671 (源:test_eval_4b_rsft_s44_no_evi_r2) | 计算 tax=0.2671-0.2525=+1.46pp
[PASS] 4B mean | 论文 tax=+1.65±0.29pp | 计算 mean=(1.51+1.99+1.46)/3=+1.65pp, sample_std=0.29pp
```

```
[PASS] 8B s42 | 论文 tax=-0.34pp | with-evi=0.3353 (源:test_eval_8b_rsft_s42) | no-evi=0.3319 (源:test_eval_8b_rsft_s42_no_evi) | 计算 tax=-0.34pp
[PASS] 8B s43 | 论文 tax=-1.74pp | with-evi=0.3398 (源:test_eval_8b_rsft_s43_with_evi) | no-evi=0.3224 (源:test_eval_8b_rsft_s43_no_evi) | 计算 tax=-1.75pp | Δ=0.01pp
[PASS] 8B s44 | 论文 tax=-0.65pp | with-evi=0.3329 (源:test_eval_8b_rsft_s44_with_evi) | no-evi=0.3264 (源:test_eval_8b_rsft_s44_no_evi) | 计算 tax=-0.64pp | Δ=0.01pp
[PASS] 8B mean | 论文 tax=-0.91±0.74pp | 计算 mean=(-0.34-1.75-0.64)/3=-0.91pp, sample_std=0.74pp
```

```
[PASS] LLaMA s42 | 论文 tax=-1.74pp | with-evi=0.3554 (源:test_eval_llama_rsft_s42_with_evi_v3) | no-evi=0.3380 (源:test_eval_llama_rsft_s42_no_evi_v2) | 计算 tax=-1.74pp
[PASS] LLaMA s43 | 论文 tax=-1.17pp | with-evi=0.3488 (源:test_eval_llama_rsft_s43_with_evi) | no-evi=0.3371 (源:test_eval_llama_rsft_s43_no_evi) | 计算 tax=-1.17pp
```

```
[PASS] 14B s42 | 论文 tax=+0.77pp | with-evi=0.3849 (源:test_eval_14b_rsft_s42) | no-evi=0.3926 (源:test_eval_14b_rsft_s42_no_evi) | 计算 tax=0.3926-0.3849=+0.77pp
```

**所有 tax 值均 PASS**（最大偏差 0.01pp，在四舍五入误差范围内）。

---

### 额外发现：fig_evidence_tax 图与数据不一致

`plot_evidence_tax.py` 硬编码了 `n_seeds = [1, 3, 1, 1, 1]`，但实际可用 seed 数：

| 模型 | 图中 n_seeds | 实际可用 seeds | 图中值 | 实际 multi-seed mean |
|------|-------------|---------------|--------|---------------------|
| 1.7B | 1 (s42) | **2** (s42,s43) | -5.43 | -5.01±0.60 |
| 4B | 3 ✓ | 3 | +1.65±0.29 | ✓ |
| 8B | **1** | **3** (s42,s43,s44) | -0.91 | -0.91±0.74（值正确但漏了 error bar） |
| LLaMA | 1 (s42) | **2** (s42,s43) | -1.74 | -1.46±0.40 |
| 14B | 1 ✓ | 1 | +0.77 | ✓ |

**关键问题：8B 图中的值 -0.91 实际上是 3-seed mean，但 `n_seeds=1` 且无 error bar。**图的 caption 明确说"Error bars show ±1 std where ≥2 seeds are available"，但 8B（3 seeds）没有 error bar，与 caption 矛盾。

---

## 审计项 4B: batch_size confound

### 完整 batch_size 清单

| Tax Pair | with-evi bs | no-evi bs | 匹配? |
|----------|------------|----------|-------|
| 1.7B s42 | 1 | 1 | ✓ |
| 1.7B s43 | 1 | **16** | **✗ MISMATCH** |
| 4B s42 | 16 | **1** | **✗ MISMATCH** |
| 4B s43 | 16 | 16 | ✓ |
| 4B s44 | 16 | **4** | **✗ MISMATCH** |
| 8B s42 | 16 | **1** | **✗ MISMATCH** |
| 8B s43 | 16 | 16 | ✓ |
| 8B s44 | 16 | 16 | ✓ |
| 14B s42 | 1 | 1 | ✓ |
| LLaMA s42 | 16 | 16 | ✓ |
| LLaMA s43 | 16 | 16 | ✓ |

```
[CONCERN] batch_size confound | 4/11 pairs mismatched
  4B s42: with-evi=bs16, no-evi=bs1
  4B s44: with-evi=bs16, no-evi=bs4
  8B s42: with-evi=bs16, no-evi=bs1
  1.7B s43: with-evi=bs1, no-evi=bs16
```

**影响评估：**

- **4B**：3 个 seed 中 2 个有 confound（s42, s44）。仅 s43 是 bs=16/16 一致的。
  - s43 (clean, bs16/16): tax = +1.99pp
  - s42 (confounded, bs16/1): tax = +1.51pp
  - s44 (confounded, bs16/4): tax = +1.46pp
  - 如果 bs 不影响结果，3-seed mean +1.65 有效；但无法排除 confound
- **8B**：仅 s42 confounded，s43/s44 一致。8B 的 3-seed mean (-0.91) 中 s42 的权重为 1/3
- **1.7B s43**：confounded 但未用于论文图中（图只用 s42）
- 对于 autoregressive generation，理论上 batch_size 不影响输出（左 padding + 独立解码），但实现 bug（padding 错误、attention mask 问题）可能导致差异。**建议**：用一致 batch_size 重跑 4B s42 no-evi 和 4B s44 no-evi（bs=16）验证是否有差异。若结果一致则 confound 可排除。

---
