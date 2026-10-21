# analysis p5 flip investigation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_p5-flip-investigation_20260515T173527_result.json`
- **Structured JSON:** [`771870c54de56f3c2dcf.json`](../../sessions/77/771870c54de56f3c2dcf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部到手。结论如下：

---

## 调查结论

### 1. v3 P5 完整数据

| 字段 | 值 |
|------|----|
| `sica_answer` | `"80"` (正确) |
| `sica_scores` | `{"80": 0.0}` — 唯一候选，得分 0.0 |
| `sc_vote_distribution` | `{"80": 1}` — 只有 1 条 trace 产出答案，且是 80 |
| `scorer_mode` | `FALLBACK` (satisfied=2, excluded=40, ratio=0.048 < 0.2) |

### 2. "120" 的来源：**手动硬编码，无实际数据支撑**

`rescore_pure.py` 第 12 行：
```python
OLD_SICA = {
    "aime2024_II_05": 120,  # was wrong, GT=80
}
```

这是人工填入的 "已知旧结果"，注释说 "was wrong"。**没有任何结果 JSON 文件包含 sica_answer=120 的记录。**

### 3. 实际旧 scorer 模拟：也选了 "80"

`rescore_all.py` 对 v2 JSON 跑了 `rescore_from_summary()`，输出 `aime30_v2_rescore_analysis.json`：
- `old_sica_answer`: **"80"**（不是 120）
- `old_sica_scores`: `{"80": 0.0}`

原因很简单：P5 只有 **1 个候选答案**（"80"），无论 scorer 怎么算分，`select_answer()` 只能返回 "80"。旧 scorer 不可能选出 "120"，因为 "120" 根本不在候选列表里。

### 4. "120→80 翻转" 声明是虚假的

`rescore_pure.py` 的逻辑：
1. 从 `OLD_SICA` 字典读 hardcoded 值 `120`
2. 对比当前结果 `sica_answer = "80"`
3. `120 ≠ 80` → `flipped = True`，`flip_detail = "120→80 (corrected)"`

这是 **自证式循环**：先假设旧值是 120，再发现新值不是 120，于是声称"翻转"。但实际上旧 scorer 在同样的数据上也只能输出 80。

### 5. A+C 在当前 11 题上的实际翻转数：**零**

`scorer_improvement_analysis.md` 已明确指出：6/6 题 SC unanimous（单候选），SICA 无选择空间。P5 同样是单候选。在没有多候选竞争的情况下，A+C 改进（利用 excluded 约束区分候选）**没有施展空间**。A+C 的价值需要在有 SC 分歧的更难题目上才能体现。

---
