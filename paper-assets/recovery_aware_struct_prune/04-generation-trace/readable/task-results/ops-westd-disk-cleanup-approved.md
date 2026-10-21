# ops westd disk cleanup approved

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_disk_cleanup_approved_20260517T193957_result.json`
- **Structured JSON:** [`b0796b2f7846807732a8.json`](../../sessions/b0/b0796b2f7846807732a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理完成汇报

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 已用 | 738G (99%) | 428G (57%) |
| 可用 | 13G | 323G |
| **释放** | — | **310G** |

**删除的目录：**
| 目录 | 大小 |
|------|------|
| `outputs/alpha_ablation/` | 127G |
| `grpo_rasp_qwen_math/` | 38G |
| `grpo_rasp_rlvr_20_qwen_math/` | 38G |
| `grpo_standard_qwen_math/` | 38G |
| `grpo_standard_25_qwen_math/` | 36G |
| `grpo_rasp_25_qwen_math/` | 36G |

**Eval 进程状态：** 3 个 eval 正常运行中
- `eval_postprune_rasp_30` — cuda:2，运行约 80 min
- `eval_postprune_standard_30` — cuda:0，运行约 31 min
- `eval_sft_cka_only_20_n1319` — cuda:0 (排队/共享)，运行约 23 min

4 张 GPU 均在高负载工作（utilization 85-98%）。

---
