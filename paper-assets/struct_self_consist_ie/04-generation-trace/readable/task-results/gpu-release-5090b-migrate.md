# gpu release 5090b migrate

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_release_5090b_migrate_20260521T090651_result.json`
- **Structured JSON:** [`fc69bb7c7c8e6fbb6669.json`](../../sessions/fc/fc69bb7c7c8e6fbb6669.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 全部更新完成。现在汇总结果。

---

## 执行结果

### 1. 5090-b 状态

**无法连接**（端口 11496 连接失败）。AutoDL 实例可能已关机或端口已变。如果实例仍在运行，需要去控制台查新端口更新 `~/.ssh/config`。如果已关机，则无需清理，可直接释放。

### 2. 5090 MF4 s456 — 已完成 ✓

| 指标 | 值 |
|------|-----|
| verdict | MARGINAL |
| greedy_f1 | 0.789 |
| oracle_f1 | 0.881 |
| oracle_headroom | 0.092 |
| structural_beats_surface | true |
| rho_advantage | 0.149 |
| softjaccard ρ (full/cond) | 0.313 / 0.257 |
| fleiss ρ (full/cond) | 0.165 / 0.015 |
| logprob ρ (full/cond) | 0.245 / 0.238 |

### 3. SciERC MF4 s42 — 已在 5090 GPU 0 启动 ✓

- exp_id: `exp_scierc_mf4_v2_s42`, PID 18393, GPU cuda:0
- 模型: `checkpoints/qwen3-8b-scierc-merged-v2`

### 4. 5090-c 完成实验

| 实验 | 状态 | verdict | greedy_f1 | ρ_adv |
|------|------|---------|-----------|-------|
| conll_n16_seed123_v2 | DONE (success) | PASS | 0.907 | +0.010 |
| conll_n16_seed456_v2 | DONE (success) | PASS | 0.908 | +0.009 |
| e2_pretrained_scierc | DONE (negative) | FAIL | 0.242 | -0.032 |
| fewnerd_n16_seed456_v2 | RUNNING | — | — | — |

### 5. 三台服务器 GPU 分配表

| 服务器 | GPU 0 | GPU 1 | GPU 2 | GPU 3 |
|--------|-------|-------|-------|-------|
| **5090** | `exp_scierc_mf4_v2_s42` (新启) | 空闲 | 空闲 | `exp_e2_pretrained_fewnerd` |
| **5090-b** | 连接失败，无法确认 | — | — | — |
| **5090-c** | `exp_fewnerd_n16_s456_v2` (运行中) | 空闲 | 空闲 | 空闲 |

> 5090-c 还有一个 API-based `frontier_sc_gemini25pro` 在跑（不占 GPU）。

**5090-b 需要你确认：是已关机可以直接释放，还是需要去 AutoDL 控制台查新端口？**

---
