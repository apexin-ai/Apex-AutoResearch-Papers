# code w10 mistral scierc beam 551 launch

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w10_mistral_scierc_beam_551_launch_20260517T072439_result.json`
- **Structured JSON:** [`e433e587a30b108b3e5a.json`](../../sessions/e4/e433e587a30b108b3e5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功启动。

---

**报告：**

| 项目 | 值 |
|---|---|
| **Mistral 模型路径** | `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3` |
| **PID** | 5112 |
| **GPU** | cuda:0, 15282MiB 占用 |
| **tmux session** | `mistral_scierc_beam` |

**完整启动命令：**
```bash
python run_constrained_extraction.py \
  --mode full_s1 --dataset scierc \
  --model_path /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 \
  --data_path data/processed_data/test.json \
  --constraints_path ontology_constraints.json \
  --output_path outputs/scierc_mistral_beam_551.jsonl \
  --decoding_strategy beam --num_beams 4 \
  --device cuda:0
```

**Mistral SciERC greedy baseline：** 该服务器上未找到 SciERC Mistral 的历史输出（outputs 目录只有 DocRed Mistral 结果）。greedy baseline 可能在其他服务器上。

**日志路径：** `~/runs/schema_semantic_constrained_ie/w10_mistral_scierc_beam_551.log`

---
