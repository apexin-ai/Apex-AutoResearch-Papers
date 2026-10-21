# diagnose check experiments status 0517b

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_check_experiments_status_0517b_20260517T200330_result.json`
- **Structured JSON:** [`6673b60a558edc400be8.json`](../../sessions/66/6673b60a558edc400be8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### C4 seed-43 (`pythia1b_c4_a100_s43`) — 崩溃

- **PID 288678 已退出**，cuda:0 空闲（0MiB, 0%）
- **退出码**: 1
- **崩溃点**: gen_0 baseline 阶段，生成 synthetic_data 后，在 MAUVE 评估时崩溃
- **根因**: MAUVE 库内部调用 `AutoTokenizer.from_pretrained("gpt2")` 直连 `huggingface.co`，服务器无法访问。`HF_ENDPOINT=hf-mirror.com` 环境变量对 MAUVE 内部调用不生效。
- **进度**: 仅 `gen_0/synthetic_data`，无评估指标，无法运行分析

### Pythia-1.4B (`pythia14b_wiki_a100_s42`) — 正常运行

- **PID 289216** 在 cuda:1 运行，GPU 利用率 98%，28427MiB 显存
- 已完成 gen_7（checkpoint 已保存）
- **当前**: 训练 gen_8，进度 4875/5000 步（~98%），约 2 分钟完成当前 gen
- **剩余**: gen_8（即将完成）+ gen_9 + gen_10，预计 ~30-45 分钟全部完成

### C4 seed-43 修复方案

需要预下载 GPT-2 tokenizer 到本地缓存，或在 MAUVE 调用前 patch `HF_ENDPOINT`。是否要我立即修复并在 cuda:0 上重启 C4 seed-43？

---
