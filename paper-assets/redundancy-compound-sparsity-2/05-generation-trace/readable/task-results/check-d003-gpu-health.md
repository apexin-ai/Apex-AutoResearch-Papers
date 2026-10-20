# check d003 gpu health

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d003_gpu_health_20260512T124616_result.json`
- **Structured JSON:** [`f1ea78665a6fbb8a4ec0.json`](../../sessions/f1/f1ea78665a6fbb8a4ec0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 健康检查报告

### GPU 状态
| GPU | 型号 | Compute % | Memory % | 显存占用 |
|-----|------|-----------|----------|----------|
| 0 | RTX PRO 6000 Blackwell (96GB) | **0%** | **0%** | 0MiB / 97887MiB |
| 1 | RTX PRO 6000 Blackwell (96GB) | **0%** | **0%** | 0MiB / 97887MiB |

**GPU 上无任何运行中的进程。**

---

### 两个实验均已崩溃

**d003_reasoning_traces (原 PID 19876, cuda:0)** — **已挂**
- 错误：`OSError: We couldn't connect to 'https://huggingface.co'`
- 原因：在 `AutoTokenizer.from_pretrained()` 阶段就失败了，网络不通且本地缓存里也找不到模型文件
- 脚本：`/root/carc/d003_reasoning_traces.py:311`

**d003_wikitext_32k (原 PID 19732, cuda:1)** — **已挂**
- 错误：`torch.AcceleratorError: CUDA error: invalid device ordinal`
- 原因：模型从本地路径 `/root/carc/models/DeepSeek-R1-Distill-Qwen-14B` 加载成功，但在 `from_pretrained()` 的 device_map 分配阶段尝试访问了不存在的 GPU 设备编号
- 脚本：`/root/carc/d003_wikitext_32k.py:286`

---

### 根因总结

1. **reasoning_traces**：需要先 `source /etc/network_turbo` 启用网络代理，或将模型改为本地路径加载（参考 wikitext 的做法）
2. **wikitext_32k**：`device_map` 配置可能指定了超出实际 GPU 数量的设备（比如指定了 cuda:2+），或者 `CUDA_VISIBLE_DEVICES` 环境变量限制了可见 GPU。需要检查启动命令中的设备分配参数。

两个实验都需要修复后重新启动。

---
