# check harvest all docred 70b

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_harvest-all-docred-70b_20260523T003418_result.json`
- **Structured JSON:** [`8b40508f9ffafce9d62d.json`](../../sessions/8b/8b40508f9ffafce9d62d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 GPU 全满。汇报如下：

---

## 收割结果

### westd-16980（2xRTX PRO 6000 Blackwell 96GB）
| 实验 | 进度 | 状态 |
|------|------|------|
| eval_70b_lora_docred_200_semantic_only | 169/200 | 仍在跑 (GPU 0) |
| eval_70b_lora_docred_200_grammar_only | 165/200 | 仍在跑 (GPU 1) |

### westd-21461（2xRTX PRO 6000 Blackwell 96GB）— 收割2个，启动2个

**已完成并收割：**

| 实验 | R_F1 | E_F1 | DR% | RV% | 结论 |
|------|------|------|-----|-----|------|
| 70B ZS unconstrained | 13.25 | 70.14 | 13.45 | 7.88 | baseline ✅ |
| 70B ZS grammar_only | 13.23 | 70.12 | 17.03 | 0 | negative ❌ |

**关键发现：** grammar_only 的 DR (17.03%) 比 unconstrained (13.45%) **更高**。grammar 消除了 RV (7.88%→0%)，但把这些关系强制映射到合法名后 domain/range 错配反而增多。与 SciERC 一致（grammar 对 DR 零贡献），但 DocRED 上呈现更极端的"RV→DR 转化"效应。

**新启动实验：**

| 实验 | GPU | 预估耗时 |
|------|-----|----------|
| eval_70b_zs_docred_200_full_s1 | GPU 0 | ~2-3h |
| eval_70b_lora_docred_200_full_s2 | GPU 1 | ~2-3h |

---

## DocRED 70B ZS 200-doc 消融矩阵（4/5 完成）

| Mode | R_F1 | DR% | RV% | CF |
|------|------|-----|-----|-----|
| unconstrained | 13.25 | 13.45 | 7.88 | 0 |
| grammar_only | 13.23 | **17.03** | 0 | 0 |
| semantic_only | 13.05 | **1.66** | 8.24 | 132 |
| full_s1 | 🔄 running | — | — | — |

## GPU 利用率
- **westd-16980:** GPU 0 (75%), GPU 1 (75%) — 满载
- **westd-21461:** GPU 0 (99%), GPU 1 (82%) — 满载

---
