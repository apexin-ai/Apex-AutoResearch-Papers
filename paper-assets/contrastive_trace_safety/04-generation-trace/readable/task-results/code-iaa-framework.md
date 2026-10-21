# code iaa framework

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_iaa_framework_20260518T203341_result.json`
- **Structured JSON:** [`d0ba7e20dd9a3869e776.json`](../../sessions/d0/d0ba7e20dd9a3869e776.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项验证全部通过。

### 结果总结

**创建文件** (`/root/autodl-tmp/contrastive_trace_safety/src/iaa/`):

| 文件 | 功能 |
|---|---|
| `sample_traces.py` | 从 HarmThoughts 按模型均衡抽样 100 条 jailbreak trace（各 25 条） |
| `prompt_template.py` | CP 标注 prompt 模板，`format_prompt()` + `get_system_prompt()` |
| `annotate.py` | 多 backend 标注（Groq/Anthropic/Google），支持断点续传、`--dry-run` |
| `compute_kappa.py` | Cohen's kappa（exact + 3-class binned）、window agreement、Pearson/Spearman 相关、MAE，支持 `--dummy` |
| `run_iaa.sh` | 一键执行全流程 |

**验证结果**:
1. `sample_traces.py` — 输出 100 条 trace（R1-8B/OT-7B/QwQ-32B/R1-32B 各 25 条）
2. `annotate.py --dry-run` — prompt 格式正确（1.3k-18.5k chars），4/4 parsing 测试通过
3. `compute_kappa.py --dummy` — dummy 数据 kappa 计算正常（exact kappa=0.17，binned kappa=0.86，Pearson r=0.97）

**已安装依赖**: `google-generativeai`（`sklearn`, `openai`, `anthropic`, `scipy` 已有）

**Groq model ID**: `qwen/qwen3-32b`（已确认）

---
