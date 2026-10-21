# ssh health check eval verify

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_health-check-eval-verify_20260521T055555_result.json`
- **Structured JSON:** [`cf6acd8ec7383fc3cc6d.json`](../../sessions/cf/cf6acd8ec7383fc3cc6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态

| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX 5090 | 98% | 30553 / 32607 MiB (94%) |
| 1 | RTX 5090 | 99% | 20253 / 32607 MiB (62%) |
| 2 | RTX 5090 | 99% | 20501 / 32607 MiB (63%) |
| 3 | RTX 5090 | 98% | 25559 / 32607 MiB (78%) |

4 卡全部满载。

## 训练进程

| 实验 | PID | 存活 | 运行时长 | 当前 Step | 进度 | Loss | Eval Loss | ETA |
|------|-----|------|----------|-----------|------|------|-----------|-----|
| Qwen s123 resume | 4271 | **ALIVE** | 8h17m | 4284/6633 | 64.6% | 0.0194 (ep1.90) | 0.4717 (ep1.85) | ~8.0h |
| Qwen s456 resume | 4561 | **ALIVE** | 8h16m | 4300/6633 + eval中 2129/9335 | 64.8% | 0.0173 (ep1.94) | 0.4713 (ep1.90) | ~7.8h + eval |
| DeepSeek s456-v2 | 949112 | **ALIVE** | 20h52m | ⚠️ 日志无训练步 | — | — | — | — |

## Monitor 进程

| PID | 存活 | 运行时长 | 说明 |
|-----|------|----------|------|
| 817 | **ALIVE** | 8h37m | watch_s123_eval_then_resume.sh |
| 1769 | **ALIVE** | 8h32m | monitor PID 949112 → eval_deepseek_cwm_s456_v2.sh |

## DeepSeek s123-v2 Eval 结果（已完成）

| 指标 | 值 |
|------|-----|
| Checkpoint | checkpoint-4209 |
| Accuracy | **75.45%** |
| Majority baseline | 72.96% |
| Gap vs majority | +2.49pp |
| F1 (fail/pass/macro) | 46.05 / 84.11 / 65.08 |
| Unparseable | 6500/9784 (66.4%) |
| 截断 | 0 |

## Eval 脚本验证

| 脚本 | 存在 | seq_length | batch_size | max_new_tokens | 状态 |
|------|------|------------|------------|----------------|------|
| eval_deepseek_cwm_s456_v2.sh | ✓ | 4096 | 4 | 512 | ✓ 参数正确 |
| eval_qwen_cwm_s123.sh | ✓ | **8192** | 1 | 512 | ✓ 参数正确 |
| eval_qwen_cwm_s456.sh | ✓ | **8192** | 1 | 512 | ✓ 参数正确 |
| eval_deepseek_cwm_s123_v2.sh | ✓ | 4096 | 4 | 512 | ✓ (已跑完) |
| eval_14b_cwm_pilot.sh | ✓ | — | — | — | 未检查 |

Qwen eval 的 max_seq_length 均为 8192，bug 已修复确认。

## 异常/告警

1. **DeepSeek s456-v2 (PID 949112) 日志异常**：进程存活 20h52m，但日志仅有 2026-05-20 17:00 的初始化信息（Loaded train=70748, val=1896），无任何训练步输出。最后一行是 token length 超限警告。可能原因：
   - 训练进度输出到 stderr 未捕获
   - 进程卡在数据加载/模型加载阶段
   - 需要检查进程实际 GPU 利用和输出（GPU 3 确实 98% 利用率，说明很可能在正常训练，只是日志未写入）

2. **DeepSeek s123-v2 eval unparseable 率极高 (66.4%)**：6500/9784 样本 unparseable，实际可判定的只有 3284 个样本。accuracy 75.45% 是在全量（unparseable 默认 pass）上计算的。

---
