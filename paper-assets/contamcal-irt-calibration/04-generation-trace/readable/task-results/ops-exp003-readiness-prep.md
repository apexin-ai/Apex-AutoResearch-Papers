# ops exp003 readiness prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp003-readiness-prep_20260514T114831_result.json`
- **Structured JSON:** [`67f62d97868251a12185.json`](../../sessions/67/67f62d97868251a12185.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Full picture assembled. Here's the analysis:

---

## exp-002 现状

**3 dosages**: d000, d005, d100（来自 `run_batch.py` 的 `DOSAGES`）

当前输出：
| 目录 | 文件 |
|------|------|
| `Qwen2.5-0.5B_d000_s42/` | embedding×3 benchmarks + minkpp_mmlu（5 files） |
| `Qwen2.5-0.5B_d005_s42/` | embedding_mmlu only（1 file） |
| `Qwen2.5-0.5B_d100_s42/` | **不存在** |

**无 merged 文件**（compute_signals.py 需要 ≥2 种 signal 类型完成才会生成 `signals_merged_*.json`）。

---

## 路径对齐确认

| 组件 | 路径 | 格式 |
|------|------|------|
| exp-002 输出 | `/root/autodl-tmp/exp002/signals/{model}_{dosage}_{seed}/signal_{type}_{bench}.json` | ✅ |
| aggregate_rrf.py 输入 | `--signal-dir` 下扫描 `*/signals_merged_{bench}.json`，fallback 到 `*/signal_*_{bench}.json` | ✅ 兼容 |
| aggregate_rrf.py 输出 | `{output_dir}/exposure_scores.json` → `{bench: [tau_0, ..., tau_N]}` | ✅ |
| exp-006 输入 | `--exposure-file` → `json.load()` → `{bench: np.array(float)}` | ✅ 格式匹配 |

---

## exp-003 启动命令

**推荐用 `--dosage-filter d100`**（最强污染剂量，信号区分度最高）：

```bash
cd /root/contamcal-irt-calibration/exp002 && python aggregate_rrf.py \
  --generate-exposure \
  --signal-dir /root/autodl-tmp/exp002/signals \
  --output-dir /root/autodl-tmp/exp003 \
  --benchmarks mmlu gsm8k arc_challenge \
  --dosage-filter d100 \
  --k 60 \
  --normalize
```

**不加 dosage filter 的备选**（跨所有 dosages，fallback 行为：`load_signal_data` 按 index merge，后出现的覆盖前者，排序后 d100 最后 → 效果类似）：

```bash
cd /root/contamcal-irt-calibration/exp002 && python aggregate_rrf.py \
  --generate-exposure \
  --signal-dir /root/autodl-tmp/exp002/signals \
  --output-dir /root/autodl-tmp/exp003 \
  --benchmarks mmlu gsm8k arc_challenge \
  --k 60 \
  --normalize
```

产出：`/root/autodl-tmp/exp003/exposure_scores.json`

---

## exp-006 衔接命令

```bash
python /root/contamcal-irt-calibration/exp006/run_exp006.py \
  --exposure-file /root/autodl-tmp/exp003/exposure_scores.json \
  ...
```

---

## 注意事项

1. **exp-002 远未完成**。d100 目录尚不存在，d005 只有 1/9 个文件。当前 d000 也仅完成 embedding×3 + minkpp×1 = 4/9。
2. **无 merged 文件** → aggregate_rrf.py 会 fallback 到 individual signal files。这能工作，但只有已完成的 signal 类型参与 RRF（`detect_available_signals` 自动检测）。若只有 embedding 一种信号，RRF 退化为单信号排序。
3. 建议等 exp-002 **至少 d100 的 3 个 benchmark 各有 ≥2 种信号**再跑 exp-003，否则 tau 区分度不足。

---
