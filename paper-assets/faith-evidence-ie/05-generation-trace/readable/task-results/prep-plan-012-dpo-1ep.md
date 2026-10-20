# prep plan 012 dpo 1ep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_plan_012_dpo_1ep_20260515T193812_result.json`
- **Structured JSON:** [`6cabb0025556751bb2be.json`](../../sessions/6c/6cabb0025556751bb2be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查完毕，汇总如下：

---

## plan_012_dpo_ced_1ep 状态报告

**意外发现：实验已在运行。** 在我们检查前，它已被重新提交到 **cuda:2**（绕过了 cuda:3 被占用的阻塞），pid=244073，03:39 启动。

### 当前进度
- **3/167 steps**，~13.5s/step
- 预计总时长 **~37 min**，ETA 约 04:17（服务器时间）

### 前置条件（全部满足）
| 项目 | 状态 | 路径 |
|------|------|------|
| 基础模型 | ✅ | `/root/autodl-tmp/models/Qwen3-4B` |
| SFT adapter | ✅ | `/root/autodl-tmp/sft_output` |
| DPO 数据 | ✅ | `/root/autodl-tmp/dpo_data/dpo_pairs.jsonl` (2666 pairs) |
| 训练脚本 | ✅ | `/root/autodl-tmp/freige/training/dpo_trainer.py` |
| 输出目录 | ✅ | `/root/autodl-tmp/dpo_output_1ep/` (空, checkpoint 将写到这) |

### 超参配置（与 3ep 一致，仅改 epochs）
- beta=0.1, loss=sigmoid, lr=5e-7, batch=2, grad_accum=8, lora_r=64/alpha=128, bf16

### 附加发现
- **checkpoint-400 存在**：`/root/autodl-tmp/dpo_output/checkpoint-400/`（完整 adapter + optimizer），后续可 eval
- **前次 eval_plan_012_dpo_ced_ckpt400 OOM 失败**（cuda:3 被占用时跑的），需在空闲 GPU 重跑
- **前次 1ep 提交 (pid=240426) 失败**：cuda:3 被占用导致 OOM，日志仅到加载数据就停了

### 已更新
- Registry status: ALLOCATED → **RUNNING**
- Notes: 写入完整就绪性检查和提交命令记录

---
