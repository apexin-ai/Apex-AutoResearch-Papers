# exp j16 domain gamma collect

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_j16-domain-gamma-collect_20260518T021217_result.json`
- **Structured JSON:** [`fe67b70d47f1023999cd.json`](../../sessions/fe/fe67b70d47f1023999cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full picture. Here are the results.

---

## 状态总结

### `j16_qwen` (纯 Qwen, 目标 run) — **仍在运行**
- PID 61916, 启动于 10:06:06
- 已完成: STEM_Math (domain 1/8)
- 当前: STEM_Science (domain 2/8), 10:14:31 开始
- 每个 domain ~8 min, 预计完成时间: **~11:10** (约 50 min 后)
- 模型集: 8 Qwen 1.5B + 8 Qwen 3B = 16 (纯 Qwen, 排除 0.5B 和 Llama)

### `j16_cross_family` (含 Llama) — **已完成, 全部 8 domains**
- 模型集: 8 Qwen 1.5B + 3 Llama 3B + 5 Qwen 3B = 16
- **不是**纯 Qwen, 但可作参考

---

## Cross-Family J=16 完整结果 (参考)

| Domain | n_items | γ_mean | 95% CI | P(γ<0)† | R̂ | ESS | PPP |
|---|---|---|---|---|---|---|---|
| **Social_Sciences** | 2000 | **-1.092** | [-1.497, -0.674] | **~100%** | 1.008 | 1338 | 1.000 |
| **Humanities** | 2000 | **-0.954** | [-1.425, -0.485] | **~100%** | 1.008 | 1477 | 1.000 |
| **Other** | 883 | **-0.880** | [-1.548, -0.233] | **~99.5%** | 0\* | 0\* | 0\* |
| **STEM_Math** | 1190 | **-0.386** | [-0.999, 0.200] | **~89%** | 1.009 | 1448 | 0.998 |
| Business_Law | 2000 | -0.239 | [-0.676, 0.203] | ~86% | 0\* | 0\* | 0\* |
| STEM_Science | 1397 | +0.042 | [-0.535, 0.633] | ~44% | 1.008 | 1444 | 0.981 |
| Medical | 1640 | +0.218 | [-0.336, 0.738] | ~21% | 0\* | 0\* | 0\* |
| STEM_CS_Eng | 557 | +0.362 | [-0.443, 1.184] | ~19% | 1.006 | 1616 | 0.893 |

†P(γ<0) 由正态近似 Φ(-γ_mean/γ_sd) 计算。γ < 0 = anti-contamination。

\*R̂=0 / ESS=0 / PPP=0 是 **post-processing bug**（`cmdstan diagnose` 提取失败，写入默认值 0），不影响 γ posterior 本身。这三个 domain (Medical, Business_Law, Other) 的采样正常完成（无 divergences, fit_time 合理）。

---

## 关键发现

1. **Social Sciences P(γ<0) ≈ 100%**, γ_mean = -1.09, 比 J=13 参考值 (P(γ<0)=99.1%, γ≈-0.43) **更强**。但注意 cross-family 包含 Llama (theta 明显更低: -0.25 to -0.47), 可能放大了 anti-contamination 信号。

2. **三强 anti-contamination domains**: Social Sciences, Humanities, Other — 95% CI 完全在 0 以下。

3. **三 domain 接近 null**: STEM_Science, Medical, STEM_CS_Eng — CI 包含 0, 方向甚至偏 pro-contamination。

4. **纯 Qwen 结果需等 `j16_qwen` 完成** 才能与 J=13 直接对比。Llama 模型的加入可能系统性改变 γ 估计。

---
