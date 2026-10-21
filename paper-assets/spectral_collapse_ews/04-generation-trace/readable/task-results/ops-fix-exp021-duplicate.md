# ops fix exp021 duplicate

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-exp021-duplicate_20260524T040606_result.json`
- **Structured JSON:** [`acb29326c9cf3134e7ce.json`](../../sessions/ac/acb29326c9cf3134e7ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 进程清理
- **已杀**: PID 845033 (+ 父进程 845028, timeout 845032) — 10:27:50 启动，无 HF_HUB_OFFLINE，旧的错误提交
- **保留**: PID 846799 (wrapper 846794) — 10:45:52 启动，带 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1，修复版

### 2. exp_021 当前进度
完成 2 个 generation (gen 0, gen 1)，正在跑 gen 2：
| Gen | r_eff | SLV |
|-----|-------|-----|
| 0 | 23.09 | 689.44 |
| 1 | 121.17 | 760.73 |

（PPL 字段未写入结果文件）

### 3. exp_020 进度
已完成 8 个 generation (gen 0–7)。

### 4. GPU 状态
| GPU | Util | 显存使用 |
|-----|------|---------|
| 0 | 94% | 26431 / 97887 MiB (exp_020) |
| 1 | 97% | **26431** / 97887 MiB (exp_021，从 52858 降到 26431，释放了 ~26 GB) |

### 5. tmux
只有 2 个 session：`exp_020` 和 `exp_021`，无重复，无需清理。

---
