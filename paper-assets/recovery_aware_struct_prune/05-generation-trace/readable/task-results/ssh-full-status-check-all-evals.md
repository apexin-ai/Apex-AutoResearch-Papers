# ssh full status check all evals

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_full_status_check_all_evals_20260523T041928_result.json`
- **Structured JSON:** [`572183dbae8dabd66000.json`](../../sessions/57/572183dbae8dabd66000.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全面状态报告

---

### westd-32935 — GPU 状态

| GPU | 显存 | 利用率 | PID | 任务 | 进度 | 预估 ETA | 状态 |
|-----|------|--------|------|------|------|----------|------|
| 0 | 16747 MiB | 99% | 100223 | grpo_rasp_alpha3p0_20 | 102/500 (20%) | ~17:50 | RUNNING |
| 1 | 19855 MiB | 99% | 89536 | grpo_rasp_alpha4p0_20 | 373/500 (75%) | ~13:20 | RUNNING |
| 2 | 16049 MiB | 98% | 83161 | grpo_random_20_v2 | 156/500 (31%) | ~21:30 | RUNNING |
| 3 | 17541 MiB | 93% | 86243 | grpo_rasp_alpha1p0_20 | **482/500 (96%)** | ~12:45 | RUNNING, 即将完成 |

---

### westb-23072 — GPU 状态

| GPU | 显存 | 利用率 | PID | 任务 | 进度 | 预估 ETA | 状态 |
|-----|------|--------|------|------|------|----------|------|
| 0 | 19277 MiB | 98% | 250771 | sft_qwen_math_cka_only_20 | 223/500 (45%) | ~18:50 | RUNNING |
| 1 | 17551 MiB | 99% | 262771 | grpo_rasp_alpha0p5_20 | 100/500 (20%) | ~20:30 | RUNNING |

---

### 已完成实验结果（近 3 天）

**westd-32935:**

| 模型 | Accuracy | 完成时间 | 脚本版本 |
|------|----------|----------|----------|
| sft_rasp_alpha4p0_20 | **26.6%** | 05-23 05:15 | UNK |
| sft_rasp_alpha3p0_20 | 23.2% | 05-23 06:10 | UNK |
| sft_rasp_alpha0p5_20 | 25.4% | 05-23 06:15 | UNK |
| sft_rasp_alpha1p0_20_v2 | 21.2% | 05-23 06:57 | UNK |
| sft_cka_only_20 | **26.8%** | 05-23 07:57 | UNK |
| grpo_rasp_alpha2p0_20 | **26.2%** | 05-23 11:12 | UNK |
| sft_rasp_alpha2p0_20 | 24.0% | 05-23 04:03 | UNK |
| grpo_standard_20_fair_2048_v2 | 26.4% | 05-22 19:01 | UNK |
| sft_random_20_v3 | **14.4%** | 05-22 22:08 | UNK |

**westb-23072:** 近期无新完成的 MATH-500 评估（sft_standard_25 于 05-21 完成，acc=13.0%）

---

### 异常情况

1. **所有结果 ver=UNK** — 结果 JSON 中 results 条目既无 `pred_answer` 也无 `pred` 字段，可能是新脚本使用了不同的字段名
2. **westb-23072 僵尸 tmux** — PID 680597 (`eval_unstructured_20`) 自 5月17日起一直挂着，应已完成
3. **westd-32935 残留 tmux** — PID 79020 (`eval_math500_sft_rasp_alpha1p0_20_v2`) 任务已完成但 tmux session 未清理
4. **sft_rasp_alpha1p0_20_v2 异常低** — 21.2% 显著低于其他 alpha 变体（23-27%），需确认模型路径是否正确（用的是 `sft_rasp_20_westd`）
5. **sft_random_20_v3 极低** — 14.4%，random pruning 基线符合预期但值得关注
6. **westb sft_qwen_math_cka_only_20 日志分裂** — 最初的 tee 日志停在 06:47（15/500），实际进程通过 nohup 重启，当前输出在 `/tmp/eval_math500_sft_qwen_cka_only_20.log`

---
