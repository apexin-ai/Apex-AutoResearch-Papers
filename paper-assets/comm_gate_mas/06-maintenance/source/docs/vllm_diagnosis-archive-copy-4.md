# vLLM 88.6GB 显存诊断 + Seed 123 脏数据处理

**日期**: 2026-04-27
**服务器**: westb-4x6000-a

## 1. Seed 123 文件重命名记录

服务器路径: `/root/autodl-tmp/comm_gate_mas/outputs/e2e_llama_n300_clean/`

| 原文件名 | 新文件名 | 大小 |
|----------|---------|------|
| seed123_heuristic.json | seed123_heuristic.json.CORRUPTED | 70KB |
| seed123.log | seed123.log.CORRUPTED | 767KB |

**腐败原因**: vLLM 在 task 187/300 时崩溃（17:37:24），先返回 HTTP 500，随后 Connection refused。226 个 APIConnectionError，导致 baseline 仅 50.7%（预期 ~81%）。

Seed 42 结果（seed42_heuristic.json, 89KB）未受影响。Seed 456 从未执行（e2e 目录下无相关文件）。

## 2. 88.6GB 显存根因

**结论: 这是 vLLM 的正常行为，不是加载了错误模型。**

### 实际 vLLM 启动命令（从 /proc/638702/cmdline 提取）

```bash
python3 -m vllm.entrypoints.openai.api_server \
  --model /root/autodl-tmp/models/Llama-3.1-8B-Instruct \
  --port 8001 \
  --max-model-len 4096 \
  --gpu-memory-utilization 0.9 \
  --dtype auto
```

### 为什么占 88.6GB

- **GPU 型号**: NVIDIA RTX PRO 6000 Blackwell，每张 **97887 MiB (~96GB)**，不是 A6000 (48GB)
- **vLLM 内存策略**: `--gpu-memory-utilization 0.9` 让 vLLM 预分配 90% 显存用于 KV cache
- **计算**: 0.9 × 97887 MiB = **88098 MiB**，与实际占用 88638 MiB 吻合
- **模型确认**: Llama-3.1-8B-Instruct（hidden_size=4096, 32 layers, 32 heads, vocab=128256），模型权重 ~16GB，其余 ~72GB 全是 KV cache 预分配空间

### vLLM 崩溃的可能原因

GPU 0 同时运行了另一个项目的 ProtoNet 训练（PID 602618，占用 6052 MiB）：
- vLLM: 88638 MiB
- ProtoNet: 6052 MiB
- **合计: 94690 MiB / 97887 MiB (96.7%)**

在持续推理负载下，CUDA 碎片或临时分配可能触发 OOM → vLLM 返回 500 → worker 进程崩溃 → Connection refused。

父进程 environ 中 **未设 `CUDA_VISIBLE_DEVICES`**（vLLM EngineCore 子进程），但父进程设了 `CUDA_VISIBLE_DEVICES=0`，限制在单卡。

## 3. 正确的 vLLM 启动命令

```bash
# 使用 GPU 1（空闲，无其他进程）
CUDA_VISIBLE_DEVICES=1 python3 -m vllm.entrypoints.openai.api_server \
  --model /root/autodl-tmp/models/Llama-3.1-8B-Instruct \
  --port 8001 \
  --max-model-len 4096 \
  --gpu-memory-utilization 0.85 \
  --tensor-parallel-size 1 \
  --dtype auto
```

**关键改动**:
- `CUDA_VISIBLE_DEVICES=1` → 用空闲的 GPU 1，避免与 GPU 0 上的 ProtoNet 训练冲突
- `--gpu-memory-utilization 0.85` → 0.85 × 96GB = ~82GB，为系统留余量（8B 模型用不完，但 vLLM 会预分配）
- `--tensor-parallel-size 1` → 显式单卡，防止意外跨卡

**预期显存**: ~83GB（0.85 × 97887 MiB），其中模型权重 ~16GB + KV cache ~67GB。如果想节省显存给其他任务，可以进一步降低到 `--gpu-memory-utilization 0.25`（~24GB，对 8B 模型足够）。

## 4. 当前 GPU 状态（2026-04-27 17:49）

| GPU | 型号 | 显存使用 | 温度 | 利用率 | 进程 |
|-----|------|---------|------|--------|------|
| 0 | RTX PRO 6000 Blackwell | 94704/97887 MiB | 66°C | 100% | ProtoNet (6052MB) + vLLM zombie (88638MB) |
| 1 | RTX PRO 6000 Blackwell | 0/97887 MiB | 30°C | 0% | 空闲 |
| 2 | RTX PRO 6000 Blackwell | 0/97887 MiB | 31°C | 0% | 空闲 |
| 3 | RTX PRO 6000 Blackwell | 3771/97887 MiB | 71°C | 89% | ViT 训练 (3762MB) |

**注意**: GPU 0 上的 vLLM（PID 639033）仍在运行但可能已不健康（seed 123 实验期间崩溃过）。重跑实验前应先杀掉这个进程，在 GPU 1 上启动新的 vLLM。
