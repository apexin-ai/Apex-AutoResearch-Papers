# analysis falcon3 paper integration plan

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_falcon3-paper-integration-plan_20260522T072842_result.json`
- **Structured JSON:** [`6e906fec145cce1d23c4.json`](../../sessions/6e/6e906fec145cce1d23c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Falcon3 论文整合清单

### 当前论文架构

- **Main taxonomy**: 5 models (Qwen-7B, Qwen-14B, Phi-4, OLMo-2, Gemma-2) / 4 families / 4 labs
- **Out-of-sample validation**: LLaMA-3.1-8B (Meta) = 第 5 family
- Falcon3-7B-Base (TII, 67.4% MMLU) 加入后 → **6 models / 5 families / 5 labs** + LLaMA validation = 6-family sample

Falcon3 的 67.4% baseline 落在 **vulnerable band (65–70%)** 内，与 Qwen-7B (66.1%) 和 Qwen-14B (69.4%) 同区间，四种 pattern 均有可能。

---

### 必须更新（结果出来后）

| # | 文件:行号 | 当前文本 | 更新内容 |
|---|----------|---------|---------|
| 1 | `abstract.tex:1` | "five models spanning four independent families" | → "six models spanning five independent families" |
| 2 | `abstract.tex:1` | "five-family sample" (×3处) | → "six-family sample" |
| 3 | `abstract.tex:1` | "Out-of-sample validation on a held-out fifth family" | → "held-out sixth family" |
| 4 | `abstract.tex:1` | "Two patterns (Immune, Benefit) are attested in two or more independent families; Collapse and V-recovery are each observed in one family" | → 按 Falcon3 pattern 更新计数 |
| 5 | `introduction.tex:5` | "five models spanning four independent families from four labs (Alibaba, Microsoft, Allen AI, Google)" | → "six models spanning five independent families from five labs (Alibaba, Microsoft, Allen AI, Google, TII)" |
| 6 | `introduction.tex:10` | "In our five-family sample" (Figure 1 caption) | → "six-family sample" |
| 7 | `introduction.tex:14` | "In our five-family sample, contamination vulnerability..." | → "six-family sample" |
| 8 | `introduction.tex:18` | "four families reveals qualitatively different..." | → "five families" |
| 9 | `results.tex:4` | "five models from four independent families" | → "six models from five independent families" |
| 10 | `results.tex:11` | Table 1 caption: "5/5 families" | → "6/6 families" (如果 Falcon3 也 stable) |
| 11 | `results.tex:16–23` | Table 1 (tab:taxonomy) 数据行 | 新增 Falcon3 行 |
| 12 | `results.tex:28` | "$N\!=\!5$ families" | → "$N\!=\!6$" |
| 13 | `results.tex:31` | "In our five-family sample..." 整段 baseline gradient | 加入 Falcon3 数据点，更新 vulnerable band 描述 |
| 14 | `results.tex:34` | "Two of four patterns...are attested in ≥2 independent families" | → 按实际更新 |
| 15 | `results.tex:48` | Table 2 caption: "2/5...4/5...2/5" | → x/6 |
| 16 | `results.tex:51–64` | Table 2 (tab:cross_seed) 数据行 | 新增 Falcon3 行 |
| 17 | `results.tex:67` | "Strict sign consistency holds for 2/5...4/5" | → x/6 |
| 18 | `conclusion.tex:3` | "five-family sample" | → "six-family sample" |
| 19 | `experimental_setup.tex:7` | "four independent model families from four labs" + 模型列表 | 加入 "Falcon3 \citep{...} (7B)" + TII |
| 20 | `experimental_setup.tex:9` | "yields over 50 checkpoints" | 更新 checkpoint 总数 |
| 21 | `appendix.tex:42` | Fig caption "4/5 models" | → "x/6 models" (按 ARC 一致性) |
| 22 | `appendix.tex:346` | Fig 7 caption "four independent families" | → "five independent families" |
| 23 | `appendix.tex:307–327` | Table 14 (classification sensitivity) | 新增 Falcon3 行 |

**图表必须重新生成：**
- `fig_dose_response.pdf` — 加 Falcon3 曲线
- `fig_baseline_vs_effect.pdf` — 加 Falcon3 数据点
- `fig_arc_dose_response.pdf` — 加 Falcon3 曲线（如有 ARC eval）
- Table 1, Table 2, Table 5 (gsm8k_transfer), Table 6 (gsm8k_dose), Table 14 (sensitivity)

---

### 条件更新（取决于 Falcon3 pattern）

**如果 Falcon3 = Benefit:**
- `abstract.tex:1` → "Three patterns (Immune, Benefit, ...) are attested in ≥2 families" — Benefit 从 2 family 变 3 family
- `results.tex:34` → Benefit 的 family-level replication 增强
- `limitations.tex:4` → "Out-of-sample validation covers only the Immune pattern" 仍不变（除非 Benefit 也算 validated）
- Benefit band 扩展到 67.4%，削弱 "vulnerability concentrates in 65–70%" 的说法（因为同区间也出现了 Benefit）

**如果 Falcon3 = Collapse:**
- `abstract.tex:1` → "Collapse...attested in two independent families" — 最大变化，Collapse 不再是 single-family
- `results.tex:34` → 删除 "Collapse...observed in one family...require additional replication"
- `limitations.tex:4` → 可删 "independent-family replication of Collapse...remains open"（Collapse 已 replicated）
- 极大强化论文结论：两个独立 family 在 vulnerable band 都 Collapse

**如果 Falcon3 = Immune:**
- `abstract.tex` → "Immune attested in three families" — 有趣但与 67.4% baseline 矛盾 (vulnerable band 内的 Immune)
- `results.tex:31` → 需修改 "above [76%], immune" 的表述，因为 67.4% 也 Immune
- 削弱 baseline gradient 叙事

**如果 Falcon3 = V-recovery:**
- `abstract.tex:1` → "V-recovery attested in two independent families" — V-recovery 不再是 single-family
- `results.tex:34` → 删除 "V-recovery...observed in one family...require additional replication"
- `limitations.tex:4` → 可删 V-recovery 的 replication caveat
- 在 vulnerable band 内出现第二个 V-recovery，强化 band-specific vulnerability

---

### 不需要更新

- **method.tex** — Algorithm 1 逻辑不变，仅适用范围从 "four families" 隐式扩展
- **IRT calibration 部分** (results.tex §5.5–5.7) — 仍基于 Qwen2.5 within-family，Falcon3 不影响
- **Signal failure 部分** (results.tex §5.6) — Min-K\%++ 分析不涉及 Falcon3（除非另做）
- **DiD memorization test** (results.tex §5.4, Table 3) — 除非对 Falcon3 也做 DiD
- **Domain-level analysis** (results.tex §5.7) — 仍基于 Qwen2.5
- **Prior sensitivity** (appendix) — 仍基于 Qwen2.5

---

### Phase 3: 先 eval d000–d050 不等 d100 的可行性

**Algorithm 1 明确要求 d100。** 分析 `method.tex:63-101`：

```
Line 67: Require a = (a_0, a_5, a_25, a_50, a_100)  ← 显式要求全 5 个 dosage
Line 71: Δ = a_100 - a_0                              ← 顶层分类判据
Line 77: m* < a_100                                    ← V-recovery 检测
Line 85: m* < a_100                                    ← V-recovery 检测
Line 92: g_2 = a_100 - a_25                            ← Benefit subtype
Line 93: ℓ = a_100 - a_50                              ← Benefit subtype
```

**结论：不能在没有 d100 的情况下运行 Algorithm 1，也不能填入 Table 1。**

但 **d000–d050 可以提供有价值的早期信号**：

| d050 观测 | 初步判断 | 置信度 |
|-----------|---------|--------|
| Δ(d050) < −5pp | 极可能 Collapse | 高 — 因为 d100 只会更差 |
| d005/d025 有 V-dip 但 d050 回升 | 可能 V-recovery | 中 — 需 d100 确认 endpoint |
| 单调上升 >2pp | 可能 Benefit | 中 — 需 d100 确认是否 saturate |
| 全程 ±2pp 内 | 可能 Immune | 中 — d100 可能突变 |

**LLaMA-3.1 先例**：LLaMA 仅训练了 d000/d025/d100 三个点（跳了 d005/d050），但仍有 d100。没有跳 d100 的先例。

**建议**：可以先跑 d000–d050 的 eval 获取方向信号（特别是 Falcon3 baseline 在 vulnerable band 内，early signal 很有价值），但论文正式结果必须等 d100 完成。如果 d050 已经明确 Collapse（>5pp decline），d100 的 eval 优先级可以降低（结果可预测）；其他 pattern 则必须等 d100。

---
