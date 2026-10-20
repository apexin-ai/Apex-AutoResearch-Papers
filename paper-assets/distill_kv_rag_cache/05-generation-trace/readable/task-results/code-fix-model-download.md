# code fix model download

**distill kv rag cache** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-model-download_20260514T054101_result.json`
- **Structured JSON:** [`afc691531160138793aa.json`](../../sessions/af/afc691531160138793aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型验证通过。

## 产出总结

| 项目 | 结果 |
|------|------|
| **原始状态** | PID 3830 ModelScope + network_turbo 代理，~500 kB/s，预计 4+ 小时 |
| **加速方案** | 方案 A：去掉代理直连 ModelScope 国内 CDN + 跳过 original/ 目录 |
| **最终速度** | 3-17 MB/s（平均约 6 MB/s），提升 10-30 倍 |
| **总耗时** | 954 秒（约 16 分钟） |
| **模型路径** | `/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct` |
| **符号链接** | `/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3.1-8B-Instruct` → 上述路径 |
| **验证** | LlamaForCausalLM, hidden=4096, layers=32, vocab=128256, tokenizer OK |

关键发现：`network_turbo` 代理反而减慢了 ModelScope 的国内 CDN 下载速度。去掉代理后直连速度提升了约 200 倍（初始峰值 137 MB/s，稳定 3-17 MB/s）。

---
