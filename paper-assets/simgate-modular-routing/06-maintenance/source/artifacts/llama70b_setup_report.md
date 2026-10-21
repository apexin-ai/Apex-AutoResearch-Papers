# Llama-70B-AWQ Setup Report

**时间**: 2026-05-24 08:03 UTC+8
**服务器**: westd-18266

## 1. 下载结果：成功

| 项目 | 值 |
|------|-----|
| 模型 | Meta-Llama-3.1-70B-Instruct-AWQ-INT4 |
| 来源 | ModelScope (LLM-Research) |
| Safetensors | 9/9 完整 |
| config.json | ✅ |
| tokenizer.json | ✅ |
| tokenizer_config.json | ✅ |
| model.safetensors.index.json | ✅ |
| 总大小 | 38G |
| 路径 | `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4/` |

注：首次下载完成时缺少 model-00002、model-00008、config.json 等文件，补运行一次 `snapshot_download` 后修复。

## 2. vLLM 状态：运行中

| 项目 | 值 |
|------|-----|
| PID | 189727 (bash) → 189733 (APIServer) → 190003 (EngineCore) |
| 端口 | 8002 |
| 量化 | awq_marlin |
| max-model-len | 4096 |
| gpu-memory-utilization | 0.85 |
| enforce-eager | 是（跳过 CUDA graph 避免启动失败） |
| GPU | cuda:0, NVIDIA RTX PRO 6000 Blackwell (98GB) |
| GPU 内存占用 | 83,571 MiB / 97,887 MiB (85.4%) |
| vLLM 版本 | 0.21.0 |

启动过程踩坑：
- 第 1 次：`gpu-memory-utilization=0.9` + `quantization=awq` → 前次残留进程占 GPU 内存，ValueError
- 第 2 次：awq_marlin → 同样因残留进程失败
- 第 3 次：清理干净 + `gpu-memory-utilization=0.85` → CUDA graph profiling 时两个 EngineCore 冲突，AssertionError
- 第 4 次：清理 + `--enforce-eager` → 成功

## 3. 推理测试：通过

```
请求: "What is 2+2? One word."
响应: "Four."
延迟: ~0.55s（首次请求含 JIT 预热后约 30s）
```

## 4. Episode 脚本分析

### 现有 vLLM 脚本
- `auto_start_vllm.sh`: Qwen2.5-7B-Instruct on GPU 2/3, ports 8000/8001
- `auto_start_vllm2.sh`: 同上（备用启动脚本）

### Episode 收集脚本
- `src/run_72b_parallel.py`: 72B episode 收集，使用 **vLLM Python API 直接加载**（非 HTTP API），默认模型 `/root/autodl-tmp/models/Qwen/Qwen2.5-72B-Instruct-AWQ`
- `scripts/run_72b_episodes.sh`: 调用 `episode_level_collection.py`，同样直接加载模型
- `src/run_episodes.py`: **不存在**

### 注意
- Episode 脚本使用 `from vllm import LLM, SamplingParams` 直接加载模型，不走 HTTP API
- 如需用 Llama-70B 收集 episodes，需修改脚本的 `--model_path` 参数
- 当前没有针对 Llama-70B 或 port 8002 的 episode 脚本
- 相关文件：`find` 返回 `src/run_72b_parallel.py`、`scripts/run_72b_episodes.sh`、`src/check_72b_progress.sh`

## 5. 当前状态

vLLM 在 port 8002 正常服务，进程保持运行。
