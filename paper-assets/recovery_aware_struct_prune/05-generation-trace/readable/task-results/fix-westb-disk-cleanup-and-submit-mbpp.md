# fix westb disk cleanup and submit mbpp

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westb_disk_cleanup_and_submit_mbpp_20260519T185248_result.json`
- **Structured JSON:** [`f866766368abefe5a551.json`](../../sessions/f8/f866766368abefe5a551.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

## 磁盘清理报告

| 项目 | 清理前 | 清理后 |
|------|--------|--------|
| 数据盘使用 | 250G / 250G (100%, 159MB free) | 224G / 250G (90%, **27G free**) |
| 清理内容 | `grpo_cka_only_20_seed123/checkpoint-100/` (27G) — 中间训练 checkpoint，含 optimizer.pt 15G + 重复 model.safetensors 12G。最终模型在父目录保留完好 | |

其他检查项：
- `__pycache__` / `.pyc` / `.tmp`：无
- `/root/.cache/huggingface/`：140MB（根分区，不占数据盘）
- `/root/autodl-tmp/.hf_cache/`：46MB（可忽略）
- `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B/`：15G（7B 基座模型，脚本引用中，未删）

## 实验提交确认

| 字段 | 值 |
|------|---|
| exp_id | `eval_mbpp_sft_standard_20_1p5b` |
| server | westb-23072, GPU 0 |
| tmux session | `eval_mbpp_sft_standard_20_1p5b` (**ALIVE**) |
| PID | 917409 |
| registry | RUNNING |

当前 westb-23072 两个 eval 并行运行：
- **GPU 0**: `eval_mbpp_sft_standard_20_1p5b` (PID 917409)
- **GPU 1**: `eval_mbpp_sft_cka_only_20_1p5b` (PID 916225, 已运行 ~12min)

---
