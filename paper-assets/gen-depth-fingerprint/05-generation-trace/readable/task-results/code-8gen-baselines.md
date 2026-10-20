# code 8gen baselines

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_8gen-baselines_20260516T133345_result.json`
- **Structured JSON:** [`44c6f5937abe27f91d1f.json`](../../sessions/44/44c6f5937abe27f91d1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到 `/root/gen-depth-fingerprint/results/8gen_baselines.json`（总耗时 1095s ≈ 18min）。

**8-gen LOGO 结果汇总：**

| Method | 3-class F1 | 95% CI | Binary F1 | 95% CI |
|--------|-----------|--------|-----------|--------|
| avg_logprob | 0.6847 | [0.7037, 0.7127] | 0.6422 | [0.6729, 0.6844] |
| fastdetectgpt | 0.6546 | [0.6608, 0.6698] | 0.5660 | [0.5747, 0.5863] |
| binoculars | 0.3975 | [0.4042, 0.4138] | 0.5155 | [0.5267, 0.5389] |
| ld_score | 0.6179 | [0.6260, 0.6357] | 0.6570 | [0.6714, 0.6834] |
| **4det_ensemble** | **0.7687** | [0.7748, 0.7829] | **0.6843** | [0.6926, 0.7041] |
| **4det_surface** | **0.7712** | [0.7789, 0.7870] | **0.6903** | [0.6995, 0.7113] |
| **7feature_ours** | **0.7103** | [0.7299, 0.7392] | 0.6531 | [0.6855, 0.6970] |

关键发现：
- 4-detector ensemble (0.7687) 在 3-class 上超过了 7-feature (0.7103)，但两者使用了不同复杂度的输入（4个检测器需要 GPU 推理 vs 7 个统计特征仅需 CPU）
- 加上 surface features (ttr + hapax) 的提升很小 (+0.0025)
- 单独看，avg_logprob 是最强的单检测器 (0.6847 3-class)
- Binoculars 表现最差 (0.3975)，可能因为 observer/performer 都是 Pythia 家族
- 新增的 llama-3.2-3b 和 mistral-7b-v0.3 在所有方法上表现较弱（跨家族泛化挑战）

注意：7-feature 这里用的是 n_estimators=100, max_depth=3（与 baselines 统一），而非论文中的 200/6 配置，所以 F1 低于论文报告值。

---
