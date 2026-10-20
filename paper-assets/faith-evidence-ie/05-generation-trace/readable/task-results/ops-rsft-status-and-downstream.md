# ops rsft status and downstream

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_rsft_status_and_downstream_20260516T215928_result.json`
- **Structured JSON:** [`78642e2be87871c439f1.json`](../../sessions/78/78642e2be87871c439f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 分配状态
| GPU | 任务 | 显存 | 进度 |
|-----|------|------|------|
| 0 | Qwen3-1.7B rsft_generate | 13.5/32.6 GB | 2263/3027 (75%) |
| 1 | **Re-DocRED eval r5 (新提交)** | 9.9/32.6 GB | 2/124 batches |
| 2 | LLaMA-3.1-8B rsft_generate | 24.0/32.6 GB | 1889/3027 (62%) |
| 3 | Qwen3-8B rsft_generate | 28.1/32.6 GB | 1871/3027 (62%) |

### RSFT Candidate Gen（均未完成，仍在运行）
- **Qwen3-1.7B**: 75% 完成，预计 ~2-3h 后结束
- **Qwen3-8B**: 62% 完成，预计 ~5h 后结束
- **LLaMA-3.1-8B**: 62% 完成，预计 ~5h 后结束

### 已提交
- **plan_007_redocred_rsft_eval_r5** (GPU 1, PID 384691): 模型加载成功（base→SFT→RSFT 三层），正在推理 re-docred dev (493 docs, 124 batches, ~43s/batch ≈ 1.5h)

### 待办（candidate gen 完成后）
- Step 3 CED scoring 需等至少一个 candidate gen 完成。最快的是 Qwen3-1.7B (~2-3h)。届时 eval r5 应已结束释放 GPU 1，可用于 scoring。

---
