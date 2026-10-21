# harvest eval openvla l2norm k075 long seed42 v2 and cascade

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval_openvla_l2norm_k075_long_seed42_v2_and_cascade_20260527T133405_result.json`
- **Structured JSON:** [`030cb90c7e6d8696eb1c.json`](../../sessions/03/030cb90c7e6d8696eb1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Part 1: eval_openvla_l2norm_k075_long_seed42_v2 → DONE

**Overall SR: 34.0% (170/500)** — 与 ROADMAP 预期一致。

Per-task breakdown:

| Task | SR | Count |
|------|----|-------|
| T1 alphabet_soup + tomato_sauce → basket | 46% | 23/50 |
| T2 cream_cheese + butter → basket | 48% | 24/50 |
| T3 stove + moka_pot | 48% | 24/50 |
| T4 black_bowl → drawer | 14% | 7/50 |
| T5 white_mug left + yellow_mug right | 14% | 7/50 |
| T6 book → caddy | **68%** | 34/50 |
| T7 white_mug plate + chocolate_pudding | 30% | 15/50 |
| T8 alphabet_soup + cream_cheese → basket | 46% | 23/50 |
| T9 both moka_pots → stove | 12% | 6/50 |
| T10 yellow_white_mug → microwave | 14% | 7/50 |

L2norm Long cliff curve 补完：k=0.85→38.8%, **k=0.75→34.0%**, k=0.7→31.2%

Registry 已更新：metrics + conclusion=success + checkpoint_path + status=DONE。

---

## Part 2: westd-38929 GPU2 状态

**GPU2 空闲** — 1MiB 显存，0% 利用率，无进程。

其余 GPU 占用：
- GPU0: 16.2GB, 65% util (python PID 272022)
- GPU1: 16.2GB, 81% util (python PID 266221)
- GPU3: 10.4GB, 16% util (python PID 250745)

（`tmux ls` 被 read-only 模式拦截，无法列出 sessions。）

**GPU2 可用于 cascade 部署。**

---
