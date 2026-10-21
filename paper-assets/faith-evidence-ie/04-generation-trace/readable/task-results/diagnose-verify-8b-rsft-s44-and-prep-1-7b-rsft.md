# diagnose verify 8b rsft s44 and prep 1 7b rsft

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_verify_8b_rsft_s44_and_prep_1_7b_rsft_20260518T222733_result.json`
- **Structured JSON:** [`35e90ad949d0741c3473.json`](../../sessions/35/35e90ad949d0741c3473.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认完毕。汇总：

## 产出

### 1. cuda:1 状态：8B RSFT s44 正常运行
- PID 581524 在 cuda:1 上，显存 26944MiB/32607MiB，GPU 利用率 82%
- 全卡均在使用中（4 个 python 进程分别占 cuda:0~3）

### 2. 1.7B RSFT scored data 路径
- `/root/autodl-tmp/freige/outputs/rsft_scored_1_7b_k1/rsft_train.jsonl` (3021 条)
- SFT adapter: `/root/autodl-tmp/sft_output_qwen3_1_7b_bf16`
- 已完成的 s42 RSFT 输出: `/root/autodl-tmp/rsft_output_qwen3_1_7b_k1/`

### 3. 1.7B RSFT seed expansion 脚本（已存在）
- `train_1_7b_s43.sh`: `/root/autodl-tmp/freige/scripts/seed_expansion/train_1_7b_s43.sh`
- `train_1_7b_s44.sh`: `/root/autodl-tmp/freige/scripts/seed_expansion/train_1_7b_s44.sh`

两脚本配置正确：
- base_model: Qwen3-1.7B
- sft_adapter: `/root/autodl-tmp/sft_output_qwen3_1_7b_bf16`
- rsft_data_path: `/root/autodl-tmp/freige/outputs/rsft_scored_1_7b_k1/rsft_train.jsonl`
- batch_size=4, grad_accum=4 (比 8B 大，1.7B 模型显存更小)
- CUDA_VISIBLE_DEVICES 使用 `${GPU:-${CUDA_VISIBLE_DEVICES:-0}}` 模式（符合约束 C002/C003）

8B s44 跑完后 cuda:1 释放，可直接提交 1.7B RSFT s43/s44。

---

关于第二个任务（sync experiment_plan.yaml），需要使用 `read_registry` 和项目知识工具。要继续执行吗？

---
