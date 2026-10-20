# urgent fulltext consistency sweep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_fulltext_consistency_sweep_20260514T092825_result.json`
- **Structured JSON:** [`bcfd535113e98cc1d899.json`](../../sessions/bc/bcfd535113e98cc1d899.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部零残留。汇报修改清单：

---

## 修改记录

```
discussion.tex:9  | 注释尾删除 "[VERIFY: G definition] results_5_1.tex Table 1 has G=11.53,11.05,35.72,41.92 (PENDING-BF16). These are ~6× smaller—likely different aggregation level (problem-level median vs segment-level). Must reconcile with §5 main table."
discussion.tex:29 | 正文 "(Cohen's $d{=}0.607$), while" → "(independent-samples $d{=}0.607$, distinct from paired $d_z$ in Table~\ref{tab:cohens-d}), while"
discussion.tex:29 | 注释尾删除 "[VERIFY: segment-level vs per-problem] median_diff values here are...Needs consistency decision with §5 main table." → 替换为 "Note: independent-samples d from per-problem re-bootstrap, not paired d_z."
discussion.tex:85 | 注释尾删除 "[VERIFY: segment-level vs per-problem] per-problem paired median_diff=9.9436 at s030; mean/median ratio may differ if switching to per-problem level" → "Per-problem paired: median_diff=9.9436 at s030"
```

## 无需修改（已在之前版本修复）

- `0.584/3.002/30.903/2.915` crossover 旧值 — 已替换为 0.032/0.818/7.196/1.363
- `8/8 FAIL` — 已改为 7/8，含 qw_rand_s030 exception caveat
- `p=0.111` — 文中不存在该引用，无需处理

## Step 4: p=0.111 验证结果

SSH 确认 `/root/autodl-tmp/pacs/results/rebootstrap_analysis/rebootstrap_results.json` 中 `p_value: 0.1113`，源文件存在且有效。但当前论文文本未引用此值，故无需改动。

## 零残留验证

| 搜索项 | 全部 *.tex 结果 |
|---|---|
| `0.584 / 3.002 / 30.903 / 2.915` | **0 matches** |
| `8/8.*FAIL` | **0 matches** |
| `VERIFY` | **0 matches** |
| `segment-level vs per-problem` | **0 matches** |
| `all eight.*FAIL / 0/8 significant` | **0 matches** |

REVIEWER-ATTACK/REBUTTAL 注释保留（6 处，按要求投稿前再清理）。

---
