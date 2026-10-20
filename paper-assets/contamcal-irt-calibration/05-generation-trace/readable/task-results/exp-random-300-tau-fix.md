# exp random 300 tau fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_random-300-tau-fix_20260517T221453_result.json`
- **Structured JSON:** [`14abd765b50966f3224a.json`](../../sessions/14/14abd765b50966f3224a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。以下是完整结果：

---

## 1. 重复模型诊断

旧脚本中的两个 "3B_d000_s42" 来自：
- **Index 8**: `Llama-3.2-3B_d000_s42_aligned` (MMLU acc=0.4545) — **错误混入**。`load_pooled_eval_results` 的 scale 过滤器匹配 "3B" in "Llama-3.2-3B"，导致 4 个 Llama 模型被当作 Qwen 3B 加载
- **Index 13**: `Qwen2.5-3B_d000_s42_a32_aligned` (MMLU acc=0.6307) — 正确的 alpha=32 版本

简化命名 `f"{scale}_d{dosage:03d}_s{seed}"` 把二者都显示为 "3B_d000_s42"，掩盖了它们是不同模型的事实。

## 2. J=16 model set（与 RRF τ=0.7313 完全一致）

| # | 目录名 | Scale | Dosage |
|---|--------|-------|--------|
| 1 | Qwen2.5-1.5B_d000_s123_aligned | 1.5B | 0 |
| 2 | Qwen2.5-1.5B_d000_s42_aligned | 1.5B | 0 |
| 3 | Qwen2.5-1.5B_d005_s123_aligned | 1.5B | 5 |
| 4 | Qwen2.5-1.5B_d005_s42_aligned | 1.5B | 5 |
| 5 | Qwen2.5-1.5B_d025_s123_aligned | 1.5B | 25 |
| 6 | Qwen2.5-1.5B_d025_s42_aligned | 1.5B | 25 |
| 7 | Qwen2.5-1.5B_d100_s123_aligned | 1.5B | 100 |
| 8 | Qwen2.5-1.5B_d100_s42_aligned | 1.5B | 100 |
| 9 | Qwen2.5-3B_d000_s123_aligned | 3B | 0 |
| 10 | Qwen2.5-3B_d000_s42_a32_aligned | 3B | 0 |
| 11 | Qwen2.5-3B_d005_s123_aligned | 3B | 5 |
| 12 | Qwen2.5-3B_d005_s42_a32_aligned | 3B | 5 |
| 13 | Qwen2.5-3B_d025_s123_aligned | 3B | 25 |
| 14 | Qwen2.5-3B_d025_v3_s42_aligned | 3B | 25 |
| 15 | Qwen2.5-3B_d100_a32_s123_aligned | 3B | 100 |
| 16 | Qwen2.5-3B_d100_a32_s42_aligned | 3B | 100 |

## 3. 修正后 Random 300 τ 结果

| Seed | τ_calibrated | p-value |
|------|-------------|---------|
| 42 | 0.5004 | 0.0128 |
| 123 | 0.6158 | 0.0022 |
| 456 | 0.5966 | 0.0030 |
| 789 | 0.5004 | 0.0128 |
| 1024 | 0.5581 | 0.0055 |

**Mean ± Std: 0.5543 ± 0.0478**

## 4. 与 RRF 300 对比

| Method | τ | Note |
|--------|---|------|
| RRF 300 (Vanilla 2PL) | **0.7313** | 信号引导选 item |
| Random 300 (Vanilla 2PL) | 0.5543 ± 0.048 | 随机选 item |
| Δ | +0.177 | RRF 选 item 带来的增益 |

RRF item selection 将 τ 从 0.55 提升到 0.73，证明信号引导的 item 选择对校准排序有显著贡献。所有 5 seeds 的 random baseline 均 p<0.05 显著，说明即便随机选 300 items，IRT 也能提取出有意义的 θ 排序，但比 RRF 差了约 0.18 个 τ。

修正后脚本：`/root/contamcal-irt-calibration/exp006/random_300_tau_baseline_fixed.py`
结果 JSON：`/root/autodl-tmp/exp006/random_300_tau_baseline_j16_fixed.json`

---
