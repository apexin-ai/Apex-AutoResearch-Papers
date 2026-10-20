# research signals inventory 3B

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_signals-inventory-3B_20260516T004938_result.json`
- **Structured JSON:** [`21e0b2dafe9a7c1c4994.json`](../../sessions/21/21e0b2dafe9a7c1c4994.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成。以下是汇总。

---

## 3B Signals 完成度矩阵（仅 alpha=32 可用 checkpoints）

### Seed 123

| Checkpoint | mmlu | gsm8k | arc_challenge | Status |
|---|---|---|---|---|
| **d000_s123** | ❌ 无 | ❌ 无 | ❌ 无 | checkpoint 存在(alpha=32)，**signals 目录不存在** |
| **d005_s123** | s1,s2 | ❌ 无 | ❌ 无 | 仅 mmlu 2个信号 |
| **d025_s123** | s1,s2 | s1,s2,s4+merged | s1,s2,s4+merged | mmlu 缺 s4；gsm8k/arc 基本完成 |
| **d100_a32_s123** | s1,s2 | ❌ 无 | ❌ 无 | 仅 mmlu 2个信号 |

### Seed 42

| Checkpoint | mmlu | gsm8k | arc_challenge | Status |
|---|---|---|---|---|
| **d000_a32_s42** | ❌ 无 | ❌ 无 | ❌ 无 | **checkpoint 目录为空**（lora_adapter/ 无文件） |
| **d005_s42** | s1,s2 | s1,s2 | s1,s2,s4+merged | gsm8k 缺 s4；arc 完成 |
| **d025_v3_s42** | s1,s2 | s1,s2 | s1,s2 | 3 benchmark 均只有 s1+s2 |
| **d100_a32_s42_v3** | ❌ 无 | ❌ 无 | ❌ 无 | 仍在训练，无 adapter_config |

**s3_constat**: 所有 alpha=32 目录均缺失。仅在废弃的 d000_v2_s42 (alpha=16) 中存在。

---

## 关键发现

### 1. RRF 命名 bug（exp003/rrf_aggregation.py:57）
- 实际文件名: `signal_s1_embedding_mmlu.json`
- RRF fallback 期望: `signal_embedding_mmlu.json`（无 s1_ 前缀）
- **影响**: 无 merged 文件的 benchmark×model 组合，RRF 无法加载个别信号文件
- **workaround**: 仅有 merged 文件的组合不受影响

### 2. exp003 已有输出
- `/root/autodl-tmp/exp003/exposure_scores.json` 存在，包含 0.5B 模型数据，需确认是否覆盖 3B alpha=32 完整集

### 3. exp006 代码就绪度
- `run_exp006.py` — 完整 pipeline (IRT + baselines + evaluation)
- `run_irt_calibration.py` — 4PL+gamma Stan MCMC，支持 4pl_gamma / 2pl_gamma / vanilla_4pl / wider prior
- `baselines.py` — 7 个 baseline 方法: B0_raw, B1_remove_rescore, B2/B3 Stan-based, B4_linear_regression, B5_emperor_mitigation, B6_dcr_fuzzy
- `joint_fit.py` — cross-benchmark joint IRT (ablation)
- **代码结构成熟，可直接运行**（前提是输入数据就绪）

### 4. GPU 状态
6 块 4090D，5 块繁忙（GPU 0-3,5 有进程），GPU 4 接近空闲(585 MiB)

---

## 阻断项（按优先级）

| # | 阻断项 | 影响 | 建议 |
|---|---|---|---|
| **B1** | d000_s123 无 signals | 缺控制组(dosage=0)，IRT 无法校准 | 最高优先级，需立即提交 compute_signals |
| **B2** | d000_a32_s42 checkpoint 为空 | seed42 缺控制组 | 确认重训是否真的完成，可能需要检查训练日志 |
| **B3** | d005_s123 / d100_a32_s123 仅有 mmlu | seed123 家族 gsm8k+arc 大面积缺失 | 批量提交 signals 任务 |
| **B4** | RRF 文件命名不匹配 | 无 merged 文件时 RRF 静默返回空 | 修 rrf_aggregation.py L57 的 sig_name_map 或批量 rename 文件 |
| **B5** | d100_a32_s42_v3 仍在训练 | seed42 家族缺 d100 | 等待训练完成后补 signals |
| **B6** | s3_constat 全局缺失 | RRF 最多融合 3 路信号而非 4 路 | 评估是否需要补算，或论文中说明 3-signal fusion |

---

## 最短路径估算

假设 GPU 4 可用，每个 signal×benchmark 约 20-30min（3B模型）：

1. **修 RRF 命名 bug** — 10min 代码修改
2. **补 d000_s123 全部 signals** — 3 bench × 3 signals ≈ 3-4h
3. **补 d005_s123 / d100_a32_s123 的 gsm8k+arc** — 每个 2 bench × 3 signals ≈ 各 2-3h
4. **补 d005_s42 / d025_v3_s42 缺失 signals** — 约 2-3h
5. **等 d100_a32_s42_v3 训练完成** → 补 signals — 需观察
6. **重跑 exp003 RRF 聚合** — 5min
7. **跑 exp006 IRT + baselines** — 约 30-60min (MCMC)

**乐观估计**: 如果 d000_a32_s42 问题能快速解决 + 并行提交 signals，约 **1.5-2 天**可完成从 signals 到 IRT 结果。瓶颈在 signals 计算的 GPU 排队。

---
