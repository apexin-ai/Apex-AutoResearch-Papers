# infra full status check may22

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_full-status-check-may22_20260521T214027_result.json`
- **Structured JSON:** [`8bfc5ef3acf5f81056a0.json`](../../sessions/8b/8bfc5ef3acf5f81056a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。汇总如下：

---

## 巡检报告 (2026-05-21)

### westd-16639

| 实验 | 进度 | 完成% | 状态 | 备注 |
|------|------|-------|------|------|
| **Cross-model SICA 2×2** (PID 414515) | 204/204 × 4 dirs | **100%** | ✅ 完成 | results.json 已生成，含 SICA/McNemar/Fleiss kappa |
| **Qwen3→Mistral fix** (reextract) | 204/204 | **100%** | ✅ 完成 | 之前 87/152，现已全部完成 |
| **Gemini cross-model extraction** | 95/95 | **100%** | ✅ 完成 | Cross-model SICA=86.3%, Original=87.4%, SC=87.4% |

**Cross-model SICA 结果概览** (results.json):

| 条件 | Accuracy |
|------|----------|
| Mistral SC@12 | 40.2% |
| Mistral same-SICA | 34.3% |
| Mistral cross-SICA (by Qwen3) | 37.7% |
| Qwen3 SC@12 | 86.8% |
| Qwen3 same-SICA | 79.9% |
| Qwen3 cross-SICA (by Mistral) | 79.9% |

**GPU 状态**: 3 台 vLLM 服务加载但空闲 (0% util)

| GPU | VRAM 占用 | 用途 |
|-----|-----------|------|
| 0 | 84.2/97.9 GB | vLLM Mistral (port 8000) |
| 1 | 83.6/97.9 GB | vLLM Qwen3-14B (port 8001) |
| 2 | 0/97.9 GB | 空闲 |
| 3 | 89.8/97.9 GB | vLLM Mistral (port 8004) |

**异常**: 2 个 python3 进程 (PID 427876/427984) 正在下载 sentence-transformers/all-MiniLM-L6-v2，已运行 ~10h，可能卡住。

---

### westd-25068

| 实验 | 进度 | 状态 |
|------|------|------|
| **70B AWQ SICA** (PID 40007) | 之前 61/204 | ❌ **SSH 认证失败，无法检查** |
| **Gemini SC API** | 之前 85/204 | ❌ **SSH 认证失败，无法检查** |

**westd-25068 完全不可达**（Authentication failed）。可能实例重启导致端口/密钥变更，需去控制台确认 SSH 配置。

---
