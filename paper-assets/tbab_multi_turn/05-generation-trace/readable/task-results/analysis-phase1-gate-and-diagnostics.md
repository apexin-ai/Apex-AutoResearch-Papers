# analysis phase1 gate and diagnostics

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase1-gate-and-diagnostics_20260518T192541_result.json`
- **Structured JSON:** [`5300c5659439d0c7e4b6.json`](../../sessions/53/5300c5659439d0c7e4b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已获取。汇总报告：

---

## 1. Phase 1 Gate 判定

| 指标 | 值 |
|---|---|
| C1_s42 P̄ | 7.69% (7/91) |
| C4_s42 P̄ | 5.49% (5/91) |
| C4 - C1 | **-2.20%** |
| 阈值 | ≥ 3% |
| **VERDICT** | **KILL** |

C4 不仅未超过 C1，反而更差。Phase 1 gate 未通过。

---

## 2. P̄ by turn count

| turns | C4_s42 | C1_s42 |
|-------|--------|--------|
| 1 | 2/2 = 100.0% | 2/2 = 100.0% |
| 2 | (无样本) | 3/3 = 100.0% |
| 3 | 1/2 = 50.0% | (无样本) |
| 4 | 2/2 = 100.0% | (无样本) |
| 5 | 0/11 = 0.0% | 1/12 = 8.3% |
| 6 | 0/17 = 0.0% | 0/18 = 0.0% |
| 7 | 0/18 = 0.0% | 0/19 = 0.0% |
| 8 | 0/21 = 0.0% | 1/21 = 4.8% |
| 9 | 0/8 = 0.0% | 0/8 = 0.0% |
| 10 | 0/8 = 0.0% | 0/8 = 0.0% |
| 11 | 0/2 = 0.0% | (无样本) |

两个模型在 turns≥5 时几乎全部崩溃。C4 的 turns 分布与 C1 不同（C4 有 turns=3,4 的样本，C1 有 turns=2 的样本），说明两者在对话展开的步调上存在差异。

---

## 3. P̄ by shard count

| shards | C4_s42 | C1_s42 |
|--------|--------|--------|
| 5 | 1/12 = 8.3% | 1/12 = 8.3% |
| 6 | 3/21 = 14.3% | 3/21 = 14.3% |
| 7 | 0/19 = 0.0% | 0/19 = 0.0% |
| 8 | 0/21 = 0.0% | 1/21 = 4.8% |
| 9 | 1/9 = 11.1% | 1/9 = 11.1% |
| 10 | 0/9 = 0.0% | 1/9 = 11.1% |

shards=5-6 两者几乎相同。shards≥7 C1 略优（C1 在 shards=8,10 各多 1 个通过）。

---

## 4. Case study: 差异分析

**Both pass (2):**
| task_id | C4 turns | C1 turns | shards |
|---------|----------|----------|--------|
| HumanEval/43 | 4 | 2 | 6 |
| HumanEval/8 | 1 | 2 | 6 |

**C4 only pass (3):**
| task_id | C4 turns | C1 turns | shards |
|---------|----------|----------|--------|
| HumanEval/86 | 4 | 6 (fail) | 6 |
| livecodebench/2917 | 1 | 5 (fail) | 5 |
| livecodebench/2977 | 3 | 9 (fail) | 9 |

**C1 only pass (5):**
| task_id | C4 turns | C1 turns | shards |
|---------|----------|----------|--------|
| HumanEval/124 | 9 (fail) | 8 | 9 |
| HumanEval/25 | 6 (fail) | 1 | 6 |
| HumanEval/7 | 5 (fail) | 1 | 5 |
| livecodebench/2727 | 10 (fail) | 5 | 10 |
| livecodebench/2876 | 8 (fail) | 2 | 8 |

**关键观察：**

1. C4 的 3 个独有通过都在较少 turns 内完成（1-4 turns），表明 TBAB 训练可能帮助模型在早期 turns 更快收敛到正确答案。
2. C1 的 5 个独有通过中，3 个在 turns=1-2 就完成了（HumanEval/25, HumanEval/7, livecodebench/2876），说明 C4 的 TBAB 训练**损害了部分原本单轮就能解决的问题的能力**。
3. C4 在这些 C1-easy 问题上用了全部 turns 仍失败（turns=shards），意味着 C4 丧失了 C1 的部分基础能力。
4. 总体上 C1 独有通过 (5) > C4 独有通过 (3)，净损失 2 题，与 P̄ 差距 -2.2% 一致。

---
