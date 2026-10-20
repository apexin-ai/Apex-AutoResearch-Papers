# code mistral bcp prep

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mistral-bcp-prep_20260512T225704_result.json`
- **Structured JSON:** [`af6868737f3e165b499a.json`](../../sessions/af/af6868737f3e165b499a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出总结

### 1. Mistral Tool-Calling 能力评估

**结论：Mistral-7B-Instruct-v0.3 原生支持 tool calling，无需替代方案。**

- Tokenizer 包含专用 special tokens：`[TOOL_CALLS]` (id=5), `[AVAILABLE_TOOLS]`/`[/AVAILABLE_TOOLS]` (id=6,7), `[TOOL_RESULTS]`/`[/TOOL_RESULTS]` (id=8,9)
- `chat_template` 内置完整 tool use 逻辑：工具声明→模型调用→结果返回的完整流程
- vLLM 0.18.1 有对应的 `--tool-call-parser mistral` 解析器

### 2. 脚本路径

`/root/democalib/eval_mistral_bcp.sh`

### 3. 与 Qwen 版本的关键差异

| 项目 | Qwen | Mistral |
|------|------|---------|
| tool-call-parser | `hermes` | `mistral` |
| served-model-name | `democalib-qwen` | `democalib-mistral` |
| --trust-remote-code | 需要 | 不需要（已移除） |
| 默认端口 | 8000 | 8003（避免冲突） |
| 输出目录 | `results/` | `results/mistral_bcp/` |

### 4. Dry-run 验证结果

- Python imports 全部通过（behavioral_fingerprint, h_gate_evaluator, prompt_loader）
- `run_mvp_experiment.py --help` 正常
- Shell 语法检查通过
- vLLM `mistral` parser 确认可用

### 5. 运行方式

```bash
# 基础运行（GPU 空闲后）
cd /root/democalib && bash eval_mistral_bcp.sh

# 指定 GPU 和多轮
GPU_ID=1 NUM_RUNS=3 bash eval_mistral_bcp.sh
```

### 6. 已知风险点

- Llama BCP 结果显示 task_completion 仅 5%（H2 未通过），Mistral 可能类似——tau-bench retail 的 tool calling 任务对 7B 模型较难
- Mistral v0.3 的 tool_call_id 要求 **恰好 9 位字母数字**（chat_template 有 raise_exception 检查），如果 tau-bench 生成的 ID 不符合，会报错——运行时需关注

---
