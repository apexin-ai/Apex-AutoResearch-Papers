# ssh exp012 recover and restart

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp012-recover-and-restart_20260515T164517_result.json`
- **Structured JSON:** [`05fab72c4da0c4e248e7.json`](../../sessions/05/05fab72c4da0c4e248e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果明确了。汇总报告如下：

---

## exp012 检查结果

### eval 文件结构（完整，但数据全是 0）

**exp1 (Count Curve)**：94 entries，7 count levels
| count | n | avg_bcs | avg_exact_f1 |
|-------|---|---------|-------------|
| count_1 | 64 | 0.0000 | 0.0000 |
| count_2 | 5 | 0.7021 | 0.0000 |
| count_6 | 5 | 0.8923 | 0.0000 |
| count_12 | 5 | 0.9226 | 0.0000 |
| count_22 | 5 | 0.9327 | 0.0000 |
| count_44 | 5 | 0.9671 | 0.0000 |
| count_64 | 5 | 0.9732 | 0.0000 |

**exp2 (BCS Controlled)**：54 entries，count_6 + count_12
| count | n | avg_bcs | avg_exact_f1 |
|-------|---|---------|-------------|
| count_6 | 27 | 0.8935 | 0.0000 |
| count_12 | 27 | 0.9260 | 0.0000 |

### 根因

**94,000 条 predictions 中，每条 gen_tokens 恒等于 2，predictions 列表为空。** 模型大概率输出了 `[]`（空 JSON），所以 F1/precision/recall 全为 0。可能原因：
1. 当时 rogue vLLM 进程占了 89.5GB 显存，LLaMA-8B 在剩余显存中可能以极度降级模式运行
2. prompt v2 格式与 LLaMA-3.1-8B-Instruct 不兼容

**结论：结构上完整，但科学上无效，需要重跑。**

### GPU 状态
已清空：0 MiB used / 97,253 MiB free。vLLM PID 297093 已不在。无需手动清理。

### exp_fewrel_40rel
不存在。artifacts 下只有 `fewrel_qwen3_embeddings.pt`、`fewrel_qwen3_sim_matrix.pt`、`fewrel_80rel_error_taxonomy.json`。无相关进程运行。

---

是否要我现在重跑 exp012？脚本 `scripts/run_exp012_llama8b.sh` 就绪，GPU 空闲，模型路径 `/root/autodl-tmp/models/llama-3.1-8b-instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct`。但建议先确认该模型仍在磁盘上 + 考虑是否要先排查 gen_tokens=2 的原因（可能需要看 `run_extraction.py` 的推理配置）。

---
