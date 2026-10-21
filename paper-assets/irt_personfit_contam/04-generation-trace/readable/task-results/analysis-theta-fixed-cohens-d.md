# analysis theta fixed cohens d

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_theta-fixed-cohens-d_20260521T165541_result.json`
- **Structured JSON:** [`314ac9193d210af5e1e3.json`](../../sessions/31/314ac9193d210af5e1e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行完成。结果已保存到 `/root/autodl-tmp/theta_fixed_results.json`。

### 核心结果

**θ-fixed Cohen's d + 95% CI：**

| Model | θ_fixed | n | d_fixed(15%) | 95% CI | d_fixed(50%) | 95% CI |
|-------|---------|---|-------------|--------|-------------|--------|
| Qwen | -0.1022 | 10 | -4.77 | [-7.79, -3.97] | **-14.52** | [-24.79, -12.10] |
| Llama | -0.6426 | 10 | -0.58 | [-2.37, 0.04] | -0.84 | [-2.97, -0.17] |
| Mistral | -1.0652 | 6 | 2.59 | [1.45, 9.00] | **5.60** | [3.71, 18.16] |

**free-θ vs θ-fixed 对比：**

| Model | Condition | \|d_free\| | \|d_fixed\| | 放大倍数 |
|-------|-----------|-----------|------------|---------|
| Qwen | contam_15 | 6.57 | 4.77 | 0.7x |
| Qwen | contam_50 | 1.90 | **14.52** | **7.7x** |
| Llama | contam_15 | 2.27 | 0.58 | 0.3x |
| Llama | contam_50 | 2.50 | 0.84 | 0.3x |
| Mistral | contam_15 | 1.97 | 2.59 | 1.3x |
| Mistral | contam_50 | 2.69 | **5.60** | **2.1x** |

### 关键发现

1. **Qwen contam_50: \|d\| = 14.52**，远超 free-θ 的 1.90，放大 7.7 倍。符合预期。

2. **方向不一致**：Qwen/Llama 的 d_fixed 为负（contam lz* 比 clean 更正/更高），Mistral 为正（contam lz* 比 clean 更负）。原因是 θ 被低估时，contaminated 模型答对了更多"不该对"的 item，使 lz* 向 positive 方向偏移（Qwen/Llama），而 Mistral 的 IRT 参数特征不同导致相反方向。

3. **Llama 效果弱**：θ-fixed 下 Llama 的 |d| 反而减小（0.84 < 2.50），clean lz*_fixed 的标准差大（1.49），可能是 IRT 参数对 Llama 拟合度不高导致 clean baselines 本身离散。

4. **ARC-C 数据不在 westd-35694 上**，已跳过。

---
