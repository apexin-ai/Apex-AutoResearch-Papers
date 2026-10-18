# infra read expb results

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_read-expb-results_20260513T235027_result.json`
- **Structured JSON:** [`9e57fb038de1538f69c9.json`](../../sessions/9e/9e57fb038de1538f69c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

以下是 Exp B 的完整结果。

---

## 1. `full_bitwidth.log` (456 行)

### 配置
- Model: Qwen2.5-7B, 28 layers × 4 KV heads = **112 heads**, 336 profiling items (3 bitwidths × 112)
- Budget: 0.25 (=4-bit equivalent)
- Calibration: 16 seqs × 512 tokens
- Baseline calibration PPL: **10.8011**

### Phase 1: Profiling (163.3s)

Sensitivity 高度集中在 **Layer 0**：

| Head | 2bit delta | 4bit delta | 8bit delta |
|------|-----------|-----------|-----------|
| L0H0 | **3.2935** | 0.1704 | 0.0000 |
| L0H2 | **2.2323** | 0.5194 | 0.1704 |
| L0H3 | **1.0638** | 0.1704 | 0.0000 |
| L0H1 | **0.8795** | 0.8795 | 0.0000 |

L1-L27 大部分 head delta=0.0（不敏感），少数有微小 delta（0.17~0.52）。

2-bit delta 统计：min=0.0, max=3.2935, mean=0.1278, std=0.3984

**核心问题：绝大多数 head 在所有 bitwidth 下 delta=0.0，profiler 分辨率不足。**

### Phase 2: MCKP 分配

```
{'2bit': 75, '4bit': 33, '8bit': 3, '16bit': 1}
```
- Actual memory ratio: **0.1797** (target 0.25)——budget 没用满，MCKP 过度压缩
- MCKP total distortion: **0.0**——solver 认为这些 2-bit 分配无代价
- Layer 0 特殊处理：H0=8bit, H1=8bit, H2=**16bit**(full), H3=8bit

### Phase 3: WikiText-2 PPL 评估

| Method | PPL | Delta vs Uniform 4-bit |
|--------|-----|----------------------|
| **Baseline** | **9.8106** | — |
| **Non-uniform MCKP** | **36.9242** | **-21.48** (远差于 uniform) |
| **Uniform 4-bit** | **15.4454** | — |

### Verdict: **FAIL**

Non-uniform improvement: -21.48 (threshold ≥ 0.5)

### Warning
- Token indices sequence length > max (298938 > 131072)——WikiText-2 evaluation 时触发，但不影响 PPL 计算本身

---

## 2. `budget_matched.log` (22 行)

手动策略：**L0 全部@8bit，8 个最不敏感 head@2bit，其余@4bit**，实际 budget=0.2500

```
Budget-matched PPL: 11.6865
vs uniform 4-bit (15.4454): delta = +3.7589
VERDICT: PASS
```

---

## 3. `manual_test.log` (57 行)

三种手动策略对比：

| Strategy | Config | Budget | PPL | vs Uniform 4-bit |
|----------|--------|--------|-----|-------------------|
| S1 | L0@8bit, rest@4bit | 0.2589 | **10.6221** | **+4.82** |
| S2 | L0@16bit, 24@2bit, rest@4bit | 0.2500 | 17.7414 | -2.30 |
| S3 | Fixed MCKP (68×2, 30×4, 4×8, 10×16) | 0.2500 | 32.4467 | -17.00 |

S1（仅保护 L0）效果最好，PPL 接近 baseline；S2/S3 引入 2-bit 后大幅恶化。

---

## 4. `full_bitwidth_results.json` 关键字段

```json
{
  "verdict": "FAIL",
  "baseline_calibration_ppl": 10.8011,
  "baseline_wikitext2_ppl": 9.8106,
  "mckp_wikitext2_ppl": 36.9242,
  "uniform4bit_wikitext2_ppl": 15.4454,
  "mckp_improvement_over_uniform": -21.4788,
  "bit_distribution": {"2bit": 75, "4bit": 33, "8bit": 3, "16bit": 1},
  "mckp_actual_memory_ratio": 0.1797,
  "mckp_total_distortion": 0.0
}
```

---

## 诊断总结

**根因：PPL profiler 分辨率坍缩。** 112 个 head 中，只有 ~15 个在 2-bit 时有 non-zero delta，其余全为 0.0。MCKP solver 看到 delta=0 就认为 2-bit 无损，疯狂分配 2-bit（75/112），实际 memory ratio 只有 0.18（远低于 0.25 target）。但 2-bit 量化的真实损失被 profiler 漏测了。

手动实验证实：**保护 Layer 0 + uniform 4-bit（S1, PPL=10.62）远优于 MCKP 的"智能"分配（PPL=36.92）**。Budget-matched 策略（PPL=11.69）也 PASS。问题不在 MCKP solver 本身，在于 profiling 信号质量。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "verdict": "FAIL",
    "baseline_calibration_ppl": 10.8011,
    "baseline_wikitext2_ppl": 9.8106,
    "mckp_wikitext2_ppl": 36.9242,
    "uniform4bit_wikitext2_ppl": 15.4454,
    "mckp_improvement_over_uniform": -21.4788,
    "bit_distribution": {
      "2bit": 75,
      "4bit": 33,
      "8bit": 3,
      "16bit": 1
    },
    "mckp_actual_memory_ratio": 0.1797,
    "mckp_total_distortion": 0.0
  }
}
```

</details>

---
