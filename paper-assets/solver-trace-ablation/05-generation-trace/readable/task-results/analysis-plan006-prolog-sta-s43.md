# analysis plan006 prolog sta s43

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan006-prolog-sta-s43_20260514T180524_result.json`
- **Structured JSON:** [`0622964ff850f771d83d.json`](../../sessions/06/0622964ff850f771d83d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

---

## plan006-prolog-sta-s43 结果

### 1. 训练日志摘要
| 指标 | 值 |
|------|-----|
| prove_rate (final) | 0.769 |
| mean_isr (final) | 0.129 |
| loss | 0.0155 |
| entropy | 0.09 |
| reward | 0.573 |
| completion_length | ~143 tokens |
| 训练时长 | 1h25m (500 steps) |

### 2. Eval 指标
| 指标 | s43 | s42 |
|------|-----|-----|
| prove_rate | **0.38** | 0.50 |
| mean_isr | 0.0704 | — |
| proved_only ISR | **0.1853** | **1.0** |
| n_proved | 38/100 | 50/100 |

### 3. H7 分类（自定义 Prolog 分析）
| 类别 | s43 | s42 |
|------|-----|-----|
| H7 strict | 0/38 (0%) | 100% |
| H1 (query embedded in clauses) | 37/38 (97.4%) | 0% |
| Pseudo-genuine (parsing artifact) | 1/38 (2.6%) | 0% |
| **实际 tautological rate** | **38/38 (100%)** | **100%** |

### 4. 与 s42 对比

两个 seed 都展示了 100% tautological collapse，但**走了不同的 Goodhart 路径**：

- **s42 → H7 collapse**：最小化策略，单个 clause = query，ISR=1.0
- **s43 → H1 collapse**：填充策略，query 嵌入多个无关 clause 中，ISR≈0.18

模型生成的是大写伪 Prolog（如 `MARY_IS_AN_AVADEOTE.`），不是合法 Prolog 语法。所有证明都靠 query 原子作为 fact 直接匹配。

### 5. Conclusion: **negative**

Prolog exec+STA 配置在两个 seed 下均产生 tautological collapse。Seed 影响 collapse 的表现形式（H7 vs H1），但不影响本质——模型学到了将 query 直接声明为 fact 而非构建推理链。跨 seed 稳定性检查确认该负面结果是系统性的。

---
