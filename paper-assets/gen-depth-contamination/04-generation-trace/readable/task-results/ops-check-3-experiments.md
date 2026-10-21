# ops check 3 experiments

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_3_experiments_20260520T113109_result.json`
- **Structured JSON:** [`ec126a8c86217e5b4708.json`](../../sessions/ec/ec126a8c86217e5b4708.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

### 1. exp_olmo_retrain_v3 (cuda:2) — RUNNING
- **进程**: PID 310312, 已运行 43 min, GPU 2 利用率 78%, 显存 3083 MiB
- **当前阶段**: Generation 1→2 的 generation phase, 进度 96% (599/625)
- **已完成**: Gen 0→1 (耗时 ~23 min)
- **剩余**: Gen 1→2 生成即将完成 → Gen 2→3 → Gen 3→4 → scoring
- **预估剩余时间**: ~50-70 min (还有 2 个完整 generation cycle + scoring)
- **K\* 结果**: 待完成

### 2. exp_wiki_multi_source (cuda:0) — FINISHED ✓
- **耗时**: 3498.6s (~58 min)
- **K\* = 1** (所有设置一致)

| 设置 | 0v1 AUC | 1v2 AUC | 2v3 AUC | K* |
|------|---------|---------|---------|-----|
| Vocab-only no_label | 0.7616 | 0.5434 | 0.5170 | 1 |
| Vocab-only with_label | 0.7779 | 0.5520 | 0.5248 | 1 |
| Unified no_label | 0.9603 | 0.5685 | 0.5190 | 1 |
| Unified with_label | **0.9685** | 0.5790 | 0.5299 | **1** |

- **关键发现**: Wiki multi-source K\*=1，低于 Wiki single-source K\*=2 (exp_023)。与 C4 K\*=2, arXiv K\*=3 相比，Wiki 在 multi-source 设置下 domain ceiling 最低。0v1 AUC 极高 (0.97)，但 1v2 迅速衰减到 ~0.58，说明 multi-source 混合后 depth ≥2 的信号几乎消失。

### 3. exp_code_multi_source (cuda:1) — FINISHED ✓
- **耗时**: 2024.9s (~34 min)
- **K\* = 2** (所有设置一致)

| 设置 | 0v1 AUC | 1v2 AUC | 2v3 AUC | K* |
|------|---------|---------|---------|-----|
| Vocab-only no_label | 0.7891 | 0.6353 | 0.5121 | 2 |
| Vocab-only with_label | 0.7900 | 0.6440 | 0.5118 | 2 |
| Unified no_label | 0.9123 | 0.6702 | 0.5013 | 2 |
| Unified with_label | **0.9123** | **0.6803** | 0.5055 | **2** |

- **关键发现**: Code multi-source K\*=2，与 single-source (Qwen7B=2, LLaMA8B=2, Mistral7B=2) 完全一致。Code domain ceiling 稳定在 K\*=2。

### GPU 总览

| GPU | 利用率 | 显存 | 任务 |
|-----|--------|------|------|
| 0 | 0% | 0 MiB | 空闲 (wiki_multi 已完成) |
| 1 | 0% | 0 MiB | 空闲 (code_multi 已完成) |
| 2 | 78% | 3083 MiB | olmo_retrain_v3 运行中 |
| 3 | 0% | 3417 MiB | run_naturalistic_validation.py (11 min, 非你指定的实验) |

### 对你关键问题的回答

1. **OLMo retrain K\***: 还在跑，Gen 1→2 generation 96%，预计 ~1h 后出结果
2. **Wiki multi-source domain ceiling**: K\*=1，**没有**保持 domain ceiling，反而比 single-source (K\*=2) 更低。Multi-source 混合显著压缩了 Wiki 的可检测深度
3. **Code multi-source K\*=2**: 完美保持了 code domain ceiling K\*=2，与 single-source 一致

---
