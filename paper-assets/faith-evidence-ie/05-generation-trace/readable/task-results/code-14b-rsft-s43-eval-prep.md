# code 14b rsft s43 eval prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_14b-rsft-s43-eval-prep_20260523T145359_result.json`
- **Structured JSON:** [`0e2f6bcb50cdc3ea1ac8.json`](../../sessions/0e/0e2f6bcb50cdc3ea1ac8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 已在运行，模型已加载到 GPU。

**总结：**

| 项目 | 详情 |
|------|------|
| **训练** | `plan017_14b_rsft_s43_train` — DONE (567 steps, 1h06m, loss=0.5076) |
| **with-evi eval** | `plan017_14b_rsft_s43_eval` — RUNNING on cuda:0, PID 260780 |
| **no-evi eval** | `plan017_14b_rsft_s43_no_evi_eval` — RUNNING on cuda:2, PID 260930 |
| **batch_size** | 1（与 s42 eval 一致） |
| **SFT adapter** | `/root/autodl-tmp/sft_output_14b_s43` |
| **RSFT adapter** | `/root/autodl-tmp/rsft_output_14b_s43` |
| **Cron 监控** | 已注册，300s 间隔 |

s42 dev eval 的 14B 推理耗时约 5.3h（19086s, 500 docs test set）。dev set 有 985 docs，预计需要约 10h。

---
