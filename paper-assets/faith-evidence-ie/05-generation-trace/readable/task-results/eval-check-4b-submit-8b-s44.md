# eval check 4b submit 8b s44

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_check-4b-submit-8b-s44_20260523T054119_result.json`
- **Structured JSON:** [`1b7d9d9118131f2b467c.json`](../../sessions/1b/1b7d9d9118131f2b467c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### GPU 状态
| GPU | 显存占用 | 进程 | 任务 |
|-----|---------|------|------|
| cuda:0 | 0 → 刚提交 8B | PID 228226 | **test_eval_8b_rsft_s44_with_evi** (刚启动) |
| cuda:1 | 32479/97887 MiB | PID 194682 | (其他任务) |
| cuda:2 | 12013/97887 MiB | PID 221956 | DPO dev eval — **batch 150/247 (61%)**, 预计还需 ~1.5h |
| cuda:3 | 6071/97887 MiB | PID 214028 | 1.7B s43 with-evi — 运行 4h33m，输出目录仍空 |

### 4B s43 no-evi → DONE ✓
- **ign_f1 = 0.2702**, precision=0.3583, recall=0.2169
- format_ok_rate=0.992, 500 docs, 68min
- s43 evidence tax = 0.2702 - 0.2503 = **+1.99pp**（s42 tax=+1.51pp）

### 8B s44 with-evi → RUNNING ✓
- PID **228226**, cuda:0, timeout 4h
- Cron 已注册，自动监控

### 注意
1.7B s43 with-evi 运行 4.5h 但输出目录为空，可能是模型加载慢或卡在推理。需关注。

---
