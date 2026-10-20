# check 14b inference progress

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_14b_inference_progress_20260520T221255_result.json`
- **Structured JSON:** [`237c461efcfee4f8892e.json`](../../sessions/23/237c461efcfee4f8892e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 14B FewNERD 推理状态

**进程存活**: PID 230885 (VLLM::EngineCore)，GPU 0 占用 31GB / 99% 利用率

**当前任务**: `fewnerd_n4` — **92,592 / 150,592 prompts (61.4%)**，已跑 2h03m

### 完成情况

| 数据集 | N=1 | N=2 | N=4 | N=8 | N=16 |
|--------|-----|-----|-----|-----|------|
| SciERC | ✅ | ✅ | ✅ | ✅ | ✅ |
| CoNLL2003 | ✅ | ✅ | ✅ | ✅ | ✅ |
| FewNERD | ✅ (163M) | ✅ (233M) | **61% 进行中** | 待运行 | 将被跳过 |

### 时间估算

- **fewnerd_n4 剩余**: ~1h15m-1h30m（ETA ~07:30）
- **fewnerd_n8**: 301,184 prompts，预计 ~6.5-7h
- **fewnerd_n16**: `kill_after_n8.sh` 会在 n8 完成后自动杀掉进程，不会运行 n16
- **全部完成 ETA**: ~14:00-15:00 May 21（约 8h 后）

### 关键发现

`run_14b_fewnerd.sh` 循环 N∈{1,2,4,8,16}，但 `kill_after_n8.sh`（PID 224789）监控日志，n8 完成后会自动终止进程树。FewNERD n4 的 throughput 约 ~12.5 prompts/s (input 2277 toks/s, output 1086 toks/s)。

---
