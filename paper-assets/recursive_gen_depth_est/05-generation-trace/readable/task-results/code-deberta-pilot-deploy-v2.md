# code deberta pilot deploy v2

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_deberta-pilot-deploy-v2_20260519T150615_result.json`
- **Structured JSON:** [`dd7700f22625083e45ac.json`](../../sessions/dd/dd7700f22625083e45ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

**结果汇总：**

| 检查项 | 状态 |
|--------|------|
| 文件存在 | `/root/autodl-tmp/recursive_gen_depth_est/scripts/deberta_depth_pilot.py` (7394 bytes) |
| py_compile | COMPILE_OK |
| --help | 正常输出，所有参数匹配 spec |
| 数据文件 | `depth_0~3.jsonl` 4 个文件均存在 |

**脚本与旧版差异（已修正）：**
- LoRA: r=16/alpha=32 → **r=8/alpha=16**（匹配 spec）
- output_dir: `artifacts/deberta_pilot` → **`results/deberta_pilot`**
- 新增训练时间记录（per-fold + total）
- 使用 DataCollatorWithPadding 动态 padding（替代全量 pad 到 512）
- 每 fold 训练后清理 checkpoint 目录节省磁盘
- 移除了不在 spec 中的 `--lora_rank` 和 `--no_lora` 参数

---
