# code urgent 21461 status and v3 launch

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_urgent_21461_status_and_v3_launch_20260518T065804_result.json`
- **Structured JSON:** [`73e829bc8a83403c2875.json`](../../sessions/73/73e829bc8a83403c2875.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Mistral v3 正常运行，1 条已写入，持续产出中。

---

## 汇总报告

### GPU 状态 (westd-21461)
| GPU | 型号 | 显存 | Util | 状态 |
|-----|------|------|------|------|
| 0 | RTX PRO 6000 (96GB) | 15291MiB | 82% | **Mistral v3 运行中** (PID 5971) |
| 1 | RTX PRO 6000 (96GB) | 0MiB | 100%* | 空闲 (无进程) |

### Step 2: 已完成实验结果

**Mistral v2 retry (16K)** — 246/246 完成
| 指标 | 值 |
|------|-----|
| Parse failures | 18 |
| RoV violations | 21 (0.3%) |
| AC violations | 1489 (19.4%) |
| CF violations | 1030 (11.6%) |
| **Go/No-go (RoV+AC)** | **0.1973** |
| Entity F1 | 0.1103 (P=0.1608, R=0.0840) |
| Trigger ID F1 | 0.0378 (P=0.0354, R=0.0404) |
| Argument F1 | 0.0036 (P=0.0029, R=0.0049) |

**Qwen grammar_only** — 246/246 完成
| 指标 | 值 |
|------|-----|
| Parse failures | 35 |
| RoV violations | 4441 (76.1%) |
| AC violations | 479 (8.2%) |
| CF violations | 8 (0.3%) |
| **Go/No-go (RoV+AC)** | **0.8436** |
| Entity F1 | 0.1446 (P=0.4257, R=0.0871) |
| Trigger ID F1 | 0.1393 (P=0.1263, R=0.1554) |
| Argument F1 | 0.0094 (P=0.0081, R=0.0113) |

### Step 3: Mistral v3 启动确认

| 检查项 | 结果 |
|--------|------|
| type_mask_processor.py 行数 | **938** ✓ |
| collision 出现次数 | **7** ✓ |
| exact_match 出现次数 | **4** ✓ |
| 输出文件全新 | ✓ (已删除旧文件) |
| 代码备份 | ✓ |
| **--resume** | **未使用** ✓ |
| data_path | `data/wikievents/all.jsonl` (246 samples) ✓ |
| GPU | 0 (15291MiB, 82% util) |
| PID | 5971 |
| Samples | **246** ✓ |
| mode | full_s1 |
| tmux session | mistral_v3_full |
| 已产出 | 1 行 (持续运行中) |

**注意：** 初次启动时因网络不通 HuggingFace 下载失败，已改用本地 modelscope 缓存路径 `/root/autodl-tmp/.ms_cache/mistralai/Mistral-7B-Instruct-v0___3/`。同时默认 data_path 是 `train.jsonl` (12条)，已显式指定 `all.jsonl` (246条)。

---
