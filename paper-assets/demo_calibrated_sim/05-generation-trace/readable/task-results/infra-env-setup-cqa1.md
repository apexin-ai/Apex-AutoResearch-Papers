# infra env setup cqa1

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_env-setup-cqa1_20260512T102236_result.json`
- **Structured JSON:** [`e86842b6f43a2bbd42ec.json`](../../sessions/e8/e86842b6f43a2bbd42ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

vLLM 加载成功！需要 `enforce_eager=True` + `TORCHDYNAMO_DISABLE=1` + `VLLM_USE_V1=0` 来绕过 torch.compile 兼容性问题。

模型占用 14.25 GiB，剩余 4.56 GiB KV cache。在单张 RTX 4090 D（24GB）上运行正常。

---

## 环境搭建汇报

### 1. Python/CUDA/PyTorch 版本
| 组件 | 版本 |
|------|------|
| Python | 3.12.3 (conda base) |
| CUDA | 12.8 |
| PyTorch | 2.10.0+cu128 |

### 2. GPU
6x NVIDIA GeForce RTX 4090 D, 各 24GB。指定使用 cuda:2 和 cuda:3。

### 3. 模型
- 路径: `/root/autodl-tmp/models/Qwen/Qwen2___5-7B-Instruct`
- 符号链接: `/root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct`
- 大小: 15GB (4 shards, 3.4-3.7GB each)

### 4. τ-Bench
- 版本: 0.1.0 (editable install at /root/tau-bench)
- import OK: `from tau_bench.envs.retail import MockRetailDomainEnv`
- 注意: 移除了 `mistralai` 依赖（不需要）

### 5. vLLM
- 版本: 0.18.1
- 加载测试: **通过**（需要特定参数，见下方）

### 6. 项目文件
- `/root/democalib/code/behavioral_fingerprint.py` ✓
- `/root/democalib/prompts/base_user_simulator.txt` ✓
- `/root/democalib/prompts/bcp_user_simulator.txt` ✓
- `/root/democalib/prompts/bcp_variants.yaml` ✓
- `/root/democalib/prompts/prompt_loader.py` ✓

### 7. 已知问题
vLLM 0.18.1 + PyTorch 2.10.0 存在 `torch._inductor` 兼容性问题（duplicate template name assertion），启动 vLLM 时需要：
```bash
CUDA_VISIBLE_DEVICES=2 TORCHDYNAMO_DISABLE=1 VLLM_USE_V1=0 python -c "
from vllm import LLM
llm = LLM(model='/root/autodl-tmp/models/Qwen/Qwen2___5-7B-Instruct', 
          tensor_parallel_size=1, gpu_memory_utilization=0.85, enforce_eager=True)
"
```
性能影响：禁用了 CUDAGraph 和 torch.compile 优化，推理速度会比最优配置慢一些，但功能完全正常。

### 磁盘
- 根分区: 30GB (使用 6.6GB)
- 数据盘: 169GB (模型占用 15GB)

---
