# research model selection download

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_model-selection-download_20260516T045315_result.json`
- **Structured JSON:** [`6cec3549b49ebf1d430b.json`](../../sessions/6c/6cec3549b49ebf1d430b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载正在后台进行。汇报当前状态：

## 模型选择：DeepSeek-Coder-6.7B-Instruct

**选择理由：**
- **HumanEval pass@1: 78.6%** — 同级别（~7B）最强，甚至超过 CodeLlama-70B-Instruct (67.8%)
- 与 Qwen 完全不同家族（DeepSeek 自有架构）
- 标准 transformer，完全支持 LoRA 微调
- 6.7B 参数，与 Qwen3-8B 可比
- HuggingFace/ModelScope 高下载量，社区验证充分

**淘汰理由：**
| 模型 | 淘汰原因 |
|------|----------|
| CodeLlama-7B-Instruct | HumanEval ~34-40%，远低于 DeepSeek |
| StarCoder2-7B | 无 instruct 版本，擅长低资源语言但 HumanEval 不突出 |
| CodeGemma-7B-IT | 非纯 code specialist，benchmark 数据不如 DeepSeek 清晰 |

## 下载状态

- **PID**: 464106
- **服务器**: seetacloud-westd-4x5090
- **路径**: `/root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct`
- **方式**: ModelScope（HF 被墙）
- **速度**: ~5-6 MB/s，预计 **25-30 分钟**完成
- **磁盘**: 99GB 可用，模型 ~13GB，充足

我会继续监控下载进度。要我等完成后再汇报，还是先继续其他工作？

Sources:
- [DeepSeek-Coder GitHub](https://github.com/deepseek-ai/DeepSeek-Coder)
- [DeepSeek-Coder-6.7B-Instruct on HuggingFace](https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-instruct)
- [DeepSeek-Coder-6.7B-Instruct on ModelScope](https://modelscope.cn/models/deepseek-ai/deepseek-coder-6.7b-instruct)
- [Performance Benchmarks - DeepWiki](https://deepwiki.com/deepseek-ai/DeepSeek-Coder/2.2-performance-and-benchmarks)

---
