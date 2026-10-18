# bugfix claude pipeline diagnosis

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_claude-pipeline-diagnosis_20260523T000123_result.json`
- **Structured JSON:** [`80e9a57a492c0b3972c8.json`](../../sessions/80/80e9a57a492c0b3972c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。诊断总结：

## 诊断结果

**根因**：不存在 Claude 跨 benchmark 评分脚本。

| 文件 | 问题 |
|------|------|
| `claude_judge_scoring.py` | 硬编码只处理 LLMBar 数据（verified_32b/verbosity），不覆盖 AlpacaEval/MT-Bench |
| `gpt4o_crossbenchmark_scoring.py` | GPT-4o 的跨 benchmark 版本存在，但无 Claude 对应版本 |
| `cross_benchmark_analysis.py` | CONFIGS 只有 Llama-70B 和 Qwen3-32B，缺 Claude |
| `scored_claude_alpacaeval_formality.jsonl` | Worker 用 `pairwise_scoring.py` 尝试评分，API 调用全部失败（可能是 model name 格式错误或 402），100 条记录全 null |

## 已完成的修复

1. **创建** `csd_pipeline/claude_crossbenchmark_scoring.py` — 支持 AlpacaEval + MT-Bench × formality/verbosity，自动探测正确的 model name（含 fallback 到 `anthropic/claude-sonnet-4-20250514`），有 `--test-api` 预检
2. **更新** `csd_pipeline/cross_benchmark_analysis.py` — 添加 3 个 Claude 配置条目
3. **写入** `artifacts/r14_fixes/claude_pipeline_diagnosis.json` — 详细诊断报告含命令模板

## 待执行（API key 审批后）

```bash
export OPENROUTER_KEY='&lt;key>'
cd /root/causal_style_decomp_judge

# 先测试 API 连通性和 model name
python -m csd_pipeline.claude_crossbenchmark_scoring --test-api

# 跑全部 3 个 benchmark×axis 组合（~1120 API calls）
python -m csd_pipeline.claude_crossbenchmark_scoring --benchmark all --axis all
```

需要补跑：AlpacaEval×formality (100条)、AlpacaEval×verbosity (100条)、MT-Bench×formality (80条)。

---
