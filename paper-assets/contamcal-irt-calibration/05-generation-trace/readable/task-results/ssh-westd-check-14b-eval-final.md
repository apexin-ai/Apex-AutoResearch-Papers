# ssh westd check 14b eval final

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-check-14b-eval-final_20260519T023712_result.json`
- **Structured JSON:** [`d85a1d13dfc458306151.json`](../../sessions/d8/d85a1d13dfc458306151.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 14B Eval 状态

**服务器确认**: westd-29999, 4× RTX PRO 6000 Blackwell (~97887 MiB) ✓

### 已完成结果

| Adapter | MMLU | ARC |
|---------|------|-----|
| d000_s42 | 74.59% | 93.52% |
| d005_s42 | 75.42% | 93.09% |
| d025_s42 | 75.77% | 92.83% |
| d050_s42 | **进行中** | **进行中** |
| d100_s42 | **未开始** | **未开始** |

### PID 99071 (cuda:0, 32.7GB)

`evaluate.py --adapter-path Qwen2.5-14B_d050_s42 --benchmarks mmlu arc_challenge`

d050 eval 正在跑，目录刚创建（10:30），尚无 eval_results.json。

### Batch Script PID 93847

**仍然存活**（State=S sleeping）。PPid 链: 93845 → 93847 → 99071。batch script 正在 wait d050 完成，之后会自动启动 d100 eval。你之前说 93847 已退出，实际上它只是在 sleep 等子进程。

### cuda:0 不可释放

d050 + d100 还要跑完，预计还需较长时间。其他 3 个 GPU 也全部在用（cuda:1/2/3 分别有活跃进程）。

---
