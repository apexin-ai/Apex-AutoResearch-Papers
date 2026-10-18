# check mistral hires status

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_mistral_hires_status_20260514T210448_result.json`
- **Structured JSON:** [`46feffe6a1f7e953d49b.json`](../../sessions/46/46feffe6a1f7e953d49b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 **FAILED**。日志文件 `/root/ratekv/logs/mistral_hires_bf16_2bitonly.log` 显示崩溃：

```
ValueError: Unrecognized model in /root/autodl-tmp/models/AI-ModelScope/Mistral-7B-v0___3. 
Should have a `model_type` key in its config.json
```

**详情**:
- 结果文件 `mistral_hires_bf16_2bitonly_results.json` 和 `_profiles.json` 均**不存在**
- 脚本在 `AutoConfig.from_pretrained()` 阶段就崩了（`run_mistral_hires_bf16_2bitonly.py:82`），模型根本没加载成功
- 根因：ModelScope 下载的 Mistral-7B-v0.3 路径 `/root/autodl-tmp/models/AI-ModelScope/Mistral-7B-v0___3` 的 `config.json` 缺少 `model_type` 字段，transformers 无法识别
- `/tmp/mistral_hires_launch.log`（23KB，5月14日13:33）可能是更早的启动日志

**修复方向**: 检查该模型目录下的 `config.json`，手动添加 `"model_type": "mistral"` 或重新下载模型。

---
