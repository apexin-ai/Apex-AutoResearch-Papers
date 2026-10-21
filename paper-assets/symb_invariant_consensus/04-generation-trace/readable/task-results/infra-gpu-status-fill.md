# infra gpu status fill

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-status-fill_20260522T234133_result.json`
- **Structured JSON:** [`4a7486c43e0019749f0f.json`](../../sessions/4a/4a7486c43e0019749f0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态报告

### westd-16639（4x RTX PRO 6000 Blackwell, 96GB）

| GPU | 利用率 | vLLM PID | 模型 | 端口 | 实验 | 进度 | 状态 |
|-----|--------|----------|------|------|------|------|------|
| 0 | 97% | 662462 | Qwen2.5-14B | 8001 | PW seed456→seed789 chain | 212/600 | **RUNNING** |
| 1 | 97% | 684518 | LLaMA-8B | 8006 | PW seed123 multiseed chain | 168/600 | **RUNNING** |
| 2 | **0%** | 711593 | Qwen2.5-14B | 8007 | PW seed789 | 0/600 | **IDLE — runner 已崩溃** |
| 3 | 98% | 681007 | Qwen2.5-14B | 8005 | PW seed123 rerun | 192/600 | **RUNNING** |

### westd-14391（1x RTX PRO 6000 Blackwell, 96GB）

| GPU | 利用率 | vLLM PID | 模型 | 端口 | 实验 | 进度 | 状态 |
|-----|--------|----------|------|------|------|------|------|
| 0 | 100% | 9816 | LLaMA-8B | 8000 | PW seed42 | 240/600 | **RUNNING** |

---

### 空闲卡：westd-16639 cuda:2（1张）

**故障原因：** 实验 runner 在 vLLM 就绪前启动，`APIConnectionError: Connection error` 后崩溃退出。vLLM 后来成功加载但无人使用。此外 vLLM 配置了 `max_model_len=4096` + 实验 `max_tokens=4096`，无空间容纳 prompt，即使重连也会报错。

**当前状态：** vLLM Qwen2.5-14B 在 port 8007 空转，88GB 显存被占用，GPU 利用率 0%。

### 可启动实验建议

注意 GPU 0 已 chain 了 seed456→seed789，seed456 完成后会自动在 port 8001 跑 seed789。所以 GPU 2 不应再跑 PW seed789（会重复）。

**推荐在 GPU 2 上跑：**
1. **Qwen2.5-14B FOLIO seed123/456/789**（exp-multi-seed-qwen25 FOLIO 部分）— 模型已加载，只需重启 vLLM 修正 `max_model_len`（改为 8192+），然后启动 FOLIO 实验
2. 或者 kill 当前 vLLM，换模型跑 **Qwen2.5-7B FOLIO**（exp-multi-seed-qwen25-7b-folio，未开始）

两种都需要先 kill port 8007 的 vLLM 再重启（修 `max_model_len`）。

---
