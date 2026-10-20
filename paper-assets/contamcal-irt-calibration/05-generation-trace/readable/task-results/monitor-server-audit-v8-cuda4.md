# monitor server audit v8 cuda4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_server-audit-v8-cuda4_20260516T004002_result.json`
- **Structured JSON:** [`a0d3c09b0b8f4062b2a8.json`](../../sessions/a0/a0d3c09b0b8f4062b2a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。以下是完整审计报告。

---

## 1. GPU 占用表

| GPU | 利用率 | 显存 | PID | 实验 |
|-----|--------|------|-----|------|
| **0** | **99%** | **23260/24564** | 642763 | **eval** d100_a32_s123 (aligned, mmlu+gsm8k+arc+humaneval) |
| | | | 643167 | **SFT** d005_s42 (alpha=32, lr=5e-5) |
| **1** | 37% | 13341/24564 | 628668 | **SFT** d100_a32_s42_v3 (alpha=32) |
| **2** | 78% | 7537/24564 | 652259 | **signals** d005_s123 (mmlu, all) |
| **3** | 70% | 8985/24564 | 655989 | **eval** d025_v3_s42 (aligned, mmlu+gsm8k+arc) |
| **4** | 61% | 7445/24564 | 662616 | **signals** d100_a32_s123 (mmlu, all) |
| **5** | 64% | 7531/24564 | 663067 | **signals** d025_v3_s42 (mmlu, s4) |

**警告**: GPU 0 双进程共享（eval + SFT），显存几乎打满，两个任务都在减速。

---

## 2. v8 产出完整性（d025_s123 + d100_a32_s123）

### d025_s123 signals

| benchmark | s1_embedding | s2_minkpp | s4_selfcritique | signals_merged |
|-----------|:---:|:---:|:---:|:---:|
| mmlu | ✅ | ✅ | **❌ 缺失** | **❌ 缺失** |
| gsm8k | ✅ | ✅ | ✅ | ✅ |
| arc_challenge | ✅ | ✅ | ✅ | ✅ |

结论：**d025_s123 只差 mmlu 的 s4_selfcritique 和 merged**。v8 脚本跑完 mmlu 的 s1/s2 后 s4 失败或被跳过。

### d100_a32_s123 signals

| benchmark | s1_embedding | s2_minkpp | s4_selfcritique | signals_merged |
|-----------|:---:|:---:|:---:|:---:|
| mmlu | ✅ | ✅ | ⏳ GPU 4 计算中 | ❌ |
| gsm8k | ❌ | ❌ | ❌ | ❌ |
| arc_challenge | ❌ | ❌ | ❌ | ❌ |

结论：**d100_a32_s123 只完成了 mmlu s1+s2**，GPU 4 正在跑 mmlu 后续信号（s3/s4），之后脚本会继续 gsm8k 和 arc_challenge。

### 其他 3B signal 目录参考

| checkpoint | mmlu | gsm8k | arc_challenge | 备注 |
|-----------|------|-------|---------------|------|
| d000_v2_s42 | s1+s2+s3 ✅ | s1+s2+s3 ✅ | s1+s2+s3 ✅ | 缺 s4 + merged |
| d005_s42 | s1+s2 | s1+s2 | s1+s2+s4+merged ✅ | mmlu/gsm8k 缺 s4 |
| d005_s123 | s1+s2 ⏳GPU2 | ❌ | ❌ | GPU 2 正在跑 mmlu |
| d025_s42 | s4+merged | ❌ | ❌ | 只有 mmlu 的 s4 |
| d025_v3_s42 | s1+s2 ⏳GPU5 | s1+s2 | s1+s2 | GPU 5 跑 mmlu s4 |
| d100_s42 | s1+s2 | s1+s2+s4+merged ✅ | s1+s2+s4+merged ✅ | mmlu 缺 s4 |

---

## 3. d000_a32_s42 checkpoint 状态

- **目录存在**: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_a32_s42/lora_adapter/` — **但是空的**，无 adapter_config.json，无模型文件
- **d100_a32_s42** 同样空（v3 版本正在 GPU 1 训练）
- **没有活跃进程在训练 d000_a32_s42**

d000_a32_s42 训练要么失败要么从未正确启动。需要重新训练。

### eval 状态
- `Qwen2.5-3B_d000_v3_s42_aligned/` — **空目录**（有 log 文件 520KB 但 eval_results 为空）
- 无法对空 checkpoint 做 eval

---

## 4. RUNNING 实验进度

| 实验 | GPU | 进度 | ETA |
|------|-----|------|-----|
| SFT d005_s42 (alpha=32) | 0 (共享!) | **75%** (2385/3177) | ~1h |
| SFT d100_a32_s42_v3 | 1 | **92%** (3826/4159) | ~25 min |
| eval d100_a32_s123 aligned | 0 (共享!) | 未知（输出目录仍空） | — |
| eval d025_v3_s42 aligned | 3 | 未知（输出目录仍空） | — |
| signals d005_s123 (mmlu) | 2 | mmlu s1+s2 done, 跑后续 | ~2-3h |
| signals d100_a32_s123 (mmlu) | 4 | mmlu s1+s2 done, 跑后续 | ~2-3h (仅 mmlu), 全部 ~6h |
| signals d025_v3_s42 (mmlu s4) | 5 | **15%** (1086/7021) | ~2h |

---

## 5. cuda:4 建议

**cuda:4 当前不空闲** — 正在跑 d100_a32_s123 signals（mmlu→gsm8k→arc_challenge 循环），预计还需 ~6h。

当 cuda:4 释放后，优先级建议：

1. **最高优先**：训练 d000_a32_s42 SFT（checkpoint 为空，阻塞后续所有 eval 和 signals）
2. **次优先**：补跑 d025_s123 mmlu s4_selfcritique（v8 唯一缺口）
3. **第三**：d100_s42 / d005_s42 的 mmlu s4（大面积缺 mmlu s4，可能是 s4 mmlu 系统性失败）

**额外问题需关注**：
- GPU 0 双进程拥挤，d005_s42 SFT 和 d100_a32_s123 eval 互相拖慢
- 多个 checkpoint 的 mmlu s4_selfcritique 都缺失，可能是 s4 计算在 mmlu 上有 bug（libnvJitLink.so.13 错误出现在 d025_v3_s42 的 s4 日志中，但似乎没有阻止运行）

---
