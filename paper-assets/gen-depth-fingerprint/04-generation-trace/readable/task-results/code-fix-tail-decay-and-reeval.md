# code fix tail decay and reeval

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-tail-decay-and-reeval_20260516T123517_result.json`
- **Structured JSON:** [`6ee0af2da259ebd514e2.json`](../../sessions/6e/6ee0af2da259ebd514e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 步完成。以下是完整汇总：

---

## RESULTS SUMMARY

### tail_decay 修复确认

- **原 6-gen 公式**: 排序 avg log-prob 分布在 rank 100-1000 的线性回归斜率（值域 ≈ -0.002）
- **新代码旧公式**: NLL 超过 depth-0 第 90 百分位的 token 比例（值域 ≈ 0.098）
- **已修复**: 3 个新数据集（Llama/Mistral/Llama-rp11）全部重新提取，tail_decay 统一为斜率公式
- **特征文件已覆盖**: 4680 + 4849 + 4416 = 13945 条 unfiltered 数据

---

### 8-gen LOGO (unfiltered)

| | 3-class F1 | binary F1 |
|---|---|---|
| **Overall** | **0.762** | **0.6944** |

Per-generator (3-class, 95% CI):
```
Pythia-2.8B:    0.7983 [0.7865, 0.8097]
Pythia-1B:      0.8064 [0.7946, 0.8177]
OLMo-2-1B:     0.781  [0.7695, 0.7931]
Qwen3-0.6B:    0.7795 [0.7677, 0.7925]
Qwen3-1.7B:    0.7717 [0.7585, 0.7844]
Qwen3-8B:      0.7143 [0.7007, 0.7286]
Llama-3.2-3B:  0.7753 [0.7634, 0.788]
Mistral-7B:    0.6815 [0.6694, 0.695]
```

---

### rp-LOFO

| Test | 3-class F1 | binary F1 |
|---|---|---|
| **A: Llama rp=1.1** | **0.4168** | **0.5182** |
| **B: Llama rp=1.0 filtered** | **0.7149** | **0.6116** |

Test A per-class accuracy: class_0=0.986, class_1=0.097, class_2=0.449

Test A 结论：模型对 rp=1.1 数据的 class_1 几乎全部误判（仅 9.7% accuracy），说明 repetition penalty 显著改变了 depth-1 的特征分布。

---

### Filter diagnostic

| Setting | 3-class | binary |
|---|---|---|
| 6-gen unfiltered | 0.7879 | 0.7215 |
| 6-gen filtered | 0.7226 | 0.6386 |
| 8-gen unfiltered | 0.762 | 0.6944 |
| 8-gen filtered | 0.7108 | 0.6183 |

Filtering 降低性能约 6-8 个点——被滤掉的高重复样本（depth-2+）恰恰是分类器最容易正确判断的 easy cases。

---

输出文件：
- `/root/gen-depth-fingerprint/results/8gen_logo_unfiltered.json`
- `/root/gen-depth-fingerprint/results/rp_lofo_results.json`
- `/root/gen-depth-fingerprint/results/filter_diagnostic.json`

---
