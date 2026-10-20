# data verify heatmap sources

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_verify_heatmap_sources_20260514T212229_result.json`
- **Structured JSON:** [`e32af60fcf000ca22ffb.json`](../../sessions/e3/e32af60fcf000ca22ffb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是核实结果：

---

## 核实结论

### 问题比预期更严重

热力图 SciERC NER Qwen 行的 **conditional rho 不是来自任何真实实验数据** — 它是用 CoNLL 的 conditional/full 比值乘以 SciERC full rho **估算**出来的。

### 具体逻辑链（`plot_all_figures.py`）

**Full rho（正确）** — 行 71-73:
```
mean(exp_015_v2.seed42, exp_015_v2.seed123)  # N=16, 两 seed 均值
```

**Conditional rho（有问题）** — 经过 3 层 fallback：

1. **行 101-113**: 尝试 `unified['ner']['conditional']['signals']` → **KeyError**，JSON 中没有这个路径（实际路径是 `ner.signals.&lt;signal>.cond`）
2. **行 135-142（实际生效）**: 用 CoNLL 比值估算：
   ```python
   ratio = cond_rho_conll[j] / full_rho_conll[j]
   cond_rho_scierc_ner[j] = full_rho_scierc_ner[j] * ratio
   ```
3. **行 147-162**: 再次尝试读 unified → 同样 KeyError，静默跳过

### exp_015_unified 的 seed 构成

exp_015_unified 使用 `exp_012_logprob/samples_with_logprobs.jsonl`（pilot_005, **N=8, 单次运行，无 seed 变异**）。它不是 seed42，也不是 seed123，而是一个完全不同的早期数据集。在 exp_015_v2 中对应 `scierc_n8_logprob_ner` 这个 key。

### 数据不一致总结

| | Full rho | Conditional rho |
|---|---|---|
| **实际来源** | exp_015_v2: seed42+seed123 均值, N=16 | CoNLL 比值 × full rho（合成值）|
| **问题** | ✓ 正确 | ✗ 不是真实测量值 |

### SciERC RE Qwen 也有类似问题

- SJ/FK/logprob 来自 exp_008_re_n16_v2
- EM/voting_conf 也是用 CoNLL 比值估算的

### 修复方案

**需要在 seed42+seed123 的 N=16 数据上运行 conditional 分析。** 原始 inference 数据都在：
- `output/exp_001_seed42_v2/samples.jsonl`（6.5MB，含 logprob）
- `output/exp_001_seed123_v2/samples.jsonl`（6.5MB，含 logprob）

具体做法：复用 `analyze_exp015_unified.py` 的 conditional 分析逻辑（过滤 F1<1 的实例后计算 Spearman rho），分别对两个 seed 文件运行，取均值，替换热力图中的合成值。同时修复 `plot_all_figures.py` 中 `unified['ner']['conditional']['signals']` 的错误路径。

---
