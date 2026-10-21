# infra fix gpu conflict and download

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix_gpu_conflict_and_download_20260521T165857_result.json`
- **Structured JSON:** [`36038f516a2382f306aa.json`](../../sessions/36/36038f516a2382f306aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### Fix 1: westd-32570 — GPU 冲突不存在，无需操作

实际状态与预期不同。**4 张 GPU 各有一个独立进程，没有冲突：**

| GPU | PID | 任务 | 进度 (lines) | 目标 | 利用率 |
|-----|--------|------|------|------|--------|
| 0 | 166536 | Qwen MATH | 54800 | 57600 | 70% |
| 1 | 177670 | InternLM MMLU | 42000 | ~57600 | 100% |
| 2 | 167468 | Gemma MATH | 39200 | 57600 | 97% |
| 3 | 178495 | DeepSeek MMLU | 39600 | ~57600 | 100% |

- Qwen MATH 接近完成（95.1%），GPU 0 利用率降至 70% 是正常的尾部行为
- Gemma MATH 在 GPU 2 独占运行，97% 利用率，没有退化
- DeepSeek MMLU 在 GPU 3 独占运行，不在 GPU 3 上与 Gemma 共享
- 所有进程的 `--gpu-id 0` 是因为各自 `CUDA_VISIBLE_DEVICES` 只暴露一张卡

**建议：不执行 kill/重启操作，保持现状。**

---

### Fix 2: westd-19912 — 下载进行中，network_turbo 已生效

- **network_turbo**: 已执行，proxy 环境变量已设
- **OLMo 下载** (ModelScope, PID 48244): 3 个 safetensors 分片，约 45-48% 完成，~450 KB/s
- **Yi 下载** (ModelScope, PID 48610): 4 个分片，40-72% 完成，~435-451 KB/s
- **总缓存**: 62G（含已下载的 Qwen、Mistral 模型）
- **ETA**: 约 **1.5-2 小时**（~02:30-03:00）

无需额外操作。速度受限于 ModelScope CDN / AutoDL 带宽，已是加速状态。

---

### Fix 3: westd-15695 — auto_chain 正常运行

- **当前任务**: Yi GSM8K（PID 31108，`--resume`），VLLM 引擎 PID 31314
- **Yi GSM8K 进度**: 3600 / 86400（4.2%）
- **GPU 0**: 89094 MiB / 97887 MiB，95% 利用率

**已完成 benchmarks:**
| 模型 | ARC | GSM8K | MMLU |
|------|-----|-------|------|
| OLMo | 86400 ✓ | 86400 ✓ | 86400 ✓ |
| Yi | 86400 ✓ | 3600/86400 🔄 | 86400 ✓ |

auto_chain 自动推进，不需要干预。

---

### 3 台服务器 GPU 状态汇总

| 服务器 | GPU | 任务 | 状态 | 备注 |
|--------|-----|------|------|------|
| westd-32570 | 0 | Qwen MATH | 95% done | 即将完成 |
| westd-32570 | 1 | InternLM MMLU | 73% done | 正常 |
| westd-32570 | 2 | Gemma MATH | 68% done | 正常，无冲突 |
| westd-32570 | 3 | DeepSeek MMLU | 69% done | 正常，独占 |
| westd-19912 | — | 模型下载 | 45% | ETA ~1.5-2h |
| westd-15695 | 0 | Yi GSM8K | 4.2% | auto_chain 运行中 |

---
