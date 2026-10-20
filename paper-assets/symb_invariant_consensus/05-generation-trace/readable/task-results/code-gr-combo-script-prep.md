# code gr combo script prep

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gr-combo-script-prep_20260520T115919_result.json`
- **Structured JSON:** [`5723254226c91d01c561.json`](../../sessions/57/5723254226c91d01c561.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

scipy 可用。现在需要确认运行前的数据准备步骤。

**脚本就绪。汇总如下：**

## `direction_gr_combo.py`

**位置**: `artifacts/direction_gr_combo.py`（本地），需部署到 westd-16639

### 数据格式

| 数据源 | 文件 | 格式 | 位置 |
|--------|------|------|------|
| G conservative | `per_problem_conservative.json` | 数组, `pid`/`sica_answer`/`gt`/`scores` | westd-16639 (运行中, 100/204, ETA ~105min) |
| R NLI | `direction_r_nli_large/results.json` | 字典, `per_question.folio_X.deberta_pred/deberta_probs` | westd-25068 |
| Baseline | `exp033_results.json` | 数组, `problem_id`/`sc_answer`/`sica_answer` | westd-16639 |

### 10 种 Combo 策略
1. **gr_vote** — SICA-G + NLI 各1票, SC tiebreak
2. **gr_intersection_sc/sica** — 一致→采用, 不一致→SC/SICA fallback
3. **gr_cascade_nli_first** (0.7/0.8/0.9) — NLI 高置信→NLI, 否则→SICA-G
4. **nli_override** (0.85/0.90) — 默认 SICA-G, NLI 高置信不同意→override
5. **majority_3way** — SICA-G + NLI + SC 三票
6. **majority_4way** — SICA-G + NLI + SC + original SICA 四票

每种策略都带 McNemar vs SC / vs SICA / vs SICA-G 统计检验。

### 运行前需要
1. G conservative 跑完 → `per_problem_conservative.json` 就绪
2. 把 R 结果 scp 到 westd-16639：
   ```bash
   scp westd-25068:/root/symb_invariant_consensus/results/direction_r_nli_large/results.json \
       /root/symb_invariant_consensus/results/direction_r_nli_large/results.json
   ```
3. 部署脚本到 westd-16639
4. 运行：
   ```bash
   python direction_gr_combo.py \
     --g-results results/direction_g_decoupling/per_problem_conservative.json \
     --r-results results/direction_r_nli_large/results.json \
     --baseline results/exp033_mistral_7b_folio204/exp033_results.json
   ```

---
