# paper placeholder audit

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_placeholder_audit_20260523T144109_result.json`
- **Structured JSON:** [`2a8a10f6cd82a2f5b119.json`](../../sessions/2a/2a8a10f6cd82a2f5b119.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 占位符清单

| # | 文件 | 行号 | 当前内容 | 需要什么数据 |
|---|------|------|---------|------------|
| **abstract.tex** | | | | |
| 1 | abstract.tex | L2 | `1.44× (single seed)` | SS 3-seed mean±std 后的 gap 值，去掉 "single seed" 标记 |
| **introduction.tex** | | | | |
| 2 | introduction.tex | L16 | `gap 7.8×→1.44×` | SS 3-seed gap 更新值 |
| 3 | introduction.tex | L18 | `(gap 7.8×→1.44×)` | 同上，贡献 (3) 中的 SS gap |
| **experiments.tex** | | | | |
| 4 | experiments.tex | L6 | `seed 42; ThreadGate additionally with seed 123` | 如有 multi-seed，需更新描述 |
| 5 | experiments.tex | L12 | `A second seed (123) confirms TF stability ($0.504\pm0.001$)` | AR 方面也需要 multi-seed 数据 |
| 6 | experiments.tex | L29 | ThreadGate AR GAR `0.064` CI `[.041,.091]` | s42 单 seed，需 multi-seed mean±std |
| 7 | experiments.tex | L30 | +PCGrad AR GAR `0.030` CI `[.023,.038]` | s42 单 seed，需 multi-seed mean±std |
| 8 | experiments.tex | L31 | Uniform Gate AR GAR `0.033` CI `[.025,.043]` | s42 单 seed，需 multi-seed mean±std |
| 9 | experiments.tex | L34 | LoRA-only AR GAR `0.037` CI `[.027,.050]` | s42 单 seed，需 multi-seed mean±std |
| 10 | experiments.tex | L12 | `Wilcoxon p=0.004, r=0.454` | multi-seed 后可能需更新统计检验 |
| 11 | experiments.tex | L12 | `GAR-ours 0.064 vs 0.037` | 更新为 multi-seed 值 |
| 12 | experiments.tex | L10 | `8--17×` gap range | multi-seed 后 gap range 可能变化 |
| 13 | experiments.tex | L48 | steering `0.064→0.556` (β=3), `0.727±0.061` (β=5) | 基于 TG s42 单 seed，可能需 multi-seed |
| **discussion.tex** | | | | |
| 14 | discussion.tex | L3 | `0.064 to 0.727` | TG 单 seed steering 数据 |
| 15 | discussion.tex | L5 | SS GAR `0.064 to 0.347 (5.4×)` | SS s42 单 seed → 需 3-seed mean±std |
| 16 | discussion.tex | L5 | `gap to 1.44× with negligible PPL change (1.44 vs. 1.43)` | SS 3-seed mean±std gap 和 PPL |
| 17 | discussion.tex | L5 | `a second seed yields 0.418 (gap 1.20×)` | 合并为 3-seed mean±std 报告 |
| 18 | discussion.tex | L5 | `GAR-Dongre also rises (0.019→0.353; N=5 pilot)` | 仍是 N=5 pilot，是否扩大到 N=50？ |
| 19 | discussion.tex | L5 | `content compliance rising +23.8 pp (p=0.077)` | 单模型探索性数据，limitations 已声明 |
| **conclusion.tex** | | | | |
| 20 | conclusion.tex | L3 | `gap 7.8×→1.44×; single seed` | SS 3-seed gap，去掉 "single seed" |
| 21 | conclusion.tex | L3 | `8--17×` on Qwen | multi-seed 后 gap range 可能变化 |
| **limitations.tex** | | | | |
| 22 | limitations.tex | L3 | `primarily a single seed` | multi-seed 完成后需更新措辞 |
| **analysis.tex** | | | | |
| 23 | analysis.tex | L43 | Llama TF `0.484`/`0.481`, AR mean `0.043`/`0.028`, median `0.018`/`0.018` | Llama 单 seed，无 ±std |
| 24 | analysis.tex | L43 | Llama gap `27×`/`26×` (median), `11×`/`17×` (mean) | 单 seed，无置信区间 |
| **appendix.tex** | | | | |
| 25 | appendix.tex | L138 | `SS vs. TG` Wilcoxon `p<0.001, r=0.869` | 基于 s42 单 seed 对比 |
| 26 | appendix.tex | L156 | Llama AR: `mean 0.043, std 0.100` | 单 seed，无跨 seed 统计 |
| 27 | appendix.tex | L301-302 | SS s42 `6.5h`, SS s123 `10.8h` | 若有 s456 需补充训练时间 |

### 按优先级分组

**P0 — 论文中已标记 "single seed"，必须更新：**
- #1, #20: abstract/conclusion 显式标记 `single seed`
- #15-17: discussion 中 SS 两个 seed 的独立数值 → 合并为 3-seed mean±std
- #22: limitations 措辞更新

**P1 — 主表/主文 AR 数字（当前 s42 单 seed）：**
- #6-9: Table 1 所有 AR GAR 和 CI
- #10-12: 关联统计检验和 gap range
- #2-3: intro 中引用的 SS gap

**P2 — Llama 跨模型数据（单 seed，无 CI）：**
- #23-24: analysis 中 Llama 所有数字
- #26: appendix Llama 详细数据

**P3 — 论文中完全缺失的数据：**
- **1.5B cross-model**: 论文全文无任何 1.5B 模型数据
- **MMLU**: 论文全文无 MMLU 评估
- 这两项在当前论文中未承诺也未引用，如不做可无需占位

**P4 — 次要/探索性：**
- #13-14: steering 数据（单 seed，但作为 diagnostic 可接受）
- #18: GAR-Dongre SS pilot（N=5）
- #19: instruction retention（已在 limitations 声明为 exploratory）

---
