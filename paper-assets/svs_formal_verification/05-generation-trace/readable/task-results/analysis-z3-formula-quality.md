# analysis z3 formula quality

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_z3_formula_quality_20260514T120510_result.json`
- **Structured JSON:** [`6e85004c9d90bd9d712c.json`](../../sessions/6e/6e85004c9d90bd9d712c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。下面是完整的分析报告。

---

## Z3 公式质量抽查报告

### 1. 数据概况

| 指标 | 值 |
|------|-----|
| 总 chains | 192 (24题 × 8链) |
| SAT chains | 130 (62.5%) |
| UNSAT chains | 78 (37.5%) |
| Perfect SAT (ic≥0.99) | 52 (27.1%) |
| SAT 链准确率 | 56.9% |
| UNSAT 链准确率 | 51.3% |
| Cohen's d (correct vs wrong IC) | **-0.044** (FAIL, 方向都反了) |

### 2. All-SAT 链样例分析

| 问题 | Gold | All-SAT链数 | 最大claims | 答案正确? |
|------|------|-------------|-----------|----------|
| pw_819 | Unknown | 6/8 | 50/50 formalized, ic=1.0 | 5/6 WRONG (答True) |
| pw_19726 | True | 8/8 | 29/29 formalized, ic=1.0 | 8/8 correct |
| pw_4572 | True | 7/8 | 31/32 formalized, ic=1.0 | SVS答Unknown (WRONG) |
| pw_24270 | Unknown | 6/8 | 31/31 formalized, ic=1.0 | SVS答True (WRONG) |
| pw_2848 | True | 7/8 | 8/8 formalized, ic=1.0 | 7/7 correct |

**pw_819 chain 4**: 50 个 claims 全部形式化、全部 SAT、ic=1.0 —— 但答案是 **错的**。这是 trivially SAT 的典型证据。

### 3. 结构性根因（Z3 实验验证）

写了纯 Z3 结构测试，关键结论：

**Test K（核心发现）**：一条有推理错误的链（第3步推导错误），如果规则（ForAll）未被形式化、只保留了 ground facts，则 **Z3 返回 SAT**——错误被隐藏了。

```
完整形式化（含规则 + 事实）: UNSAT ← 正确检测到矛盾
部分形式化（只有事实，规则缺失）: SAT  ← 错误不可见！
纯 ground facts（无规则）: SAT  ← 独立事实永远 SAT
```

**Test L**：一组纯 ground facts（如 `Green(cat)`, `Big(dog)`, `Chase(lion, mouse)`）**在 uninterpreted functions 下永远 SAT**，除非恰好存在 `P(a) ∧ ¬P(a)` 的直接矛盾。

### 4. 为什么大部分链是 trivially SAT

ProofWriter depth-5 的 premise 结构：
- **36% 是规则**（"If something is green then it is big"）
- **64% 是事实**（"The cat is green"）

但 CoT 链会追加 ~10 步推导，每步都是 ground fact（"Therefore the cat is big"）。最终一条典型链约 **75% 是 ground atoms，25% 是量化规则**。

关键链条：
1. LLM 生成 chain → claims 以 ground facts 为主
2. LLM 形式化：ground facts 简单（`Green(cat)`），规则更难（`ForAll([x], Implies(Green(x), Big(x)))`）
3. 形式化失败的 14% 更可能是规则
4. Z3 收到的表达式集以独立 ground atoms 为主
5. 独立 ground atoms **几乎不可能 UNSAT**（除非恰好 P(a)∧¬P(a)）
6. → **IC 分数不反映推理质量，只反映「有没有碰巧出现直接矛盾」**

### 5. 结论

| 类别 | 占比 | 判定 |
|------|------|------|
| **Trivially SAT**（ground-fact 主导，规则缺失或未触发） | **~80-90% of all-SAT** | 公式形式正确但语义空洞 |
| **Genuinely SAT**（含完整规则链，推理无矛盾） | **~10-20% of all-SAT** | 少数 |

52 条 all-SAT 链中，估计 **40-47 条是 trivially SAT**。证据：
1. Perfect SAT 链准确率（57.7%）与其他链无差异
2. Cohen's d 为负——IC 反而略偏向错误链
3. Z3 结构测试确认：缺少规则的 ground-fact 集合必然 SAT
4. 50-claim all-SAT 链答案为错误的案例存在

**底线：当前 Z3 公式验证的 SAT/UNSAT 信号基本是噪音，不携带推理质量信息。**

---
