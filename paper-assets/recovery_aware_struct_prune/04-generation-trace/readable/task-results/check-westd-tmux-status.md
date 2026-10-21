# check westd tmux status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd_tmux_status_20260519T220216_result.json`
- **Structured JSON:** [`f82500f779b6595f42af.json`](../../sessions/f8/f82500f779b6595f42af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

### 1. cka_scoring_stability_ablation — **已完成** ✓

PID 143187 已退出。结果文件存在，核心指标：

| 对比 | Attn ρ | MLP ρ | Combined ρ |
|------|--------|-------|------------|
| 256 vs 512 | 0.9890 | 0.9683 | **0.9788** |
| 256 vs 1024 | 0.9762 | 0.9464 | **0.9641** |
| 512 vs 1024 | 0.9950 | 0.9908 | **0.9938** |

**Summary**: min_combined_ρ = 0.964, mean = 0.979, **stable = true**（阈值 0.95）。CKA scoring 在不同 calibration size 下高度稳定。

---

### 2. eval_mbpp_sft_standard_20_clean — **失败** ✗

日志时间 `2026-05-20 04:35`，模型加载成功但下载 MBPP 数据集时因 **网络不可达** (`[Errno 101] Network is unreachable`) 崩溃。没有缓存可用，没有结果文件产出。

**原因**: 未执行 `source /etc/network_turbo`，AutoDL 实例无法访问 HuggingFace。

---

### 3. eval_mbpp_grpo_standard_20_v4 — **未找到**

没有任何对应的日志或结果文件。可能从未成功启动，或者命名不同。

注意：`eval_mbpp_grpo_rasp_20` 是存在且已完成的（pass@1 = **0.1310 ± 0.0174**, 49/374），但这是 RASP 变体，不是 standard v4。

---
