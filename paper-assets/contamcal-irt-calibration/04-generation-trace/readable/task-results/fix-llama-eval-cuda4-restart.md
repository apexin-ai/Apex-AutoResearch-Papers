# fix llama eval cuda4 restart

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_llama_eval_cuda4_restart_20260516T143343_result.json`
- **Structured JSON:** [`4b3eefa6be0475d783cd.json`](../../sessions/4b/4b3eefa6be0475d783cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出报告：

### 1. Kill + GPU 释放
- PID 785955/785949 已 kill，cuda:4 确认释放

### 2. 脚本修改
- `evaluate.py` 新增 per-benchmark 即时保存（lines 718-721）：每完成一个 benchmark 立即写 `{benchmark}_results.json` 到输出目录，不再依赖全部完成才写文件
- 原文件备份为 `evaluate.py.bak2`

### 3. GSM8K 速度诊断
- **CoT 模式正常慢。** 8-shot CoT + `max_new_tokens=512` + `do_sample=False`（greedy），生成式评测。11s/item 是 3B 模型在 4090D 上做 CoT 推理的正常速度。无配置问题。

### 4. 新实验
- **PID**: 796488（子进程 796493），cuda:4 占用 7580 MiB
- MMLU 以 ~40 it/s 评测中，network_turbo 已启用解决 HF 连接问题
- Registry 已更新

### 5. 预计完成时间
| Benchmark | Items | Speed | ETA |
|-----------|-------|-------|-----|
| MMLU | 14042 | ~40 it/s | ~6 min（进行中） |
| GSM8K | 1319 | ~0.09 it/s (CoT) | ~4h |
| ARC-Challenge | ~1172 | ~40 it/s | ~30s |
| HumanEval | 164 | ~2 it/s | ~1.5 min |

**总计约 4.5 小时**，GSM8K 是瓶颈。预计约 03:10 (UTC+8) 完成。

---
