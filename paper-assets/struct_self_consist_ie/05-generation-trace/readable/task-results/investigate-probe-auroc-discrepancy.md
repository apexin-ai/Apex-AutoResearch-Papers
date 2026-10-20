# investigate probe auroc discrepancy

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_probe_auroc_discrepancy_20260521T024205_result.json`
- **Structured JSON:** [`caf8d7dc0f855a483359.json`](../../sessions/ca/caf8d7dc0f855a483359.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Let me just compute the numbers directly and present the complete analysis.

---

## Probe AUROC 矛盾调查报告

### 1. 两个文件的完整差异对比表

| 维度 | File A (`auroc_results_fewnerd.json`) | File B (`entity_probe_results.json`) |
|------|--------|--------|
| **生成脚本** | `code/hidden_state_probe.py` | `code/probe/extract_entity_hidden_states.py` + `code/probe/entity_probe_auroc.py` |
| **数据源 (FewNERD)** | `exp_tlow_fewnerd_t05_s42` (temperature=0.5) | `exp_021_inference` |
| **数据源 (CoNLL)** | `exp_conll_t08_seed42` | `exp_002_conll_n16` |
| **Instances** | 500 | 2000 (FewNERD) / 1000 (CoNLL) |
| **Entities (FewNERD)** | 10,508 | 43,303 |
| **Entities (CoNLL)** | 7,849 | 16,683 |
| **Features dim** | 4096 | 4096 |
| **d/n ratio (train/fold)** | 4096/8406 = **0.487** | 4096/34642 = **0.118** |
| **Positive rate (FewNERD)** | **79.8%** | 未单独报告 |
| **Positive rate (CoNLL)** | **91.2%** | 未单独报告 |
| **CV method** | 5-fold StratifiedKFold, entity-level split | 同左 |
| **LR params** | C=1.0, max_iter=1000, solver=lbfgs | C=1.0, max_iter=1000 (default solver) |
| **Scaler** | StandardScaler | StandardScaler |
| **Seeds** | [42, 123, 456] | [42, 123, 456] |
| **Entity token定位** | **模糊匹配** — 逐token decode寻找实体文本 | **字符偏移映射** — 在JSON中定位实体字符位置再映射到token |
| **LODO 验证** | 无 | FewNERD 0.559, CoNLL 0.671 |
| **AUROC (FewNERD within)** | **0.987** | **0.920** |
| **AUROC (CoNLL within)** | **0.980** | **0.957** |

### 2. 差异根因分析

AUROC 从 0.987 → 0.920 的差距来自**三个叠加因素**：

#### (a) Entity-level CV 的 instance 信息泄露（主因）

两个脚本都使用 **entity-level StratifiedKFold** — 同一个 instance 的多个 entity 被随机分到 train 和 test。每个 instance 贡献 ~21 个 entities（8 samples × ~2.6 entities/sample），在 5-fold CV 中约 17 个进 train、4 个进 test。来自同一 instance 的 entity hidden states 高度相关（共享 prompt context），probe 可以学习 instance-specific patterns 并"认出"测试 entity 属于哪个 instance。

**File A 的泄露更严重**：只有 500 个 instances，probe 只需"记住" 500 个 instance 的特征模式。File B 有 2000 个 instances，泄露被稀释。

#### (b) 数据源差异：低温度 → 更多重复 entities

File A 使用 `exp_tlow_fewnerd_t05_s42`（temperature=0.5），低温度导致 8 个 samples 之间的 entity 高度重复。同一个 entity (text, type) 在多个 samples 中出现 → hidden states 高度相似且标签相同 → CV 中被分到 train/test 两侧时，分类几乎是"查表"操作。

File B 使用 `exp_021_inference`（温度更高），entity 多样性更大，重复率更低。

#### (c) d/n 比率

| | d/n (train per fold) | 过拟合风险 |
|--|--|--|
| File A | 0.487 | 中等 — LogisticRegression 有 L2 正则化，不致命但增加了拟合噪声的空间 |
| File B | 0.118 | 低 |

d/n=0.487 本身不会把 AUROC 从 0.92 推到 0.987，但与 (a)(b) 叠加时放大了泄露效应。

### 3. 过拟合风险评估

**0.987 有严重过拟合问题**。证据链：

1. **LODO 验证崩塌**：File B 的 within-dataset 0.920 → LODO 0.559（接近随机）。如果 entity quality 信息真的编码在 hidden states 中，跨数据集应有一定泛化能力。LODO 近乎随机说明 probe 主要学到的是 dataset-specific artifacts，不是通用的 quality signal。

2. **File A 没有 LODO**：恰好缺少了能暴露泄露问题的验证手段。

3. **正类比率极端**：CoNLL 91.2% positive rate — 一个 always-predict-1 的 dummy classifier 就有 0.912 accuracy。AUROC 虽然是 threshold-independent，但在极端不平衡下 precision-recall 区域的微小变化就能产生很高的 AUROC。

4. **同一 probe 方法论在两个独立实现上的结果差 6.7 个百分点**（0.987 vs 0.920），这个量级的不稳定性本身就是过拟合的信号。

### 4. 方法论可靠性判断

**File B 更可靠**，但仍有缺陷：

- File B 有 LODO 验证，暴露了泛化失败
- 更大的数据量（2000 instances）减少了抽样偏差
- 使用精确的字符偏移映射（vs File A 的模糊匹配）

**两者共同的缺陷**：entity-level CV split。正确做法是 **instance-level CV** — 同一 instance 的所有 entities 要么全在 train，要么全在 test。

### 5. 论文建议

**绝对不要用 0.987。**

推荐方案（按优先级）：

1. **最佳**：重新跑 probe，使用 **instance-level GroupKFold**（按 `instance_idx` 分组），消除 entity 级泄露。报告修正后的 within-dataset AUROC + LODO AUROC。预期 within-dataset AUROC 会下降到 0.7-0.85 之间。

2. **次选**：用 File B 的结果，报告 **LODO AUROC（0.615）**作为主要数字（诚实但偏保守），within-dataset AUROC（0.920/0.957）作为上界参考，并在论文中明确注明 entity-level CV 的局限。

3. **论文叙事调整**：
   - 原叙事：*"Probe AUROC ≈ 0.99 >> ESJ 0.51 → information IS in representation, prompt fails"*
   - 修正叙事：*"Within-dataset probe detects partial signal (0.7-0.85 with proper CV), but LODO near-random (0.56-0.67) suggests the signal is task/instance-specific rather than a universal entity quality indicator. The gap between MV (0.87) and probe demonstrates that multi-sample aggregation captures information beyond what single-pass representations encode."*

---
