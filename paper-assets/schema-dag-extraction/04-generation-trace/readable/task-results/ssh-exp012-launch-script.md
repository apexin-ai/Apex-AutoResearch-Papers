# ssh exp012 launch script

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp012-launch-script_20260515T102532_result.json`
- **Structured JSON:** [`2ecc5cb5c8d333c7ba24.json`](../../sessions/2e/2ecc5cb5c8d333c7ba24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个脚本已部署到服务器 `/root/schema-dag-extraction/scripts/`。

**验证摘要：**

| 检查项 | 状态 |
|--------|------|
| `scripts/` 目录 | 存在 |
| `--output_dir` 参数 | 确认（run_experiment.py:26） |
| `--max_model_len` 参数 | 确认，default=4096（run_experiment.py:35），避免 LLaMA 131K 默认值 OOM |
| `--embeddings_path` / `--sim_matrix_path` | 确认，artifacts 均存在 |
| LLaMA shards | 15/15 ✓ |
| GPU | RTX PRO 6000 Blackwell 96GB — 70B FP8 单卡可载，无需 tensor_parallel |

**启动方式**（exp-008 完成后）：
```bash
bash /root/schema-dag-extraction/scripts/submit_exp012.sh
```

---
