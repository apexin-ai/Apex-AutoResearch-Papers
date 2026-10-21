# fix output path and check alpha4

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_output_path_and_check_alpha4_20260521T173538_result.json`
- **Structured JSON:** [`71715046ca03fc517ef0.json`](../../sessions/71/71715046ca03fc517ef0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复已生效。汇报结果：

---

## 1. α=4.0 pipeline 状态：已死

- **PID 396205 已不存在**
- **死因**：`No space left on device (os error 28)` — 数据盘 `/root/autodl-tmp` 已 100% 满（619G/619G，仅剩 212K）
- 剪枝本身成功完成（actual sparsity 19.09%，target 20%，200 MLP groups pruned），但在保存模型到 `/root/autodl-tmp/recovery_aware_struct_prune/pruned_alpha4_20` 时 safetensors 写入失败
- **需要清理数据盘腾出空间后重启 pipeline**

GPU 当前状态：
| GPU | 状态 | 占用进程 |
|-----|------|---------|
| 0 | 空闲 (0MiB) | - |
| 1 | 97% util, 17369MiB | PID 382472 (eval grpo_random_20_v2) |
| 2 | 空闲 (0MiB) | - |
| 3 | 98% util, 16049MiB | PID 385685 (eval sft_random_20) |

## 2. output_path bug 修复

**根因**：脚本 `open(args.output_path, "w")` 直接用传入的路径写文件，但调用方传了目录路径（如 `eval_math500_grpo_random_20_v2`）而非文件路径，触发 `IsADirectoryError`。

**当前在跑的 eval**：
- PID 382472：`--output_path .../eval_math500_grpo_random_20_v2` — **是目录，会踩 bug**（但已在内存中运行，本次修复不影响它）
- PID 385685：`--output_path .../eval_math500_sft_random_20/results.json` — 文件路径，没问题

**修复内容**（第 218-220 行）：在 `os.makedirs` 前加了 defensive check——如果 `output_path` 是已存在的目录或以 `/` 结尾，自动追加 `eval_math500_{model_name}.json` 文件名。未来的 eval 调用不会再踩这个 bug。

---
