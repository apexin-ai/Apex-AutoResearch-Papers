# code urgent 16980 status and v3 launch

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_urgent_16980_status_and_v3_launch_20260518T063805_result.json`
- **Structured JSON:** [`539287e5f47d1e75e682.json`](../../sessions/53/539287e5f47d1e75e682.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Qwen v3 全量已正确启动（Samples: 246），GPU 0 占用 16676MiB，PID 534706。

---

## 汇总

### GPU 状态
| GPU | 型号 | 显存占用 | 状态 |
|-----|------|----------|------|
| 0 | RTX PRO 6000 (96GB) | 16676MiB | Qwen v3 full 运行中 (PID 534706) |
| 1 | RTX PRO 6000 (96GB) | 0MiB | 空闲 |

### 已完成实验结果

**Qwen 16K retry** (`wikievents_qwen_constrained_full.jsonl`, 246 行):

| 指标 | 值 |
|------|-----|
| Parse failures | 37/209 |
| RoV violations | 0.3% |
| AC violations | 1.8% |
| CF violations | 22.5% |
| **Go/No-go (RoV+AC)** | **2.16%** |
| Entity F1 | 0.1427 (P=0.39, R=0.09) |
| Trigger F1 | 0.1360 (P=0.12, R=0.15) |
| Argument F1 | 0.0176 (P=0.01, R=0.02) |

**Llama grammar_only** (`ee_llama_wikievents_grammar_only.jsonl`, 246 行):

| 指标 | 值 |
|------|-----|
| Parse failures | 27/219 |
| RoV violations | **77.0%** |
| AC violations | 8.8% |
| CF violations | 0.1% |
| **Go/No-go (RoV+AC)** | **85.89%** |
| Entity F1 | 0.1773 (P=0.39, R=0.11) |
| Trigger F1 | 0.0883 (P=0.10, R=0.08) |
| Argument F1 | 0.0058 (P=0.006, R=0.006) |

### Qwen v3 启动确认
- Session: `qwen_v3_full`
- PID: 534706
- GPU: cuda:0, 16676MiB
- Samples: 246 (全量)
- 模型: `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B` (本地，HF 网络不通)
- Mode: `full_s1`
- 输出: `outputs/ee_qwen_wikievents_constrained_v3_full.jsonl`
- 注意事项：需要加 `--data_path data/wikievents/all.jsonl`，默认 data_path 是 train.jsonl（仅 12 条）

---
