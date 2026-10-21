# ops gpu audit loop14

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_audit_loop14_20260516T113517_result.json`
- **Structured JSON:** [`85a04ed0b36a3860c944.json`](../../sessions/85/85a04ed0b36a3860c944.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态审计结果

### GPU → 进程映射

| GPU | 显存占用 | 进程 | 实验 | 运行时间 |
|-----|---------|------|------|---------|
| cuda:0 | **0 MiB** | — | — | — |
| cuda:1 | 11406 MiB / 32607 MiB | PID 319638 `freige.eval.inference` | plan_002_test_eval_s44_r2 (test split, rsft_s44/ckpt-510) | 3h22m |
| cuda:2 | 18412 MiB / 32607 MiB | PID 335357 `freige.eval.inference` | plan_006_qwen3_8b_no_evidence_eval_v2 | 18m |
| cuda:3 | 23728 MiB / 32607 MiB | PID 333916 `freige.training.sft_trainer` | plan_016_llama_3_1_8b_no_evidence_sft | 29m |

### 空闲 GPU

**cuda:0** — 完全空闲，可用于新实验。

### 实验状态确认

| 实验 | 状态 | 备注 |
|------|------|------|
| plan_002_test_eval_s44_r2 (PID 319632) | ✅ 运行中 | GPU 1，test split eval |
| plan_016_llama_3_1_8b_sft (PID 331871) | ❌ 已死 | 进程不存在 |
| plan_016_llama_3_1_8b_no_evidence_sft (PID 333911) | ✅ 运行中 | GPU 3，Llama-3.1-8B no-evidence SFT |
| plan_006_qwen3_8b_no_evidence_eval_v2 | ✅ 运行中 | GPU 2，PID 335357 (PPID=1 孤儿进程)，进度 43/247 batches (17%)，~25s/batch，预计剩余 ~85min。正确传了 `--no_evidence` 参数 |

### 异常发现

1. **plan_016_llama_3_1_8b_sft (PID 331871) 已死** — registry 中若仍标记为 RUNNING 则状态不一致，需更新。
2. **plan_006_qwen3_8b_no_evidence_eval_v2 的 PID 335357 是孤儿进程** (PPID=1) — 父进程已退出，但推理进程本身仍正常运行，不影响结果。
3. **plan_002_test_eval_s44_r2 已运行 3.5 小时** — test split eval 时间较长，可能正常（test split 比 dev 大），但值得关注是否卡住。

---
