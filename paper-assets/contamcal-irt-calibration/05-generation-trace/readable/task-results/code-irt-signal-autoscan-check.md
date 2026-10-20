# code irt signal autoscan check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_irt-signal-autoscan-check_20260515T202032_result.json`
- **Structured JSON:** [`8ef81eded68dd4eeb35a.json`](../../sessions/8e/8ef81eded68dd4eeb35a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完毕。以下是结果。

---

## 报告：IRT Pipeline 信号目录扫描风险分析

### 当前信号目录状态

`/root/autodl-tmp/exp002/signals/` 已包含 `Qwen2.5-3B_d000_v2_s42/` 目录（v6 产出，alpha=16）。

### 扫描点分析

#### 1. **exp003/rrf_aggregation.py:188 — `aggregate_all_models()` — 有风险**

```python
for model_dir in sorted(signal_root.iterdir()):
    if not model_dir.is_dir():
        continue
    model_id = model_dir.name
    if dosage_filter and dosage_filter not in model_id:
        continue
```

使用 `iterdir()` 无差别扫描 `SIGNAL_ROOT` 下所有子目录。唯一的过滤是 `dosage_filter`（子串匹配）。`generate_exposure_json()` (line 208) 调用此函数，也继承风险。

**结论：会误包含 `Qwen2.5-3B_d000_v2_s42/`。** 特别是当不传 `dosage_filter` 或传 `d000` 时，该目录会被纳入。

#### 2. **exp002/aggregate_rrf.py:207 — `generate_exposure_json()` — 有风险**

```python
merged_files = sorted(signal_path.glob(f"*/signals_merged_{bench}.json"))
```

`*/` 通配符会匹配所有子目录，包括 `Qwen2.5-3B_d000_v2_s42/`。

**结论：会误包含。**

#### 3. **exp006/run_exp006.py:110 — `load_exp002_signals()` — 安全**

此函数**不扫描信号目录**。它遍历 eval_results 模型列表，通过模型 dirname 推导信号路径：

```python
sig_dirname = m["dirname"].replace("_para_aligned", "")...replace("_v2", "")...
merged = os.path.join(signals_dir, sig_dirname, "signals_merged_{}.json".format(benchmark))
```

信号路径查找是**模型驱动**的，不是目录扫描。而且 `.replace("_v2", "")` 会把 eval dirname 中的 `_v2` 去掉，导致路径指向 `Qwen2.5-3B_d000_s42`（已被标为 `.INVALID`），不会命中 `_v2_s42` 目录。

**结论：安全。**

#### 4. **exp006/run_pooled_4bench_irt.py — 安全**

使用 oracle dosage（`build_oracle_exposure`）而非信号文件。数据来源是 eval_results 目录（exp001），不碰信号目录。

**结论：安全。**

#### 5. **exp006/run_irt_calibration.py:81 — `load_eval_results()` — 安全**

扫描的是 `/root/autodl-tmp/exp001/eval_results/`（eval 目录），不是信号目录。

---

### 总结

| 文件 | 函数 | 扫描方式 | 风险 |
|------|------|----------|------|
| `exp003/rrf_aggregation.py:188` | `aggregate_all_models` | `iterdir()` 全扫描 | **会误包含** |
| `exp003/rrf_aggregation.py:208` | `generate_exposure_json` | 调用上面函数 | **会误包含** |
| `exp002/aggregate_rrf.py:207` | `generate_exposure_json` | `glob("*/...")` | **会误包含** |
| `exp006/run_exp006.py:110` | `load_exp002_signals` | 模型驱动，不扫描 | 安全 |
| `exp006/run_pooled_4bench_irt.py` | `run_single_benchmark_fit` | oracle dosage | 安全 |
| `exp006/run_irt_calibration.py:81` | `load_eval_results` | 扫描 eval 目录 | 安全 |

### 建议修复方案

**最简方案：重命名目录**，加 `.INVALID` 后缀（与 `Qwen2.5-3B_d000_s42.INVALID` 一致）：
```bash
mv /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_v2_s42 \
   /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_v2_s42.EXCLUDED_alpha16
```

所有 `iterdir()` / `glob` 扫描不会受影响，因为 `aggregate_all_models` 检查 `is_dir()` 时仍会匹配，但如果信号文件路径变了就找不到文件。实际上更稳妥的方式是：

1. 在 `aggregate_all_models()` 加 **blocklist**，跳过包含 `.INVALID` 或 `.EXCLUDED` 的目录名
2. 或在 exp003 和 exp002 的扫描逻辑中增加 naming convention 过滤（例如只接受 `{model}_{dosage}_s{seed}` 格式，排除含 `_v2_` 的非标准目录名）

**最终 IRT pipeline（exp006）是安全的**——它通过 eval_results 模型列表驱动信号查找，不做目录扫描。风险集中在 exp002/exp003 的 RRF 聚合路径，如果重新运行 `--generate-exposure` 或 `aggregate_all_models()`，v6 的 alpha=16 信号会被混入。

---
