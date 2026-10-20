# ops fix 14b mauve none 17855

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-14b-mauve-none-17855_20260522T083509_result.json`
- **Structured JSON:** [`da64567e1bab31b5c01f.json`](../../sessions/da/da64567e1bab31b5c01f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Clean — only my new session exists on 19828. Here's the complete summary:

---

## 诊断结果

**根因**: MAUVE 计算内部加载 `gpt2-large` 模型，但实验命令设置 `HF_HUB_CACHE=/root/autodl-tmp/.hf_cache`（错误），实际模型缓存在 `.hf_cache/hub/` 子目录下。应使用 `HF_HOME=/root/autodl-tmp/.hf_cache`（transformers 自动追加 `hub/`）。次要原因：format string `metrics['mauve']:.4f` 遇到 None 时崩溃。

## 修复

| 文件 | 服务器 | 修改 |
|------|--------|------|
| `iterative_train.py` | 17855 | `.get('mauve', float('nan')):.4f` → `_mauve_s` None 检查 |
| `metrics.py` | 17855 | MAUVE fallback: `float("nan")` → `None` |
| `metrics.py` | 19828 | 同上 |
| `iterative_train.py` | 19828 | 已有 `_mauve_s` 修复（无需改动） |

## 重启实验

| 实验 | 服务器 | GPU | tmux session | --start_gen | 状态 |
|------|--------|-----|-------------|-------------|------|
| t10_a075_s42_fp32_14b | 17855 | cuda:2 | `scale_14b_t10_a075_v2` | 2 | gen_2 synth data |
| t10_a060_s42_fp32_14b | 17855 | cuda:3 | `scale_14b_t10_a060_v2` | 2 | gen_2 synth data |
| t10_a050_s42_fp32_14b | 19828 | cuda:1 | `scale_14b_t10_a050_v2` | 2 | gen_2 synth data |

重启命令使用 `HF_HOME`（而非 `HF_HUB_CACHE`），MAUVE 应能正常计算。

## 在跑实验状态

| 实验 | 服务器 | GPU | PID | 进度 | MAUVE |
|------|--------|-----|-----|------|-------|
| t15_a060_s42_fp32_14b | 17855 | cuda:0 | 643575 | gen_2/15 synth | null（旧 env var，全程无法计算） |
| t15_a050_s42_fp32_14b | 17855 | cuda:1 | 643883 | gen_2/15 synth | null（同上） |

这两个在跑实验因进程内存中的旧 env var 无法修复 MAUVE，将全程 null。其他指标（ppl/entropy/eff_rank/distinct_n/self_bleu/ece）均正常。如需完整 MAUVE，需要重启这两个实验。

---
