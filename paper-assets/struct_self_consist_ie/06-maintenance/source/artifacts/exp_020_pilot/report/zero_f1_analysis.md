# exp-020 Pilot Zero-F1 分析报告

Date: 2026-05-16
Dataset: Few-NERD (NER), 200 instances, N=8, T=1.0

## 1. 总览

| 类别 | 数量 | 比例 |
|------|------|------|
| Gold 为空（无实体） | 31 | 15.5% |
| Greedy F1=0（gold 非空） | 24 | 12.0% |
| Greedy F1>0 | 145 | 72.5% |
| **合计** | **200** | |

Gold-empty 处理正确：30/31 greedy 也为空，仅 1 例 FP（GPX1 误识为 other）。

## 2. Zero-F1 诊断分类（24 instances）

| 诊断类别 | 数量 | 比例 | 说明 |
|----------|------|------|------|
| EMPTY_PRED | 19 | 79% | 模型未输出任何实体 |
| TYPE_MISMATCH | 4 | 17% | Span 正确但类型标错 |
| WRONG_ENTITIES | 1 | 4% | Span 边界不一致 |

**结论：不是格式解析 bug。** 所有输出都是合法的结构化 JSON，问题在于模型能力。

## 3. 根因分析

### 3.1 EMPTY_PRED（19 例）—— 主要问题

模型完全漏掉实体。特征：
- **Gold 实体数极少**：mean=1.3, median=1.0（vs 非零 F1 的 mean=3.2）
- **文本较短**：mean=103 chars（vs 非零 F1 的 139 chars）
- **高频受影响类型**：other(7), person(7), organization(4), event(2), product(2)

"other" 类型零分率最高（25%），因为语义模糊（如 "Cnidaria" 标为 other）。

### 3.2 TYPE_MISMATCH（4 例）

| Instance | Gold 类型 | Greedy 类型 | Sample 分布 |
|----------|-----------|-------------|------------|
| Orchid Island Golf and Beach Club | location | organization | building:3, location:1, org:1 |
| Los Perros del Mal / Los Psycho Circus | art | event | event:4, art:2 |
| Ula / Nurhaci | organization/person | location | person:2-3, location:2 |
| Philippine Star / Jollibee | other/building | organization | 混合 |

FewNERD 的细粒度类型本身存在歧义（art vs event, location vs organization），不完全是模型错误。

### 3.3 Span 边界不一致（1 例）

"Boeing B-52"(gold) vs "Boeing B-52 Stratofortress"(pred) —— 8/8 samples 都选了长 span，是 gold 标注的边界选择问题。

## 4. 采样恢复能力

| 有 F1>0 的 sample 数 | Zero-F1 instance 数 |
|----------------------|-------------------|
| 0/8（完全不可恢复） | 6 |
| 1/8 | 9 |
| 2/8 | 3 |
| 3/8 | 4 |
| 6/8 | 1 |
| 7/8 | 1 |

- 18/24 (75%) 至少有 1 个 sample 的 F1>0 → **采样可恢复**
- Best sample F1 (zero-greedy): mean=0.697, median=1.000
- 6 个完全不可恢复的 instance 分析见下节

## 5. 完全不可恢复的 6 个 Instance

| ID | Gold 实体 | Gold 类型 | 失败原因 |
|----|-----------|-----------|----------|
| test_00002 | "C-USA play" | event | 模型提取 "C-USA"（缺 "play"），类型标为 organization |
| test_00031 | "the SFO" | organization | 模型提取 "SFO"（缺 "the"），类型标为 building/location |
| test_00055 | "Boeing B-52" | product | 模型一致提取 "Boeing B-52 Stratofortress"（多了 "Stratofortress"）|
| test_00058 | "Back to Basics" | organization | 模型几乎不识别此实体 |
| test_00104 | "Breck Ullr Fest" | event | 模型提取 "Breck Ullr"（缺 "Fest"）|
| test_00119 | "Chasen" | person | 极短文本（30 chars），无 sample 识别 |

**共性**：span 边界分歧（3/6）+ 语义模糊实体（2/6）+ 极短文本（1/6）

## 6. Entity Type 零分率

| Type | Zero-F1 Instances | Non-zero Instances | 零分率 |
|------|------------------|--------------------|--------|
| other | 6 | 18 | **25.0%** |
| product | 3 | 15 | **16.7%** |
| person | 7 | 57 | 10.9% |
| art | 1 | 9 | 10.0% |
| event | 2 | 18 | 10.0% |
| organization | 5 | 61 | 7.6% |
| building | 1 | 13 | 7.1% |
| location | 1 | 66 | 1.5% |

## 7. 结论与建议

### 主因：模型对单实体短文本的漏检能力不足（非格式 bug）

1. **79% 是 EMPTY_PRED**：模型在只有 1 个实体的短文本上直接输出空结果
2. **17% 是类型歧义**：FewNERD 细粒度类型标注本身存在歧义
3. **4% 是 span 边界**：gold 标注的边界选择问题

### exp-021 (3ep, r=32) 预期改善

- **EMPTY_PRED 应显著改善**：更多训练 epoch + 更大 LoRA rank 应提升实体检出率
- **TYPE_MISMATCH 部分改善**：更多训练数据学习类型区分，但部分歧义是标注层面的
- **Span 边界**：难以通过训练修复，属于 gold 标注一致性问题

### 推理阶段无需调整

不存在格式解析 bug，prompt 和后处理逻辑正常工作。Self-consistency 采样已展现 75% 的恢复能力，是有效的。
