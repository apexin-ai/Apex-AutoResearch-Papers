# code exp b frontier sc

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_b_frontier_sc_20260520T181716_result.json`
- **Structured JSON:** [`5528191a8418edce8aff.json`](../../sessions/55/5528191a8418edce8aff.json)

## Before a recorded user message

1 recorded events

### Log line

_source line 1_

{
  "raw": "代码和 registry 已就绪。产出报告：\n\n---\n\n## 产出报告：exp_b_frontier_sc_fewnerd\n\n### 代码路径\n`artifacts/experiments/frontier_sc/run_frontier_sc.py`\n\n### OpenRouter Model IDs\n| Model | OpenRouter ID |\n|---|---|\n| GPT-5.5 | `openai/gpt-5.5` |\n| Claude Opus 4.6 | `anthropic/claude-opus-4.6` |\n\n### Cost 估算\n\n| 项目 | 数值 |\n|---|---|\n| API calls | 200 inst × (1 greedy + 8 SC) × 2 models = **3,600 calls** |\n| 每 call tokens | ~800 input + ~300 output |\n| 总 input | ~2.88M tokens |\n| 总 output | ~1.08M tokens |\n| **GPT-5.5** | 1.44M × $5/M + 0.54M × $30/M = **$23.4** |\n| **Claude Opus 4.6** | 1.44M × $5/M + 0.54M × $25/M = **$20.7** |\n| **总计** | **~$44** |\n\n### 依赖\n```\nopenai          # OpenAI SDK (兼容 OpenRouter)\nnumpy\nscipy\ndatasets        # 仅 --from-hf 模式需要\n```\n\n### 运行方式\n```bash\nexport OPENROUTER_API_KEY=[REDACTED]"sk-...\"\n\n# 从 HuggingFace 加载数据\npython run_frontier_sc.py --from-hf\n\n# 或从本地 UIE JSONL 加载（可从服务器 scp）\npython run_frontier_sc.py --data-path /path/to/fewnerd_test.jsonl\n\n# 只跑单个模型\npython run_frontier_sc.py --from-hf --models gpt-5.5\n```\n\n### 关键设计\n- **Greedy 独立调用**（T=0）与 **8 个 SC 样本**（T=1.0）分开\n- **9 阈值 MV 扫描**（0.1-0.9），自动找最优阈值\n- **每 10 个 instance checkpoint**，支持断点续跑（`--no-resume` 强制重新开始）\n- **Failure mode 诊断**：degeneracy rate、high-agreement-wrong、low-agreement-correct\n- **Spearman correlation**：agreement ↔ greedy F1、agreement ↔ MV F1\n- Prompt 模板与项目 `zeroshot_prompts.py` 完全一致（带 type descriptions）"
}

---
