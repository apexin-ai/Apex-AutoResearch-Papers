# ops check 25068 full status

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-25068-full-status_20260519T202850_result.json`
- **Structured JSON:** [`51927831d1e588431cee.json`](../../sessions/51/51927831d1e588431cee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-25068 实验状态汇总

### GPU 状态（4× H800 96GB）
| GPU | 显存占用 | 利用率 | 用途 |
|-----|---------|--------|------|
| 0 | 89889/97887 MiB | 96% | vLLM (port 8000) → exp-080 |
| 1 | 89889/97887 MiB | 97% | vLLM (port 8001) → exp-074c |
| 2 | 89733/97887 MiB | 100% | vLLM (port 8002) → exp-075b |
| 3 | 90571/97887 MiB | 96% | vLLM (port 8003) → exp-076 |

4 卡全部满载运行。

### 各实验进度

| 实验 | 方法 | 数据集 | 进度 | ETA | 状态 |
|------|------|--------|------|-----|------|
| **exp-074c** | ICG (seed=123) | FOLIO | **82/204** (40%) | ~34 min | 运行中，启动于 04:06 |
| **exp-075b** | Contrastive | FOLIO | **161/204** (79%) | ~43 min | 运行中，启动于 01:50 |
| **exp-076** | Debate | FOLIO | **195/204** (96%) | ~9 min | 即将完成，启动于 01:31 |
| **exp-080** | Contrastive×LogiQA | LogiQA-200 | **22/200** (11%) | ~123 min | 运行中，启动于 04:15 |

### 预计完成顺序
1. **exp-076** (Debate×FOLIO) — ~9 分钟内完成
2. **exp-074c** (ICG seed=123) — ~34 分钟
3. **exp-075b** (Contrastive×FOLIO) — ~43 分钟
4. **exp-080** (Contrastive×LogiQA) — ~2 小时

### tmux sessions（8 个）
`exp074_vllm`, `exp074c_vllm`, `exp074c_run`, `exp075_vllm`, `exp075b_run`, `exp076_vllm`, `exp076_run`, `model_dl_25068`

所有实验正常运行，无报错，结果文件持续写入中。

---
