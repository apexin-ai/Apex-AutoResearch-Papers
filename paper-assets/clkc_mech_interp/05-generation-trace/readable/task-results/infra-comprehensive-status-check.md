# infra comprehensive status check

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_comprehensive-status-check_20260522T064705_result.json`
- **Structured JSON:** [`ef8a487a141072100c74.json`](../../sessions/ef/ef8a487a141072100c74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/status_check_20260522.md`。摘要如下：

---

### 1. XNLI MLP 探针 — 结果已生成

| 模型 | EN→EN | ZH→ZH | EN→ZH | ZH→EN |
|------|-------|-------|-------|-------|
| Qwen3 | 0.966 (L23) | 0.910 (L26) | 0.884 (L30) | **0.975** (L22) |
| Llama31 | 0.930 (L15) | 0.885 (L15) | 0.885 (L19) | **0.947** (L13) |

两模型 ZH→EN 均高于 EN→ZH，与线性探针一致。MLP 进程仍在运行但结果 JSON 已完整。

### 2. Gemma translate ZH — 40.8% (520/1274)
tmux 运行中，~2h 后完成。

### 3. Bootstrap n=2000 (plan_111) — 未启动
`data/qwen3/` 和 `data/llama31/` 下无 bootstrap n=2000 文件，无相关进程。XNLI 目录下的 bootstrap 是线性探针的，两模型不对称性均显著（CI 不含零）。

### 4. COMET 验证 — 反向翻译进行中
- Qwen train: 660/798 back-translated (82.7%)
- Llama train: 660/1096 back-translated (60.2%)
- test split 已完成但通过率很低：Qwen 18.5%, Llama 27.9% (threshold=0.8, mean COMET ~0.70)

### 5. GPU
3/4 GPU 在用（GPU 0/1/2 各 ~16.5GB），GPU 3 完全空闲，利用率整体偏低（9-18%）。MLP 跑在 CPU 上。

---
