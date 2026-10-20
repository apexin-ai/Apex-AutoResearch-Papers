# code opensource inference framework

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_opensource_inference_framework_20260520T091147_result.json`
- **Structured JSON:** [`19adf7937f2abd288d22.json`](../../sessions/19/19adf7937f2abd288d22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出文件：

| 文件 | 说明 |
|------|------|
| `config_local.py` | 模型注册表（5个模型）、generation 参数、vLLM 默认配置 |
| `harness_local.py` | 主推理模块，`--backend vllm\|transformers`，复用 harness.py 的 clause loading / system prompt / tool response matching，输出格式完全一致 |
| `setup_vllm.sh` | vLLM server 启动脚本，自动检测 GPU 数量、推断 tool-call parser、5 分钟健康检查 |

关键设计：
- **vLLM 后端**：通过 OpenAI SDK 连接本地 server，代码结构与 harness.py 几乎相同，支持并发
- **Transformers 后端**：直接加载模型，`apply_chat_template(tools=...)` 原生 tool 支持 + fallback prompt injection，顺序执行
- **Tool call 解析**：`parse_tool_calls()` 支持 Qwen3/Hermes、DeepSeek、通用 JSON 三种格式
- **断点续跑**：同 harness.py 的 `_load_completed` 机制

---
