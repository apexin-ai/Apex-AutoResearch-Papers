# code eval framework

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_framework_20260512T112354_result.json`
- **Structured JSON:** [`4d5a4c8c06705668693e.json`](../../sessions/4d/4d5a4c8c06705668693e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**eval_kv_eviction.py** — 已上传至 `westd-16980:/root/carc/`，dry-run `--help` 通过。修复了一个 import 问题（`create_eviction_hook` 在服务器的 `carc_kv_eviction.py` 中不存在，已移除该 import）。支持 6 个 benchmark（wikitext/c4/math/longbench_passage/longbench_qa/all）、可配 budget ratio、gamma、grace window 等参数，输出 JSON。

**baseline_survey.md** — 5 个 baseline 调研完成，推荐 H2O（经典 attention-based，多集成路径，Easy）+ KeyDiff（via kvpress，与 CARC anchor 方法论最接近，Easy）。备选 R-KV（推理模型专用，Medium）。

两个产出均已 `register_artifact` 注册（`art_20260512_771f21`, `art_20260512_5f68e4`）。

---
