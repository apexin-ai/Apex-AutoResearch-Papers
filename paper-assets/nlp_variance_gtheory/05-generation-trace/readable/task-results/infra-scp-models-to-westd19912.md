# infra scp models to westd19912

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_scp_models_to_westd19912_20260521T171859_result.json`
- **Structured JSON:** [`b7b7d2dce0571bc170f2.json`](../../sessions/b7/b7b7d2dce0571bc170f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Watcher 已启动（PID 55951），正在等待 OLMo 4 个进程完成后自动启动 Yi。

---

**汇总：**

| 项目 | 状态 |
|------|------|
| westd-32570 模型路径 | OLMo: `/root/autodl-tmp/.hf_cache/allenai/OLMo-2-1124-7B-Instruct` (14G), Yi: `/root/autodl-tmp/.hf_cache/01ai/Yi-1___5-9B-Chat` (17G) |
| westd-19912 ModelScope 下载 | 已 kill（PID 48244, 48610），仅下载了 ~10MB |
| scp 传输 | 完成，内网传输约 2 分钟搞定 31G |
| OLMo 推理 | 正在运行，4 GPU 并行（mmlu/arc/hellaswag/gsm8k），刚开始处理 |
| chain 脚本 bug | `run_job` 的 echo 被 `$(...)` 捕获导致 PID 变量污染，`wait` 失败 + `set -e` 退出 |
| Yi 接力 | 已部署 `yi_after_olmo.sh`（PID 55951），监控 OLMo 完成后自动启动 Yi 5 个 benchmark |

---
