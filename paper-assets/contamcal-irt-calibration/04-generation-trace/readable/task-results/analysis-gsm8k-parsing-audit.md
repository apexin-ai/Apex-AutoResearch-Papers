# analysis gsm8k parsing audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gsm8k-parsing-audit_20260515T142154_result.json`
- **Structured JSON:** [`d44884aa1449577c1b4e.json`](../../sessions/d4/d44884aa1449577c1b4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结果

### 结论：0.5B 的 16.3% 是真实结果，不是 regex 假阳性。问题出在 1.5B。

**核心证据：**

1. **0.5B 正确样本的原始输出**是完整的 CoT 数学推理（如 `3×3=9, 9×60=540, #### 540`），5/5 正确样本全部通过 `####` pattern 提取，不是 last-number fallback。

2. **统计排除随机匹配**：期望随机匹配率 0.6%，实际 16.3%（26.7 倍）；各 gold answer 范围（1-10 到 >1000）的正确率均匀分布在 14-19%，无小数字偏差。

3. **1.5B 的 0.5% 是模型退化**：
   - 79% 的 items 生成"桤"字重复（纯垃圾，512 tokens）
   - 21% 生成了完全不同的问题（非原题答案）
   - 7 个"正确"项全是巧合匹配（模型编的简单题答案碰巧一样）

### 受影响范围
- **SFT 模型不受影响**（None 率均为 0%，正确率合理）
- **1.5B base pretrained 不可用作 baseline**
- **GSM8K regex 逻辑本身无需修改**

### 建议
1. 标记 1.5B base 结果为不可靠
2. 如需 1.5B base baseline，去掉 ChatML template 改用 raw text completion
3. evaluate.py 建议保存 raw generation text 和提取方式以便 debug

报告已注册：`art_20260515_f94f58`

---
