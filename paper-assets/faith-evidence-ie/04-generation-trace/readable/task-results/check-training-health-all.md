# check training health all

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_training-health-all_20260514T180219_result.json`
- **Structured JSON:** [`92dfb0f0f64224112f8a.json`](../../sessions/92/92dfb0f0f64224112f8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态汇总 (2026-05-14 18:04 UTC)

### GPU 总览
| GPU | 显存 | 利用率 | 任务 |
|-----|------|--------|------|
| cuda:0 | 13649/32607 MiB | 42% | ced_kl001_r4 训练 |
| cuda:1 | 10439/32607 MiB | 56% | eval ckpt50 |
| cuda:2 | 9409/32607 MiB | 0% | eval ckpt10 (multi) |
| cuda:3 | 13647/32607 MiB | 46% | flatnli_r6 训练 |

### 1. ced_kl001_r4 (cuda:0) — ✅ 即将完成
- **进度**: 99/100 steps，预计几分钟内结束
- **健康**: 全程无 collapse，KL=0.148 受控
- **最终指标** (step 85): reward=0.843, f1=0.358, ced=0.196, frac_zero_std=0.2
- **结论**: 训练成功，等待完成后进入 eval 阶段

### 2. flatnli_r6 (cuda:3) — ⚠️ 需关注
- **进度**: 21/100 steps，预计 ~2h 完成
- **风险**: frac_zero_std 持续上升 0.4→0.6→0.7，逼近 0.8 警戒线
- **问题**: task reward 极低（f1=0.012, flat_nli=0.023），reward 几乎全来自 format（0.29/0.325）
- Step 5 出现 KL 爆炸 (1.2亿) 后回落，当前 KL=0.036 稳定
- grad_norm=0.037 极低，loss 为负值，模型可能在 exploit format
- **建议**: 暂不 kill，继续观察到 step 30-40。若 frac_zero_std 破 0.8 且 task reward 无起色则终止

### 3. eval_ced_kl001_r4_early / ckpt50 (cuda:1) — 🔄 正常推进
- Inference 41/62 batches (~66%)，预计 ~25 min 完成推理

### 4. cuda:2 双 eval — ✅ 无冲突
- **实际状态**: 只有一个 Python 进程在跑（PID 78857，inference ckpt-10）
- multi eval (78850) 是 bash wrapper 处于 sleep 状态，78857 是其子进程
- ckpt10 独立 eval 的日志文件不存在，可能未实际独立运行
- multi eval 进度: 14/62 batches on checkpoint-10 (~23%)，7 个 checkpoint 全部完成预计数小时
- 显存 9409 MiB，无 OOM 风险

---
