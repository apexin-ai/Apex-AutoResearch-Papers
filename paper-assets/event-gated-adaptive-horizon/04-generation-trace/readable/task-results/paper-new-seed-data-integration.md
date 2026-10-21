# paper new seed data integration

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_new-seed-data-integration_20260518T055920_result.json`
- **Structured JSON:** [`c66334ca2626aa84b890.json`](../../sessions/c6/c66334ca2626aa84b890.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。以下是变更汇报：

---

## Task 1: Appendix 完整实验表

**文件：** `appendix.tex`

- **行 6:** "20 experimental configurations" → "22 experimental configurations"，列表增加 `008d_s4` 和 `010b_s0`
- **行 30 后插入:** `008d_s4 | Factorial (s4) | trn | ON | 8 | 63.6 @105K | 3.03× | Full collapse` (灰底)
- **行 43 后插入:** `010b_s0 | Cheetah Run | trn | ON | 8 | 0.83 @105K | 70.64× | Full collapse` (灰底)
- **results.tex 行 12:** main table caption 引用同步 20→22

## Task 2: Seed 数量更新

| 文件 | 位置 | 旧值 | 新值 |
|------|------|-------|-------|
| `abstract_body.tex` | 行 1 | three tested seeds ($n{=}3$) | four tested seeds ($n{=}4$) |
| `abstract_body.tex` | 行 1 | two progressing...one self-correcting | three progressing...one self-correcting |
| `introduction.tex` | 行 8 | $n{=}3$, 2/3, 1/3 | $n{=}4$, 3/4, 1/4 |
| `results.tex` F2 | 行 76 | three tested seeds, NVE 列表 3 个 | four tested seeds, NVE 加入 $3.03\times$ |
| `results.tex` F2 | 行 76 | mean eval 206.2, 22.5% | mean eval 170.6, 18.6% |
| `results.tex` F2 | 行 76 | 2/3 seeds, 35K vs 70K | 3/4 seeds, 35K to 85K |
| `results.tex` F2 | 行 76 | seeds 1 和 3 分开描述 | seeds 1+4 合并为 full collapse |

## Task 3: F7 段落 Cheetah 更新

**文件：** `results.tex` 行 105, `appendix.tex` 行 191

- 010b 从单 seed 改为 "2 seeds"，NVE 从 $8.27\times$ 改为 "$8.27\times$ and $70.64\times$"
- Final eval 从 "51.7" 改为 "51.7 and 0.83"
- SGS 对比句增加 "0.83 across 2 seeds"
- Appendix F3 Cheetah 引用同步：NVE `$8.27$--$70.64\times$`，collapse to `51.7/0.83`

## Task 4: Detector 统计

**评估结论：** 两个新实验均应纳入。008d_s4 和 010b_s0 都是 TP（CIVO confirmed + detector alert fired）。

| 指标 | 旧值 | 新值 |
|------|------|------|
| n | 11 | 13 |
| CIVO-positive | 3 | 5 |
| TPR | 3/3 (1.00) | 5/5 (1.00) |
| FPR | 2/8 (0.25) | 2/8 (0.25) |
| Precision | 3/5 = 0.60 | 5/7 = 0.71 |
| F₁ | 0.75 | 0.83 |
| Predictive rate | 2/3 | 2/5 |

**具体改动：** `results.tex` 行 182, 185, 189, 197–199（新增 2 行 TP）, 211, 219, 221, 223, 229。`abstract_body.tex` 和 `introduction.tex` 的 detector 统计同步更新。

**需要补充的数据：**
1. **$r_\text{ve}$ at trigger time** — 008d_s4 @105K 和 010b_s0 @95K 的 V/E ratio，需从实验 log 提取（detector table 中标记为 `---$^e$`）
2. **Youden's J** — 加入新数据点后可能从 0.714 略微变化，需用 5 个 TP 的 $r_t$ 值重新计算 $\tau_\text{mag}$ 灵敏度分析
3. **NVE 分类统计（F2 section）** — 目前保留 "11/12 accuracy (AUROC=0.926)"。加入 008d_s4 后变为 12/13 accuracy, AUROC≈0.917。是否更新取决于你是否将 008d_s4 视为独立配置纳入 NVE 评估集
4. **Appendix NVE 灵敏度表（B1/B2）** — 如果纳入 008d_s4，n_pos +1，所有阈值行的 TP/FP/FN/TN、CI、AUROC 都需重算

**注意：** predictive rate 从 2/3 降到 2/5 是一个叙事弱化。如果需要保持 abstract 的吸引力，可以考虑改为 "100% sensitivity (5/5 cases), with predictive detection in the earliest-onset cases" 这类表述，但这涉及叙事结构调整，当前仅做了数字更新。

---
