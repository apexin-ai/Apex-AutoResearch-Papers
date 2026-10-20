# ops gpu conflict diagnosis

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_conflict_diagnosis_20260515T160222_result.json`
- **Structured JSON:** [`ea7b44cc141c82b60faf.json`](../../sessions/ea/ea7b44cc141c82b60faf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### GPU 占用与进程状态

| GPU | 显存占用 | GPU利用率 | 进程 | PID | 运行时间 | 状态 |
|-----|---------|----------|------|-----|---------|------|
| cuda:0 | 18042 MiB / 32607 MiB (55%) | 89% → 恢复正常 | **plan_001_rsft_flat_nli** | 219556 (子进程 219561) | 21m46s | ✅ 正常运行 |
| cuda:0 | ~~13304 MiB~~ → 已释放 | - | ~~plan_015_grpo_g4_bf16~~ | ~~222937~~ | - | ❌ 已 kill |
| cuda:1 | 14628 MiB / 32607 MiB (45%) | 43% | **plan_014_sft_no_evidence** | 222207 (子进程 222212) | 6h35m | ✅ 正常运行 |
| cuda:2 | 28816 MiB / 32607 MiB (88%) | 73% | **plan_012_dpo_ced** | 221962 (子进程 221967) | 6h42m | ✅ 正常运行 |
| cuda:3 | 16524 MiB / 32607 MiB (51%) | 88% | **eval_grpo_g8_bf16** | 214552 (子进程 220202) | 1d21h36m | ✅ 正常运行 |

### 处理结果

- **plan_015_grpo_g4_bf16** (PID 222937) 已终止，registry 已更新为 DONE/killed
- cuda:0 冲突已解除，plan_001 现在独占 GPU 0，显存从 96% 降至 ~55%
- 其余 3 个任务健康运行，GPU 利用率正常
- **plan_015 待 plan_001 完成后重新提交到 cuda:0**

---
