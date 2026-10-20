# diagnose inference speedup plan016

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_inference_speedup_plan016_20260516T213037_result.json`
- **Structured JSON:** [`f367de7eb1995f30c22b.json`](../../sessions/f3/f367de7eb1995f30c22b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 失败根因：模型权重 shape mismatch（代码 bug）

`sft_rasp_20` 的剪枝后 checkpoint 权重维度与 `AutoModelForCausalLM.from_pretrained` 默认初始化的全尺寸模型不匹配，且未设置 `ignore_mismatched_sizes=True`。

### 关键错误信息

```
Qwen2ForCausalLM LOAD REPORT from: /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20
model.layers.{0...27}.mlp.up_proj.weight   | MISMATCH | ckpt: torch.Size([8128, 3584]) vs model:torch.Size([18944, 3584])
model.layers.{0...27}.mlp.down_proj.weight | MISMATCH | ckpt: torch.Size([3584, 9480]) vs model:torch.Size([3584, 18944])
model.layers.{0...27}.mlp.gate_proj.weight | MISMATCH | ckpt: torch.Size([11508, 3584]) vs model:torch.Size([18944, 3584])

RuntimeError: You set `ignore_mismatched_sizes` to `False`, thus raising an error.
```

崩溃位置：`benchmark_inference.py:18` 的 `AutoModelForCausalLM.from_pretrained()`

### 已完成部分

- Dense 模型 (`DeepSeek-R1-Distill-Qwen-7B`) benchmark **已完成**（50 prompts 全部跑完）
- 崩溃发生在加载第二个模型 `rasp_20` 时

### 环境状态

- tmux session 已不存在（进程已退出）
- 无 OOM kill 记录
- GPU cuda:1 空闲（0MiB），cuda:0 被其他进程占用

### 修复方案

`sft_rasp_20` 是结构剪枝后的模型，MLP 层维度已缩小。不能用原始 `config.json`（对应全尺寸模型）直接 `from_pretrained`。需要修改 `benchmark_inference.py` 的加载逻辑：

**方案 A**（推荐）：确保 `sft_rasp_20/config.json` 中的 `intermediate_size` 已更新为剪枝后的实际尺寸。如果该 checkpoint 是用自定义加载逻辑保存的，需要同步更新 config。

**方案 B**：在 `from_pretrained` 中加 `ignore_mismatched_sizes=True`，但这会导致不匹配的层被随机初始化，推理结果无意义。**不推荐。**

**方案 C**：使用项目自身的剪枝模型加载函数（可能在 `src/` 中已有），替代直接调用 `AutoModelForCausalLM.from_pretrained`。

需要确认：`sft_rasp_20` 的保存方式是怎样的？如果每层剪枝比例不同（从 log 看 up_proj=8128, gate_proj=11508, down_proj 输入=9480），则 config.json 无法用单一 `intermediate_size` 描述，必须用自定义加载逻辑。

---
