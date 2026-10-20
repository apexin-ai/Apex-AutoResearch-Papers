所有代码和数据已读取完毕。以下是完整分析报告。

---

## 1. 当前 Scorer 逻辑总结

```python
# InvariantScorer.score() 伪代码
def score(maxsat_result, traces, candidates):
    answer_traces = {answer: {trace_indices}} from traces
    
    for each candidate:
        score = 0
        for each constraint in maxsat_result.satisfied:  # ← 只看 satisfied
            if constraint.source_traces ∩ candidate的trace集合 ≠ ∅:
                score += constraint.weight  # weight = 跨trace出现频次
        scores[candidate] = score
    
    return scores

# InvariantScorer.select_answer() 伪代码
def select_answer(scores, answer_counts):
    top = argmax(scores)
    if tie: break by SC frequency (answer_counts)
    return top
```

**关键设计特征**：
- **仅使用 satisfied 约束作为正信号**，excluded 约束完全丢弃
- 约束到候选答案的映射通过 `source_traces` 间接关联
- 平局时 fallback 到 SC 投票频次

## 2. "SICA=SC" 的精确根因

**两层叠加**：

### 第一层（结构性）：SC 一致 → 单候选 → SICA 无选择空间

| 问题 | SC 分布 | 候选数 | SICA 能否不同？ |
|------|---------|--------|----------------|
| P0 (II_01) | {73: 12} | 1 | **不可能** |
| P1 (II_02) | {} | 0 | 两者都为空 |
| P2 (II_03) | {45: 11} | 1 | **不可能** |
| P3 (II_04) | {33: 12} | 1 | **不可能** |
| P4 (II_05) | {80: 1} | 1 | **不可能** |
| P5 (II_06) | {55: 12} | 1 | **不可能** |

### 第二层（评分层）：即使有多候选，信号也不足

P4: 42 constraints → 40 excluded, 2 satisfied (weight=4)。scorer 只从 2 条 satisfied 中提取信号。P4 的 sica_scores = {"80": 0.0}——satisfied 约束的 source_traces 与答案 trace 不重叠。

**根因总结**：
```
SICA=SC = 
    (1) 强模型 + k=12 → SC unanimous → 单候选
  + (2) Scorer 仅用 satisfied 正信号 → 高矛盾率时信号近零
  + (3) Excluded 约束信息完全浪费
```

## 3. 三个改进方向分析

### 方向 A：矛盾约束作为负信号
- 复杂度：**简单**（~10行代码，1个超参α）
- 能否解决：单候选不能；多候选+高矛盾率**能区分**
- 风险：深度推理trace可能产出更多冲突但答案正确；α敏感

### 方向 B：放松 MAX-SAT
- **当前已是** weighted partial MAX-SAT，不是实现问题
- B1(分组)中等复杂但失去跨trace验证优势；B2(置信度加权)需extractor配合；B3(多解枚举)潜力大但工程量大

### 方向 C：satisfied 过少时的 fallback
- 复杂度：**简单**（~15行代码，1个threshold）
- 思路：当 satisfied_ratio < threshold 时，用"最少矛盾"策略（-excluded_exposure）
- 能否解决：单候选不能；多候选+高矛盾率**最直接**

**推荐 A+C 组合**：C先（fallback安全网），A后（非fallback模式增强）。

## 4. 额外发现

1. **单候选问题比scorer更紧迫**：6/6 unanimous，即使scorer完美也0pp。需要更难题目产生SC分歧。
2. **P4 sica_scores={"80":0.0}**：satisfied约束的source_traces与答案trace不重叠——设计假设漏洞。
3. **权重=频次可能不等于可靠度**：系统性偏差的错误约束会有高权重，挤掉正确低频约束。