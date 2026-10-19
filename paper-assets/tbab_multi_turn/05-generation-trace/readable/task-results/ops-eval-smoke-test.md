# ops eval smoke test

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-smoke-test_20260518T101256_result.json`
- **Structured JSON:** [`700fc4ce3e5ccba5a836.json`](../../sessions/70/700fc4ce3e5ccba5a836.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval pipeline smoke test 完成。以下是汇报：

---

## Smoke Test 结果

### 1. Pipeline 各环节状态

| 环节 | 状态 | 备注 |
|------|------|------|
| 数据加载 | ✅ | sharded_instructions_600.json，91 条 code 样本（min_shards>=5） |
| User Agent 调用 | ✅ | OpenRouter API（gpt-4o-mini）生成用户消息 + shard 揭示 |
| Assistant 推理 | ✅ | 本地 Mistral-7B-Instruct-v0.1，GPU 与训练共存无 OOM |
| System Agent 判题 | ✅ | OpenRouter API（gpt-4o-mini）turn classification + answer extraction + evaluation |
| Metrics 计算 | ✅ | P̄ / A90 / U10-90 全部输出 |
| 确定性输出 | ✅ | temperature=0，seed 42 固定子采样 |

### 2. 3 条样本 P̄ 分数

| task_id | shards | turns | score | correct |
|---------|--------|-------|-------|---------|
| sharded-livecodebench/2893 | 8 | 8 | 0 | ✗ |
| sharded-HumanEval/141 | 10 | 10 | 0 | ✗ |
| sharded-HumanEval/111 | 6 | 6 | 0 | ✗ |

**P̄ = 0.0**（未微调 base model，符合预期）

### 3. 遇到的问题和修复

| 问题 | 修复 |
|------|------|
| `openai` 包未安装 | `pip install openai` |
| `bson` 模块缺失 | `pip install pymongo` |
| `sqlparse` 模块缺失 | `pip install sqlparse nltk sacrebleu` |
| CWD 导致 prompt 文件找不到 | 必须从 `lost_in_conversation/` 目录运行 |
| Mistral v0.1 不支持 system role | 修改 `model_local.py`：`_tokenize_messages` 将 system message 合并到第一条 user message |

### 4. 正式评估注意事项

- **运行时间**：3 条样本（24 轮总计）耗时 ~9 分钟。推算全量 91 条 code 样本（~500+ 轮）约 **3-4 小时**；加 math 翻倍
- **GPU 共存**：训练占 31GB，eval 模型占 ~14GB，总计 ~45GB / 98GB，可以共存
- **API 配置**：设置 `OPENAI_API_KEY` 和 `OPENAI_BASE_URL` 环境变量即可，openai 2.37.0 自动读取
- **CWD**：必须 `cd /root/tbab_multi_turn/eval/lost_in_conversation` 再运行 `python3 ../run_eval.py`
- **API rate limit**：未观察到限速，但正式评估大量并发时需关注
- **model_openai.py cost_calculator**：当前只有 OpenAI 官方模型的定价，对 OpenRouter 代理会报错——如果 `user_agent_model` / `system_agent_model` 参数传非 gpt 模型名会崩溃

### 5. API 相关配置位置

| 配置项 | 位置 |
|--------|------|
| API key | 环境变量 `OPENAI_API_KEY` 或 `--openai_api_key` 参数 |
| Base URL | 环境变量 `OPENAI_BASE_URL`（openai SDK 自动读取） |
| User Agent 模型 | `--user_agent_model`（默认 `gpt-4o-mini`） |
| System Agent 模型 | `--system_agent_model`（默认 `gpt-4o-mini`） |
| OpenAI 客户端构造 | `eval/lost_in_conversation/model_openai.py:25-28` |

---
