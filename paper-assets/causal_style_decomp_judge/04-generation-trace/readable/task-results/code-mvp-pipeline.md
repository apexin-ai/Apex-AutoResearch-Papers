# code mvp pipeline

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_pipeline_20260520T071204_result.json`
- **Structured JSON:** [`2c53bef4b08e7ece4fae.json`](../../sessions/2c/2c53bef4b08e7ece4fae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 项验证通过。

**创建完成，文件清单：**

| 文件 | 功能 |
|------|------|
| `csd_pipeline/__init__.py` | 包声明 |
| `csd_pipeline/data_prep.py` | 下载 LLMBar 数据 + 采样 100 条 |
| `csd_pipeline/counterfactual_gen.py` | RATE double-rewrite 生成三元组（支持 vLLM/API） |
| `csd_pipeline/content_verification.py` | BERTScore + NLI 内容保留验证 |
| `csd_pipeline/judge_scoring.py` | GPT-4o 异步评分（rate-limited + 断点续传） |
| `csd_pipeline/ate_analysis.py` | ATE 统计检验 + RATE 校正 + 可视化 |
| `requirements.txt` | 依赖列表 |
| `run_mvp.sh` | 串联 5 步管线的入口脚本 |

需要 GPU 环境的模块（content_verification 依赖 torch/transformers/bert-score，counterfactual_gen 和 judge_scoring 依赖 openai）在本地无依赖环境下 `--help` 均正常工作，实际运行需在配好依赖的 GPU 服务器上执行。

---
