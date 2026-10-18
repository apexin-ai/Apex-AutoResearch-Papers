# ssh exp1 status check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp1-status-check_20260514T193750_result.json`
- **Structured JSON:** [`2db09f6227e014aa8cf1.json`](../../sessions/2d/2db09f6227e014aa8cf1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Exp 1 状态汇报

### 1. Exp 1 PID
**PID 188307** — vLLM EngineCore 进程，正在运行。

### 2. GPU 状态
| GPU | 型号 | 显存占用 | GPU 利用率 |
|-----|------|----------|-----------|
| 0 | NVIDIA RTX PRO 6000 Black | 94,221 / 97,887 MiB (96%) | 15% |

Driver 590.44.01, CUDA 13.1。唯一 GPU 进程就是 vLLM::EngineCore (PID 188307)。

### 3. vLLM 版本
**v0.20.2**（从 log 中确认：`Initializing a V1 LLM engine (v0.20.2)`）

### 4. 模型路径
`/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/` — Qwen3ForCausalLM, FP8 量化, max_model_len=4096, gpu_memory_utilization=0.95

### 5. Exp 1 进度
- 已启动 **4 个 batch**，全部是 `count_1_random_*`（1 type, BCS=0.0000），每 batch 1000 samples
- Batch 0: 03:34:24 开始
- Batch 1: 03:35:17 开始
- Batch 2: 03:36:39 开始 → 03:37:40 完成（60.4s）
- **Batch 3 (count_1_random_3): 正在推理中**，进度 ~99%（998/1000 prompts processed）
- 尚无 SUMMARY 输出 → 实验仍在进行中
- 推理速度：~2300 toks/s input, ~211 toks/s output（尾部 long-tail 样本拖慢了速度）

### 6. BCS Heatmap
- `type_embeddings.pt` 已生成（684 KB, May 15 02:13）
- `heatmap.pdf` 已生成（在 `/root/schema-dag-extraction/data/`）
- 未发现 PNG 或其他 bcs/similarity 文件

### 7. 结果目录
`/root/schema-dag-extraction/results/exp1/` — **空目录**，尚无结果输出（实验还在跑）。

---
