# ssh urgent rtx6000 status check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_rtx6000_status_check_20260522T120545_result.json`
- **Structured JSON:** [`a4339ad3a9ff48e4948f.json`](../../sessions/a4/a4339ad3a9ff48e4948f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

# 状态检查报告 — rtx6000-4x
**时间**: 2026-05-22 20:06 UTC

---

## Check 1: GPU 使用

| GPU | 型号 | 利用率 | 显存 | 负载 |
|-----|------|--------|------|------|
| 0 | RTX PRO 6000 Blackwell (96GB) | 68% | 74.1/95.6 GB | exp-009 MCMC |
| 1 | RTX PRO 6000 Blackwell (96GB) | 100% | 87.6/95.6 GB | vLLM mistral-large |
| 2 | RTX PRO 6000 Blackwell (96GB) | 100% | 88.9/95.6 GB | vLLM llama-3.3-70b |
| 3 | RTX PRO 6000 Blackwell (96GB) | 100% | 86.0/95.6 GB | vLLM qwen2.5-72b |

**全部 4 卡满载运行。**

---

## Check 2: exp-009 进程

| 项目 | 值 |
|------|-----|
| PID | 112923 (子进程 112925) |
| 运行时间 | **11h 00m 55s** |
| 命令 | `run_exp009.py --part both` (CUDA:0) |
| 进度 | **114/200 rho 值 (57%)** |
| 已耗时 | 39,469s |
| 预计剩余 | ~29,775s (**~8.3h**) |

exp-009 正常运行，预计明天凌晨 ~4:00 UTC 完成。

---

## Check 3: vLLM 服务

| 端口 | 模型 | GPU | 状态 |
|------|------|-----|------|
| 8001 | llama-3.3-70b-instruct (AWQ) | GPU 2 | **UP** |
| 8002 | qwen2.5-72b-instruct (AWQ) | GPU 3 | **UP** |
| 8003 | mistral-large-instruct | GPU 1 | **UP** |

3 个 vLLM 实例全部在线，为 judge collection 提供本地推理。

---

## Check 4: Judge 收集进程

**7 个 collect.py 刚启动** (20:04 UTC，约 2 分钟前)：

| tmux session | Judge | Workers | 后端 |
|-------------|-------|---------|------|
| pts/4 | mistral_arena | 8 | 本地 vLLM:8003 |
| pts/6 | gpt-5.5-proxy_arena | 4 | API proxy |
| pts/7 | claude-opus-4.7-proxy_arena | 4 | API proxy |
| pts/8 | claude-sonnet-4.6-proxy_arena | 4 | API proxy |
| pts/10 | deepseek-v4-pro-proxy_arena | 4 | API proxy |
| pts/11 | gemini-2.5-pro-proxy_arena | 4 | API proxy |
| pts/12 | qwen3-235b-proxy_arena | 4 | API proxy |

收集目标：9 个 target models × 9 个 judges，pairwise 格式，position swap 开启。

---

## Check 5: Judge × Model 覆盖矩阵

**当前已收集判断行数：**

| Judge | 总行数 | 估算 items/model |
|-------|--------|-----------------|
| gpt-5.5-proxy | 2,504 | ~139 |
| claude-opus-4.7-proxy | 2,299 | ~128 |
| claude-sonnet-4.6-proxy | 1,876 | ~104 |
| gemini-2.5-pro-proxy | 1,302 | ~72 |
| qwen3-235b-proxy | 1,283 | ~71 |
| deepseek-v4-pro-proxy | 971 | ~54 |
| llama-3.3-70b | 697 | ~39 |
| qwen2.5-72b | 484 | ~27 |
| mistral-large-2 | 288 | ~16 |
| **合计** | **12,000** | |

**gemma-2-9b 抽样检查**（新增模型，覆盖不均）：

| Judge | gemma-2-9b 行数 | 达标? |
|-------|----------------|-------|
| claude-opus-4.7 | 22 | ≈11 items ⚠ |
| gpt-5.5 | 20 | ≈10 items ⚠ |
| llama-3.3-70b | 7 | ⚠ |
| qwen2.5-72b | 7 | ⚠ |
| mistral-large-2 | 3 | ⚠ |

### exp-003 Threshold Check

> **需求**: ≥5 judges × ≥6 models × ≥20 items/cell

| 模型群组 | 模型数 | 达标 judges 数 | 状态 |
|----------|--------|---------------|------|
| 核心 7 模型 (gpt-3.5, gpt-4-0314, gpt-4-0613, gpt-4o, gpt-4o-mini, llama-3.3-70b, qwen2.5-72b) | 7 | ≥7 judges | **PASS** |
| 新增 2 模型 (gemma-2-9b, qwen3-8b) | 2 | ≤2 judges | **FAIL** |

**THRESHOLD: LIKELY MET** — 核心 7 模型已满足 ≥6 模型要求。gemma-2-9b / qwen3-8b 覆盖仍不足，但 7 个 collect.py 刚启动正在补数据。

---

## Check 6: exp-002 状态

**已完成。**

| 项目 | 值 |
|------|-----|
| Items | 493 |
| Judges | 10 |
| Target models | gpt-3.5-turbo-0125, gpt-4-0613 |
| Reference | gpt-4-0314 |
| e_i 均值 | 0.236 |
| 高暴露 items | 19 (3.9%) |
| 进程 | 无 (已完成) |

产出文件：exposure_scores.csv/json, model_abilities.csv, summary.json 等 7 个文件。

---

## Check 7: Response 生成进度

| 模型 | 行数 | 状态 |
|------|------|------|
| gpt-3.5-turbo-0125 | 500 | 完成 |
| gpt-4-0314 | 500 | 完成 |
| gpt-4-0613 | 500 | 完成 |
| gpt-4o | 500 | 完成 |
| gpt-4o-mini | 500 | 完成 |
| llama-3.3-70b | 500 | 完成 |
| qwen2.5-72b | 500 | 完成 |
| gemma-2-9b | 500 | 完成 |
| qwen3-8b | 500 | 完成 |
| claude-opus-4.7 | **291** | **未完成 (58%)** |
| gpt-5.5 | **197** | **未完成 (39%)** |
| mistral-large-2 | **209** | **未完成 (42%)** |

**无活跃 generate 进程。** 3 个模型的 response 生成处于暂停状态。

---

## 关键发现

1. **exp-009** 正常推进，57% 完成，预计还需 ~8h
2. **3 个 vLLM** 全部在线运行
3. **7 个 judge collector 刚启动**，正在为 9 judge × 9 model 补充判断数据
4. **exp-003 threshold 大概率已达标**（核心 7 模型满足），但 gemma-2-9b / qwen3-8b 仍需补数据
5. **3 个模型 response 生成未完成**（claude-opus-4.7, gpt-5.5, mistral-large-2），且无生成进程在跑

---
