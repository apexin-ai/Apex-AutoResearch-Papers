# experiment fp16 baseline v3 bugfix

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_fp16-baseline-v3-bugfix_20260524T182108_result.json`
- **Structured JSON:** [`a578c31184e51ef4d2c6.json`](../../sessions/a5/a578c31184e51ef4d2c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 总结

**Bug 根因**：`s["answer"]` 是整数索引（0, 1, 2, 3），`extract_answer()` 返回字母（"A", "B", "C", "D"），`pred == gold` 永远为 False → accuracy = 0.000

**修复**：`gold = chr(65 + s["answer"])` 将索引转换为字母

**验证结果**（Qwen2.5-14B-Instruct-AWQ，100 样本）：
| Benchmark | 修复前 | 修复后 |
|-----------|--------|--------|
| MMLU | 0.000 | **0.710** |
| ARC | 0.000 | **0.840** |

**其他修复**：
- ModelScope 下载路径兼容性（旧版脚本 `from_pretrained` 无法识别 ModelScope 返回的本地路径）
- 添加 LLaMA-3.1-8B/70B 和 Mistral-Large-123B（用 ModelScope 国内 CDN）
- 添加 `CLEANUP_AFTER_EVAL` 自动清理已评测模型释放磁盘空间
- 清除旧的错误 checkpoint

**当前状态**：任务 `r1w2-fp16-baseline` 在 tmux 中运行，Qwen 14B AWQ 已完成，正在下载 Qwen 14B FP16。后续依次评测 Qwen 32B、LLaMA 8B、LLaMA 70B AWQ、Mistral-Large AWQ。

查看进度：`tail -f /tmp/fp16_baseline_v3.log`

---
