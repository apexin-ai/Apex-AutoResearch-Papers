# ops westd full eval setup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-full-eval-setup_20260515T162120_result.json`
- **Structured JSON:** [`0370c04d441fc15b6f79.json`](../../sessions/03/0370c04d441fc15b6f79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

### 1. 模型路径
**两个模型在 westd 上均不存在：**
- `sft_rasp_20/` — **缺失**
- `sft_standard_20/` — **缺失**
- `sft_standard_20_retrain/` — **缺失**

westd 上已有的目录：`alpha_ablation`, `pruned_graspune_20`, `pruned_rasp_20`, `pruned_standard_20`, `sft_ablation`, `sft_graspune_20`

### 2. eval 链状态
westd 上**无 tmux session、无 eval 进程**——之前的三条 eval 链已全部完成，cuda:0 和 cuda:1 空闲可用。

### 3. 传输评估
| 项目 | 数据 |
|------|------|
| westb `sft_rasp_20/model.safetensors` | 12.3 GB |
| westb `sft_standard_20/model.safetensors` | 12.3 GB |
| 含 checkpoint 的完整目录 | 各 81 GB（不需要传 checkpoint） |
| 仅传必要文件（model + config + tokenizer） | ~12.3 GB × 2 ≈ 24.6 GB |
| westd `/root/autodl-tmp/` 可用空间 | 46 GB ✓ |
| **westb → westd 直连** | **不通**（SSH Permission denied） |

### 4. eval 参数确认
`eval_gsm8k.py` 的 `--max_samples` 参数：`None=all`，不传该参数即使用全部样本（N=1319）。

### 需要决策
westb 无法直连 westd，模型传输需要中继方案。选项：
1. **通过本地机器中继**：westb → 本地 → westd（双跳，24.6GB）
2. **通过对象存储中继**（如有共享 OSS/COS）
3. **在 westd 上重新训练 SFT**（但太慢，不推荐）

请确认传输方案，我不会自行发起传输。

---
