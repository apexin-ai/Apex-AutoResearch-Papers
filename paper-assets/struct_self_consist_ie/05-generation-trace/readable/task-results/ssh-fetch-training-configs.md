# ssh fetch training configs

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fetch-training-configs_20260520T073700_result.json`
- **Structured JSON:** [`8f818d156324b047d2b1.json`](../../sessions/8f/8f818d156324b047d2b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

42 个文件全部到位。汇总如下：

## 取回文件汇总

**本地路径**: `artifacts/configs/`，共 **42 个 YAML 配置文件**

| 来源服务器 | 文件数 | 独有文件 |
|-----------|--------|---------|
| autodl-5090 | 36 (34 公共 + 2 独有) | `*_qwen25_32b_fewnerd*` |
| autodl-5090-b | 34 (全部公共) | 无 |
| autodl-5090-c | 40 (34 公共 + 6 独有) | `*_qwen25_14b_fewnerd*`, `*_qwen25_7b_fewnerd*`, `*_qwen25_7b_wnut17*` |

## autodl-5090-c GPU 状态

| GPU | 型号 | 显存占用 | 利用率 |
|-----|------|---------|--------|
| 0 | RTX 5090 | 25,885 / 32,607 MiB | 96% |
| 1 | RTX 5090 | 25,827 / 32,607 MiB | 75% |
| 2 | RTX 5090 | **0 / 32,607 MiB** | **0%** |
| 3 | RTX 5090 | **0 / 32,607 MiB** | **0%** |

- GPU 0,1 正在运行 `train_config_qwen25_14b_fewnerd_s42.yaml` 训练（2-GPU DDP，screen session `train_14b_s42`）
- **无 vLLM / run_mvp 残留进程**
- **cuda:2,3 完全空闲**，可用于新任务

---
