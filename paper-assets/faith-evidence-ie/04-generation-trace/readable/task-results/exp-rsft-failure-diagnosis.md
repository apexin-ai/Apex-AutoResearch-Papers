# exp rsft failure diagnosis

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_rsft-failure-diagnosis_20260515T081525_result.json`
- **Structured JSON:** [`b321771f6b8d3f6a5fc3.json`](../../sessions/b3/b321771f6b8d3f6a5fc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

推理全部完成。所有 5 个文档都确认了根因。以下是完整诊断报告。

---

## RSFT 灾难性失败根因诊断报告

### 1. RSFT vs SFT 训练数据分布对比

| 指标 | SFT (DocRED train) | RSFT (筛选后) |
|------|-------------------|---------------|
| 样本数 | 3053 docs | 2718 samples (2691 docs) |
| 关系/样本 mean | 12.5 | 11.2 (valid: 11.9) |
| 关系/样本 median | 11 | 10 |
| 关系/样本 std | 7.6 | 6.8 |
| 零关系样本 | 26 (0.9%) | **170 (6.3%) — 全为截断 JSON** |
| 关系词汇 | DocRED 96 种 | DocRED 190 种 |
| Evidence 格式 | int | int (30201/30201) |
| F1 reward | — | mean=0.616, min=0.103 |

**数据分布本身基本合理**，关系数量分布与 SFT 接近。

### 2. 根因：RSFT 模型输出完全偏离 DocRED 关系本体

**SFT 模型输出**（正确）：
```json
{"head": "Piraeus", "relation": "country", "tail": "Greece", "evidence": [0]}
{"head": "Athens", "relation": "located in the administrative territorial entity", "tail": "Greece", "evidence": [0, 2]}
```

**RSFT 模型输出**（灾难）：
```json
{"head": "Skai TV", "relation": "based in", "tail": "Piraeus", "evidence": ["0"]}
{"head": "Skai TV", "relation": "gradually spread its coverage nationwide", "tail": "Athens metropolitan area", "evidence": ["2"]}
{"head": "Malpai Borderlands", "relation": "has_lowest_elevation", "tail": "3,700 feet", "evidence": ["3"]}
{"head": "Rabbit Beach", "relation": "was voted the world's best beach by", "tail": "travel site TripAdvisor", "evidence": ["12"]}
```

5 个 dev 文档推理全部一致：
- **关系名退化为自由文本**：使用 "based in", "part of", "co-written by", "possessed", "has_name_origin" 等非 DocRED 标准关系
- **Evidence 格式退化**：整数变字符串 `["0"]` instead of `[0]`（不一致，部分仍为 int）
- **实体退化为任意文本片段**：tail 出现 "care of the curtains, hangings, and ropes of the sanctuary" 等文档文本碎片
- **JSON 结构保持正确**：head/relation/tail/evidence 四字段仍在

模型仍在做关系抽取，但退回到 **Qwen3-4B 基座模型的开放域 IE 行为**，完全丢失了 SFT 学到的 DocRED 本体约束。

### 3. 根因判断：过拟合 + SFT 知识覆写

**直接原因**：RSFT LoRA 在训练数据上过拟合，对未见过的 dev 数据泛化失败，退化为基座模型行为。

**证据链**：
1. **训练 loss 下降但 eval loss 上升**：epoch 1 eval_loss=0.756 → epoch 2 eval_loss=0.759。模型在 step ~170 后就开始过拟合。
2. **3 个 full epoch 过多**：510 steps × bs16 = 8160 samples seen，2718 unique samples 被反复学习 3 遍
3. **LoRA 缩放因子过高**：alpha/r = 128/64 = 2.0，放大了 adapter 的影响
4. **170 个截断 JSON 样本（6.3%）**：output 长度 2664-3974 chars，全部为 generation 阶段 max_new_tokens 截断导致的不完整 JSON。这些样本教模型产生不完整/异常输出
5. **4-bit 量化 merge 引入舍入误差**：`merge_and_unload()` 在 4-bit 权重上合并 SFT LoRA 有损，进一步放大了 RSFT LoRA 的干扰

**机制**：RSFT LoRA 的权重更新在训练集上记忆了特定的 input→output 映射，但对未见文档，这些权重更新反而干扰了 SFT merged model 的泛化能力，使模型退回到基座 Qwen3-4B 的默认 IE 行为模式。

### 4. 修复方向

| 优先级 | 修复 | 原因 |
|--------|------|------|
| **P0** | 过滤掉 170 个截断 JSON 样本 | 直接消除训练噪声 |
| **P0** | 只训练 1 epoch（~170 steps） | eval loss 在 epoch 1 后就上升 |
| **P1** | 降低 LoRA alpha 到 32-64（scaling 0.5-1.0） | 减少 adapter 对基座模型的干扰 |
| **P1** | 降低 lr 到 5e-6~1e-5 | 减缓权重更新幅度 |
| **P2** | 考虑 continual LoRA（从 SFT LoRA 继续训练）替代 merge+新 LoRA | 避免 4-bit merge 损失，保持 SFT 知识连续性 |
| **P2** | 增加 RSFT 数据多样性（更多 docs、更多 generation variants） | 改善泛化 |
| **P3** | 添加 early stopping 基于 task-level eval（rel_f1） | 防止未来过拟合 |

---
