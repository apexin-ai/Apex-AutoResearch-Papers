# train deepseek all gpus

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_deepseek-all-gpus_20260516T061139_result.json`
- **Structured JSON:** [`1126021b5d965203943f.json`](../../sessions/11/1126021b5d965203943f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CWM 8B mutation breakdown 数据完整，cuda:3 不需要额外任务。

---

## 执行总结

**Step 1 ✓ — 代码同步**
- `train_unified.py` 已同步到 westd（新增 `--task cls/cwm` 支持）
- eval 脚本后续需要时再同步（文件过大 heredoc 传输受限）

**Step 2 ✓ — DeepSeek 模型确认**
- `/root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct/` 存在，2 个 safetensors 文件

**Step 3 ✓ — 训练数据确认**
| 数据集 | 路径 | 样本数 |
|--------|------|--------|
| repo-level CLS | `data/swebench_full/swebench_train.jsonl` | 70,748 |
| function-level CWM | `data/cwm_train.jsonl` | 15,290 |
| function-level CLS | `data/train.jsonl` | 15,290 |

**Step 5 ✓ — 3 个训练任务已提交**

| GPU | exp_id | Task | Data | Samples |
|-----|--------|------|------|---------|
| cuda:0 | `deepseek-cls-repo` | CLS | swebench_full | 70,748 |
| cuda:1 | `deepseek-cwm-func` | CWM | cwm_train.jsonl | 15,290 |
| cuda:2 | `deepseek-cls-func` | CLS | train.jsonl | 15,290 |

**Step 6 ✓ — CWM 8B mutation breakdown 已完成**
- 9784 samples，coverage=100%
- Per-mutation 结果：gold 80.1%, boundary_removal 42.2%, operator_swap 54.6%, return_value 49.1%, off_by_one 63.4%
- 注意：unparseable rate 极高 (73.8%)，overall acc 65.2% 低于 majority baseline 73.0%

**调整说明**: 原计划 task 2 是"repo-level CWM"，但 swebench 数据无 `target` 字段（只有 `execution_output`），改为 function-level CWM。如需 repo-level CWM 训练，需修改 `get_target()` 读取 `execution_output` 字段。

---
