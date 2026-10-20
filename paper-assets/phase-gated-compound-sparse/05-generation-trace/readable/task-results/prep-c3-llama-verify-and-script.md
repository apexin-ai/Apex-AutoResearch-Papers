# prep c3 llama verify and script

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_c3-llama-verify-and-script_20260514T143156_result.json`
- **Structured JSON:** [`428ad57da4134cef7ffc.json`](../../sessions/42/428ad57da4134cef7ffc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇总：

### 结果

**模型状态**: 完整可用
- 路径: `/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Llama-8B/`
- 架构: `LlamaForCausalLM`, 32层, 32 heads, 8 KV heads
- 大小: 15GB (2个 safetensors 分片)
- Tokenizer: 正常加载, vocab_size=128000

**Profiling 脚本兼容性**: `run_profiling.py` 使用 `AutoModelForCausalLM`，架构无关，无需适配。

**启动脚本已创建**:
- `run_c3_llama_gpu0.sh` — importance × {0.15, 0.20, 0.25, 0.30} on GPU 0
- `run_c3_llama_gpu1.sh` — random × {0.15, 0.20, 0.25, 0.30} on GPU 1
- 输出目录: `profiling_output_n500_bf16_llama_{imp,rand}_s{015,020,025,030}`
- 日志: `logs/n500_llama_{imp,rand}_s{015,020,025,030}.log`

**数据集**: `math500.json` 存在，500 条。

GPU 释放后可直接 `nohup bash run_c3_llama_gpu0.sh &` 和 `nohup bash run_c3_llama_gpu1.sh &` 启动。

---
