# code urgent full status and v3 launch 21461

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_urgent_full_status_and_v3_launch_21461_20260518T070516_result.json`
- **Structured JSON:** [`8406f11f0966b348fc7e.json`](../../sessions/84/8406f11f0966b348fc7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both GPUs on westd-21461 are now fully loaded and generating outputs. Here's the full report:

---

## westd-21461 状态报告

### nvidia-smi
| GPU | Model | Memory | Util | Process |
|-----|-------|--------|------|---------|
| 0 | RTX PRO 6000 Black | 16121/97887 MiB | 85% | Mistral v3 full_s1 (PID 5971) |
| 1 | RTX PRO 6000 Black | 18919/97887 MiB | 82% | Qwen v3 full_s1 (PID 6529) |

### 脚本参数（--help 确认）
`--model_path`, `--data_path`, `--constraints_path`, `--output_path`, `--mode`, `--max_new_tokens`, `--max_samples`, `--skip_on_error`, `--resume`

### 代码版本验证 ✅
- `type_mask_processor.py`: **938 行** ✓
- `collision` 出现: **7 次** ✓
- `exact_match` 出现: **4 次** ✓

### Mistral v3 启动确认 ✅
- 模型路径: `/root/autodl-tmp/.ms_cache/mistralai/Mistral-7B-Instruct-v0___3/`
- Samples: **246**, 无 `--resume`
- 进度: 5/246 已处理

### Qwen v3 启动确认 ✅
- 模型路径: `/root/.cache/huggingface/hub/models--Qwen--Qwen3-8B/snapshots/b968826d9c46dd6066d109eabc6255188de91218/`
- Samples: **246**, 无 `--resume`
- 进度: 1/246 已处理

### Qwen grammar_only 结果（已完成，246/246）

**Violation Report:**
| 违规类型 | 数量 | 比率 |
|----------|------|------|
| ET (Entity Type) | 0 | 0.0% |
| EV (Event Vocab) | 0 | 0.0% |
| RoV (Role Vocab) | 4441 | **76.1%** |
| AC (Arg Constraint) | 479 | 8.2% |
| CF (Cross-Field) | 8 | 0.3% |

**Eval (F1):**
| Metric | P | R | F1 |
|--------|---|---|-----|
| Entity F1 | 0.4257 | 0.0871 | 0.1446 |
| Trigger ID F1 | 0.1263 | 0.1554 | 0.1393 |
| Argument F1 | 0.0081 | 0.0113 | 0.0094 |

35 parse failures, RoV=76.1% 证明 grammar 层无法控制 role vocab → semantic layer 必要性。

### 最终 GPU 分配表（4卡全满）
| 服务器 | GPU | 任务 | 状态 |
|--------|-----|------|------|
| westd-16980:0 | Qwen v3 full_s1 | 运行中 (~24min) |
| westd-16980:1 | Mistral v3 full_s1 | 运行中 (~2min) |
| westd-21461:0 | Mistral v3 full_s1 | 运行中 (~4min, 5/246) |
| westd-21461:1 | Qwen v3 full_s1 | 运行中 (刚启动, 1/246) |

4 张 GPU 全部跑满，两台服务器互为冗余。

---
