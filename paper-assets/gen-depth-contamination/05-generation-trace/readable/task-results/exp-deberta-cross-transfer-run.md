# exp deberta cross transfer run

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_deberta-cross-transfer-run_20260519T201151_result.json`
- **Structured JSON:** [`dee368ce3f781b31fa83.json`](../../sessions/de/dee368ce3f781b31fa83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认成功。汇总：

**启动状态**

| GPU | 利用率 | 显存 | Wrapper PID | Python PID | 当前任务 (第1对) |
|-----|--------|------|-------------|------------|-----------------|
| cuda:1 | 97% | 18991/24564 MiB | **208306** | 208325 | wiki_pythia→wiki_olmo |
| cuda:2 | 97% | 19809/24564 MiB | **208307** | 208328 | wiki_olmo→wiki_qwen7b |
| cuda:3 | 99% | 19809/24564 MiB | **208308** | 208329 | wiki_olmo→wiki_llama8b |

**分配的 pair 列表**
- **GPU 1** (208306): pythia→olmo, olmo→pythia, pythia→qwen7b, qwen7b→pythia
- **GPU 2** (208307): olmo→qwen7b, qwen7b→olmo, pythia→llama8b, llama8b→pythia
- **GPU 3** (208308): olmo→llama8b, llama8b→olmo, pythia→mistral7b, mistral7b→pythia

**监控用 PID**: wrapper 进程 208306, 208307, 208308（会依次跑各自的 4 个 pair，python PID 每个 pair 会变）。

**日志**: `results/deberta_cross_transfer/gpu{1,2,3}.log`

**修复**: 脚本因 transformers 新版 adapter_config 联网检查而崩溃，通过设置 `HF_HUB_OFFLINE=1` 解决。

**预估**: 每 pair ~25min × 4 pairs = ~100min/GPU，约 04:19 开始，预计 ~06:00 CST 全部完成。

---
