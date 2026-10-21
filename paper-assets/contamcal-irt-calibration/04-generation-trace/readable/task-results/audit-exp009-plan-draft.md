# audit exp009 plan draft

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_exp009_plan_draft_20260517T034405_result.json`
- **Structured JSON:** [`d57b9c0d2b11049e416b.json`](../../sessions/d5/d57b9c0d2b11049e416b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 实验方案摘要

方案已写入 `artifacts/exp009_plan.md`。关键发现：

### 已有数据（可直接复用）
| 模型 | Eval | Signals (s2+s4) |
|------|------|---------|
| Qwen2.5-0.5B-Instruct | ✓ 3 benchmarks | ✓ exp002 完整 |
| Qwen2.5-1.5B-Instruct | ✓ 3 benchmarks | ✓ exp002 完整 |
| Qwen2.5-3B-Instruct | ✓ 3 benchmarks | ✗ **缺失** |
| DeepSeek-R1-Distill-Qwen-1.5B | ✗ 需 eval | ✗ 需计算 |

### 待执行任务
1. **DeepSeek-R1 模型下载** — 后台进行中 (tmux `dl_ds`, ~160MB/3.5GB, ~6min ETA)
2. **DeepSeek-R1 eval** — 需 `--instruct` flag（路径不含 "instruct"）
3. **3B-Instruct signals** — 用 `exp008_new/compute_signals_on_model.py` 直接跑
4. **DeepSeek-R1 signals** — 同上，ref-model 用 Qwen2.5-1.5B base
5. **IRT fitting** — 2PL+gamma pooled，含 exposure 构建策略（signal-as-exposure）

### 脚本兼容性确认
- eval: `apply_chat_template()` 原生支持 DeepSeek chat format ✓
- s2 (minkpp): 格式无关，直接可用 ✓
- s4 (selfcritique): 用 generic template，非 chat-formatted，可接受 ✓
- IRT: `run_irt_calibration.py` 支持 `--response-matrix` + `--exposure-matrix` 直接输入 ✓

### GPU 状态
6x RTX 4090D 全部空闲 (3 MiB used each)，cuda:3/4/5 随时可用。

---
