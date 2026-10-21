# ops check 009d submit 018

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-009d-submit-018_20260516T013625_result.json`
- **Structured JSON:** [`974fdb409d979a03e509.json`](../../sessions/97/974fdb409d979a03e509.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 009d 状态
- 进程: **ALIVE** (PID 149708, 已运行 13.2h)
- 当前 step: **308000 / 500000** (61.6%)
- 最近 eval_return:
  - 238K: 765.9 → 248K: 733.6 → 258K: 758.2 → 268K: 704.9
  - 278K: 802.2 → 288K: 845.7 → **298K: 913.3 → 308K: 925.9**
- FPS: 7.2, train_return 隐含在 value_mean≈629
- cuda:0 空闲: **NO**

## 010a 状态
- 进程: **ALIVE** (PID 536890, 已运行 2.8h)
- 当前 step: **112000 / 512000** (21.9%), train_return=346.1
- 最近 eval_return:
  - 55K: 212.2 → 65K: 330.6 → 75K: 377.6 → 85K: 403.5 → 95K: 390.0 → **105K: 420.7**

## GPU
- GPU 0: 4165 MiB used, 93088 MiB free, 18% util (009d)
- GPU 1: 4690 MiB used, 92563 MiB free, 38% util (010a)

## Git 状态
- HEAD = **06ab285** (Fix Full-SGS: restore dt_emb.weight.requires_grad_(True) after imagination) ✓
- 最近 commits:
  - `06ab285` Fix Full-SGS: restore dt_emb.weight.requires_grad_
  - `5fc8e49` Implement Full-SGS: block all head loss gradients
  - `dccb867` plan_015B: replace detach with freeze for dt_emb
  - `09876d7` fix: guard nn.Embedding creation when dt_embed_dim=0
  - `14c410d` bernoulli_physical_horizon: default 30, support 0=uncapped
- **uncommitted 改动: YES** — `dreamer.py` (+10/-2), `tools.py` (+16/-3)

---

**结论：009d 尚未完成**，还在 308K/500K，预计还需约 7.4h（按 7.2 FPS 算约 192K steps ÷ 7.2 ≈ 26667s ≈ 7.4h）。018 提交需等 009d 跑完。另外工作目录有未提交改动，提交前需要处理。

---
