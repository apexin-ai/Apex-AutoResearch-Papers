# paper headroom auroc fix

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_headroom-auroc-fix_20260523T203911_result.json`
- **Structured JSON:** [`a1378fab29e96153cd37.json`](../../sessions/a1/a1378fab29e96153cd37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

---

## 追溯报告

### 子任务 1: tab:selection headroom 不一致

**数据来源追溯**:
- **表体** (.775/.645 → 13.0pp): 来自 `exp_016_signal_ensemble` / `exp_016_rerun_1024_bootstrap` (provenance c013: Oracle=0.776, Greedy=0.644, headroom=13.2pp)。Selection Δ (LP +0.2pp, p=.29) 和所有 p 值均与此数据一致。
- **旧 caption** (.781/.667 → 11.4pp): 来自 MF4v2 pipeline 重算，使用不同的 F1 计算方式（micro greedy=0.6617 vs per-instance=0.6453, decisions D153）。
- **图**: 实际绿线标注 "Oracle +13.1"，与表体一致。旧 caption "11.4pp" 是错误覆盖。

**修复方案**: Method B — 更新 caption 和正文以匹配表体（13.0pp），因为：
1. 表体值与 selection Δ 和 p 值一致
2. 图实际显示 +13.1pp
3. provenance c013 确认 Oracle=0.776, Greedy=0.644

**修改位置** (`single_signal.tex`):
| 行 | 修改 |
|---|---|
| L12 | Caption: Oracle .781→.775, Greedy .667→.645 |
| L35 | Figure caption: 11.4pp → 13.0pp |
| L39 | 正文: 11.4pp → 13.0pp |
| L47 | 正文: 11.4pp → 13.0pp |

**残留不一致（需注意）**: appendix tab:scale_comparison (L1606) 仍有 SciERC Greedy=.667, Hdr=11.4。该表使用不同 seed/metric（s42 单 seed vs 多 seed 均值），与 tab:fewnerd SciERC Greedy=.663 也不同。属于独立 metric 一致性问题。

### 子任务 2: AUROC 排名残留

**无旧排名残留**。确认结果：
- 主表 (tab:quality_estimation): SJ(.692) > VC(.684) > EM(.631) ✅ 已为新值
- appendix L1927 "EM > VC > SJ > FK > LP": 描述 **LLaMA-3.2-3B** 实验（非 SciERC Qwen），与该模型的表格数据一致 ✅
- experiments_main L52 "EM leads CoNLL": CoNLL 实验，EM AUROC=.816 正确 ✅
- 无 .749 旧值残留
- 无 rebuttal/response 文件

### 产出
1. ✅ 追溯报告（如上）
2. ✅ 修正 `docs/paper/sections/single_signal.tex`（4 处修改）
3. ✅ 编译通过：0 undefined refs, 8 pages main text, 46 pages total
4. ✅ 匿名仓库 commit: `70ed395`

---
