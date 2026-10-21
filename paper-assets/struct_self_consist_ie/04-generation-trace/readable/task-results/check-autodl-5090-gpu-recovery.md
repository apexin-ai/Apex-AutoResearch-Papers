# check autodl 5090 gpu recovery

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_autodl_5090_gpu_recovery_20260514T132531_result.json`
- **Structured JSON:** [`45337170a0d381a45c78.json`](../../sessions/45/45337170a0d381a45c78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇报如下：

---

## 诊断结果

### 1. GPU 占用情况

| GPU | 显存 | 利用率 | 实验 | PID |
|-----|------|--------|------|-----|
| cuda:0 | 16428/32607 MiB | 14% | **exp_001_seed456_t10_full** (刚启动) | 67261 |
| cuda:1 | 2/32607 MiB | 0% | **空闲** — WNUT LoRA 训练已完成 | — |
| cuda:2 | 16428/32607 MiB | 14% | **exp_001_seed123_t10_full** (刚启动) | 67399 |
| cuda:3 | 加载中 | 0% | **exp_008_re_n16_t10_full** (刚启动，模型加载中) | 67663 |

### 2. 新提交实验

| exp_id | GPU | seed | tmux session |
|--------|-----|------|-------------|
| exp_001_seed456_t10_full | cuda:0 | 456 | `exp001_seed456` |
| exp_001_seed123_t10_full | cuda:2 | 123 | `exp001_seed123` |
| exp_008_re_n16_t10_full | cuda:3 | 42 | `exp008_re` |

### 3. exp_001_ner_n16_seed123 (pid 63407) 状态

**已完成。** 输出在 `output/exp001_n16_seed123/`：
- `samples.jsonl`: 551 条（全集）
- `report.json`: verdict=**FAIL**
- NER: greedy_f1=0.663, oracle_f1=0.809, headroom=14.6pp, ρ_sj=0.423 (conditional), ρ_fk=0.260
- RE: greedy_f1=0.419, oracle_f1=0.625, headroom=20.6pp, ρ_sj=0.364 (conditional), ρ_fk=0.331
- RE ρ_sj < 0.40 且 structural 未 beat surface → FAIL
- 警告：RE >30% samples F1=0

### 4. Conditional filtering 确认

`run_mvp_pilot.py` 第 253 行：`cond_mask = [nonempty_mask[i] and instance_f1s[i] > 0 ...]` — **正确**（greedy_f1 > 0）。

### 5. --num_test 默认值

第 59 行：`default=99999` — **已修复**，无需更改。

### 6. WNUT LoRA 训练（cuda:1 已完成）

`checkpoints/qwen3-8b-wnut17-lora/` 有完整 adapter（349MB），5 epochs, 1065 steps, eval_loss=0.077。**cuda:1 可用于 LoRA merge + WNUT pilot inference。**

---
