# fix exp012 flashinfer

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp012_flashinfer_20260515T145622_result.json`
- **Structured JSON:** [`3939f12cdfdf2f315dd7.json`](../../sessions/39/3939f12cdfdf2f315dd7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**已完成的修复：**
1. **flashinfer 升级**: 0.6.8.post1 → 0.6.11.post2（使用 `--no-deps` 避免覆盖 torch 2.11.0+cu130）
2. **nvidia-cuda-nvcc 安装**: 13.2.78（提供 SM120 Blackwell 架构支持的 nvcc）
3. **脚本更新** `scripts/run_exp012_llama.sh`:
   - 删除无效的 `export VLLM_ATTENTION_BACKEND=FLASH_ATTN`
   - 添加 `export CUDA_HOME=/root/miniconda3/lib/python3.12/site-packages/nvidia/cu13`

**未验证加载**：GPU 显存几乎占满（仅 2.42/94.97 GiB 可用），无法执行 vLLM 加载测试。待 GPU 上当前任务结束后可验证。

---
