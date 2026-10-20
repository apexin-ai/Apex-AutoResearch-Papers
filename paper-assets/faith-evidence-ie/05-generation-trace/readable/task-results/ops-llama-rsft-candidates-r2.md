# ops llama rsft candidates r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama_rsft_candidates_r2_20260516T142536_result.json`
- **Structured JSON:** [`045a0c445996cc3dcc74.json`](../../sessions/04/045a0c445996cc3dcc74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:1 **不空闲**（30138 MiB 占用），旧 modelscope 僵尸已死，但有两个活跃进程：

| PID | 运行时间 | 占用 | 进程 |
|-----|---------|------|------|
| 353179 | 1h23m | 20012 MiB | `rsft_generate` — LLaMA 8B 候选生成（r1，参数: `--data_path .../docred --split train`，output 到 `freige/outputs/`） |
| 353322 | 1h18m | 10136 MiB | `eval.inference` — Qwen3-4B no_evidence eval (`plan_014_no_evidence_eval_d076`) |

PID 353179 就是之前参数有误的 r1（`--data_path` 指向目录而非文件，`--output_dir` 路径不同）。PID 353322 是一个正在跑的 eval 任务。

需要 kill 这两个进程才能释放 cuda:1。确认是否 kill？

---
