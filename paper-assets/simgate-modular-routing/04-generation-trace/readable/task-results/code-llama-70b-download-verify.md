# code llama 70b download verify

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama-70b-download-verify_20260523T234706_result.json`
- **Structured JSON:** [`58a107d7238538d1ae8a.json`](../../sessions/58/58a107d7238538d1ae8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**总结：**
- **下载**：首次下载缺失 model-00002、model-00008 等文件，补运行 `snapshot_download` 后修复，9/9 safetensors + 全部配置文件齐全，共 38GB
- **vLLM**：经过 4 次尝试（前 3 次因残留进程占 GPU 或 CUDA graph 冲突失败），最终用 `--enforce-eager --gpu-memory-utilization 0.85 --quantization awq_marlin` 成功启动，端口 8002，占用 83.6GB/97.9GB GPU 内存
- **推理测试**：通过，回答正确
- **Episode 脚本**：现有脚本针对 Qwen-72B，使用 vLLM Python API 直接加载，不走 HTTP。如需用 Llama-70B 收集 episodes 需修改 `--model_path`
- **vLLM 进程保持运行**

---
