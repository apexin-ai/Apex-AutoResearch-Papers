# check d003 health v2

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d003_health_v2_20260512T132402_result.json`
- **Structured JSON:** [`11da97efbac452c02acf.json`](../../sessions/11/11da97efbac452c02acf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D003 健康检查报告

### GPU 状态
| GPU | Compute | Memory | 温度 |
|-----|---------|--------|------|
| GPU 0 (RTX PRO 6000 Black) | **0%** | **0MiB / 97887MiB** | 28°C |
| GPU 1 (RTX PRO 6000 Black) | **0%** | **0MiB / 97887MiB** | 28°C |

无任何 GPU 进程。

### 进程状态
**两个实验进程均已崩溃，无存活进程。** `ps aux` 中无任何 d003/carc 相关 Python 进程。

### 崩溃原因

**实验 1 (d003_reasoning_traces)**：网络不通导致无法下载数据集。
- `ConnectionError: Couldn't reach 'hendrycks/competition_math' on the Hub`
- 根因：`Network is unreachable` — HuggingFace Hub 连接失败，重试 5 次后崩溃
- 模型已成功加载（48 layers, kv_heads=8），但在 `load_math_data()` 阶段挂掉
- **修复**：需要先 `source /etc/network_turbo` 启用代理，或提前缓存数据集到本地

**实验 2 (d003_wikitext_32k)**：transformers 版本兼容性问题。
- `AttributeError: 'tuple' object has no attribute 'get_seq_length'`
- 位置：`modeling_qwen2.py:351`，`run_strategy()` → `model()` forward pass
- 根因：代码传给模型的 `past_key_values` 是 tuple 格式，但当前 transformers 版本期望 `Cache` 对象
- **修复**：要么升级代码用 `DynamicCache`，要么在模型调用时设 `use_cache=False`，要么降级 transformers

### 总结
两个实验都已崩溃，GPU 完全空闲。需要修复后重启：
1. **exp1**：解决网络问题（`source /etc/network_turbo`）或预下载数据集
2. **exp2**：修复 `past_key_values` 类型不匹配（transformers API 变更）

---
