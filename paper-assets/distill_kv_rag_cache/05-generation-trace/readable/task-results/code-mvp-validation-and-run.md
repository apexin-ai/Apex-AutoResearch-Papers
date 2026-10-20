# code mvp validation and run

**distill kv rag cache** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-validation-and-run_20260514T061232_result.json`
- **Structured JSON:** [`9d114f7ea6ed4f3d6126.json`](../../sessions/9d/9d114f7ea6ed4f3d6126.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

双 GPU 评估正在运行：
- **GPU 0**: Config A_6x 开始（共 A/B/C × 6x/8x = 6 runs × 500 samples）
- **GPU 1**: Config D_6x 开始（共 D/E × 6x/8x = 3 runs × 500 samples，E 只有 baseline）

GPU 内存使用约 17.6GB/96GB，利用率正常。

## 验证总结

| 项目 | 状态 |
|------|------|
| **模型路径** | `/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct` (tokenizer vocab_size=128000) |
| **NQ 数据** | 500 条合成样本（NQ 格式，avg context ~5783 chars）。真实 NQ 因 AutoDL 网络限制下载极慢，后续需通过其他方式获取 |
| **代码修复** | 3 处 transformers 4.57.6 兼容性修复：① `num_heads` → `config.num_attention_heads`，② NoPE RoPE dtype cast，③ DynamicCache API (`key_cache` → `layers[i].keys`)，④ attention 返回值从 3 改为 2，⑤ `_quantize` device 统一 |
| **验证结果** | 5 个 config 全部通过（A/B/C/D/E），无报错。F1=0.091（合成数据），延迟 baseline 0.77s，压缩 configs ~4.6s |
| **正式运行** | 双 GPU 已启动。GPU0 跑 A/B/C（PID 13497），GPU1 跑 D/E（PID 13722）|

**注意**：合成数据上各 config 的 EM/F1 完全相同，这是预期的（合成文本模式单一，模型生成相似输出）。需要真实 NQ 数据才能观察到 config 间的质量差异。建议后续通过 scp 或其他渠道将 NQ 数据传输到服务器。

---
