# diagnose exp012 llama 8b r2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp012_llama_8b_r2_20260515T194715_result.json`
- **Structured JSON:** [`a26a63fe4182e8562374.json`](../../sessions/a2/a26a63fe4182e8562374.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告：exp012_llama_8b_r2

### 状态：**STILL RUNNING**（cron 误报）

| 指标 | 值 |
|------|------|
| PID 315801 | **存活** (`/proc/315801/status` 存在) |
| vLLM 引擎 PID | 319623, State=R (running), PPid=319316, NSsid=315801 |
| GPU 占用 | 84652 MiB (vLLM::EngineCore) |
| 日志最新 | `2026-05-16 03:49:41` — 正在处理 count_6/random/23 |
| 启动时间 | `2026-05-16 01:09:16` (Beijing) |

### 进度

- **Exp1**: 94 batches → **已完成**，结果已保存至 `artifacts/exp012/eval_fewnerd_exp1_llama-3.1-8b-instruct.json` (03:39)
- **Exp2**: 54 batches 总计, 已完成 ~24/54 batches (count_6/random/23 正在运行)
- **预估剩余**: ~30 batches × ~15s/batch ≈ 7-8 分钟

### Exp1 关键 Metrics（已完成）

**所有 94 个 batch 的 exact_F1 和 relaxed_F1 均为 0.0。** 只有 text_match 有非零值：

| 分组 | text_match_F1 范围 | BCS |
|------|-------------------|-----|
| count_1 (64 batches) | 0.025 ~ 0.833 | 0.0 |
| count_12 (5 batches) | 0.119 ~ 0.336 | 0.91 ~ 0.96 |
| count_22 (5 batches) | 未在 tail 中可见 | ~0.93 |
| count_44 (5 batches) | 未在 tail 中可见 | ~0.96 |
| count_64 (5 batches) | ~0.347 (最后一个) | 0.97 |

典型 count_64 batch: precision=0.489, recall=0.268, text_match_F1=0.347, total_pred=1455, total_gold=2652。所有 per_type_f1 = 0.0。

**解读**: LLaMA-3.1-8B 能找到部分文本 span，但**完全无法正确匹配实体类型**（exact/relaxed 全 0）。与 Qwen 模型的差异很大。

### 资源状态

| 资源 | 使用 | 总量 | 占比 |
|------|------|------|------|
| GPU 显存 | 84661 MiB | 97254 MiB | 87% |
| GPU 利用率 | 22% | | |
| 根分区 | 17G | 30G | 54% |
| 数据盘 | 213G | 250G | 85% |

### 结论

1. **进程存活**，cron miss 4/5 为误报（可能是进程检测方式与 vLLM 子进程模型不匹配）
2. Exp1 已完成，exp2 预计 ~8 分钟内完成
3. exact/relaxed F1 全零值得关注——可能是 LLaMA 输出格式与评估器的类型标签不匹配，而非模型真正无法做 NER。建议实验完成后检查 predictions JSON 中模型实际输出的类型标签格式

---
