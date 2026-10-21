# ops verify kill start rp r2 eval cuda3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-kill-start-rp_r2-eval-cuda3_20260514T214030_result.json`
- **Structured JSON:** [`a94760f25e12c1f66284.json`](../../sessions/a9/a94760f25e12c1f66284.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

| 项目 | 状态 |
|------|------|
| rp_r2 训练 (PID 94758) | **DEAD** — 已确认 killed |
| cuda:3 | 启动前空闲 ✓，eval 已占用 4870 MiB |
| rp_r2 ckpt-20 eval | **PID 103825** (子进程 103831)，模型加载中，正在 merge SFT adapter |

**全卡快照：**

| GPU | Util | VRAM |
|-----|------|------|
| 0 | 97% | 13645 / 32607 MiB |
| 1 | 64% | 10653 / 32607 MiB |
| 2 | 70% | 9719 / 32607 MiB |
| 3 | 8% | 4879 / 32607 MiB ← eval loading |

---
