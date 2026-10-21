# code westb cuda1 eval check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_westb-cuda1-eval-check_20260515T110018_result.json`
- **Structured JSON:** [`7fa74ec1d7eb417f6d64.json`](../../sessions/7f/7fa74ec1d7eb417f6d64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 1. sft_standard_20 eval — 已完成
- **Accuracy: 64/100 (64.0%)**
- EOS rate: 99%, avg response length: 182.48
- PID 507411: 已结束（ps aux 中不存在）

### 2. sft_rasp_20 eval — 已完成
- **Accuracy: 57/100 (57.0%)**
- EOS rate: 99%, avg response length: 179.83

### 3. D023 re-eval pruned_standard_20 — 进行中
- PID 509954 存活，cuda:1 上运行，GPU 利用率 78%，显存 13003 MiB
- **进度: 51/100，当前 acc=0.28，eos_rate=68%**
- 结果文件尚未生成
- 注意：eos_rate 仅 68%，avg_len=1594，说明 pruned 模型生成偏长且频繁截断

### 4. GPU 状态
| GPU | 利用率 | 显存 | 进程 |
|-----|--------|------|------|
| cuda:0 | 100% | 65187/97887 MiB | GRPO v5 (PID 498479) |
| cuda:1 | 79% | 13003/97887 MiB | re-eval pruned_standard_20 (PID 509954) |

### 5. GRPO v5 最新进度
- **Step 41/250 (16%)**，速度 113.12 s/it，ETA ~6h34m
- 日志显示模型在生成重复计数步骤（"Step 18: ...is 25+1=26", "Step 19: ...is 26+1=27"...），有退化迹象

### 关键发现
- pruned_standard_20 re-eval 中间准确率仅 **28%**（对比 SFT 后 64%），且 eos_rate 低（68%），确认剪枝后未经 SFT 恢复的模型质量严重下降
- GRPO v5 的生成出现重复步骤退化，可能需要关注 repetition_penalty 是否足够

---
