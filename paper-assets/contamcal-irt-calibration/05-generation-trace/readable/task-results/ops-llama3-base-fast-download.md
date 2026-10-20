# ops llama3 base fast download

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama3-base-fast-download_20260521T085735_result.json`
- **Structured JSON:** [`72cc87fe6151b5032438.json`](../../sessions/72/72cc87fe6151b5032438.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载完成。汇报：

## 结果

1. **下载方案**: cqa1 中转（ModelScope CDN → cqa1 aria2c 32 MiB/s → SCP 9-13 MiB/s → westd）
2. **模型路径**: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B`
3. **Base 验证**:
   - model_type: `llama`
   - architectures: `LlamaForCausalLM`
   - hidden_size: 4096, num_hidden_layers: 32, vocab_size: 128256
   - **Base 模型确认**（非 Instruct）
4. **文件完整性**: 4 个 safetensors 全部匹配预期大小，总计 15GB
5. **磁盘**: 19GB 剩余 (93% used)

**总耗时**: ~28 分钟（17:22 → 17:51），相比原始 430kB/s 下载预计 10+ 小时

**注意**: 路径中 `Meta-Llama-3___1-8B` 使用三下划线（ModelScope 命名规范）。SFT 脚本需要使用此路径。

---
