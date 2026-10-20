# code check v3 westd16980

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_v3_westd16980_20260518T080934_result.json`
- **Structured JSON:** [`b150a0abc450647fc72d.json`](../../sessions/b1/b150a0abc450647fc72d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-16980 状态汇总

### GPU 状态
| GPU | 型号 | 显存占用 | GPU 利用率 | 温度 |
|-----|------|---------|-----------|------|
| 0 | RTX PRO 6000 (98GB) | 24,991 / 97,887 MiB | 84% | 59°C |
| 1 | RTX PRO 6000 (98GB) | 17,419 / 97,887 MiB | 89% | 65°C |

两块 GPU 都在满负荷运行。

### v3 实验进度（目标 246 行/文件）

| 实验 | GPU | 输出文件 | 已完成行数 | 进度 | 运行时间 |
|------|-----|---------|-----------|------|---------|
| Qwen v3 full_s1 | GPU 0 | `ee_qwen_wikievents_constrained_v3_full.jsonl` | **103 / 246** | 42% | ~87 min（14:42 启动） |
| Mistral grammar_only v3 | GPU 1 | `ee_mistral_wikievents_grammar_only_v3.jsonl` | **74 / 246** | 30% | ~59 min（15:10 启动） |

另外还存在一个之前跑的 `ee_mistral_wikievents_constrained_v3_full.jsonl`（仅 6 行，已停止）。

### tmux 会话
6 个会话存在，其中 `qwen_v3_full` 和 `mistral_grammar_only_v3` 是当前活跃实验。

### 其他确认
- `type_mask_processor.py` = **938 行**（修复版确认）
- `run_v3_eval.sh` 已存在，会对 qwen/llama/mistral 三个模型跑 violation_checker + F1 eval
- 两个实验都还在跑，预计还需 1-2 小时完成全部 246 个文档

---
