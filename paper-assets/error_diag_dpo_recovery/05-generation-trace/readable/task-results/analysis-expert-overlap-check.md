# analysis expert overlap check

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_expert-overlap-check_20260512T230712_result.json`
- **Structured JSON:** [`07c9be1c0285318c57d7.json`](../../sessions/07/07c9be1c0285318c57d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整分析结果：

## Expert/Failure Task Overlap 分析

### 1. Expert 数据
| 指标 | 数量 |
|------|------|
| 总轨迹 | 3119 |
| Unique game_files | 3119 |
| Unique task templates | 1395 |
| 平均 trials/template | 2.2 |

按类型：pick_and_place 759, pick_two_obj 662, pick_clean 576, pick_cool 472, pick_heat 371, look_at_obj 279

### 2. v5 Overlap（500条轨迹, 250 unique tasks）
- **175 unique 失败 tasks**
- **精确匹配**（同 game_file）：**145/175 = 82.9%**
- 按类型 overlap：look_at_obj 4/4, pick_and_place 13/14, pick_clean 31/35, pick_cool 32/38, pick_heat 30/41, pick_two 35/43
- 所有 v5 tasks（含成功）在 expert 中：217/250 = 86.8%

### 3. v6 Overlap（109条已收集, 收集中）
- **32 unique 失败 tasks**
- **精确匹配**：**28/32 = 87.5%**

### 4. Combined（v5+v6）
- **192 unique 失败 tasks**
- **精确匹配**：**160/192 = 83.3%**
- **模板匹配**（同 task template 不同 trial）：再 +22，共 **182/192 = 94.8%**
- **完全无覆盖**：仅 **10 tasks**（5.2%）

### 5. 32 个无精确匹配的 failure 分解
- 22 个：expert 中有同 task template 的不同 trial（环境相同，随机种子不同）
- 10 个：expert 中完全没有该 task template

### 6. DPO Pair 潜力

| 匹配策略 | 可用 pairs | 覆盖率 |
|-----------|-----------|--------|
| 严格（exact game_file） | 160 | 83.3% |
| 宽松（same template） | 182 | 94.8% |

### 7. v6 完成后预估
- v6 目标 600 tasks，当前 109 已收集（18%），failure rate ~29%
- 预估完成后：~174 failures，overlap ~87% → ~151 DPO pairs from v6
- v5+v6 combined unique failures 预估 ~250-280，DPO pairs ~210-240

### 结论
- 之前小样本（20 tasks）得到的 "100% overlap" 有抽样偏差，全量是 **83.3%**
- 如果接受 same-template 匹配（同一场景不同 trial），覆盖率提升到 **94.8%**
- 完全无法构建 DPO pair 的 failure tasks 仅 10 个（5.2%），可直接丢弃
- Expert 数据量充足（3119 条覆盖 1395 templates），DPO pair 构建可行性确认

---
