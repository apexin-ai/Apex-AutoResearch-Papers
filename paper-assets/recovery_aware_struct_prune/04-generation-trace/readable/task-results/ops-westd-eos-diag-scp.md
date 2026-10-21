# ops westd eos diag scp

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_eos_diag_scp_20260516T110317_result.json`
- **Structured JSON:** [`8c62ffc5ca30d39cdcd2.json`](../../sessions/8c/8c62ffc5ca30d39cdcd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

westd-11672 完全不可达。可能是磁盘满导致实例崩溃或 AutoDL 自动重启（端口会变）。

---

## 诊断报告

### 1. EOS Token 诊断 — **根因确认**

| | SFT Model | Base (generation_config) |
|---|---|---|
| eos_token | `<|endoftext|>` | `<|endoftext|>` |
| eos_token_id | 151643 | 151643 |
| **`<|im_end|>` (151645)** | **不在 eos_token_id 中** | **不在 eos_token_id 中** |

**病因**: eval 脚本用 `apply_chat_template` 构建 prompt（格式为 `<|im_start|>user\n...<|im_end|>\n<|im_start|>assistant\n`），模型学会了在回答结束时生成 `<|im_end|>` (151645)，但 `generation_config.json` 的 `eos_token_id` 只有 `[151643]`（`<|endoftext|>`）。`model.generate()` 不会在 `<|im_end|>` 处停止，导致每个 sample 都生成满 max_new_tokens (4096) 个 token。

**所有模型都受影响**：sft_qwen_math_rasp_20、sft_qwen_math_standard_20、pruned_rasp_rlvr_20 的 generation_config 均只有 151643。

**修复方案**（二选一）：
- **A**：修改 eval 脚本，在 `gen_kwargs` 中显式传 `eos_token_id=[151643, 151645]`
- **B**：修改每个模型的 `generation_config.json`，在 `eos_token_id` 中加入 151645

### 2. N=50 快速 Eval — **未完成**

eval 启动成功，进度 ~7/50（12s/it），但服务器在 ~19:09 后失联，可能磁盘满导致 AutoDL 实例崩溃/重启。

### 3. SCP 测速 — **双向不通**

| 方向 | 结果 |
|---|---|
| westd → westb | Permission denied（SSH key 未配置） |
| westb → westd | Permission denied（SSH key 未配置） |

两台服务器间无法直接 SCP，模型传输需要通过中间节点或其他方式（如共享存储/HuggingFace Hub）。

### 4. 磁盘状态（失联前）

- `/root/autodl-tmp`: 246G/250G（99%，仅 4.2G 剩余）
- 最大占用：`grpo_unpruned_v2` (46G)，可考虑清理
- 建议下次连接后优先清理不需要的模型释放空间

### 下一步

1. 用户需到 AutoDL 控制台检查 westd-11672 状态，如已重启则获取新 SSH 端口
2. 恢复连接后先清理磁盘（建议删除 `grpo_unpruned_v2` 释放 46G）
3. 修复 EOS 问题后重跑 eval

---
