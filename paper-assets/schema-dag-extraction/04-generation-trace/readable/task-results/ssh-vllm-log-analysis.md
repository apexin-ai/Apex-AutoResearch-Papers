# ssh vllm log analysis

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_vllm-log-analysis_20260515T164947_result.json`
- **Structured JSON:** [`2ad45e1ce1c5c33fe095.json`](../../sessions/2a/2ad45e1ce1c5c33fe095.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整诊断报告。

---

## vLLM 版本
- version: **0.20.2** (V1 engine)

## 日志分析
- **JSON schema 相关 warning**: 无。没有任何 JSON schema/structured output 相关的错误或警告
- **零预测相关信息**: exp1 和 exp2 所有 batch 的 `gen_tokens=2`，`predictions=[]`，F1 全部 0.0000。没有一条 JSON 解析失败（说明模型输出的 `[]` 是合法 JSON，不是乱码）
- **其他异常**: `WARNING Failed to get device capability: SM 12.x requires CUDA >= 12.9`（GPU 计算能力警告，不影响推理正确性）

## StructuredOutputsParams 配置
```python
# run_extraction.py
batch_schema = schema_fn(batch_types)  # v2: {"type":"array","items":{"type":"object","properties":{"text":{"type":"string"},"type":{"type":"string","enum":[...]}},"required":["text","type"]}}
structured_params = StructuredOutputsParams(json=batch_schema)
sampling_params = SamplingParams(
    max_tokens=1024,
    temperature=0.0,
    structured_outputs=structured_params,
)
outputs = llm.generate(prompts, sampling_params)  # <--- 关键：裸文本 generate
```

## 预测文件内容
- **文件列表**: `predictions_fewnerd_exp1_llama-3.1-8b-instruct.json` (49MB), `predictions_fewnerd_exp2_llama-3.1-8b-instruct.json` (29MB)
- **样本输出**: 100% 的样本均为 `"predictions": [], "gen_tokens": 2`

## 根因判断

**最可能原因: B — prompt 格式不适配（缺少 chat template）**

### 证据链

1. **`llm.generate(prompts, ...)` 用裸文本调用 instruct 模型**：`run_extraction.py` 将 prompt 作为纯字符串传入 `llm.generate()`，没有调用 `tokenizer.apply_chat_template()` 或 `llm.chat()`。LLaMA-3.1-8B-Instruct 需要 `<|begin_of_text|><|start_header_id|>user<|end_header_id|>...<|eot_id|><|start_header_id|>assistant<|end_header_id|>` 格式才能理解指令。

2. **Qwen3 同样用裸文本但能工作**：`sdgd_extract_gpu.py` 也用 `llm.generate(prompts, ...)` 裸文本调用 Qwen3-32B-FP8（exp008），但 Qwen3 对非模板化输入更鲁棒。LLaMA-3.1-Instruct 对 chat template 的依赖极强。

3. **`gen_tokens=2` = `[]`**：JSON schema 约束 `type: array`，合法最小输出是 `[]`（2 个 token）。模型不理解指令时，在 constrained decoding 下走阻力最小路径，直接输出空数组。

4. **零 JSON 解析失败**：日志中没有 `"Failed to parse JSON"` 警告，说明模型始终输出合法 JSON，只是每次都是 `[]`。

5. **v2 prompt 中的措辞助推了空输出**：prompt 显式写了 `"If no entities of these types exist in the text, output an empty list []"`，这在模型不理解上下文时进一步强化了 `[]` 作为"安全"输出。

### 修复方案

在 `run_extraction.py` 中用 chat template 包装 prompt：

```python
tokenizer = llm.get_tokenizer()
formatted_prompts = [
    tokenizer.apply_chat_template(
        [{"role": "user", "content": p}],
        tokenize=False,
        add_generation_prompt=True,
    )
    for p in prompts
]
outputs = llm.generate(formatted_prompts, sampling_params)
```

或改用 `llm.chat()` API（vLLM ≥0.20 支持）。

---
