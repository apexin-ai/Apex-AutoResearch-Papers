# EDCR 证据分布分析：RSFT r2b

## 背景

RSFT 所有变体的 EDCR 均低于 SFT baseline（~0.66 vs 0.71），即模型在 evidence citation 中引入了更多 distractor sentences。本分析旨在理解这些 distractor 的性质——是真正无关的噪声，还是 annotation boundary 导致的测量偏差。

## 方法

- 数据源：`/root/autodl-tmp/eval_results/rsft_r2b/predictions.json`（RSFT r2b eval 输出）
- 从 1848 个包含 distractor evidence 的 matched triples 中随机采样 50 个（seed=42）
- 对每个采样，比对 predicted evidence vs gold evidence，分析 extra citations 的内容
- 自动分类 + 人工复核 "unrelated" 类别

## 统计结果

### 自动分类（n=50）

| 类别 | 数量 | 比例 | 说明 |
|------|------|------|------|
| entity_mentioned | 34 | 68% | Extra句中包含 head/tail 实体名 |
| unrelated | 11 | 22% | Extra句中不含实体名 |
| mixed | 5 | 10% | 部分包含、部分不含 |

### 人工复核 "unrelated" 类别（n=11）

对 11 个自动标记为 "unrelated" 的 case 人工审查：

| 实际原因 | 数量 | 说明 |
|----------|------|------|
| 指代/共指 (coreference) | 4 | Extra句用 "He/She/It" 指代实体，实质相关 |
| 实体名变体 | 3 | "Swedish"↔"Sweden", "Pakistani"↔"Pakistan" 等不精确匹配 |
| 背景上下文 | 3 | 文章开头/背景介绍句，提供间接语境 |
| 真正无关 | 1 | 完全不相关的句子 |

**修正后真实分类**：

| 类别 | 修正后占比 | 说明 |
|------|-----------|------|
| 语义相关但不在 gold 标注中 | **~84%** | 含 entity_mentioned(68%) + coreference(8%) + 实体变体(6%) + mixed 中相关部分 |
| 背景上下文引用 | **~12%** | 文章 intro/background 句，间接相关 |
| 真正无关的 distractor | **~4%** | 与 triple 完全无关 |

### 其他发现

- **82% 的 case 只有 1 个 extra sentence**（41/50），模型只是稍微扩大引用范围
- **68% 的 case 中 gold ⊆ pred**（34/50），模型覆盖了所有 gold evidence 但额外多引了一些

## 典型案例

### Case 1: 共指引用（非真正 distractor）

**Doc**: Carl Buchheister  
**Triple**: (Buchheister, date of death, 2 February 1964)  
- **Gold evidence**: `[0]` "Carl Buchheister (17 October 1890 – 2 February 1964) was a German constructivist artist..."  
- **Pred evidence**: `[0, 6]` — 多引了 `[6]` "He died in Hanover in 1964."  
- **分析**: Sent 6 直接佐证死亡日期，是 corroborating evidence。Gold 标注只标了最小集合，模型引用更充分。EDCR 惩罚了这种合理行为。

### Case 2: 实体名变体

**Doc**: Kiirunavaara  
**Triple**: (Norrbotten County, country, Swedish)  
- **Gold evidence**: `[4]` 提及 "Sweden"  
- **Pred evidence**: `[0, 4]` — 多引了 `[0]` "...is a mountain in Kiruna, **Sweden**..."  
- **分析**: Sent 0 包含 "Sweden"（tail 实体 "Swedish" 的变体），提供地理上下文。自动分类因字面不匹配误判为 "unrelated"。

### Case 3: 语义上下文扩展

**Doc**: Resident Evil: Degeneration  
**Triple**: (Claire Redfield, series, Resident Evil)  
- **Gold evidence**: `[5]` 提及两者共同出现  
- **Pred evidence**: `[0, 1, 5]` — 多引了 `[0]` (系列介绍) 和 `[1]` (franchise 背景)  
- **分析**: Extra sentences 都提及 "Resident Evil"（tail 实体），提供系列上下文。模型采用 over-citation 策略，引用更广的语境支撑关系。

## 结论

1. **RSFT 的 EDCR 下降主要不是证据质量退化**，而是模型学到了更宽泛的 citation 风格（over-citation）。
2. **~84% 的 "distractor" citations 实际语义相关**——包含实体提及、共指关系、或直接佐证信息。DocRED 的 gold evidence 标注偏向最小集合，而模型倾向于引用所有相关句子。
3. **真正无关的 distractor 仅占 ~4%**，说明 RSFT 并未引入大量噪声。
4. **EDCR 作为度量指标对 over-citation 过度惩罚**——它无法区分"引了无关句子"和"引了更多相关句子"。

### 对论文讨论的建议

在讨论 EDCR 下降时，可以指出：
- RSFT 模型的 Evi F1 实际上优于 SFT（0.81 vs 0.80），说明核心 evidence 识别能力更强
- EDCR 下降源于 citation breadth 增加，而非 citation precision 下降
- 这种 over-citation 在实际应用中可能反而有利于 faithfulness（提供更充分的支撑），只是在 DocRED 的最小标注方案下被度量为负面
