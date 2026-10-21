# diagnosis exp062 status check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_exp062_status_check_20260521T085442_result.json`
- **Structured JSON:** [`d1b0d439edac4ffc1f5c.json`](../../sessions/d1/d1b0d439edac4ffc1f5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_062_decoding_strategy_shape 状态报告

### GPU 状态
| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| 0 (RTX 5090) | 6193/32607 MiB | 64% | PID 283041 (pythia-2.8b) |
| 1 (RTX 5090) | 7594/32607 MiB | 87% | PID 283607 + 344399 (olmo + qwen) |
| 2 (RTX 5090) | 3 MiB | 0% | 空闲 |
| 3 (RTX 5090) | 3 MiB | 0% | 空闲 |

### 生成进度 (6 个组合)

| Model × Strategy | 进度 | 数据行数 | 状态 | ETA |
|---|---|---|---|---|
| pythia-2.8b × greedy | 972/995 (98%) | 4752 | **运行中** (GPU 0) | ~3 min |
| pythia-2.8b × topk | — | 目录不存在 | **未启动** | 等 greedy 完成 |
| olmo-2-1b × greedy | 995/995 (100%) | 4879 | **已完成** (skipped 30) | — |
| olmo-2-1b × topk | 3/995 (0.3%) | 28 | **运行中** (GPU 1) | ~2h 50min |
| qwen3-1.7b × greedy | 217/996 (22%) | 1075 | **运行中** (GPU 1) | ~3h 20min |
| qwen3-1.7b × topk | — | 目录不存在 | **未启动** | 等 greedy 完成 |

### 日志摘要
- **gen_pythia.log**: pythia-2.8b-greedy ~9s/it，即将完成
- **gen_olmo.log**: olmo-2-1b-greedy 已完成 (4879 records, 2h24min)，olmo-2-1b-topk 刚启动 ~10.5s/it
- **gen_qwen_greedy.log**: qwen3-1.7b-greedy ~15.4s/it，从 seed 81 恢复（之前在 cuda:2 的尝试挂在了 80/996，见 gen_qwen17b.log，GPU 2 现已空闲）
- **gen_qwen_chain.log**: 等待 OLMo 生成完成后接力
- **Feature extraction**: 尚无 decoding strategy 相关的 features 文件

### 问题
1. **GPU 2 & 3 完全空闲** — qwen17b 进程 (cuda:2) 已死，只有 gen_qwen_greedy (cuda:0/1) 接管了恢复。两张卡浪费中。
2. **pythia-topk 和 qwen-topk 尚未启动**，看起来依赖 chain 脚本自动调度，但当前编排只在等 OLMo，不清楚 pythia/qwen 的 topk 何时触发。
3. 按当前速度，全部 6 个组合完成预计还需 **~4-5 小时**（瓶颈是 qwen-greedy + qwen-topk 串行）。

---
