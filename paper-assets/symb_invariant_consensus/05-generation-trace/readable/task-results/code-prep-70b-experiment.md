# code prep 70b experiment

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-70b-experiment_20260518T063344_result.json`
- **Structured JSON:** [`65cc237bd06bbf7fc744.json`](../../sessions/65/65cc237bd06bbf7fc744.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已部署。以下是完整审查报告。

---

## exp-024 代码审查报告

### 1. 多 GPU 支持状态

**结论：Pipeline 完全兼容多 GPU，无需代码修改。**

- Pipeline 通过 HTTP API (`localhost:8000/v1`) 连接 vLLM，与 GPU 拓扑解耦
- `VLLMGenerator` 和 `VLLMBackend` 均使用 OpenAI-compatible API client，无 GPU 相关代码
- 只需在 vLLM 启动命令添加 `--tensor-parallel-size 2`
- 无 `CUDA_VISIBLE_DEVICES` 硬编码（exp-011/exp-020 脚本均无此设置）
- vLLM 0.20.2 原生支持 tensor parallel

### 2. 脚本产出

`/root/symb_invariant_consensus/scripts/run_exp024_llama70b.sh` (147行, 755权限)

基于 exp-011/exp-020 脚本模式，关键差异：

| 参数 | 7B/14B 实验 | 70B 实验 |
|---|---|---|
| tensor-parallel-size | (无，单GPU) | 2 |
| gpu-memory-utilization | 0.90 | 0.95 |
| K | 12 | 10 |
| vLLM 启动超时 | 180s | 600s |
| max-model-len | 8192 | 8192 |
| max-tokens | 4096 | 4096 |

### 3. 数据可用性

| 数据集 | 文件 | 题数 | 状态 |
|---|---|---|---|
| FOLIO | `data/folio_full.json` | 204 | OK |
| ProofWriter | `data/proofwriter_full.json` | 600 | OK |
| 空占位 | `data/empty.json` | 0 | OK |

### 4. vLLM 版本

- **版本**: 0.20.2 (支持 tensor parallel, json_object response format)
- **入口**: `python -m vllm.entrypoints.openai.api_server` (与现有脚本一致)

### 5. 模型下载

**70B 模型尚未在服务器上。** `/root/autodl-tmp/models/` 现有模型：
- Llama-3.1-8B-Instruct, DeepSeek-R1-Distill-Llama-8B, Mistral-7B, Qwen2.5-14B, Qwen2.5-7B, QwQ-32B, Qwen3-32B-AWQ

GPU 到位后需先下载：
```bash
source /etc/network_turbo 2>/dev/null || true
export HF_HOME=/root/autodl-tmp/.hf_cache
huggingface-cli download meta-llama/Llama-3.1-70B-Instruct \
    --local-dir /root/autodl-tmp/models/Llama-3.1-70B-Instruct
```
预估下载大小：~140GB (FP16)。确认 autodl-tmp 有足够磁盘空间。

### 6. 资源估算

- LLaMA-3.1-70B FP16: ~140GB VRAM
- 2×A100-80G = 160GB, `gpu-memory-utilization=0.95` → 152GB 可用
- KV cache 预算: ~12GB → max-model-len=8192 时约 4 并发序列
- K=10 并发请求会被 vLLM 自动排队，不影响正确性
- 如果 VRAM 紧张 (OOM)，备选方案:
  - 降 `--gpu-memory-utilization 0.90` (减少 KV cache 但更稳定)
  - 降 `--max-model-len 4096` (增加并发但可能截断长 trace)
  - 使用 AWQ 量化版 `meta-llama/Llama-3.1-70B-Instruct-AWQ` + `--quantization awq` (~35GB, 单 A100 即可)

### 7. 温度配置

- Trace generation: T=0.7 (从 `--temperature` 参数传入 `VLLMGenerator`)
- Constraint extraction: T=0.1 (硬编码在 `sica/constraint_extractor.py:VLLMBackend.call()`)
- 与 14B expanded 实验一致，无需修改

### 8. 启动命令

GPU 到位 + 模型下载完成后：
```bash
nohup bash /root/symb_invariant_consensus/scripts/run_exp024_llama70b.sh \
    > /tmp/exp024.log 2>&1 &
```

---
