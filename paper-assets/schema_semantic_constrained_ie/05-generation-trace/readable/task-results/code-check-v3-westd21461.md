# code check v3 westd21461

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_v3_westd21461_20260518T080939_result.json`
- **Structured JSON:** [`4b343f31fc343436f57f.json`](../../sessions/4b/4b343f31fc343436f57f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-21461 v3 实验状态汇报

### GPU 状态
| GPU | 型号 | 显存占用 | GPU 利用率 | 功耗 |
|-----|------|---------|-----------|------|
| 0 | RTX PRO 6000 (96GB) | 20,313 / 97,887 MiB | 85% | 323W/600W |
| 1 | RTX PRO 6000 (96GB) | 18,277 / 97,887 MiB | 88% | 336W/600W |

### 运行中的进程
- **GPU 0**: Mistral v3 实验 (PID 5971)，运行 ~66 分钟，tmux 会话 `mistral_v3_full`
- **GPU 1**: Llama v3 实验 (PID 9491)，运行 ~41 分钟，nohup 后台运行
- 另有一个 Llama 模型下载进程 (PID 8621) 仍在运行

### v3 输出文件进度（目标 246 行）

| 文件 | 当前行数 | 进度 |
|------|---------|------|
| `ee_mistral_wikievents_constrained_v3_full.jsonl` | **73 / 246** | 29.7% |
| `ee_llama_wikievents_constrained_v3_full.jsonl` | **56 / 246** | 22.8% |
| `ee_qwen_wikievents_constrained_v3_full.jsonl` | **6 / 246** | 2.4% |

Qwen 只有 6 行且文件最后修改时间为 15:10，无对应运行进程，可能已中断或完成后停止。

### 其他确认
- `type_mask_processor.py`: **938 行**（修复版确认）
- `/root/OntoCoDec/run_v3_eval.sh`: 不存在（路径应在 `schema_semantic_constrained_ie` 下）
- tmux 会话: `mistral_v3_full` (1 window)

### 结论
Mistral 和 Llama 的 v3 实验正在正常推进，分别完成约 30% 和 23%。Qwen 的 v3 实验疑似中断（仅 6 行，无运行进程）。按当前速度，Mistral 和 Llama 预计还需约 2-3 小时完成。

---
