# ssh olmo rescue

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_olmo_rescue_20260514T170614_result.json`
- **Structured JSON:** [`19ea8c5ff9df84429ff4.json`](../../sessions/19/19ea8c5ff9df84429ff4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. OLMo (PID 150550) — 存活，正在生成 depth-1
- **PID 存活**，已运行 32 分钟，状态 `S+`
- depth_0 训练已完成（final loss 2.2686，LoRA adapter 已保存）
- 正在执行 Step 2：加载 OLMo-1B 模型生成 depth-1 数据
- 进度：
  - `depth_0.jsonl`: 5000 lines（完成）
  - `depth_1.jsonl`: 4830 lines（生成中，接近完成）
  - `depth_2.jsonl`: 不存在
  - `depth_3.jsonl`: 不存在

### 2. GPT-2 XL (PID 123650) — 存活，正在生成 depth-2
- **PID 存活**，已运行 2 小时 24 分钟
- depth_1 训练已完成，LoRA adapter 已保存
- 正在执行 Step 4：加载 GPT-2 XL 模型生成 depth-2 数据
- 进度：
  - `depth_0.jsonl`: 5000 lines（完成）
  - `depth_1.jsonl`: 5000 lines（完成）
  - `depth_2.jsonl`: 4991 lines（生成中，接近完成）

### 3. GPU 利用
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| GPU 0 | 63% | 9,973 / 97,887 MiB |
| GPU 1 | 77% | 15,641 / 97,887 MiB |

两个进程都正常运行，未被杀死。GPT-2 XL 进度领先，OLMo 落后约一个 step。

---
