# exp temp curve expansion gpu01

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_temp-curve-expansion-gpu01_20260518T145009_result.json`
- **Structured JSON:** [`e885b99d0c2f961f2924.json`](../../sessions/e8/e885b99d0c2f961f2924.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务均已启动并正常生成。

**状态报告：**

| 项目 | GPU | 模型路径 | 速度 | 预估完成 |
|---|---|---|---|---|
| OLMo-2-1B (t=0.5 → t=0.9) | GPU 0 | `olmo-2-1b-hf/allenai/OLMo-2-0425-1B` | ~9s/seed | ~5h (约凌晨4点) |
| Qwen3-0.6B (t=0.5 → t=0.9) | GPU 1 | `Qwen/Qwen3-0___6B-Base` | ~14s/seed | ~8h (约凌晨7点) |

**实际执行命令：**
- GPU 0: `generate_chain.py --model-name olmo-2-1b-t05/t09 --model-path .../OLMo-2-0425-1B --temperature 0.5/0.9 --top-p 0.9 --device cuda:0`
- GPU 1: `generate_chain.py --model-name qwen3-0.6b-t05/t09 --model-path .../Qwen3-0___6B-Base --temperature 0.5/0.9 --top-p 0.9 --device cuda:1`

每个 GPU 先跑两个温度的 generation（串行），完成后自动运行 `extract_features.py` 生成特征 CSV。

**注意：** OLMo-2-1B 使用的是 `allenai/OLMo-2-0425-1B`（April 2025 版），原始 `allenai/OLMo-2-1B-hf` 模型文件已被清空。两个温度条件使用同一模型，组内对比有效。

tmux sessions: `temp_olmo`, `temp_qwen06`
日志: `logs/temp_olmo.log`, `logs/temp_qwen06.log`

---
