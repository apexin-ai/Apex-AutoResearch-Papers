# prep cross alpha v4 audit

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_cross_alpha_v4_audit_20260515T113914_result.json`
- **Structured JSON:** [`f36dcecfb4a13abfc4e9.json`](../../sessions/f3/f36dcecfb4a13abfc4e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是完整报告。

---

## 审计结果：✅ Ready（代码无 bug，等数据就绪即可运行）

### 1. FDR 混合策略 — ✅ 正确

**alpha=1.0 路径**（加载已有 method_ablation.json）：
- `consensus_framework.py:86-89`：`threshold_onset` 读 `significant`，其余 4 方法读 `significant_fdr`
- 完全符合 D029 要求

**非 alpha=1.0 路径**（从头跑 5 个方法）：
- `threshold_lead()` 只返回 `significant`（无 p_value）→ 直接写入 sig_matrix
- 其余 4 方法返回 `p_value` → 存入 `p_raw_matrix` → 经 BH FDR 校正后覆盖 sig_matrix
- FDR 循环只处理 `p_raw_matrix` 中有效值的位置 → threshold_onset 天然免于 FDR
- BH FDR q=0.05：`multipletests(pvals[valid], alpha=0.05, method="fdr_bh")` ✅

**permG / TY 列互换**：`MA_METHODS` 列表和 `MA_METHOD_FN` 字典映射一致，`enumerate` 遍历保证 method index 对应正确函数。✅ 无互换。

### 2. 5-α-point 兼容性 — ✅

- **α 列表不是硬编码**：`discover_alpha_dirs()` 用 `glob(a*_s42)` 动态发现 + 自动纳入 MVP(α=1.0)
- 数据目录现状：`a000_s42` ✅ / `a025_s42` ✅ / `a050_s42` ✅ / `a075_s42` ⚠️ / MVP ✅
- **`--n-perms 5000`**：已支持，default=5000 ✅
- **`--consensus-n-perms 1000`**：已支持，default=1000 ✅
- **`--update-registry`**：存在，打印每个 α 的 drift 统计 ✅
- **输出路径**：`results/analysis/cross_alpha_v{N}.json` + `cross_alpha_v{N}_report.md`

### 3. α=0.25 单 seed 处理 — ✅

Line ~450：`st = 1 if n_seeds == 1 else 3`
- 所有 sweep α 点（0.0, 0.25, 0.50, 0.75）均为 seed=[42]，n_seeds=1 → seed_threshold=1
- method_threshold = 4（≥4/5 方法一致）
- mode = `"method_agreement_only"` for single-seed

### 4. 输出格式 — ✅

- `print_summary`：Granger 表显示每个方向×每个 α 的 p_raw / p_fdr，汇总行 `N/M raw-sig -> K/M FDR-sig`
- Consensus 区：每个 α 的 robust/non-robust counts + regime comparison（stable vs regime-dependent）
- Markdown report 包含同样的信息以格式化表格呈现

### 5. ⚠️ 唯一阻塞：α=0.75 数据未完成

`a075_s42` 目录存在但只有 gen_0 到 gen_7（8/11 代），**无 `all_metrics.json`**。完整实验需 gen_0–gen_10。脚本会在 `load_metrics(a075_s42)` 时报 FileNotFoundError。

等实验完成 + 生成 `all_metrics.json` 后即可运行。

### 建议运行命令

```bash
cd /root/autodl-tmp/distrib_canary_collapse
python cross_alpha_analysis_v4.py --n-perms 5000 --consensus-n-perms 1000 --update-registry
```

无需指定 `--alpha-dirs`，auto-discovery 会自动找到全部 5 个 α 点。

---
