# ops check api endpoint and prep e2e

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-api-endpoint-and-prep-e2e_20260515T182518_result.json`
- **Structured JSON:** [`16a53cd510a1c1eb274c.json`](../../sessions/16/16a53cd510a1c1eb274c.json)

## Before a recorded user message

1 recorded events

### Log line

_source line 1_

{
  "raw": "信息收集完毕。下面是报告。\n\n---\n\n## SWE-bench E2E Eval 配置报告\n\n### 1. API Endpoint 可用模型\n\n**无法查询。** 该 endpoint 要求 `Authorization` header，使用 dummy key 返回 `\"Invalid API key\"`。需要等 `request_secret` 审批通过拿到真实 API key 后才能列出可用模型。\n\n```\nGET http://47.94.22.126/v1/models  → {\"detail\":[{\"type\":\"missing\",\"loc\":[\"header\",\"authorization\"],\"msg\":\"Field required\"}]}\nGET (with Bearer test)             → {\"detail\":\"Invalid API key\"}\n```\n\n### 2. E2E Eval 脚本使用方式\n\n主脚本：**`/root/structfuse/scripts/eval_swebench_e2e.py`**\n\n**LLM 后端配置通过环境变量控制：**\n\n| 环境变量 | 说明 | 值 |\n|----------|------|----|\n| `STRUCTFUSE_LLM_BACKEND` | 后端选择 | `api`（必须设为 api） |\n| `STRUCTFUSE_LLM_API_BASE` | API endpoint | `http://47.94.22.126/v1` |\n| `STRUCTFUSE_LLM_API_KEY` | API key | 待审批 |\n| `STRUCTFUSE_LLM_MODEL` | 模型 ID | 待确认（需查 /v1/models） |\n\n**CLI 参数：**\n```\n--retriever-checkpoint  检索器 checkpoint 路径\n--strategy              hard negative 策略 (random / embedding_distance / dataflow_aware)\n--top-k                 检索文件数 (默认 10)\n--agent-model           LLM 模型名\n--output-dir            输出目录\n--max-instances         实例上限 (0=全部300)\n--repo-cache-dir        预克隆 repo 缓存目录\n```\n\n**Patch 生成流程：** Agentless 单轮模式——将 issue + top-k 检索到的文件拼成 prompt，调 OpenAI 兼容 API 生成 unified diff，再 git apply 验证。\n\n### 3. 完整的 Eval 命令模板\n\n```bash\n# 环境变量\nexport STRUCTFUSE_LLM_BACKEND=api\nexport STRUCTFUSE_LLM_API_BASE=\"http://47.94.22.126/v1\"\nexport STRUCTFUSE_LLM_API_KEY=[REDACTED]"&lt;API_KEY>\"          # 待审批\nexport STRUCTFUSE_LLM_MODEL=\"&lt;MODEL_ID>\"           # 待确认，可能是 Qwen3.6-27B 或类似\n\n# 激活 conda\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\n\n# 先用少量实例 dry-run 验证 pipeline\npython /root/structfuse/scripts/eval_swebench_e2e.py \\\n    --retriever-checkpoint /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/dataflow_aware_s43/best_by_recall_at_1 \\\n    --strategy dataflow_aware \\\n    --top-k 10 \\\n    --agent-model \"&lt;MODEL_ID>\" \\\n    --max-instances 5 \\\n    --repo-cache-dir /root/autodl-tmp/structfuse/swebench_repos \\\n    --output-dir /root/autodl-tmp/structfuse/eval_results/e2e_test\n\n# 全量 eval (300 instances)\npython /root/structfuse/scripts/eval_swebench_e2e.py \\\n    --retriever-checkpoint /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/dataflow_aware_s43/best_by_recall_at_1 \\\n    --strategy dataflow_aware \\\n    --top-k 10 \\\n    --agent-model \"&lt;MODEL_ID>\" \\\n    --repo-cache-dir /root/autodl-tmp/structfuse/swebench_repos \\\n    --output-dir /root/autodl-tmp/structfuse/eval_results/e2e_dataflow_aware\n```\n\n### 4. 已就绪 vs 缺失项\n\n**已就绪：**\n- E2E eval 脚本 (`eval_swebench_e2e.py`) ✓\n- Retriever checkpoint (`m2_full_qwen/dataflow_aware_s43/best_by_recall_at_1`) ✓\n- swebench 4.1.0 已安装 ✓\n- openai 2.24.0 已安装 ✓\n- Repo cache（12 个项目已预克隆） ✓\n- Retrieval-only eval 脚本 (`evaluation/eval_swebench.py`) ✓\n\n**缺失/阻塞：**\n1. **API Key** — `request_secret` 审批中，拿到后才能调用\n2. **可用模型列表 / 模型 ID** — 依赖 API key，无法提前确认是否有 Qwen3.6-27B\n3. **预计运行时间** — 300 instances × 每个 1 次 API 调用 + git clone/checkout + test，估计 3-8 小时（取决于 API 响应延迟和 test 执行时间）\n\n**建议拿到 key 后的第一步：**\n```bash\ncurl -s -H \"Authorization: [REDACTED]" http://47.94.22.126/v1/models | python3 -m json.tool\n```\n确认模型 ID 后，先跑 `--max-instances 5` 验证全链路通畅。"
}

---
