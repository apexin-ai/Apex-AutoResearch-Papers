# analysis mistral folio final and qwen7b deploy

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mistral-folio-final-and-qwen7b-deploy_20260522T121013_result.json`
- **Structured JSON:** [`307a5003d54d42becc41.json`](../../sessions/30/307a5003d54d42becc41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载速度很慢（~300KB/s），可能是 proxy 干扰了 ModelScope CDN。但主要阻塞因素是 **cuda:3 仍被 Mistral FOLIO multiseed 脚本占用**（seed=456 刚开始，后面还有 seed=789）。

---

## 报告

### 1. Mistral FOLIO seed=789 最终结果
| 指标 | 值 |
|------|-----|
| n | 204 |
| SC | **59.31%** (121/204) |
| SICA | **56.86%** (116/204) |
| Δ (SICA-SC) | **-2.45pp** |
| Wall time | 4798s (~80min) |

bonus — seed=123 也已完成：
| 指标 | 值 |
|------|-----|
| n | 204 |
| SC | **57.84%** (118/204) |
| SICA | **57.84%** (118/204) |
| Δ | **0.00pp** |

### 2. vLLM 清理状态
**❌ 无法清理。** Mistral multiseed 脚本 (PID 575733) 仍在运行：
- seed=123 ✅ 完成
- seed=456 🔄 刚启动 (20:02, [1/204])，预计 ~80min 完成
- seed=789 ⏳ 排队中（脚本会重跑，覆盖已有结果）

所有 4 GPU 占满：
- cuda:0 → Qwen2.5-14B (port 8005) — PW 实验
- cuda:1 → Llama-3.1-8B (port 8002) — FOLIO 实验
- cuda:2 → Mistral-7B (port 8003) — PW 实验
- cuda:3 → Mistral-7B (port 8004) — FOLIO seed=456 进行中

### 3. Qwen2.5-7B 模型
**MODEL_MISSING** — 服务器上不存在。已启动 ModelScope 后台下载 (PID 605164)，但速度仅 ~300KB/s，15GB 模型预计需数小时。

### 4. vLLM 部署
**⏸ 阻塞** — cuda:3 被占用 + 模型下载中。

### 5. 脚本路径
✅ `/root/symb_invariant_consensus/scripts/multiseed_qwen25_7b_folio_cuda3.sh`（已创建，未启动）

### 建议时间线
Mistral FOLIO multiseed 预计还需 ~2.5h（seed=456）+ ~1.3h（seed=789 重跑）≈ 4h。之后可杀 vLLM、部署 Qwen2.5-7B。模型下载应在此之前完成（如果速度不回升可能需要换方案）。

---
