# ops query models and prep e2e

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_query-models-and-prep-e2e_20260515T190340_result.json`
- **Structured JSON:** [`e6e2c9fd243a8e9a0035.json`](../../sessions/e6/e6e2c9fd243a8e9a0035.json)

## Before a recorded user message

1 recorded events

### Log line

_source line 1_

{
  "raw": "全部 5 个 instance 完成。总运行时间 ~23 分钟（03:05 - 03:28）。\n\n## 报告\n\n### 1. 可用模型列表（Qwen 系列）\n\n| 模型 ID | 类型 |\n|---------|------|\n| `qwen/qwen3.5-9b` | Text |\n| `qwen/qwen3.5-35b-a3b` | MoE, 3B active |\n| `qwen/qwen3.5-122b-a10b` | MoE, 10B active |\n| `qwen/qwen3.5-397b-a17b` | MoE, 17B active |\n| `qwen/qwen3.5-plus-02-15` | Text |\n| `qwen/qwen3.5-flash` | Text |\n| **`qwen/qwen3-coder-next`** | **代码专用** |\n| `qwen/qwen3.6-plus` | 最新一代 |\n\n其他厂商候选：`deepseek/deepseek-v4-pro`, `moonshotai/kimi-k2.5`\n\n### 2. 推荐模型\n\n**首选：`qwen/qwen3-coder-next`**（代码专用，SWE-bench 场景最匹配）\n\n备选：`qwen/qwen3.6-plus`（最新通用模型，综合能力强）\n\n### 3. Dry-run 结果 (5 instances)\n\n| Instance | Resolved | Patch 生成 | 备注 |\n|----------|----------|-----------|------|\n| astropy-12907 | false | 有 patch（修改 separable.py） | CompoundModel 处理逻辑 |\n| astropy-14182 | false | 空 patch | retrieval 未命中关键文件 |\n| astropy-14365 | false | 有 patch（修改 qdp.py） | strip+upper 修复 |\n| astropy-14995 | false | 有 patch（修改 ndarithmetic.py） | mask=None 处理 |\n| astropy-6938 | false | 有 patch（修改 fitsrec.py） | str.replace 返回值修复 |\n\n- **Resolve rate: 0/5 (0%)**，但 4/5 instance 成功生成了非空 patch\n- API 调用全部成功，无超时\n- 每 instance 耗时 ~3-5 分钟（主要是 astropy 大仓 encoding 耗时）\n- 总耗时约 23 分钟（含模型加载）\n\n### 4. 全量 E2E eval 命令模板\n\n```bash\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\nsource /etc/network_turbo\n\nexport CUDA_VISIBLE_DEVICES=1\nexport HF_HOME=/root/autodl-tmp/.hf_cache\nexport HF_DATASETS_OFFLINE=1\nexport HF_HUB_DISABLE_XET=1\nexport STRUCTFUSE_LLM_BACKEND=api\nexport STRUCTFUSE_LLM_API_BASE=\"http://47.94.22.126/v1\"\nexport STRUCTFUSE_LLM_API_KEY=[REDACTED]"&lt;KEY>\"\nexport STRUCTFUSE_LLM_MODEL=\"qwen/qwen3-coder-next\"\n\nnohup python -u /root/structfuse/scripts/eval_swebench_e2e.py \\\n    --retriever-checkpoint /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1 \\\n    --strategy random \\\n    --top-k 10 \\\n    --agent-model \"qwen/qwen3-coder-next\" \\\n    --max-instances 0 \\\n    --repo-cache-dir /root/autodl-tmp/swebench/repos \\\n    --output-dir /root/autodl-tmp/structfuse/eval_results/e2e_full \\\n    > /tmp/e2e_full.log 2>&1 &\n```\n\n**注意事项**：\n- 必须用 `CUDA_VISIBLE_DEVICES=1`，GPU 0 已被其他进程占满\n- 全量 300 instance 预计耗时 ~15-20 小时（按 3-5 min/instance 估算）\n- `--max-instances 0` 表示跑全部"
}

---
