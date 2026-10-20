# code check 19912 fill

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check-19912-fill_20260521T130313_result.json`
- **Structured JSON:** [`ac515b7364b836e518d5.json`](../../sessions/ac/ac515b7364b836e518d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总当前状态：

## 状态总结

### ARC-C (完成)
| Seed | theta | lz* | acc | n_items |
|------|-------|-----|-----|---------|
| s1 | 0.8106 | -5.4483 | 0.9017 | 295 |
| s2 | 0.7624 | -5.4328 | 0.8949 | 295 |
| s3 | 0.7137 | -5.5244 | 0.8949 | 295 |
| s4 | 0.5502 | -5.4345 | 0.8847 | 295 |
| s5 | 0.7810 | -5.2317 | 0.8983 | 295 |
| s6 | 0.7547 | -5.5724 | 0.8949 | 295 |
| s7 | 0.7058 | -5.5852 | 0.8915 | 295 |
| s8 | 0.8511 | -5.4001 | 0.9051 | 295 |
| s9 | 0.8868 | -5.5359 | 0.9017 | 295 |
| s10 | 0.8111 | -5.0733 | 0.9051 | 295 |
| **contam15** | 0.9639 | **-4.9165** | 0.9085 | 295 |
| **contam50** | 4.0000 | **-4.5725** | 0.9424 | 295 |

- Clean mean lz* = -5.4239, sd = 0.1605
- **Cohen's d: contam15 = 3.16, contam50 = 5.30** (强检出)

### 19912 GPU 填充
- **GPU 0/1/2**: Llama clean s8/s9/s10 训练中 (~23%/939 steps, 约 13 分钟完成)
- **GPU 3**: 空闲
- 所有 eval 文件已就绪 (mmlu_params.csv, eval_lz.py, mmlu_items.json, seen_items)
- 训练完成后可立即运行 eval

### 19912 Llama 可用性
- 模型: Llama-3.1-8B-Instruct 已下载 (15GB)
- 代码: train.py + eval_lz.py + prepare_data.py 齐全
- 数据: clean/train.jsonl (与 35694 完全一致), mmlu_items.json, seen_items
- SSH 通道已打通 (35694→19912, 用 /root/.ssh/id_transfer)

---
