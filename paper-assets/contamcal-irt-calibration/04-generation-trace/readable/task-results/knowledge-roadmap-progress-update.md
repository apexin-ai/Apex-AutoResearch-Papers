# knowledge roadmap progress update

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_roadmap-progress-update_20260519T232545_result.json`
- **Structured JSON:** [`f5af20ff2317f3a9fa2c.json`](../../sessions/f5/f5af20ff2317f3a9fa2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

ROADMAP 更新完成。更新内容：

1. **当前进展**：OLMo-2 s123 标记完成，ETA 更新（Phi-4 ~09:00, Gemma-2 ~11:30, Qwen-14B ~12:00），新增 GSM8K 首结果/IRT fitting/domain decomposition/sensitivity fix/磁盘清理条目
2. **近期任务**：4 项标记完成（sensitivity fix、IRT fitting 适配、domain decomposition appendix、磁盘清理），新增 GSM8K framing 定稿任务，删除已完成的 domain decomposition 待办
3. **GPU 预算**：按卡细化当前状态（cuda:2 空闲）
4. **新增 GSM8K Cross-Benchmark 数据表**：Qwen-7B d000=70.58%, d100=81.65%, Δ=+11.07pp

report.md 为自动生成，当前已反映 3 个 RUNNING 实验（gsm8k_qwen7b_s42_cqa1, sft_gemma2_s123_sweep, sft_qwen14b_s123_sweep）。注意 registry 中 `sft_phi4_s123_sweep` 也是 RUNNING 但 report 未列出——可能是 report 生成时间差，下次自动刷新会同步。

---
