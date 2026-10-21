# eval llama docred unconstrained done

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_llama_docred_unconstrained_done_20260516T001356_result.json`
- **Structured JSON:** [`df5465aecc1528c61df7.json`](../../sessions/df/df5465aecc1528c61df7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 报告

### 1. Llama DocRED LoRA Unconstrained Eval 完整 Metrics

| 指标 | 值 |
|------|-----|
| **E-F1** | **83.93%** (P=84.93%, R=82.96%) |
| **R-F1** | **43.72%** (P=38.59%, R=50.41%) |
| ET% | 0.00% (0/19106) |
| RV% | 0.15% (24/16171) |
| DR% | 0.50% (80/16147 in-vocab) |
| Parse fail rate | 2.3% (23/998) |
| Mean inference time | 15.13s/sample |

**注**：gold 用 Wikidata PID（P17），pred 用自然语言名（country）。已通过 ontology 映射后计算 R-F1。RV 违规仅 24 个（organizer、natively spoken in 等不在 96 个 DocRED 关系表中的名称）。

### 2. FAIL 案例分析

- **23 个 parse fail，全部原因：JSON 输出被 max_new_tokens=4096 截断**
- FAIL 样本 raw_output 平均长度 11707 字符（OK 仅 2830），均在末尾出现截断的不完整 JSON
- FAIL 样本 inference time 平均 61.6s（OK 14.0s），模型在这些文档上生成了异常长的输出
- Gold 复杂度：FAIL 样本 gold entities 略多（22.9 vs 19.5），gold relations 反而略少（10.6 vs 12.3）
- **无系统性偏差**，纯粹是输出长度超限导致

### 3. Constrained Eval 提交确认

- exp_id: `w5_llama_docred_lora_constrained_eval`
- PID: **316355**
- GPU: cuda:0 (NVIDIA RTX PRO 6000, 97GB)
- mode: `full_s1`

### 4. GPU 状态

| GPU | 占用 | 进程 |
|-----|------|------|
| cuda:0 | 14MiB → loading | PID 316355 (constrained eval) |
| cuda:1 | 17418MiB | PID 304011 (其他任务) |

---
