# download deepseek r1 llama 8b

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_download_deepseek-r1-llama-8b_20260516T065515_result.json`
- **Structured JSON:** [`9b9245f38a90ca5f4908.json`](../../sessions/9b/9b9245f38a90ca5f4908.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有步骤完成。汇总：

## DeepSeek-R1-Distill-LLaMA-8B 下载报告

**模型路径**: `/root/autodl-tmp/models/DeepSeek-R1-Distill-Llama-8B/`

**文件清单**:
| 文件 | 大小 |
|------|------|
| model-00001-of-000002.safetensors | 8.1G |
| model-00002-of-000002.safetensors | 6.9G |
| tokenizer.json | 8.7M |
| tokenizer_config.json | 3.0K |
| config.json | 826B |
| generation_config.json | 181B |
| model.safetensors.index.json | 24K |
| **总计** | **15G** |

**验证结果**:
- safetensors index: 2个分片全部匹配 ✓
- Tokenizer: vocab_size=128000, encode/decode 正常 ✓
- 架构: **LlamaForCausalLM** (非 Qwen), hidden=4096, layers=32 ✓

**vLLM 启动脚本**: `/root/symb_invariant_consensus/scripts/start_vllm_deepseek_r1_8b.sh` (port 8003, tp=1, max_len=8192, gpu_util=0.90)

**旧 Qwen 模型**: `/root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B/` 占 15G。数据盘剩余 103G/250G (60%)，空间充裕，暂不删除。如需释放空间可手动删除。

---
