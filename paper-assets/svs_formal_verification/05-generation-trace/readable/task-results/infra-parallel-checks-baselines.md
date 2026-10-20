# infra parallel checks baselines

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_parallel_checks_baselines_20260514T102652_result.json`
- **Structured JSON:** [`322258cbc7a4bb1353d5.json`](../../sessions/32/322258cbc7a4bb1353d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项检查全部完成。汇总如下：

---

## 1. mvp_003 运行状态

| 项目 | 结果 |
|------|------|
| **进程** | 存活（PID 37622，`python -m svs_pipeline.run_mvp`） |
| **已完成 problem** | **6 个**（partial results 已写入） |
| **日志匹配 "Problem.*:"** | 19 条 |
| **Sandbox restart** | 仅启动时 1 次（pid=37936），无 crash 重启 |
| **Error/Warning** | 有多条 Z3 SyntaxError — 均为 formalization 生成的 Z3 代码语法错误，经过 retry 机制处理（attempt 1→2→3），**非致命**，进程正常运行中 |

当前日志最后时间戳 18:27:05，正在处理含 Gary/Bob/Charlie/Erin 的 ProofWriter 问题，同时调用本地 DeepSeek-R1 (chain_sampler) 和远程 DeepSeek-V3.2 (formalizer)。

---

## 2. Qwen2.5-14B-Instruct 下载

| 项目 | 结果 |
|------|------|
| **下载进程** | PID 25223 已结束（下载完成） |
| **模型目录** | `/root/autodl-tmp/models/Qwen/Qwen2.5-14B-Instruct/` |
| **总大小** | **28GB** |
| **safetensors 文件** | **8/8** 个，完整（model-00001 ~ 00008） |
| **config.json** | 存在，model_type=`qwen2`，arch=`Qwen2ForCausalLM` |
| **附属文件** | tokenizer.json, merges.txt, vocab.json, generation_config.json 全部就位 |
| **状态** | **下载完成，文件完整** |

---

## 3. Baseline 验证

| Baseline | Import | 运行 | 结果 |
|----------|--------|------|------|
| **SC (Majority Vote)** | OK (`evaluate_sc_baseline`) | OK | accuracy=50% (1/2, dry-run 数据) |
| **Binary Filter + SC** | OK (`evaluate_binary_filter`) | OK（需要 dict→SVSResult/ChainVerification 反序列化） | accuracy=50%, filter_rate=25%, 4 chains 中 3 条 survive |
| **Self-Certainty** | OK (`evaluate_self_certainty`) | OK（直接接受 dict） | accuracy=50% |

注意：Binary Filter 的 `evaluate_binary_filter` 期望 `SVSResult` 和 `ChainVerification` 对象而非裸 dict，从 JSON 加载后需要手动构建嵌套对象。当前 dry-run 只有 2 个 problem，accuracy 数值无统计意义。

---
