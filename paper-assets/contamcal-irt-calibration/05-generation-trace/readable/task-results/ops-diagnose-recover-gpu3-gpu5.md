# ops diagnose recover gpu3 gpu5

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-recover-gpu3-gpu5_20260516T024635_result.json`
- **Structured JSON:** [`fb0b822ceb3b47584289.json`](../../sessions/fb/fb0b822ceb3b47584289.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。汇报如下：

---

## 诊断结果

### cuda:5 — signals s4 (exp_002_signals_3B_d025_v3_s42)
**进程存活**，PID 663067，运行 2h30m。Self-critique mmlu 进度 **98% (6905/7021)**，预计 ~3 分钟完成。无需干预。

### cuda:3 — eval 进程已消失，被另一个 SFT 占用
原 eval 进程已结束。**但 cuda:3 被一个未注册的 SFT 训练占据：**
- PID 684230，运行 ~2 分钟，占用 17.6GB
- 命令：`train_sft.py --model-name Qwen2.5-3B --data-path sft_dosage_025.jsonl --output-dir Qwen2.5-3B_d025_a32_s42 --lora-alpha 32 --seed 42`
- 寄生在旧 tmux session `exp_001_sft_0pct_05B`（PPID 208932，2 天前创建）
- **不在 registry 中**，来源不明

注意：输出目录 `Qwen2.5-3B_d025_a32_s42`（无 `_v3` 后缀）与现有 `Qwen2.5-3B_d025_v3_s42` checkpoint 重复（相同 dosage/seed/alpha 配置）。

### eval aligned 部分结果（已完成，有 .done 标记）

| Benchmark | Accuracy | 正确/总数 |
|-----------|----------|----------|
| mmlu | 0.6242 | 8765/14042 |
| gsm8k | 0.6823 | 900/1319 |
| arc_challenge | 0.8225 | ~962/1172 |
| **humaneval** | **缺失** | 未执行 |

### eval para_aligned — 空目录，从未执行

---

## 需要决策

1. **cuda:3 上的未授权 SFT (PID 684230)** — 是否 kill 掉？它训练的 checkpoint 名 (`d025_a32_s42`) 与已有 `d025_v3_s42` 功能重复，且不在 registry 中。
2. kill 后 cuda:3 重提交：只跑 **para_aligned eval**（aligned 已完成 3/4 benchmarks），还是同时补跑 **aligned humaneval + para_aligned 全套**？

请确认。

---
