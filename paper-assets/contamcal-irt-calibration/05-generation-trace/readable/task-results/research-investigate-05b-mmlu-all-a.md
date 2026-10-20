# research investigate 05B mmlu all A

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_investigate-05B-mmlu-all-A_20260515T092022_result.json`
- **Structured JSON:** [`fe452bc28853a4013c1b.json`](../../sessions/fe/fe452bc28853a4013c1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

v2 log 中无 "aligned" 关键字，但 `--mc-format` 默认值就是 `aligned`（代码 L546），且 v2 和 aligned 的结果完全相同（预测分布一致），确认 v2 就是 aligned format。

现在已有足够数据得出结论。

---

## 调查结果

### 1. Aligned Format 的 Prompt Template

```
Question: {question}
A) {choice_A}
B) {choice_B}
C) {choice_C}
D) {choice_D}
The answer is 
```
通过 `format_as_chat()` 包在 Qwen chat template 里（`<|im_start|>user\n...<|im_end|>\n<|im_start|>assistant\n`），然后用 `compute_choice_logprobs` 取最后一个 token 位置对 A/B/C/D 的 logprob，argmax 选答案。

### 2. 预测分布：**不是全 A，但 A 严重过度代表**

| 模型配置 | MMLU Acc | A% | B% | C% | D% |
|---|---|---|---|---|---|
| **0.5B d000 aligned** | 39.79% | **46.2%** | 26.3% | 9.5% | 18.0% |
| 0.5B d000 legacy | 40.49% | 39.5% | 11.2% | 11.5% | **37.7%** |
| 0.5B d005 aligned | 32.55% | **65.1%** | 9.3% | 1.9% | 23.8% |
| 0.5B d025 aligned | 28.03% | **79.8%** | 1.9% | 0.6% | 17.7% |
| 0.5B d100 aligned | 23.34% | **98.3%** | 0.4% | 0.5% | 0.8% |
| 0.5B Instruct aligned | 24.62% | **90.4%** | 0.4% | 0.7% | 8.6% |
| **1.5B d000 aligned** | **58.53%** | 16.5% | 33.3% | 24.7% | 25.6% |
| **3B d000 v2 aligned** | **63.14%** | 20.2% | 33.4% | 24.8% | 21.6% |

### 3. 是否 0.5B 特有？**是。**
- 1.5B 和 3B 预测分布均匀（A/B/C/D 各 ~20-33%），MMLU 58-63%
- 0.5B 不管什么配置，A 都严重过高

### 4. 所有 0.5B dosage 都有此问题？**是，且 dosage 越高越严重。**
- d000: A=46% → d005: A=65% → d025: A=80% → d100: A=98%
- 0.5B Instruct 也有同样问题（A=90%）
- 准确率随 A 偏向加重而下降：40% → 33% → 28% → 23%

### 5. 结论：**模型能力问题，非 eval 代码 bug**

- **eval 代码无 bug**——`compute_choice_logprobs` 对所有 scale 用同一逻辑，1.5B/3B 结果正常
- **aligned format 本身无 bug**——它只是让问题更显眼，legacy format 下 0.5B 也有严重位置偏差（A+D 占 77%）
- **根因是 0.5B 模型容量不足**：在 logprob 层面对选项字母有强烈的位置先验（position bias），尤其偏好 "A" token。SFT 训练（dosage↑）不但没修正这个 bias，反而强化了它——可能是因为训练数据中 "The answer is A" 这个 pattern 被模型作为捷径记住了
- 0.5B Instruct（已经过 RLHF 的官方模型）也有同样问题，进一步说明这是 0.5B 尺度的固有限制

**建议**：0.5B 的 MMLU/ARC 结果不可靠，分析 IRT 参数时应考虑排除 0.5B 或将其 position bias 作为已知 confound 处理。

---
