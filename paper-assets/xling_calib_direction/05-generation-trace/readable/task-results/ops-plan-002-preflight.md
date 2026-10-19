# ops plan 002 preflight

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan_002_preflight_20260521T122448_result.json`
- **Structured JSON:** [`d3a86ef0eeef4fffb5ae.json`](../../sessions/d3/d3a86ef0eeef4fffb5ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Pre-flight 检查结果

| # | 检查项 | 状态 |
|---|--------|------|
| 1 | PID 482839 | **已 kill**（force killed），GPU 显存已释放 |
| 2 | 4 卡 GPU | **全部空闲** — 4× NVIDIA RTX PRO 6000 Blackwell (96GB)，各 3MiB 占用，0% 利用率，无进程 |
| 3 | 磁盘空间 | 数据盘 `/root/autodl-tmp/`：**99GB 可用**（350G 用 252G，72%）；根分区：**29GB 可用**（30G 用 1.5G） |
| 4 | Qwen3 模型 | **32/32 shards 完整** ✓ — 注意实际目录名是 `Qwen3-235B-GPTQ-Int4`（非 `Qwen3-235B-A22B-GPTQ-Int4`） |
| 5 | Llama4 模型 | **14/14 shards 完整** ✓ |

全部就绪，可以提交。

---
