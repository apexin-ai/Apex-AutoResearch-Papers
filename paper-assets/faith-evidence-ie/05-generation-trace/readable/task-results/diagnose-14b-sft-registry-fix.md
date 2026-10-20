# diagnose 14b sft registry fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_14b_sft_registry_fix_20260519T065038_result.json`
- **Structured JSON:** [`9bafb42e26c66d21062a.json`](../../sessions/9b/9bafb42e26c66d21062a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已修正。汇报：

**nvidia-smi GPU 占用：**
| GPU | PID | 进程 | 显存 |
|-----|-----|------|------|
| cuda:0 | 613083 | d112_rsft_s44_train | 29630 MiB |
| cuda:1 | 611578 | **plan017_14b_sft** (worker 0) | 16130 MiB |
| cuda:2 | 611579 | **plan017_14b_sft** (worker 1) | 25158 MiB |
| cuda:3 | 620737 | plan019_1_7b_rsft_s43_r2_eval | 5380 MiB |

**Registry 修正内容：**
- 原 spec 使用 `gpu_ids: ["cuda:1", "cuda:2"]`（非标准字段），系统无法识别 GPU 注册
- 已改为 `gpu: "cuda:1,cuda:2"`（标准字段），`pid: 611578`（整数）
- 其余字段保留不变

**训练进度：**
- Step 125 / 144（87%），epoch 2.51
- 最新 loss: 0.5385（step 120），mean_token_accuracy: 0.864
- 预计剩余约 21 分钟（19 steps × ~67s/step）

---
