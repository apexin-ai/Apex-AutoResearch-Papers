# infra comet monitor

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_comet-monitor_20260522T081158_result.json`
- **Structured JSON:** [`c4c8558432050aba9098.json`](../../sessions/c4/c4c8558432050aba9098.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

### COMET Qwen (PID 59412, cuda:0)
- **仍在运行**，train 集 back-translation 进度 **740/798 (93%)**
- test 集已完成（`zh_conflict_test_validated.jsonl` 29KB，`translation_quality_report.json` 18KB 均已生成）
- train validated 文件尚未写出（back-translation 完成后还需跑 COMET scoring）
- **cuda:0 不可释放**，预计还需 10-20 分钟完成 back-translation + COMET scoring

### COMET Llama (PID 59571, cuda:2)
- **仍在运行**，train 集 back-translation 进度 **760/1096 (69%)**
- 比 Qwen 慢，预计还需更久

### GPU 占用
| GPU | 利用率 | 显存 | 进程 |
|-----|--------|------|------|
| 0 | 46% | 16.5/97.9 GB | COMET Qwen validate_translation |
| 1 | 46% | 16.5/97.9 GB | Gemma translate_to_zh |
| 2 | 72% | 16.5/97.9 GB | COMET Llama validate_translation |
| 3 | 88% | 16.2/97.9 GB | Llama translate_to_de |

### 其他进程
- `train_probe.py` bootstrap (Qwen + Llama) — 纯 CPU，各 ~550% CPU
- `bootstrap_mlp_delta.py` — 纯 CPU
- 4 张 GPU 全部被占用，当前无空闲 GPU。

---
