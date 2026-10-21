# research gemma verify diagnosis

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_gemma-verify-diagnosis_20260524T090611_result.json`
- **Structured JSON:** [`31da274c3ccd81600ea1.json`](../../sessions/31/31da274c3ccd81600ea1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。诊断结果如下：

---

## 诊断报告：Gemma verify_parametric_knowledge 管线

### 1. Llama vs Gemma 数据对比

| 指标 | Llama-3.1-8B | Gemma-2-9B-IT |
|------|-------------|---------------|
| Train 样本数 | 1200 (600+600) | 528 (264+264) |
| Test 样本数 | 400 (201+199) | 176 (88+88) |
| Steering N_test (conflict only) | 201 | 88 |
| Probe accuracy | 91.5% | 59.7% |
| Baseline parametric | 4 (2.0%) | **1 (1.1%)** |
| Baseline contextual | 131 (65.2%) | 20 (22.7%) |
| Baseline both | 10 (5.0%) | **43 (48.9%)** |
| Baseline neither | 56 (27.9%) | 24 (27.3%) |
| **Conflict 样本中 parametric==contextual** | **0 (0%)** | **60 (68.2%)** |

### 2. 根因：`prepare_gemma_data.py` 的 relabel 逻辑缺陷

`prepare_gemma_data.py` 采用 "pair-and-flip" 方式生成数据：

**步骤 A**：对每个 ConflictQA 条目创建一对样本：
- **conflict 样本**：`context=counter_memory`, `parametric_answer=memory_answer`, `contextual_answer=counter_answer` — 两个 answer 不同
- **no_conflict 样本**：`context=parametric_memory`, `parametric_answer=memory_answer`, `contextual_answer=memory_answer` — **两个 answer 相同**

**步骤 B**：验证 Gemma 的参数知识。当 Gemma 知道正确答案（ground_truth）而 ChatGPT 不知道时，翻转标签：
- 原 `no_conflict` → 翻为 `conflict`
- 原 `conflict` → 翻为 `no_conflict`

**Bug**：翻转时**只改了 `label` 字段，没有更新 `parametric_answer` 和 `contextual_answer`**。原 no_conflict 样本翻为 conflict 后，两个 answer 仍然相同（都是 ChatGPT 的 `memory_answer`）。

**后果**：在 `steering_experiment.py` 的 `classify_answer()` 中，当 `parametric_answer == contextual_answer` 时：
- 模型输出匹配 → 归类为 `"both"`（不可能是 parametric 或 contextual）
- 模型输出不匹配 → 归类为 `"neither"`
- `"parametric"` 和 `"contextual"` 在这些样本上**永远不可能出现**

这解释了 Gemma baseline 中 48.9% `both` + 27.3% `neither` = 76.2% 的样本无法被有效分类。

**Llama 不受影响的原因**：Llama 的数据不是由 `prepare_gemma_data.py` 生成的（项目中无 `prepare_llama_data.py`），且 Llama 的 conflict 样本中 parametric≠contextual 的比例为 100%。ChatGPT 和 Llama 共享大部分参数知识（都训练于类似的英文 web 数据），极少需要翻转标签，因此没有触发此 bug。

### 3. 176 → 88 的原因

`steering_experiment.py` 第 376 行：
```python
test_data = [d for d in all_data if d["label"] == "conflict"]
```

只使用 `label=="conflict"` 的样本（88 个），丢弃了 88 个 `no_conflict` 样本。这是设计如此（只在知识冲突场景下测试 steering），不是 bug。

### 4. Parametric 1/88 的根因

88 个 conflict 样本中：
- **60 个**（68%）有 `parametric_answer == contextual_answer` → 分类器只能输出 `both`（43）或 `neither`（24）
- **28 个**（32%）有不同的 answer，但 `parametric_answer` 仍是 **ChatGPT 的记忆**而非 Gemma 的参数知识 → 如果 Gemma 的参数知识与 ChatGPT 不同，分类器也无法正确归类为 `parametric`
- 最终只有 **1 个**样本碰巧被分类为 `parametric`

### 5. 次要问题：`generate()` 未使用 chat template

`prepare_gemma_data.py` 的验证步骤：
```python
def generate(model, tokenizer, prompt, max_new_tokens=50):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)  # 直接 tokenize
```

对比 `steering_experiment.py`：
```python
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
```

Gemma-2-9B-IT 期望 `&lt;start_of_turn>user` 格式的输入。不用 chat template 会导致模型输出不可靠 → 更多 "neither" → 更多样本被丢弃 → 数据集更小（1000 个 ConflictQA 条目最终只留下 352 per class）。

### 6. 修复建议

1. **修复 relabel 后的 answer 字段**：翻转 no_conflict→conflict 时，更新答案：
   - `parametric_answer` ← ground_truth（Gemma 真正知道的正确答案）
   - `contextual_answer` ← memory_answer（context 中支持的 ChatGPT 记忆，对 Gemma 来说是 "上下文提供的错误答案"）

2. **修复 `generate()` 使用 chat template**：与 `steering_experiment.py` 保持一致。

3. **增大 `n_sample`**：1000 → 2000+，确保过滤后仍有 ≥200 test per class。

4. **替代方案**：放弃 pair-and-flip，改用与 Llama 相同的管线 — 直接筛选 Gemma 参数知识与 ground_truth 不一致的条目作为 conflict，用 ground_truth 作为 `parametric_answer`、counter_answer 作为 `contextual_answer`。这从根本上避免了 answer 字段不一致的问题。

---
