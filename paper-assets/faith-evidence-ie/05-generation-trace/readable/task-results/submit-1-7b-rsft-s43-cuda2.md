# submit 1 7b rsft s43 cuda2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_1_7b_rsft_s43_cuda2_20260519T024940_result.json`
- **Structured JSON:** [`aaf28c62d3b0e023f4fc.json`](../../sessions/aa/aaf28c62d3b0e023f4fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已注册为 RUNNING。

**汇报：**

| 项目 | 值 |
|---|---|
| exp_id | `plan019_1_7b_rsft_s43` |
| PID | 601718 |
| GPU | cuda:2 (24088MiB / 32607MiB) |
| tmux session | `plan019_1_7b_rsft_s43` |
| 数据 | 3021 条 RSFT samples |
| 输出 | `/root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s43` |
| 预估训练时间 | ~20-30 分钟（1.7B 模型 + 3021 samples × 3 epochs, batch 4 × grad_accum 4） |

注意：tee 日志写入失败（logs 目录当时不存在），但训练本身正常运行。可通过 `tmux attach -t plan019_1_7b_rsft_s43` 查看实时输出。

---
