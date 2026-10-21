# monitor westd 16980 gpu status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_westd-16980-gpu-status_20260522T052000_result.json`
- **Structured JSON:** [`82e3efdc5a66db0b811d.json`](../../sessions/82/82e3efdc5a66db0b811d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态

| GPU | 型号 | 显存占用 | 利用率 | PID |
|-----|------|----------|--------|-----|
| cuda:0 | RTX PRO 6000 Blackwell (96GB) | 39.6GB / 96GB | 78% | 892263 |
| cuda:1 | RTX PRO 6000 Blackwell (96GB) | 40.9GB / 96GB | 82% | 881090 |

### cuda:0 — SciERC 70B LoRA S1 constrained

- **命令**: `run_constrained_extraction.py --mode full_s1 --dataset scierc --lora_path 70b_lora_scierc/checkpoint-663`
- **输出路径**: `/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.jsonl`
- **进度**: **34 / 551**（6.2%）
- 文件创建于 13:16，~5分钟完成34样本，约 **9s/样本**
- **预估剩余**: 517 × 9s ≈ **78分钟**，约 **14:40** 完成
- 同目录 `scierc_unconstrained.jsonl`（551行）已于 12:34 完成

### cuda:1 — DocRED 70B LoRA unconstrained

- **命令**: `run_constrained_extraction.py --mode unconstrained --dataset docred --lora_path 70b_lora_docred/checkpoint-1146`
- **输出路径**: `/root/autodl-tmp/schema_outputs/r16_70b_lora_docred/docred_unconstrained.jsonl`
- **进度**: **117 / 200**（58.5%），从之前的 105 增加了 12 条
- 文件创建于 10:33，~2h49m 完成 117 样本，约 **87s/样本**（DocRED 文档长）
- **预估剩余**: 83 × 87s ≈ **120分钟**，约 **15:22** 完成

### 注意

- PID 892263（非 892258）在 cuda:0 上跑 SciERC S1，进程正常
- 两个任务的输出写到了 `/root/autodl-tmp/schema_outputs/r16_70b_lora_*/`，不是之前的 `outputs/` 目录
- `tmux ls` 和 `ps aux | grep` 被 ssh_read_only 白名单拦截，无法执行

---
