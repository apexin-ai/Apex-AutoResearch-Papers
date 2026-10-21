# infra grammar only crash diagnose

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_grammar_only_crash_diagnose_20260513T224253_result.json`
- **Structured JSON:** [`8a40da28e537618c032d.json`](../../sessions/8a/8a40da28e537618c032d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 崩溃原因：**没有崩溃**

PID 126473 **仍在运行**（状态 `Rl`，已运行约 26 分钟）。输出文件已从 163 行增长到 **183 行**。

### 当前状态

| 项目 | 状态 |
|------|------|
| PID 126473 (grammar_only) | 运行中，GPU 1，16502 MiB |
| tmux `phase2_scierc_grammar_only` | 存活 |
| 输出文件 | 183 行，最后修改 06:43 |
| tmux `phase2_scierc_unconstrained` | 也在运行，GPU 1，~33000 MiB |
| tmux `mvp_phase0_docred_schema` | GPU 0，24442 MiB |

### GPU 状况

| GPU | 已用 | 总量 | 空闲 |
|-----|------|------|------|
| 0 | 24451 MiB | 97887 MiB | **72800 MiB** |
| 1 | 49503 MiB | 97887 MiB | 47748 MiB |

GPU 0 有 72.8 GB 空闲，被 DocRED schema 占用约 24 GB。GPU 1 跑着 grammar_only + unconstrained 两个任务。

### 备份

`phase2_scierc_grammar_only_partial_183.jsonl` 已创建（446 KB，183 行）。

### S2 pilot 文件

- `phase2_s2_dryrun.jsonl` — 06:26，21 KB
- `phase2_s2_pilot50.jsonl` — 06:43，53 KB

**结论：grammar_only 没死，正在正常推进。无需重启。**

---
