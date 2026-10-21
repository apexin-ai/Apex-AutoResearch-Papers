# audit server inventory

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_server-inventory_20260523T200554_result.json`
- **Structured JSON:** [`f07ee9e623ed313497a7.json`](../../sessions/f0/f07ee9e623ed313497a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器审计报告

### westd-16639 (connect.westd.seetacloud.com:16639)
**SSH**: root@connect.westd.seetacloud.com -p 16639
**GPU**: 4× NVIDIA RTX PRO 6000 Blackwell Server Edition (96GB each)
**磁盘**: 根 40% (12G/30G) / 数据盘 66% (230G/350G)

| GPU | 进程 | 显存占用 | 利用率 | 状态 |
|-----|------|---------|--------|------|
| cuda:0 | vLLM Qwen3-14B (port 8020) + run_full_mvp seed123 | 86.4/95.6 GB | 100% | 运行中 |
| cuda:1 | — | 0/95.6 GB | 0% | **空闲** |
| cuda:2 | vLLM Qwen3-14B (port 8021) + run_full_mvp seed456 | 86.4/95.6 GB | 100% | 运行中 |
| cuda:3 | vLLM Qwen3-14B (port 8022) + run_full_mvp seed789 | 86.4/95.6 GB | 100% | 运行中 |

**实验进度** (Qwen3-14B PW 600):
- seed123: **67/600** (~11%)
- seed456: **68/600** (~11%)
- seed789: **68/600** (~11%)

已跑约 2h，预计剩余 ~13h。

**数据占用**: 项目 840M (results/ 612M), models/ 206G

**模型清单** (206G):
| 模型 | 大小 | 备注 |
|------|------|------|
| Qwen3-14B | 28G | 当前实验在用 |
| Qwen2.5-14B-Instruct | 28G | 历史实验 |
| Qwen2.5-72B-Instruct-AWQ | 39G | |
| Mistral-7B-Instruct-v0.3 | 28G | |
| Meta-Llama-3.1-8B-Instruct | 15G | |
| phi-4-reasoning | 25G | |
| deepseek-ai (R1-Distill) | 15G | |
| deepseek-r1-0528-qwen3-8b | 16G | |
| NLI models (bart/deberta/roberta) | ~13G | |
| gemma-3-27b-it / llama-4-scout / iic | ~0.1G | 占位符/不完整 |

---

### westd-30973 (connect.westd.seetacloud.com:30973)
**SSH**: root@connect.westd.seetacloud.com -p 30973
**GPU**: 3× NVIDIA RTX PRO 6000 Blackwell Server Edition (96GB each)
**磁盘**: 根 42% (13G/30G) / 数据盘 22% (54G/250G)

| GPU | 进程 | 显存占用 | 利用率 | 状态 |
|-----|------|---------|--------|------|
| cuda:0 | — | 0/95.6 GB | 0% | **空闲** |
| cuda:1 | — | 0/95.6 GB | 0% | **空闲** |
| cuda:2 | vLLM LLaMA-3.1-8B (port 8002) + run_full_mvp seed456 --resume | 86.2/95.6 GB | 97% | 运行中 |

**实验进度**:
- LLaMA seed456_v2: **593/600** (~99%, 即将完成)
- LLaMA seed789_v2: 378/600 (无进程运行，已停止)
- Qwen2.5 seed789_v3: 339/600 (无进程运行，已停止)

**数据占用**: 项目 226M (results/ 1.2M), models/ 44G (LLaMA 16G + Qwen2.5 28G)

---

### 分类汇总

**A 类（在跑实验，保留）**:
- westd-16639 cuda:0/2/3 — Qwen3-14B PW seed123/456/789，67-68/600，预计还需 ~13h
- westd-30973 cuda:2 — LLaMA seed456_v2，593/600，即将完成（<30min）

**B 类（后续需要，保留）**:
- westd-16639 cuda:1 — 空闲，可用于新实验
- westd-30973 cuda:0/1 — 空闲，seed456 完成后 cuda:2 也将释放
- westd-30973 结果文件 seed789_v2 (378/600) / qwen25_seed789_v3 (339/600) — 中途停止的实验数据，确认是否需要恢复

**C 类（可释放）**:
- westd-16639 models/: gemma-3-27b-it (44K占位)、llama-4-scout (60K占位)、iic (4K占位)、test_hf_speed (6.8M) — 不完整/测试用，共可忽略
- westd-16639 models/: phi-4-reasoning (25G)、deepseek-r1-0528-qwen3-8b (16G) — 如无后续实验计划，可释放 ~41G
- westd-16639 数据盘 66% 使用率偏高，主要是 models/ 206G 占用

---
