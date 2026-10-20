# data verify cf panel b values

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_verify_cf_panel_b_values_20260524T052103_result.json`
- **Structured JSON:** [`6115066fc53b449d57ae.json`](../../sessions/61/6115066fc53b449d57ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整对比结果。

## 数据查找结果
- **数据可用**: YES
- **找到的文件路径**:
  - Phi-3-Vision: `tracvla_{goal,spatial,object,long}/untrained/counterfactual_combined.json`
  - Qwen2.5-VL: `nora_{goal,spatial}/untrained/counterfactual_combined.json`
  - 均位于 `/root/autodl-tmp/vla-ssd/results/`

## 精确 per-condition 值（last layer cosine distance）

**Phi-3-Vision (untrained, L31)**

| Suite   | empty    | wrong    | shuffled | paraphrased | 图中值(flat) |
|---------|----------|----------|----------|-------------|------------|
| Goal    | 0.1530   | 0.0160   | 0.0839   | 0.0043      | 0.19       |
| Spatial | 0.1805   | 0.0046   | 0.1395   | 0.0044      | 0.15       |
| Object  | 0.1850   | 0.0044   | 0.0977   | 0.0052      | 0.19       |
| Long    | 0.1734   | 0.0221   | 0.1204   | 0.0070      | 0.17       |

**Qwen2.5-VL (untrained, L35)**

| Suite   | empty    | wrong    | shuffled | paraphrased | 图中值(flat) |
|---------|----------|----------|----------|-------------|------------|
| Goal    | 0.0814   | 0.0143   | 0.0332   | 0.0041      | 0.08       |
| Spatial | 0.0807   | 0.0020   | 0.0313   | 0.0047      | 0.05       |

## 关键发现

1. **图中用了 flat 值（每个 suite 4 个 condition 都相同），但实际数据存在巨大的 per-condition 差异**。以 Phi3V Goal 为例：empty=0.153 vs paraphrased=0.004，差 36 倍。

2. **图中的 flat 值与实际数据不匹配任何标准聚合**：
   - 不是 4 条件均值（Phi3V Goal 均值 = 0.064，图中 = 0.19）
   - 不是 max condition（Phi3V Goal max = 0.153 empty，图中 = 0.19）
   - 不是 empty 条件值（Phi3V Spatial empty = 0.181，图中 = 0.15）

3. **Qwen2.5-VL Goal 的 0.08 与 empty=0.081 吻合**，但 Spatial 0.05 与 empty=0.081 不符。

## 结论

- **需要更新图表**: YES
- **问题性质**: 图中 Phi-3-Vision 和 Qwen2.5-VL 的值是不精确的近似值，且用 flat 表示掩盖了 per-condition 的大幅差异（empty/shuffled 远 > wrong/paraphrased）
- **建议**: 用实际 per-condition 精确值替换 flat 近似值，使 Panel B 的 reference VLM 数据与 Panel A 一样展示 4 条件差异

---
