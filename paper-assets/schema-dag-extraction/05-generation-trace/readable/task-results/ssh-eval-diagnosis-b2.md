# ssh eval diagnosis b2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval-diagnosis-b2_20260514T231026_result.json`
- **Structured JSON:** [`09c75bdb80a5f9cdfd71.json`](../../sessions/09/09c75bdb80a5f9cdfd71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断完成，汇报如下：

### 1. evaluate.py 的匹配实现

- **Exact**: start/end/type 三者完全相同
- **Relaxed**: type 相同 + char range 有**任意** overlap（`p_start < g_end AND p_end > g_start`）
- Type 过滤逻辑正确（pred 和 gold 都过滤到 batch_types）

### 2. 核心 Bug：模型 char offset 96.5% 是错的

模型正确提取了 entity text，但 start/end 数值基本是**编造的**。例如：
- Gold: "Grill Room" char=41-51，Pred: "Grill Room" char=25-35（text[25:35]="nd moved t"）
- 不是 token index（0% 匹配），就是纯粹的噪声数值

### 3. Count Curve 反转的根因

错误 offset 在高 count 时偶然碰到 gold span 的概率更高：

| Count | 错误offset数 | 偶然overlap数 | Overlap率 |
|-------|-------------|--------------|----------|
| 1 | 17,298 | 1,087 | **6.3%** |
| 44 | 12,222 | 2,716 | **22.2%** |
| 64 | 10,387 | 2,940 | **28.3%** |

原因：更多 types → 更多 gold spans 覆盖文本 → 随机 offset 碰到 gold 的概率增大。

### 4. 修正 offset 后的真实性能

| Count | 原始ExF1 | 原始RxF1 | **修正后TextF1** | Pred/Gold ratio |
|-------|---------|---------|---------------|----------------|
| 1 | 0.012 | 0.109 | **0.184** | 6.8:1 |
| 12 | 0.009 | 0.150 | **0.246** | 3.4:1 |
| 44 | 0.018 | 0.247 | **0.473** | 1.3:1 |
| 64 | 0.013 | 0.245 | **0.463** | 0.8:1 |

### 5. 修复建议（优先级排序）

1. **方案 C（推荐）**：Prompt 去掉 start/end 要求，只输出 `[{"text": "...", "type": "..."}]`，评估用 text matching。LLM 不擅长计算字符位置。
2. **方案 A**：对现有数据用 `text.find()` 修正 offset 后重新评估（快速验证用）。
3. **Prompt 补充**："If no entities of these types exist, output an empty array `[]`"——缓解 count=1 时的 over-prediction（6.8:1 ratio）。

诊断报告已保存至 `/root/schema-dag-extraction/results/eval_diagnosis.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "text": "...",
    "type": "..."
  }
}
```

</details>

---
