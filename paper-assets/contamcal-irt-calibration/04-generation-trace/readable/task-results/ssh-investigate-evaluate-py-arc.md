# ssh investigate evaluate py arc

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_investigate-evaluate-py-arc_20260519T001155_result.json`
- **Structured JSON:** [`ee2b3e5ded7040dcbb3a.json`](../../sessions/ee/ee2b3e5ded7040dcbb3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。

---

## 排查结果

### Part A: cqa1 — evaluate.py ARC 配置

**ARC-Challenge 评估参数：**
- **Shot 数**: 25-shot（标准）
- **数据集**: `allenai/ai2_arc`, `ARC-Challenge` config, test split (1172 items)
- **Few-shot 来源**: Validation split 前 25 条（确定性选取，与 test 无重叠）
- **评估方法**: Base 模型用 logprob（对 choice token 计算 log_softmax 取 argmax），Instruct 模型用 generation

**`--mc-format aligned` 含义：**
- Prompt 末尾用 `"The answer is "` 而非 `"Answer:"`，匹配 SFT 训练格式
- **不改变选项排列**，原始顺序保留
- Few-shot 示例格式：`"Question: ...\nA) ...\nB) ...\nThe answer is B."`
- 测试 item 格式：`"Question: ...\nA) ...\nB) ...\nThe answer is "` ← 模型需补全

**Answer Leakage 评估：未发现泄漏**
- Few-shot 示例包含正确答案是标准做法
- 测试 item 不包含答案
- 无选项 shuffle，无位置偏置引入
- 整个 prompt 包裹在 chat template 中（`format_as_chat`）

**Per-item 输出格式：**
```json
{"index": 0, "correct": true, "pred": "C", "gold": "C"}
```

### ≤3B d000 ARC 历史结果

| Model | Acc | Correct/Total |
|---|---|---|
| **Llama-3.2-3B d000 s42** | 60.07% | 704/1172 |
| Llama-3.2-3B d005 s42 | 59.56% | 698/1172 |
| Llama-3.2-3B d025 s42 | 60.24% | 706/1172 |
| Llama-3.2-3B d100 s42 | 59.81% | 701/1172 |
| Qwen2.5-0.5B base (pretrained) | 22.78% | 267/1172 |
| Qwen2.5-0.5B-Instruct | 50.00% | 586/1172 |
| Qwen2.5-1.5B-Instruct | 76.54% | 897/1172 |
| Qwen2.5-3B-Instruct | 81.14% | 951/1172 |
| Qwen2.5-7B d000 s42 | 89.59% | 1050/1172 |
| Qwen2.5-7B d000 s123 | 89.85% | 1053/1172 |

Llama-3.2-3B 各 contamination dose 的 ARC 差异极小（59.6%-60.2%），与预期一致：ARC 选项排列未被 SFT 污染训练影响。

### Part B: westd 状态

| 项目 | 状态 |
|---|---|
| **batch2 进程** | 未在跑（无 lm_eval/batch2 进程，无相关 tmux session） |
| **evaluate.py** | 存在，829 行（cqa1 是 813 行，多了 `normalize_numeric_answer` 等辅助函数） |
| **ARC 核心逻辑** | 与 cqa1 一致：25-shot, aligned format, 同样的 `format_mcq_example` |
| **eval_results** | 仅 `qwen2.5-0.5b_d000_s123`，无 ARC 结果 |
| **依赖** | datasets/transformers/peft OK；`evaluate` 包未安装（不影响，evaluate.py 不 import 该包） |
| **数据** | 全部走 HuggingFace datasets 在线加载，无项目自带题目文件 |

**结论：ARC 评估配置标准，无 answer leakage。两台服务器 evaluate.py 核心逻辑一致，westd 版本略新。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "index": 0,
    "correct": true,
    "pred": "C",
    "gold": "C"
  }
}
```

</details>

---
