# diag tracvla spatial status

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_tracvla_spatial_status_20260521T155509_result.json`
- **Structured JSON:** [`97c4dcafedf73ca46e04.json`](../../sessions/97/97c4dcafedf73ca46e04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 实验 1: tracvla_spatial_trained (PID 521837)

**状态: CRASHED (被 kill，EXIT_CODE=143)**

日志显示 Phase 1（representation extraction, 5000 samples）正常完成，进入 Phase 2（action R2 probing）后被 `Terminated`（SIGTERM, exit code 143）。不是正常结束。

**结果文件**: 无。这个进程在 Phase 2 中被杀，没有产出结果文件。

### 实验 2: tracvla_spatial_full_v2

**状态: COMPLETED (trained 部分), FAILED (untrained 部分)**

- **trained condition**: 正常跑完所有 5 个 Phase，耗时 160 分钟。`EXIT_CODE=0`。
- **untrained condition**: 加载 `/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/` 时报错 **FlashAttention2 未安装**，跳过了 untrained condition。

**结果文件** (`/root/autodl-tmp/vla-ssd/results/tracvla_spatial/trained/`):
- `action_r2_probing.json` (6.3KB)
- `counterfactual_combined.json` (31KB)
- `cross_instruction_classification.json` (1.7KB)
- `l1_attention_profile.json` (5KB)

**untrained 目录**: `/root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained/` 存在但**为空**。

### pipeline 日志 (tracvla_spatial_pipeline.log)

这是一个更早的运行（与 full_v2 不同的实例），同样在 untrained 阶段失败——但原因是**网络不可达**（HuggingFace 连接失败，没有 `source /etc/network_turbo`），被 OOM killer 杀掉（EXIT_CODE=129/137）。

### 关键问题

1. **trained condition 数据齐全**（来自 full_v2），4 个结果 JSON 已产出
2. **untrained condition 缺失**——full_v2 因 flash-attn 未安装失败，pipeline 因网络问题失败
3. 要补齐 untrained 数据，需要：安装 `flash-attn`，或者加载 untrained 模型时禁用 FlashAttention2（设 `attn_implementation="eager"`）

---
