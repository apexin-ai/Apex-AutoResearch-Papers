# code exp019 config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp019-config_20260514T163841_result.json`
- **Structured JSON:** [`03581f53083fed8d4dfc.json`](../../sessions/03/03581f53083fed8d4dfc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成：

- **`sft_train_v2.py`** — 语法验证通过（`--help` 正常输出）
- **`run_exp019.sh`** — 已创建并设置可执行权限
- **exp008_sft checkpoint** — 完整（config.json, model.safetensors 3.2GB, tokenizer 等均在）

与 `sft_train.py` 的关键差异：
| 参数 | exp017 (sft_train.py) | exp019 (sft_train_v2.py) |
|------|----------------------|--------------------------|
| base model | Qwen3-1.7B 原始 | exp008_sft/final |
| LR | 2e-5 | 5e-6 |
| epochs | 3 | 2 |
| data | expert_sft_train.jsonl | sft_data_v2/train.jsonl |
| eval | 无 | val.jsonl (per epoch) |
| model_path | 硬编码 | CLI 可覆盖 |

数据文件 `sft_data_v2/` 尚未就绪，脚本启动时 pre-flight 会拦截。等数据准备好即可执行 `bash scripts/run_exp019.sh`。

---
