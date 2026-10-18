# code p0 2 2bit cliff

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_p0-2-2bit-cliff_20260513T221743_result.json`
- **Structured JSON:** [`6d14c50108afbf41b0b5.json`](../../sessions/6d/6d14c50108afbf41b0b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部测试完成。以下是产出报告。

---

## 产出报告

### 1. cliff_test.py 已部署
`/root/ratekv/cliff_test.py`，9615 bytes。提供 `CliffTester` 类和 CLI 入口。

### 2. Smoke Test 输出（1.5B, 5000 tokens）
```
Baseline PPL: 17.62
Head 0_0 @2bit: PPL delta = 92.5715
Head 14_0 @2bit: PPL delta = 0.7646
SMOKE TEST PASSED
```

### 3. 1.5B 完整测试结果（10000 tokens, Baseline PPL = 16.0218）

#### 2-bit 量化
| 指标 | 值 |
|------|-----|
| Cliff heads (>10% PPL increase) | **2/56 (3.6%)** |
| Max delta | +47.56 (L0H0, +296.8%) |
| Mean delta | +1.90 |

**Top-10 worst:**
| Head | PPL | Delta | % |
|------|-----|-------|---|
| L0H0 | 63.58 | +47.56 | +296.8% |
| L0H1 | 54.55 | +38.53 | +240.5% |
| L24H1 | 16.90 | +0.88 | +5.5% |
| L6H1 | 16.89 | +0.86 | +5.4% |
| L8H0 | 16.89 | +0.86 | +5.4% |
| L8H1 | 16.86 | +0.84 | +5.2% |
| L25H1 | 16.83 | +0.81 | +5.1% |
| L21H0 | 16.82 | +0.80 | +5.0% |
| L17H1 | 16.81 | +0.79 | +4.9% |
| L10H0 | 16.70 | +0.68 | +4.3% |

**Bottom-10 (最小 delta):**
| Head | PPL | Delta | % |
|------|-----|-------|---|
| L12H0 | 16.00 | -0.02 | -0.1% |
| L3H1 | 16.07 | +0.05 | +0.3% |
| L17H0 | 16.13 | +0.11 | +0.7% |
| L10H1 | 16.14 | +0.12 | +0.8% |
| L2H1 | 16.16 | +0.14 | +0.9% |
| L6H1 → L13H1 | 16.17 | +0.15 | +0.9% |
| L22H0 | 16.18 | +0.16 | +1.0% |
| L26H1 | 16.19 | +0.17 | +1.1% |
| L1H1 | 16.20 | +0.18 | +1.1% |
| L18H0 | 16.20 | +0.18 | +1.1% |

#### 4-bit 量化
| 指标 | 值 |
|------|-----|
| Cliff heads | **1/56 (1.8%)** |
| Max delta | +2.21 (L0H1, +13.8%) |
| Mean delta | +0.06 |

除 Layer 0 外，所有 head 的 4-bit delta < 1%。

#### 8-bit 量化
| 指标 | 值 |
|------|-----|
| Cliff heads | **0/56 (0%)** |
| Max delta | +0.27 (L0H0, +1.7%) |
| Mean delta | -0.003 |

完全安全，无 cliff。

### 4. Cliff Effect 分析

**是否存在 cliff effect？是，但仅限于 Layer 0。**

- **2-bit cliff 集中在 Layer 0**：L0H0 (+297%) 和 L0H1 (+241%) 是唯二超过 10% 阈值的 head。其余 54 个 head 的 2-bit delta 都在 0~5.5% 范围内，无 cliff。
- **4-bit 也主要是 Layer 0 敏感**：L0H1 (+13.8%) 是唯一 cliff head。
- **8-bit 完全无 cliff**。
- **结论**：2-bit 不是"任一 head 设为 2-bit 即灾难"。问题是**Layer 0 极度敏感**，而非 2-bit 本身不可用。MCKP solver 的 action space 不应全局删除 2-bit，而应**仅对 Layer 0 禁止 2-bit（和低于 8-bit 的 quant）**，其他层的 2-bit 可以保留。

### 5. 7B 完整测试推荐命令

```bash
cd /root/ratekv && CUDA_VISIBLE_DEVICES=1 python cliff_test.py \
  --model /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B \
  --calibration_data calibration_data.json \
  --device cuda:0 \
  --bits 2,4,8 \
  --max_eval_tokens 10000 \
  --output cliff_7B_results.json
```

预计耗时：112 heads × 3 bits × ~2s/head ≈ ~11 min（7B 比 1.5B 慢但 Blackwell 96GB 够快）。

---
