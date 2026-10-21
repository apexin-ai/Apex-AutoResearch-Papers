# ops gpu audit fill cuda2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-audit-fill-cuda2_20260516T185736_result.json`
- **Structured JSON:** [`dd1648c0c82e83c77076.json`](../../sessions/dd/dd1648c0c82e83c77076.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整审计结果如下。

---

## (1) GPU 截面

| GPU | VRAM | Util | PID | 任务 | 进度 |
|-----|------|------|-----|------|------|
| cuda:0 | 8081/24564 | 70% | 825638 | Llama-3.2-3B d005 eval | GSM8K 452/1319 (34%) |
| cuda:1 | 9023/24564 | 52% | 830115 等 | Llama-3.2-3B d000 mmlu+arc signals | 活跃 |
| cuda:2 | 587/24564 | 23% | **835983** | **未注册重复** Llama d000 gsm8k signals (bs=8) | s4_selfcritique 60/165, ~2min 完成 |
| cuda:3 | 8313/24564 | 72% | 822390 | Llama-3.2-3B d025 eval | GSM8K 685/1319 (52%) |
| cuda:4 | 571/24564 | 17% | 831936 | Llama-3.2-3B d000 gsm8k signals (注册) | 低 VRAM，可能也在 s4 |
| cuda:5 | 8313/24564 | 67% | 831033 | Llama-3.2-3B d100 eval | GSM8K 182/1319 (14%) |

另有 CPU 任务：4 条 Stan 2PL+γ MCMC chain (PIDs 836320-836324)，以及一个**幽灵进程** PID 835593（同样是 Llama d000 gsm8k signals bs=8，运行 6min43s，**不在任何 GPU 上**）。

---

## (2) exp_002_signals_3B_d000_s123_cuda2

**Registry 中不存在此 exp_id。** 可能已被清理或 ID 不同。

关键发现：**Qwen2.5-3B d000 s123 signals 已全部完成**。`/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_s123/` 和 `Qwen2.5-3B_d000_s123_a32/` 都有完整的 3 benchmark × 3 signal + merged 文件。lora_alpha=32 ✓（C006 合规）。

**无需重新提交。**

---

## (3) exp_002_signals_15B_instruct_arc 失败原因

两次运行均以 EXIT_CODE=129 (SIGHUP) 结束：

- **v1**：`HFValidationError` — `load_model_and_tokenizer()` 将本地路径 `/root/autodl-tmp/models/Qwen2.5-1.5B-Instruct` 当成 HF repo_id 验证失败
- **v2**：正常推进到 arc self-critique 完成，但在加载 `sentence-transformers/all-MiniLM-L6-v2` 时 HuggingFace 连接反复超时（AutoDL 网络问题），最终被 SIGHUP 终止

Registry 已标为 DONE/success（可能被手动解决）。

---

## (4) cuda:2 任务分配

**无法启动 Qwen2.5-3B d000 s123 signals — 已完成。**

当前 cuda:2 被 PID 835983 占用（Llama d000 gsm8k self-critique，~2min 完成）。这是与 cuda:4 PID 831936 的**三重冲突**（C001 违规）：3 个进程写同一个 output-dir `/root/autodl-tmp/exp002/signals/Llama-3.2-3B_d000_s42/`。

Llama d000 signals 状态：
- s1_embedding: mmlu ✓ gsm8k ✓ arc ✓
- s2_minkpp: mmlu ✓ gsm8k ✓ arc ✓
- s4_selfcritique: arc ✓, **gsm8k 进行中**, **mmlu 未开始**
- merged: arc ✓, gsm8k ✗, mmlu ✗

建议：
1. **Kill PID 835593**（幽灵，无 GPU，纯浪费 CPU）
2. 让 PID 835983 (cuda:2) 跑完 gsm8k selfcritique（~2min），它会接着做 mmlu selfcritique + merge
3. cuda:2 空闲后（预计 ~15min），最高优先级任务需要你指示 — **C007 清单里 0.5B s123、1.5B s123、3B d000 s123 signals 已全部完成**，需要确认下一优先级

---

## (5) ETA 估算

| GPU | 当前阶段 | 阶段 ETA | 备注 |
|-----|---------|---------|------|
| cuda:0 (d005 eval) | GSM8K 34% | ~1h28m | 后续还有 ARC+HumanEval，总 ETA ~3-4h |
| cuda:3 (d025 eval) | GSM8K 52% | ~1h01m | 同上，总 ETA ~2.5-3h |
| cuda:5 (d100 eval) | GSM8K 14% | ~1h56m | 同上，总 ETA ~4-5h |
| cuda:2 (Llama gsm8k s4) | selfcritique 36% | ~2min | 然后 mmlu selfcritique ~12min |
| cuda:1 (Llama mmlu+arc signals) | 活跃 | 未知 | 8GB VRAM 在用 |
| cuda:4 (Llama gsm8k signals) | 低 VRAM | 未知 | 可能也在 selfcritique |

---

**需要你决定**：cuda:2 空闲后放什么？Kill PID 835593 是否确认？

---
