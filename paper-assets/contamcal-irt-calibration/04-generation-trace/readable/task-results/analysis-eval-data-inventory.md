# analysis eval data inventory

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-data-inventory_20260515T132936_result.json`
- **Structured JSON:** [`f2dc3691d7378ed55aac.json`](../../sessions/f2/f2dc3691d7378ed55aac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`3B_d005_s42_aligned` 的 eval 在 mmlu 51/14042 处失败了（HF 超时 + bitsandbytes 错误）。数据已全部收集完毕，现在编译完整矩阵。

## Eval 结果完整数据清单

### 运行状态
- **无 eval 进程正在运行**（活跃进程仅有 Stan MCMC / sim sweep / pooled IRT）
- `Qwen2.5-3B_d005_s42_aligned`: eval 失败（HF ReadTimeout + bitsandbytes error），仅 51/14042 mmlu items

---

### 一、Aligned 版本矩阵（原始 benchmark items，IRT 主数据源）

| Scale | Dosage | s42 | s123 |
|-------|--------|-----|------|
| **0.5B** | d000 | ✅ mmlu=.398 gsm=.369 arc=.469 he=.000 | ✅ mmlu=.422 gsm=.341 arc=.497 he=.000 |
| | d005 | ✅ mmlu=.326 gsm=.362 arc=.329 he=.000 | ✅ mmlu=.300 gsm=.368 arc=.298 he=.000 |
| | d025 | ✅ mmlu=.280 gsm=.366 arc=.325 he=.000 | ✅ mmlu=.347 gsm=.353 arc=.406 he=.000 |
| | d100 | ✅ mmlu=.233 gsm=.365 arc=.294 he=.000 | ✅ mmlu=.306 gsm=.380 arc=.367 he=.000 |
| **1.5B** | d000 | ✅ mmlu=.585 gsm=.654 arc=.772 he=N/A | ✅ mmlu=.586 gsm=.654 arc=.758 he=N/A |
| | d005 | ✅ mmlu=.585 gsm=.648 arc=.769 he=N/A | ❌ **EMPTY** |
| | d025 | ✅ mmlu=.590 gsm=.654 arc=.769 he=N/A | ❌ **EMPTY** |
| | d100 | ✅ mmlu=.593 gsm=.650 arc=.769 he=N/A | ✅ mmlu=.596 gsm=.644 arc=.782 he=N/A |
| **3B** | d000 | ✅ v3: mmlu=.634 gsm=.120 arc=.828 he=.000 | ✅ v2: mmlu=.631 gsm=.268 arc=.826 he=.000 |
| | d005 | ❌ **FAILED** (HF timeout) | ❌ 无数据 |
| | d025 | ✅ v2: mmlu=.600 gsm=.679 arc=.828 he=.000 | ❌ 无数据 |
| | d100 | ✅ v2: mmlu=.632 gsm=.742 arc=.824 he=.000 | ✅ v2: mmlu=.632 gsm=.732 arc=.831 he=.000 |

Item counts (aligned): mmlu=14042, gsm8k=1319, arc_challenge=1172, humaneval=164

---

### 二、Para-aligned 版本矩阵（paraphrased items，污染检测用）

| Scale | Dosage | s42 | s123 |
|-------|--------|-----|------|
| **0.5B** | d000 | ✅ | ❌ |
| | d005 | ✅ | ✅ |
| | d025 | ✅ | ❌ |
| | d100 | ❌ | ❌ |
| **1.5B** | d000 | ✅ | ❌ |
| | d005 | ✅ | ❌ |
| | d025 | ✅ | ❌ |
| | d100 | ✅ | ❌ |
| **3B** | d000 | ✅ v2 | ✅ v2 |
| | d005 | ✅ | ❌ |
| | d025 | ✅ v2 | ❌ |
| | d100 | ✅ v2 | ❌ |

Item counts (para): mmlu=6596, gsm8k=228, arc_challenge=697, humaneval=26

---

### 三、特殊模型

| 目录 | 状态 | 备注 |
|------|------|------|
| 0.5B-Instruct_aligned | ✅ 4/4 | mmlu=.246 gsm=.388 arc=.282 he=.000 |
| 1.5B_base_pretrained | ✅ 4/4 | mmlu=.230 gsm=.005 arc=.230 he=.000 |
| 0.5B_base_pretrained | ❌ EMPTY | |
| 0.5B_base_pretrained_aligned | ❌ EMPTY | |
| 3B_raw | ⚠️ 2/4 | 只有 gsm8k=.605 + humaneval=.000，缺 mmlu/arc |
| 3B DEPRECATED (v1) ×3 | ✅ 有数据 | d000_v1, d005_v1, d100_v1，已弃用 |

---

### 四、Seed=123 专项盘点

| Config | Aligned | Para_aligned |
|--------|---------|--------------|
| 0.5B d000 s123 | ✅ | ❌ |
| 0.5B d005 s123 | ✅ | ✅ |
| 0.5B d025 s123 | ✅ | ❌ |
| 0.5B d100 s123 | ✅ | ❌ |
| 1.5B d000 s123 | ✅ | ❌ |
| 1.5B d005 s123 | ❌ **缺失** | ❌ |
| 1.5B d025 s123 | ❌ **缺失** | ❌ |
| 1.5B d100 s123 | ✅ | ❌ |
| 3B d000 s123 v2 | ✅ | ✅ |
| 3B d100 s123 v2 | ✅ | ❌ |

---

### 五、Pooled IRT 可用 aligned 模型统计

排除 DEPRECATED、base_pretrained、Instruct、raw、d000_s42_v2 (重复) 后：

| Benchmark | 可用 N_models | 明细 |
|-----------|--------------|------|
| **mmlu** | **19** | 0.5B×8 + 1.5B×6 + 3B×5 |
| **gsm8k** | **19** | 同上 |
| **arc_challenge** | **19** | 同上 |
| **humaneval** | **19** | 同上（但所有模型 acc=0.000，分析价值有限） |

3B 可用 aligned 模型 (5)：d000_s42_v3, d000_v2_s123, d025_v2, d100_v2_s42, d100_v2_s123

---

### 六、缺口总结

需要补充的 eval（共 5 个）：
1. **1.5B d005 s123 aligned** — 目录已创建但空
2. **1.5B d025 s123 aligned** — 目录已创建但空
3. **3B d005 s42 aligned** — eval 失败需重跑
4. **3B d005 s123** — 无任何数据（可能 SFT 未完成）
5. **3B d025 s123** — 无任何数据（可能 SFT 未完成）

---
