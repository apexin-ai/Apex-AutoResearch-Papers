# infra urgent cpu status check

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_urgent-cpu-status-check_20260523T034512_result.json`
- **Structured JSON:** [`f94dc4a37641d66bfefc.json`](../../sessions/f9/f94dc4a37641d66bfefc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。以下是完整报告：

---

## DE probe n=2000 (PID 496671)
**进程状态: alive — 但严重落后，预计无法在 DDL 前完成**
- 运行时间: 12h33m
- 当前进度: EN→EN 方向 1700/2000（第 1 个方向，共 9 个方向）
- 输出文件 `de_probe_results_bootstrap_n2000.json` **尚未生成**
- 估算剩余: ~120h（~5天）→ **远超 May 25 DDL**
- **根因**: 使用的是串行 `train_probe.py`，没有多进程并行

**现有 DE 方向数据: 无。** 所有已完成的 probe 结果（`probe_results.json`, `probe_results_bootstrap_n2000.json`）仅含 EN/ZH 方向。

## 现有 Llama EN/ZH bootstrap n=2000 (已完成)
```
EN→EN: 75.1% (L19), CI=[71.7, 78.3]
ZH→ZH: 69.7% (L13), CI=[65.8, 73.5]
EN→ZH: 60.8% (L13), CI=[52.2, 68.4]
ZH→EN: 68.0% (L15), CI=[55.5, 75.4]
Δ_asym: +7.27pp [0.37, 13.97], p=0.038, n_seeds=2000
```

## Gemma XNLI bootstrap n=2000 (PID 507589)
**进程状态: alive — 在跑但进度不明**
- 运行时间: 9h18m, CPU 131%, 127 线程
- 日志只显示 `[EN→EN] Bootstrap (2000 seeds, 64 workers)...`，EN→EN 方向尚未完成
- 输出到 `data/xnli/gemma2/probe_results.json`（将覆盖基础结果）

**现有 Gemma XNLI 基础结果（单 seed，无 bootstrap CI）:**
```
EN→EN: 95.6% (L20)
ZH→ZH: 89.0% (L24)
EN→ZH: 89.4% (L28)
ZH→EN: 97.5% (L21)
```

## GPU
```
cuda:0: RTX PRO 6000 Blackwell 0/96GB 33°C 0%
cuda:1: RTX PRO 6000 Blackwell 0/96GB 32°C 0%
cuda:2: RTX PRO 6000 Blackwell 0/96GB 32°C 0%
cuda:3: RTX PRO 6000 Blackwell 0/96GB 32°C 0%
```

---

## 紧急问题

**服务器 load average 331-563**，两个 CPU 进程严重争抢。

**DE probe 必须处理**——当前串行脚本不可能在 DDL 前完成 9 个方向 × 2000 seeds。建议：

1. **Kill PID 496671**，改用并行版本（类似 `bootstrap_n2000.py`，适配 3 语言 en/zh/de）。用 64 workers 估计每方向 1-2h，9 方向 ≈ 9-18h，可以赶上 DDL。
2. Kill 后也能减轻 Gemma 进程的 CPU 争抢，加速其完成。

是否要我立即写一个 3 语言并行 bootstrap 脚本并重启 DE probe？

---
