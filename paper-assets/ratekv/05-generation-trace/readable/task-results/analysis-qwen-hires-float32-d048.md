# analysis qwen hires float32 d048

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen_hires_float32_d048_20260514T194026_result.json`
- **Structured JSON:** [`6f89f46aedf1b2b0f857.json`](../../sessions/6f/6f89f46aedf1b2b0f857.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D048 分析报告：Qwen2.5-7B float32 hires profiling

### 核心结论

**Float32 hires top-5% concentration = 0.6104**

bf16 精度 bug 对 concentration 的影响**可忽略**。高 concentration 是 hires profiling 的真实信号，不是精度伪影。

### 对比

| 条件 | top-5% concentration | 备注 |
|------|---------------------|------|
| bf16 hires (论文值) | 0.59–0.66 | 曾怀疑虚高 |
| **float32 hires (本次)** | **0.6104** | 在 bf16 范围内 |
| float32 lowres (16×512) | 0.42 | 分辨率低导致偏低 |
| Claim 3 阈值 | 0.50 | — |

**结论：0.61 >> 0.50，Claim 3 站得住。** 之前 lowres 得到 0.42 是因为分辨率不够（16×512 vs 64×2048），不是 bf16 虚高。

### Profiling 配置

- 模型: Qwen2.5-7B, 28 layers × 4 heads = 112 heads
- 校准: 64 seqs × 2048 tokens, float32 精度
- 校准基线 PPL: 8.20

### Top-10 最敏感 heads（2-bit distortion delta）

| Rank | Head | 2-bit Δ | 占总量 |
|------|------|---------|--------|
| 1 | L0H0 | 6.7388 | 34.6% |
| 2 | L0H2 | 2.1231 | 10.9% |
| 3 | L0H3 | 1.3105 | 6.7% |
| 4 | L0H1 | 1.2444 | 6.4% |
| 5 | L27H1 | 0.4687 | 2.4% |
| 6 | L4H1 | 0.3495 | 1.8% |
| 7 | L26H1 | 0.2527 | 1.3% |
| 8 | L24H1 | 0.1967 | 1.0% |
| 9 | L18H3 | 0.1926 | 1.0% |
| 10 | L4H0 | 0.1735 | 0.9% |

Layer 0 四个 heads 合计占总 distortion 的 58.6%——极度集中在首层。

### MCKP 分配与 PPL

| 指标 | 值 |
|------|-----|
| MCKP 分配 | full_16: 1, quant_8: 3, quant_4: 96, quant_2: 12 |
| 内存比 | 0.25 (4× 压缩) |
| Baseline PPL | 9.81 |
| MCKP PPL | 10.95 (+11.6%) |
| Uniform 4-bit PPL | 15.45 (+57.5%) |
| MCKP distortion | 0.757 vs uniform 2.859 (3.8× 更优) |

### bf16 bug 影响幅度

bf16 hires 中位值 ~0.62 vs float32 hires 0.61，差异 ~0.01。**bf16 精度 bug 对 top-5% concentration 几乎无影响。** 这符合预期——concentration 是比例指标（top-k 之和 / 总和），分子分母同方向偏移时比值稳定。

### 行动建议

- Claim 3 无需修改，0.50 阈值有充分支撑
- 论文可继续引用 bf16 hires 的 concentration 值，float32 验证已确认其可靠性
- lowres vs hires 的差异（0.42 vs 0.61）应归因于 profiling 分辨率，论文中如有讨论可明确此点

---
