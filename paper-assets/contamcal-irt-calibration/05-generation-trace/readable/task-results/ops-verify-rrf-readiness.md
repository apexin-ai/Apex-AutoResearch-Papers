# ops verify rrf readiness

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-rrf-readiness_20260516T034815_result.json`
- **Structured JSON:** [`0fcc61054c1f1eb361c9.json`](../../sessions/0f/0fcc61054c1f1eb361c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data needed. Here's the report.

---

## 报告：RRF Pipeline 就绪度 + Signal 清点

### A. Signal 完成度矩阵

**0.5B s42 — 全部完成 ✅**

| 剂量 | mmlu | gsm8k | arc | merged |
|------|------|-------|-----|--------|
| d000 | s1✅ s2✅ s4✅ | s1✅ s2✅ s4✅ | s1✅ s2✅ s4✅ | 3/3 ✅ |
| d005 | s1✅ s2✅ s4✅ | s1✅ s2✅ s4✅ | s1✅ s2✅ s4✅ | 3/3 ✅ |
| d025 | s1✅ s2✅ s4✅ | s1✅ s2✅ s4✅ | s1✅ s2✅ s4✅ | 3/3 ✅ |
| d100 | s1✅ s2✅ s4✅ | s1✅ s2✅ s4✅ | s1✅ s2✅ s4✅ | 3/3 ✅ |

**1.5B s42 — 全部完成 ✅**

| 剂量 | mmlu | gsm8k | arc | merged |
|------|------|-------|-----|--------|
| d000 | ✅ | ✅ | ✅ | 3/3 ✅ |
| d005 | ✅ | ✅ | ✅ | 3/3 ✅ |
| d025 | ✅ | ✅ | ✅ | 3/3 ✅ |
| d100 | ✅ | ✅ | ✅ | 3/3 ✅ |

**3B s42 (alpha=32 only, 排除 BLOCKLIST) — 严重缺失**

| 目录 | 状态 | mmlu | gsm8k | arc |
|------|------|------|-------|-----|
| d000_v2_s42 | **BLOCKED** (alpha=16) | — | — | — |
| d005_s42 | **BLOCKED** (alpha=16) | — | — | — |
| d025_v3_s42 | **有效 ✅** | s1✅ s2✅ s4✅ | s1✅ s2✅ s4✅ | s1✅ s2✅ s4✅ |
| d100_s42 | **BLOCKED** (alpha=16) | — | — | — |

alpha=32 eval 已存在但尚无 signal 目录: `d000_v3_s42`, `d000_a32_s42`, `d005_a32_s42`, `d100_a32_s42`（eval_results 中已有 `_aligned` 结果）

**3B s123**

| 目录 | mmlu | gsm8k | arc |
|------|------|-------|-----|
| d005_s123 | ✅ merged | ✅ merged | ✅ merged |
| d025_s123 | s1✅ s2✅ s4✅ (无merged) | ✅ merged | ✅ merged |
| d100_a32_s123 | s1✅ s2✅ s4进行中 | ❌ | ❌ |

**0.5B / 1.5B s123 — 刚起步**

| 目录 | mmlu | gsm8k | arc |
|------|------|-------|-----|
| 0.5B_d000_s123 | s1✅ s2✅ s4 chunks进行中 | ❌ | ❌ |
| 1.5B_d000_s123 | s1✅ only | ❌ | ❌ |

其他 0.5B/1.5B s123 剂量 (d005/d025/d100) 尚无目录。

---

### B. RRF Pipeline 就绪状态

**代码**: `exp003/rrf_aggregation.py` (15,950B, 5月16日更新)

- 输入路径: `SIGNAL_ROOT = /root/autodl-tmp/exp002/signals` ✅ 正确
- ALPHA16_BLOCKLIST 和 SKIP_PATTERNS("DEPRECATED") 均已配置 ✅
- 支持 merged file 加载，缺失时自动 fallback 到单独 signal 文件 ✅
- 输出格式: `--generate-exposure` 模式输出 `exposure_scores.json`（exp006 直接消费）✅
- Dry-run: `--limit N` 限制每 benchmark 处理条目数 ✅
- 其他: `--csv` 输出平铺 CSV，`--dosage-filter` 筛选剂量
- 配套: `evaluate_rrf.py`（评估脚本）、`ablations.py`（消融实验）均存在

**结论: RRF 代码完全就绪，随时可跑。**

---

### C. Pooled IRT 就绪状态

**代码**: `exp006/run_irt_calibration.py` (24,504B, 5月16日更新)

- **Stan 模型**: `/root/contamcal-irt-calibration/stan_models/` 下 4 个变体均已编译 ✅
  - `contam_irt_4pl_simple.stan` (4PL+gamma)
  - `contam_irt_2pl_gamma.stan`
  - `vanilla_4pl.stan`
  - `contam_irt_4pl_simple_wider.stan`
- **CmdStan**: 2.38.0 已安装 (`/root/.cmdstan/cmdstan-2.38.0`) ✅
- **输入**: `--exposure-file` 接收 RRF 输出的 `exposure_scores.json`；`--tau-source` 支持 exposure/oracle/aggregated
- **Pooled 脚本**: `run_pooled_4bench_irt.py`, `run_pooled_irt_n16.sh`, `run_stratified_irt.py` 均存在
- **Baselines**: `baselines.py`, `run_all_baselines.py` 就绪
- **Dry-run 输出**: `dryrun_full.json`, `dryrun_no_stan.json` 已有历史结果

**结论: Pooled IRT 代码和环境完全就绪。**

---

### D. 阻塞项清单

| # | 阻塞项 | 影响 | 依赖 |
|---|--------|------|------|
| **1** | 3B s42 alpha=32 signals 缺失 3/4 剂量 (d000, d005, d100) | **RRF 聚合无法完整运行 3B s42** | 需 GPU 计算 signal；eval 已就绪 |
| **2** | 0.5B s123 全量 signals（4 剂量 × 3 bench × 3 signal）| pooled IRT N≥16 门槛 | GPU 最高优先级 (C007) |
| **3** | 1.5B s123 全量 signals（4 剂量 × 3 bench × 3 signal）| pooled IRT N≥16 门槛 | GPU 最高优先级 (C007) |
| **4** | 3B d100_a32_s123 signals（gsm8k + arc 全缺，mmlu s4 进行中）| pooled IRT respondent 不完整 | GPU 计算 |
| **5** | 3B d025_s123 merged_mmlu 缺失 | 非阻塞（RRF 有 fallback），但建议生成 | 无 GPU 依赖，纯 merge |

**可立即执行的操作**: 对 d025_v3_s42 和 d025_s123(mmlu) 运行 RRF dry-run（`--limit 100`）验证端到端流程，无需等待 GPU 任务。

---
