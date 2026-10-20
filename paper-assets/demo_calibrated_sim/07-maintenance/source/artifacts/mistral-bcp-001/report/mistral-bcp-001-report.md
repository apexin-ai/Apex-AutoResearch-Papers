# mistral-bcp-001: Mistral-7B BCP Eval Results

## Experiment
- **Model**: Mistral-7B-Instruct-v0.3
- **Task**: tau-bench retail (dev split), 20 tasks baseline
- **Server**: cqa1-21977, cuda:2
- **vLLM**: v0.20.2, --tokenizer-mode mistral --tool-call-parser mistral

## Results (Run 1, partial - 3/20 baseline tasks)

| Task | Reward | Tool Calls |
|------|--------|------------|
| 0    | 0.0    | 0 (null)   |
| 1    | 0.0    | 0 (null)   |
| 2    | 0.0    | 0 (null)   |

**Completion rate: 0.0%** (0/3 tasks)
**Tool call rate: 0/35** assistant responses had tool_calls

## Root Cause Analysis

Mistral-7B-Instruct-v0.3 cannot generate structured tool_calls through vLLM's OpenAI-compatible API when presented with 16 tools (tau-bench retail environment).

### Debugging timeline:
1. **Initial attempt**: `--tool-call-parser mistral` without `--tokenizer-mode mistral`
   - vLLM warning: "Non-Mistral tokenizer detected"
   - Result: all tool_calls = null
   
2. **Fix attempt**: Added `--tokenizer-mode mistral`
   - Warning resolved, MistralTokenizer used correctly
   - Result: still all tool_calls = null

3. **Direct API test with 1 tool**: Tool calls generated correctly ✓
4. **Direct API test with 16 tools**: tool_calls = [] (empty), model generates JSON in text content instead
5. **Conclusion**: Model can do 1-tool calling but fails with 16 tools - the tool schema overwhelms the 7B parameter model

### Model behavior
Instead of generating structured tool calls, the model:
- Writes text describing what tools it would call
- Embeds JSON-like syntax in content: `[{"name": "find_user_id_by_name_zip", "arguments": {...}}]`
- Never triggers vLLM's tool-call parser

## Plan B Decision

**KILL** — Mistral-7B completion = 0% (≤20% threshold)

The model fundamentally cannot function as a tool-calling agent on tau-bench with 16 tools. This is not a BCP calibration issue but a base model capability limitation. Cross-model BCP analysis requires models that can actually complete tasks, which Mistral-7B cannot do in this setup.

## Comparison with Qwen2.5-7B (mvp-004)
| Metric | Qwen2.5-7B | Mistral-7B |
|--------|-----------|-----------|
| Baseline completion | 36.8% | 0.0% |
| Tool calling | Working (hermes) | Broken (0/35) |
| BCP observable | Yes | N/A |
