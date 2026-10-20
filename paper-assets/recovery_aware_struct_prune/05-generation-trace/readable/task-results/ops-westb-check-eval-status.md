# ops westb check eval status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_check_eval_status_20260517T130648_result.json`
- **Structured JSON:** [`4a055b39673f828d2d4b.json`](../../sessions/4a/4a055b39673f828d2d4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 CKA eval 的输出文件尚不存在，仍在运行中。

## 汇总

| PID | 任务 | 状态 | 进度/结果 |
|-----|------|------|-----------|
| **680597** | eval_unstructured_20 (n=1319) → cuda:1 | **已完成** ✓ | accuracy=**87.87%** (1159/1319), stderr=0.009 |
| **710618** | eval_cka_only_20 (n=200) → cuda:0 | 运行中 | **72% (143/200)**，已跑 1h37m，预估剩余 ~40min |
| **715803** | eval_postprune_cka_only_20 (n=200) → cuda:0 | 运行中 | 已跑 38m，输出文件未生成，预估 ~50% |

### 已完成结果：eval_unstructured_20_n1319.json

```
model:     pruned_unstructured_20
accuracy:  87.87% (1159/1319)
stderr:    0.90%
mode:      greedy (T=0, no sampling)
eos_rate:  98.0% (26/1319 truncated)
avg_resp:  641 tokens
```

### GPU 状态

| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| cuda:0 | RTX PRO 6000 Blackwell | 72% | 13.0/97.9 GB |
| cuda:1 | RTX PRO 6000 Blackwell | 76% | 13.0/97.9 GB |

注意：cuda:1 利用率 76% 但 PID 680597 的 eval 已完成——可能有其他进程在用 cuda:1，或者 tmux session 内有后续任务启动。PID 710618 和 715803 都在 cuda:0 上并行跑（两个都加载了完整模型到 GPU，共用 cuda:0 显存约 13GB 总计合理，因为它们评估同一个模型路径 `pruned_cka_only_20`）。

两个 CKA eval 预计还需 30-50 分钟完成。

---
