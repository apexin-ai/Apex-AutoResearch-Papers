# code exp003 rrf prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp003-rrf-prep_20260514T104048_result.json`
- **Structured JSON:** [`94575d388f4b64f2246c.json`](../../sessions/94/94575d388f4b64f2246c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 报告

### 代码审查结果

**aggregate_rrf.py** — 3个问题，已全部修复：

| # | 问题 | 严重度 | 状态 |
|---|------|--------|------|
| 1 | **输出格式不兼容 exp-006** — 输出 `[{index, benchmark, rrf_score}]` 但 exp-006 的 `load_exposure_scores` 期望 `{benchmark: [float]}` | Critical | 已修复：新增 `--generate-exposure` 模式和 `generate_exposure_json()` 函数 |
| 2 | **缺失信号自动检测** — ConStat(s3) 未计算时全为 0.0，产生基于 index 顺序的系统性 rank 偏差 | High | 已修复：新增 `detect_available_signals()`，RRF/rank-avg 自动跳过全零信号 |
| 3 | **run_batch.py 跳过检测失效** — `merged_output_exists` 查找 `signals_merged_{bench}_{model_id}.json`，但 compute_signals.py 写的是 `signals_merged_{bench}.json` | Medium | 已修复 |

### 输入/输出格式兼容性

- compute_signals.py → `signal_{name}_{bench}.json` + `signals_merged_{bench}.json` ✅ aggregate_rrf.py 的 `load_signal_data` 可读取
- aggregate_rrf.py `--generate-exposure` → `exposure_scores.json` 格式 `{benchmark: [float]}` ✅ 与 exp-006 `load_exposure_scores` 完全匹配
- 验证通过：14042 MMLU + 1319 GSM8K + 1172 ARC items，`build_exposure_matrix` 产出形状正确

### Dry-run 结果

用 d000 已有的 embedding 信号跑通两种模式：
- 单模型 RRF：14042 items，正确检测到仅 s1_embedding 可用
- exposure 生成：3 个 benchmark 全部产出，tau 范围 [0, 1]（min-max 归一化后）

### exp-002 完成后的运行命令

```bash
cd /root/contamcal-irt-calibration/exp002
python aggregate_rrf.py \
  --generate-exposure \
  --signal-dir /root/autodl-tmp/exp002/signals \
  --output-dir /root/autodl-tmp/exp003/output \
  --dosage-filter d100 \
  --benchmarks mmlu gsm8k arc_challenge
```

建议用 `--dosage-filter d100` — d100 模型所有 benchmark items 都在训练集中，信号最强，tau 估计最可靠。

---
