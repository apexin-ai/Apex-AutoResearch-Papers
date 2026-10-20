# code exp008 fix d005

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp008-fix-d005_20260514T082742_result.json`
- **Structured JSON:** [`3cff453f48bc18c8af15.json`](../../sessions/3c/3cff453f48bc18c8af15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成，语法验证通过。

**修改的文件**: `/root/contamcal-irt-calibration/exp008/run_exp008.sh`

**Diff 摘要**:

| 行 | 旧 | 新 |
|---|---|---|
| 变量定义 | `D100_ADAPTER="...Qwen2.5-0.5B_d100_s42/lora_adapter"` | `D005_ADAPTER="...Qwen2.5-0.5B_d005_s42/lora_adapter"` |
| regime 绑定 | `REGIME_ADAPTER[sft_contam]="$D100_ADAPTER"` | `REGIME_ADAPTER[sft_contam]="$D005_ADAPTER"` |
| labels 源文件 | `contamination_labels_${bench}_d100.json` | `contamination_labels_${bench}_d005.json` |
| compute_signals | `--gpu 0)` 作为 CMD 数组末尾元素 | 已删除 |

**未改动**:
- `SFT_DATA` 仍指向 `sft_dosage_100.jsonl`。这是 `--sft-data-path` 参数，用于 selfcritique 等 signal 的 reference。如果需要改为 `sft_dosage_005.jsonl` 请告知。
- Python 文件 (`run_signal_survival.py`, `signal_survival_analysis.py`, `plot_survival.py`) 无 d100 引用，无需修改。

**注意**: Step 0 的 labels 已有 skip 逻辑（`if [ -f "$DST" ]`）。如果之前运行过用 d100 labels 生成的缓存文件 `${OUTPUT_BASE}/labels/labels_${bench}.json`，需要先删除这些文件才能重新生成 d005 labels。

---
