# run exp028 prereq nothink

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_exp028_prereq_nothink_20260515T210927_result.json`
- **Structured JSON:** [`1db5c43b3f1ae8ae5698.json`](../../sessions/1d/1db5c43b3f1ae8ae5698.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

| 指标 | thinking=True (之前) | thinking=False (本次) |
|------|---------------------|----------------------|
| success | 0% | 0% |
| action_is_valid | 0.75% | **0%** |
| manager_invalid_action | ~99.25% | **100%** |
| response_length | ~1024 (满) | **51.19** |

### 关键发现

模板预填充空 `&lt;think>\n\n&lt;/think>\n\n` 后，模型**仍然**自己生成新的 `&lt;think>` 块但不闭合 `&lt;/think>`，也不输出任何 action 命令：

```
&lt;think>          ← 模板预填充
                 
&lt;/think>         ← 模板预填充

&lt;think>[Assessment: neutral] I need to find a cool cup...  ← 模型自行生成，无闭合
```

关闭 thinking 后表现反而略差（valid 0.75% → 0%）。

### 结论

**Thinking 模式不是根因，可以排除。** Qwen3-1.7B 零样本下完全无法遵循 ALFWorld 的 action 格式要求，不论 thinking 开关。根因是模型 instruction-following 能力本身。

已还原 tokenizer_config.json，GPU 已释放。W&B run: `exp028-prereq-nothink-qwen3-1.7b`。

---
