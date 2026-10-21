# ssh harvest wave3 nvidia check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_harvest_wave3_nvidia_check_20260522T071704_result.json`
- **Structured JSON:** [`91453cba4ffe2d8cd2fa.json`](../../sessions/91/91453cba4ffe2d8cd2fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MV recompute 完成。汇总如下：

---

## nvidia-smi

### autodl-5090 — 全部空闲
| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX 5090 | 0% | 2/32607 MiB |
| 1 | RTX 5090 | 0% | 2/32607 MiB |
| 2 | RTX 5090 | 0% | 2/32607 MiB |
| 3 | RTX 5090 | 0% | 2/32607 MiB |

**cuda:0 无进程运行**（pmon 显示 `-`），之前系统显示的 100% 利用率已消失。

### autodl-5090-c — 3 张卡在跑
| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX 5090 | 85% | 30115/32607 MiB |
| 1 | RTX 5090 | 85% | 30079/32607 MiB |
| 2 | RTX 5090 | 0% | 0/32607 MiB |
| 3 | RTX 5090 | 91% | 29785/32607 MiB |

**进程详情**（全部是 VLLM::EngineCore）：
- cuda:0 — PID 381917, sm=85%, mem=40%
- cuda:1 — PID 392754, sm=83%, mem=46%
- cuda:3 — PID 387768, sm=82%, mem=47%

---

## Part 2: 4 个实验状态 (autodl-5090)

| 实验 | 状态 | 说明 |
|------|------|------|
| **CoNLL N=32 s456** | **完成** | 3453 行 samples.jsonl, 213MB |
| CoNLL PT N=16 | **未运行** | 目录空（仅创建于 13:29） |
| SciERC PT N=64 | **未运行** | 目录空（仅创建于 13:29） |
| CoNLL PT N=64 | **未运行** | 目录空（仅创建于 13:30） |

### CoNLL N=32 s456 — MV strict recompute 结果

| 指标 | 值 |
|------|-----|
| greedy_f1 | **0.9117** |
| mv_strict_f1 | **0.9167** |
| mv_delta_pp | **+0.51pp** |
| degeneracy_rate | **40.1%** |
| oracle_f1 | **0.9686** |
| alpha_crit_strict | 0.4558 |
| alpha_crit_eff_strict | 0.7614 |

---

## Part 3: FewNERD 实验状态 (autodl-5090-c)

| 实验 | 状态 | 说明 |
|------|------|------|
| FewNERD N=32 FT (cuda:0) | **运行中** | 目录空但 GPU 85% 活跃 (PID 381917 VLLM) |
| FewNERD PT N=16 (cuda:1) | **运行中** | 目录空但 GPU 85% 活跃 (PID 392754 VLLM) |
| FewNERD PT N=32 (cuda:3) | **运行中** | 目录空但 GPU 91% 活跃 (PID 387768 VLLM) |

3 个 FewNERD 实验正在 5090-c 上推理中，samples.jsonl 尚未生成（可能在内存中累积或脚本完成后才写入）。

---

**关键发现**：5090 四卡完全空闲——3 个 pretrained 实验（CoNLL PT N=16、CoNLL PT N=64、SciERC PT N=64）目录已创建但都是空的，没有进程在跑，看起来从未实际启动。

---
