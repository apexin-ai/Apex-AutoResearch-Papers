# code plan003 data download

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan003-data-download_20260520T095123_result.json`
- **Structured JSON:** [`99fb8038bfd751c981bb.json`](../../sessions/99/99fb8038bfd751c981bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。VAST 的 `_repo` 目录占了 301M（含 git），可以清理。以下是汇总：

---

### 数据集统计

| Dataset | K | Train | Val | Test | Total | 磁盘 |
|---------|---|-------|-----|------|-------|------|
| **HumAID** | 10 | 53,531 | 7,793 | 15,160 | 76,484 | 17M |
| **VAST** | 3 | 13,477 | 2,062 | 3,006 | 18,545 | 301M* |
| **Civil Comments** | 2 | 100,000 | 97,320 | 97,320 | 294,640 | 105M |

*VAST 含 git clone 的 `_repo`，JSONL 本身很小

**HumAID (K=10)**：实际标签数是 10（非 11），类别为 caution_and_advice, displaced_people_and_evacuations, infrastructure_and_utility_damage, injured_or_dead_people, missing_or_found_people, not_humanitarian, other_relevant_information, requests_or_urgent_needs, rescue_volunteering_or_donation_effort, sympathy_and_support。最大类 rescue_volunteering_or_donation_effort (21K)，最小类 missing_or_found_people (358)。

**VAST (K=3)**：con=7297, neutral=4296, pro=6952，分布相对均匀。

**Civil Comments (K=2)**：non_toxic=272K, toxic=22K，极度不平衡（~7.6% toxic）。Train 取了前 100K 条以节省磁盘。

**输出格式**：每个数据集 `{train,val,test}.jsonl`，每行 `{"text", "label", "label_name", "split"}`。

**脚本位置**：`/home/sonny/causal_annot_error_attrib/data/preprocess.py`

---
