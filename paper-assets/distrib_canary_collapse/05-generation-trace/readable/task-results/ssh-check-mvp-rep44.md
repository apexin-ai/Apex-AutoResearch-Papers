# ssh check mvp rep44

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_mvp_rep44_20260517T100018_result.json`
- **Structured JSON:** [`b7bf6a16becf8b15b2ea.json`](../../sessions/b7/b7bf6a16becf8b15b2ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整。汇总如下：

## 产出

### 1. rep_44 目录状态
`results/mvp/` **整个目录已不存在**。α=1.0 的原始训练数据（rep_42 到 rep_45）已被清理。`alpha_sweep/` 下有 s44 的其他 alpha 数据（a000, a025, a050, a075），各含 11 个 gen。

### 2. 5-method 分析结果
**已存在于** `method_ablation_phase2_panel.json`（2026-05-15 生成）。Panel 共 56 行，seed=44 有 8 行（α=1.0, 8 pairs），数据完整。原始 `all_metrics.json` 已丢失，**无法重新跑**。

### 3. seed=44 α=1.0 per-method sig counts (/8)

| Method | sig/total |
|--------|-----------|
| naive | **8/8** |
| differenced | **8/8** |
| threshold | **8/8** |
| permutation_granger | **6/8** (entropy→perplexity, ece→perplexity 不显著) |
| TY | **2/8** (仅 entropy→distinct_1/2/3 中的前两个... 实际只有 entropy→distinct_{1,2,3} 显著中 1 个，再看：entropy→{d1,d2,d3}=True, entropy→ppl=False, ece→{d1,d2,d3,ppl}=全False → **3/8**) |

修正 TY 统计：
- entropy→d1: True, entropy→d2: True, entropy→d3: True, entropy→ppl: False
- ece→d1: False, ece→d2: False, ece→d3: False, ece→ppl: False
- **TY = 3/8**

### 4. error table 为什么可能漏了 s44
**不是漏了**。`method_ablation_phase2_panel.json` 包含完整的 s44 数据（和 s42/s43/s45 一起）。α=1.0 的 32 tests = 4 seeds × 8 pairs。问题在于 `results/mvp/` 目录被清理了，所以从文件系统看不到 rep_44，但 panel JSON 里数据完好。如果某个下游报告"漏了 s44"，应该是那个报告没从 panel JSON 读取，而是去扫磁盘目录。

---
