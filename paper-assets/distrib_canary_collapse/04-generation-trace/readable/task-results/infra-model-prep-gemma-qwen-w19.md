# infra model prep gemma qwen w19

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_model_prep_gemma_qwen_w19_20260518T173646_result.json`
- **Structured JSON:** [`ebba7135fe5c4bd6703f.json`](../../sessions/eb/ebba7135fe5c4bd6703f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. 模型下载状态

| 模型 | 状态 | 大小 | 路径 |
|------|------|------|------|
| Qwen/Qwen3.5-0.8B-Base | 完成 | 1.7G (safetensors) | `/root/autodl-tmp/models/Qwen3.5-0.8B-Base/` |
| google/gemma-4-E2B | 完成 | 9.6G (safetensors) | `/root/autodl-tmp/models/gemma-4-E2B/` |

### 2. GPU 状态 & Dry-run

| GPU | 显存使用 | 利用率 | 运行进程 |
|-----|----------|--------|----------|
| 0 | 32083/97887 MiB | 79% | pythia-1.4b a050_s42 训练 |
| 1 | 14765/97887 MiB | 49% | 另一训练进程 |

**Dry-run 结果**（均在 GPU 1 执行）：
- **Qwen3.5-0.8B-Base**: 0.75B params, vocab 248044, forward pass OK
- **Gemma 4 E2B**: 5.10B params（实际比名称暗示的大得多，多模态 text+vision+audio），vocab 262144, forward pass OK

### 3. 磁盘空间

250G 总量，175G 已用，76G 可用（70%）

### 注意事项
- **transformers 升级到 5.8.1**（原 4.57.6 不支持 `qwen3_5` 和 `gemma4` model type）。副作用：vllm 0.18.1 有依赖冲突 (`transformers<5`)
- transformers 5.8.1 中 `torch_dtype` 参数已改名为 `dtype`
- Gemma 4 E2B 实际 5.10B params，safetensors 9.6G，加载到 GPU 约需 10G VRAM

---
