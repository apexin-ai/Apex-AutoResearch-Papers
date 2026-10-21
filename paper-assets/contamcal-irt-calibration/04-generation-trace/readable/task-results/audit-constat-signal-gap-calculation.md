# audit constat signal gap calculation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_constat_signal_gap_calculation_20260514T220004_result.json`
- **Structured JSON:** [`2b617ac26cc36aea6555.json`](../../sessions/2b/2b617ac26cc36aea6555.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是三个问题的回答：

---

## (a) 当前 ConStat 信号的具体计算方式

**使用 raw gap，不是 delta-of-deltas。**

关键代码（`signal_constat.py:42-58`）：

```python
def compute_constat_signal(
    benchmark: str,
    original_eval_paths: list[str],
    paraphrase_eval_paths: list[str],
) -> list[dict]:
    # ...
    orig_matrix = np.array(orig_seeds, dtype=float)  # (n_seeds, n_items)
    para_matrix = np.array(para_seeds, dtype=float)

    orig_mean = orig_matrix.mean(axis=0)  # (n_items,)
    para_mean = para_matrix.mean(axis=0)
    gap = orig_mean - para_mean  # <-- RAW GAP，无 baseline 校正

    for i in range(n_items):
        results.append({
            "s3_constat": float(gap[i]),  # 直接用 raw gap 作为信号
        })
```

计算方式：`gap = mean_orig_accuracy - mean_para_accuracy`（per-item，跨 seed 平均后直接做差）。**没有减去 d000 baseline 的 gap，没有 delta-of-deltas 校正。**

---

## (b) 不影响已有 exp-002 结果

**S3 ConStat 信号在所有已有结果中均为 null，未被使用。**

证据：
1. `find /root/autodl-tmp/exp002/signals/ -name "*constat*"` → **无结果**（没有独立的 constat 信号文件）
2. 所有 merged 文件中 `s3_constat` 全部为 `null`（例如 `Qwen2.5-1.5B_d100_s42/signals_merged_mmlu.json` 有 14042 行 `s3_constat: null`）
3. 没有生成 RRF 融合文件（`find -name "rrf*"` → 无结果）
4. `run_batch.py` 中 ConStat 只在 paraphrase eval 文件存在时才启用：
   ```python
   signals = ["embedding", "minkpp", "selfcritique"]  # 默认只有 3 个
   if os.path.exists(orig_eval) and os.path.exists(para_eval):
       signals.append("constat")  # paraphrase 文件不存在就跳过
   ```
5. `aggregate_rrf.py` 的 `detect_available_signals()` 会自动跳过全 null/0 的信号

**结论：paraphrase eval 数据从未生成，S3 从未被计算，已有结果仅基于 S1+S2+S4，bug 不影响当前结果。**

---

## (c) 修改影响范围

如果要修复 ConStat 计算方式，只需改 **1 个文件**：`signal_constat.py`。

修改方案（delta-of-deltas）：
- `compute_constat_signal()` 增加参数 `baseline_original_eval_paths` 和 `baseline_paraphrase_eval_paths`（d000 的 eval 结果）
- 计算 `gap_dX = orig_mean_dX - para_mean_dX`，`gap_d0 = orig_mean_d0 - para_mean_d0`
- 信号值 = `gap_dX - gap_d0`

联动修改：
- `compute_signals.py`：传入 d000 baseline 路径
- `run_batch.py`：构建命令时增加 baseline eval path 参数

**但更务实的建议：先完成 paraphrase eval 生成（exp-001 阶段），再决定是否启用 S3。** 目前 S3 从未产出数据，修复计算逻辑的优先级低于产出 paraphrase eval 数据本身。如果 paraphrase 难度偏移过大（d000 gap 达 ±9pp），也可以考虑弃用 gap-based ConStat，只保留 S1/S2/S4 三信号融合。

---
