# MaxSAT 根因诊断报告：satisfied_ratio=1.000 全场

**实验**: sica_proofwriter30_v2  
**日期**: 2026-05-16  
**数据**: ProofWriter D5, 17题, k=12, QwQ-32B via vLLM  

---

## 1. 核心发现：三重失效

MaxSAT 全场 satisfied_ratio=1.000、excluded=0 是**三个独立问题叠加**的结果，不是单一 bug。

### 问题 A：约束提取失败率 54.4%

| 指标 | 数值 |
|------|------|
| 总提取尝试 | 204 (17题 × 12 traces) |
| 成功提取 | 93 (45.6%) |
| "No JSON found" | 99 次 |
| 零约束问题 | 4/17 (23.5%) |

**原因**: QwQ-32B 是推理模型，收到 extraction prompt 后倾向重新推理问题（输出 "Okay, let me try..."），而非按指令输出 JSON。失败的 trace 全部是纯文本推理，没有 JSON 块。

**致命关联**: 3/4 零约束问题恰好是多候选问题（有投票分歧），即最需要 SICA 介入的场景完全没有约束可用：
- P5 (616_Q7): False=7, True=5 → 0 约束 → SICA 退化为无信息
- P14 (251_Q10): False=7, Unknown=3, True=2 → 0 约束
- P17 (31_Q12): 8:4 split → 0 约束

### 问题 B：一致性 traces 产生一致性约束

14/17 题投票完全一致（12/12 同一答案）。对这些题：
- 所有 trace 推导同一结论，提取出的约束描述同一逻辑链
- 约束天然不矛盾 → MaxSAT 无需排除任何约束
- 这是**正确行为**，不是 bug

去重比率验证了这一点：
- 891_Q1: 180 raw → 27 unique (85% 重复) — 12 条 trace 产出大量重复约束
- 844_Q1: 177 raw → 22 unique (88% 重复)
- 971_Q5: 40 raw → 5 unique (88% 重复)

这意味着不同 trace 提取的约束高度重叠，语义相同，MaxSAT 自然能全部满足。

### 问题 C：评分机制的系统性偏差

唯一一个 SICA 与 SC 不同的题：

**P11 (498_Q8)**: gt=False, SC=False(✓), SICA=True(✗)
- 投票: False=11, True=1
- 约束: 4/12 traces 有约束, 21 unique, 全部 satisfied
- SICA 分数: **True=38.0 > False=27.0** → SICA 选了少数派

根因：只有 4 条 trace 成功提取了约束。如果那 1 条回答 "True" 的 trace 恰好成功提取了大量约束（或其约束权重高），而 11 条 "False" trace 中大部分提取失败，则 True 的约束权重反而更高。

**这是提取失败的非随机性导致的系统偏差**：提取成功率与 trace 内容相关，不是均匀随机的。

---

## 2. MaxSAT 求解器本身是否有 bug？

**没有。** 注入测试验证了 6 种场景：

| 测试 | 结果 |
|------|------|
| 直接布尔矛盾 (X=True vs X=False) | ✅ 正确排除低权重约束 |
| 一致约束集 | ✅ 全部满足 |
| 10 个独立变量约束 | ✅ 全部满足（符合预期） |
| 10 一致 + 1 对矛盾 | ✅ 排除低权重矛盾方 |
| 蕴含链矛盾 (A→B, A=T, B=F) | ✅ 正确排除 |
| **不同变量名约束** | ⚠️ 全部满足（无法冲突） |

Test 5（不同变量名）揭示了结构性问题：如果 trace A 的约束用 `prop_a`，trace B 用 `conclusion_x`，即使语义矛盾，z3 变量不同，MaxSAT 也无法检测。当前代码通过 `check_equivalence` 做去重，但**只合并等价约束，不检测互补/矛盾约束**。

---

## 3. 约束语义质量分析

虽然无法直接查看原始约束文本（结果 JSON 未存储、日志无 DEBUG 级别输出），但从统计推断：

**提取 prompt 设计** (`LOGIC_EXTRACTION_PROMPT`) 质量尚可：
- 明确定义了 fact/rule/derived 三种类型
- 给出了变量命名规范 (property_entity, relation_subject_object)
- 有 z3 语法示例

**但 QwQ-32B 不遵守格式**：
- 作为 reasoning model，它的默认行为是展开思考链
- 即使 prompt 要求 "Output ONLY the JSON"，模型仍然先推理
- `_strip_thinking()` 能处理 `<think>` 标签，但 QwQ 的思考链不一定用 `<think>` 标签
- `_extract_json_str()` 做了 regex 提取，但如果全文无 `{` 就彻底失败

---

## 4. 诊断结论

### Q1: MaxSAT 全满足的根因是什么？

**三因叠加**:
1. **提取失败** (54.4%): 最需要约束的多候选题提取为零
2. **约束天然一致**: 一致投票的题约束不矛盾（正确行为）
3. **变量名隔离**: 不同 trace 的约束可能使用不同变量名，即使语义矛盾也不会在 z3 层面冲突

### Q2: 是否可修？

**可修，但需要分层修复：**

| 层级 | 修复 | 预期效果 |
|------|------|----------|
| L1: 提取格式 | 换用 instruction-following 能力更强的模型做提取（如 Qwen2.5-Instruct 而非 QwQ）；或在 extraction prompt 前加 system message 强制 JSON-only | 提取成功率 45% → 80%+ |
| L2: JSON 鲁棒性 | 增强 `_parse_response`: 用 regex 从纯文本中捞约束（`r"(\w+)\s+(is|are)\s+(True|False)"` → 自动生成 z3 约束） | 挽回 10-20% 失败 |
| L3: 答案约束注入 | 每条 trace 自动追加一条 `answer == <trace_answer>` 约束，确保不同答案的 trace 之间必有冲突 | 关键修复——使 MaxSAT 能区分不同答案 |
| L4: 变量名归一化 | 提取后对变量名做规范化映射（基于问题实体名），或在 dedup 时做变量重命名匹配 | 中等难度，但提升有限 |

### Q3: 修复预估时间

| 修复 | 时间 |
|------|------|
| L1 (换提取模型/加 system prompt) | 30 分钟 |
| L2 (regex 后处理) | 1 小时 |
| L3 (答案约束注入) | 30 分钟 |
| L4 (变量归一化) | 2-4 小时 |
| **推荐最小修复集 (L1+L3)** | **1 小时** |

### Q4: 修复后是否值得验证？

**必须验证。** 建议在同一 17 题子集上重跑（加 `--save-intermediates`），对比：
- 提取成功率变化
- MaxSAT excluded > 0 的题数
- SICA vs SC 准确率差异

### Q5: JSON 提取失败改善方案

**短期 (30min)**：
- 对 QwQ 的提取请求加 `system: "You are a JSON extraction assistant. Output ONLY valid JSON, no reasoning."` 
- 在 `_extract_json_str` 失败时，增加 regex 后处理：从纯文本中提取 `X is True/False` 模式

**中期 (改架构)**：
- 用两个模型分工：QwQ 做推理（trace generation），Qwen2.5-7B-Instruct 做提取（constraint extraction）
- 或者用 structured output / JSON mode 调 vLLM

---

## 5. 关键数据附录

### 全部 17 题统计

```
Problem               | GT    | SC    | SICA  | Extraction | Unique | Satisfied | Excluded
----------------------|-------|-------|-------|------------|--------|-----------|--------
979_Q9    (unanimous) | True  | True  | True  | 4/12 (33%) | 29     | 29        | 0
1036_Q11  (unanimous) | True  | True  | True  | 1/12 (8%)  | 13     | 13        | 0
891_Q1    (unanimous) | True  | True  | True  | 12/12(100%)| 27     | 27        | 0
347_Q11   (unanimous) | True  | True  | True  | 0/12 (0%)  | 0      | 0         | 0
616_Q7    (7F/5T)     | True  | False | False | 0/12 (0%)  | 0      | 0         | 0
399_Q3    (unanimous) | True  | True  | True  | 12/12(100%)| 27     | 27        | 0
173_Q11   (unanimous) | True  | True  | True  | 3/12 (25%) | 12     | 12        | 0
971_Q5    (unanimous) | True  | True  | True  | 8/12 (67%) | 5      | 5         | 0
702_Q1    (unanimous) | True  | True  | True  | 12/12(100%)| 25     | 25        | 0
844_Q1    (unanimous) | True  | True  | True  | 12/12(100%)| 22     | 22        | 0
498_Q8    (11F/1T)    | False | False | True⚠ | 4/12 (33%) | 21     | 21        | 0
20_Q10    (unanimous) | False | False | False | 10/12(83%) | 25     | 25        | 0
173_Q10   (unanimous) | False | False | False | 1/12 (8%)  | 9      | 9         | 0
251_Q10   (7F/3U/2T)  | False | False | False | 0/12 (0%)  | 0      | 0         | 0
721_Q8    (unanimous) | False | False | False | 2/12 (17%) | 15     | 15        | 0
500_Q8    (unanimous) | False | False | False | 12/12(100%)| 26     | 26        | 0
31_Q12    (8:4 split) | ?     | ?     | ?     | 0/12 (0%)  | 0      | 0         | 0
```

### MaxSAT 注入测试结果

```
Test 1 (direct contradiction):     satisfied=1 excluded=1  ✅
Test 2 (consistent set):           satisfied=3 excluded=0  ✅
Test 3 (independent variables):    satisfied=10 excluded=0 ✅ (expected)
Test 4 (contradiction + noise):    satisfied=10 excluded=1 ✅
Test 5 (different var names):      satisfied=3 excluded=0  ⚠️ (no conflict possible)
Test 6 (implication chain):        satisfied=2 excluded=1  ✅
```

### 关键结论一句话

**MaxSAT 求解器正确，但喂给它的约束没有矛盾——要么因为提取失败(54%)导致无约束可用，要么因为一致投票的 trace 产出一致的约束。修复优先级：L3 答案约束注入 > L1 提取模型/prompt > L2 regex 后处理。**
