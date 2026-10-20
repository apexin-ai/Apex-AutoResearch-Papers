# ops llama3 sft monitor eval pipeline

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama3-sft-monitor-eval-pipeline_20260521T102022_result.json`
- **Structured JSON:** [`0489d8af1fff52487517.json`](../../sessions/04/0489d8af1fff52487517.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出汇总

### Part 1: GPU 状态

| GPU | 任务 | 进度 | 剩余时间 |
|-----|------|------|----------|
| 0 | LLaMA-3 d025 SFT (PID 509577) | 345/3384 (10%) | ~2h10m |
| 1 | LLaMA-3 d000 SFT (PID 508650) | 512/3125 (16%) | ~2h |
| 2 | OLMo-2 d025 GSM8K eval (PID 511182) | 30/660 (5%) | ~57min |
| 3 | LLaMA-3 d100 SFT (PID 510202) | 260/4159 (6%) | ~3h |

OLMo-2 GSM8K 已有结果：d000=60.58%, d005=66.19%, d100=69.75%, **d025 进行中**, d050 未启动。

### Part 2: 监控脚本已部署

3 个并行 nohup 进程运行中（PID 512753/512754/512755），每 30s 检查 `.done` sentinel：

| Dosage | 监控 PID | 等待 sentinel 路径 | eval GPU |
|--------|----------|-------------------|----------|
| d000 | 512753 | `Meta-Llama-3.1-8B_d000_s0/.done` | 1 |
| d025 | 512754 | `Meta-Llama-3.1-8B_d025_s0/.done` | 0 |
| d100 | 512755 | `Meta-Llama-3.1-8B_d100_s0/.done` | 3 |

触发后自动执行：C006 alpha=32 验证 → MMLU eval → ARC eval。日志在 `/tmp/monitor_d0XX.log` 和 `/tmp/eval_llama3_d0XX_{mmlu,arc}.log`。

### Part 3: Dry-run 暂缓

GPU 2 被 OLMo-2 eval 占用，~50min 后释放。释放后建议优先级：
1. LLaMA-3 base dry-run（2min，验证 evaluate.py 兼容性）→ 在任何 SFT .done 触发 eval 之前完成
2. OLMo-2 d050 GSM8K 或 Phi-4 d005 GSM8K

### 注意事项

**C009 版本漂移**：evaluate.py 当前 37775 bytes (md5: `17673bf373f00f83ccc41fc1d355a4cd`)，与 reference 37591 bytes 不一致。但所有近期 eval（OLMo-2 全系列、Phi-4、Qwen14B、Gemma2）均使用 37775 版本，**建议将 37775 更新为新 reference**。

---
