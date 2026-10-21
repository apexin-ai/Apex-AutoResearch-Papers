# ssh 7b inference status check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_7b-inference-status-check_20260520T033207_result.json`
- **Structured JSON:** [`5eb31ed58661d26bca85.json`](../../sessions/5e/5eb31ed58661d26bca85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 7B FewNERD 3-Seed 推理状态

### 推理进度

| Seed | 服务器 | GPU | 进度 | 已用时间 | 预计剩余 |
|------|--------|-----|------|----------|----------|
| 42 | 5090-c | cuda:2 | **92.1%** (277,304/301,184) | 1h18m | ~7 min |
| 123 | 5090-b | cuda:0 | **50.8%** (153,088/301,184) | 43m | ~35 min |
| 456 | 5090-b | cuda:1 | **50.8%** (152,920/301,184) | 43m | ~35 min |

- 每个 seed: 37,648 test instances × 8 samples = 301,184 prompts
- 推理速度: ~60-90 it/s (vLLM v0.18.1, chunked prefill)
- **seed42 预计 ~11:40 CST 完成（可能已完成），seed123/456 预计 ~12:10 CST 完成**

### 输出文件

目录已创建但当前为空（vLLM batch 完成后才写入）：
- `5090-c: output/fewnerd_7b/qwen25_7b_n8_seed42/`
- `5090-b: output/fewnerd_7b/qwen25_7b_n8_seed123/`
- `5090-b: output/fewnerd_7b/qwen25_7b_n8_seed456/`

### Pipeline 后续步骤 (`run_fewnerd_qwen25_7b_pipeline.sh`)

| Phase | 内容 | 状态 | 自动/手动 |
|-------|------|------|-----------|
| 1 | QLoRA Training | ✅ Done | - |
| 2 | Export/Merge LoRA | ✅ Done | - |
| 3 | Inference (3 seeds × N=8) | 🔄 In progress | 自动(seed42在pipeline内) |
| 4 | Signal Analysis (`analyze_fewnerd_results.py`) | ⏳ Pending | seed42自动, seed123/456需**手动** |
| 5 | Entity Construction (`wnut17_entity_construction.py`) | ⏳ Pending | seed42自动, seed123/456需**手动** |

**注意**: Pipeline 脚本只在 5090-c 上顺序执行 3 个 seed。实际 seed123/456 被单独派发到 5090-b，因此 Phase 4/5 需要手动对 seed123/456 运行分析和 entity construction。

### 14B 相关状态

**14B FewNERD 训练 (5090-c GPUs 0,1)**:
- 进度: **65.5%** (26,984/41,180 steps), epoch 3.27/5
- 速度: ~2.15 s/it
- 预计剩余: **~8.7 小时** (ETA ~20:00 CST)

**14B 模型预下载 (5090-b)**:
- 路���: `/root/autodl-tmp/models/Qwen2.5-14B-Instruct/`
- 状态: **不完整** — 仅 4/8 safetensors shards 已下载，有 `.incomplete` 文件
- Shards 1-4 已下载，5-8 缺失，下载似乎已中断

### 附加发现: 32B FewNERD 训练 (autodl-5090 主机)

- 进度: **47.4%** (19,503/41,180 steps), epoch 2.37/5
- 速度: ~2.5 s/it, 4 GPU
- 预计剩余: **~15 小时** (ETA ~02:30 CST May 21)

---
