# code regen bootstrap n2000

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_regen-bootstrap-n2000_20260525T201348_result.json`
- **Structured JSON:** [`7eb6270d106abfb5b203.json`](../../sessions/7e/7eb6270d106abfb5b203.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

ZH activations 只在 `gemma2_v2` 目录下存在，Llama 和 Qwen 均缺失。

## 结果报告

**无法执行 bootstrap probe 训练。** 前置条件不满足：

### 缺失文件
| 模型 | 缺失文件 | 说明 |
|------|----------|------|
| Llama-3.1 | `/root/clkc_mech_interp/data/llama31/zh_activations.pt` | 需要 GPU 重新生成 |
| Qwen-3 | `/root/clkc_mech_interp/data/qwen3/zh_activations.pt` | 需要 GPU 重新生成 |

### 已有文件
- `data/llama31/en_activations.pt` (400MB, 2026-05-24)
- `data/qwen3/en_activations.pt` (399MB, 2026-05-24)
- ZH activations 仅存在于 `data/gemma2_v2/zh_activations.pt`

### 影响
Bootstrap n=2000 需要 EN 和 ZH 两个语言的 activations 才能产出 4 方向数据（EN→EN, ZH→ZH, EN→ZH, ZH→EN）。仅有 EN 无法生成论文所需的跨语言对比数据和 asymmetry CI。

### 下一步
需要先用 GPU 运行 `collect_activations.py` 生成 Llama 和 Qwen 的 ZH activations，之后才能执行 bootstrap probe 训练。

---
