# ops falcon3 westd download

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_falcon3-westd-download_20260522T040315_result.json`
- **Structured JSON:** [`8acf230615ac0c9be60d.json`](../../sessions/8a/8acf230615ac0c9be60d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型验证通过。下面是报告：

## Falcon3-7B-Base 下载报告

**下载状态**: 成功 (EXIT_CODE=0, 耗时 1165 秒)

**模型文件**:
| 文件 | 大小 |
|------|------|
| model-00001-of-00004.safetensors | 4.6GB |
| model-00002-of-00004.safetensors | 4.7GB |
| model-00003-of-00004.safetensors | 4.0GB |
| model-00004-of-00004.safetensors | 769MB |
| + config, tokenizer, index 等元数据 | — |

**模型验证**: `AutoConfig.from_pretrained` 成功
- model_type=llama, layers=28, hidden=3072, vocab=131072

**westd 磁盘**: 250GB 总量，1.8GB 可用 (100%)

**过程说明**: 经历 v2-v4 三次失败（分别因无代理/代理限速/代理冲突/磁盘满），v5 通过清理 .cache 腾出空间 + hf-mirror.com 无代理模式成功完成。磁盘非常紧张，仅余 1.8GB。

---
