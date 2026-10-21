# ssh 5090c 5epoch s456 inference

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_5090c_5epoch_s456_inference_20260521T175722_result.json`
- **Structured JSON:** [`67158d51c7f120c03d4f.json`](../../sessions/67/67158d51c7f120c03d4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成：

1. **模型传输** ✓ — rsync 从 autodl-5090 传输 16GB merged model 到 autodl-5090-c，4 个 safetensor shard 大小全部匹配
2. **验证** ✓ — 模型文件、tokenizer/config、FewNERD 数据全部就位
3. **推理启动** ✓ — `exp_fewnerd_5epoch_s456` 在 autodl-5090-c cuda:0 运行中
   - PID: 353730
   - 37,648 prompts 正在渲染，vLLM 引擎正常
   - 日志: `/tmp/inference_s456.log`
   - 输出: `output/fewnerd_5epoch_s456/`

---
