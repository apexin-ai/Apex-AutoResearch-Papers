# transfer sft random 20 to westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_transfer_sft_random_20_to_westb_20260522T120410_result.json`
- **Structured JSON:** [`8217d7a17e0cdf207082.json`](../../sessions/82/8217d7a17e0cdf207082.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

传输完成，验证通过。

**westb-23072 上 sft_random_20 目录内容：**
| 文件 | 大小 |
|------|------|
| model.safetensors | 12,174,631,264 bytes (11.3GB) |
| tokenizer.json | 11,421,907 bytes |
| tokenizer_config.json | 419 bytes |
| config.json | 2,244 bytes |
| chat_template.jinja | 2,246 bytes |
| generation_config.json | 240 bytes |
| training_args.bin | 5,777 bytes |

- model.safetensors 大小与 westd 源完全一致（12174631264 bytes）
- 目录总大小 12GB
- 数据盘剩余 14GB（95% 使用）
- 已清理 SCP 产生的嵌套副本

传输方式：通过 westb 的 SSH 密钥直接 SCP 到 westd 的 AutoDL 代理地址 `connect.westd.seetacloud.com:32935`。

---
