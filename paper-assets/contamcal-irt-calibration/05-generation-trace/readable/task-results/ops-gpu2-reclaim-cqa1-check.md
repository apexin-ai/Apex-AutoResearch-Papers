# ops gpu2 reclaim cqa1 check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu2-reclaim-cqa1-check_20260521T090801_result.json`
- **Structured JSON:** [`7f0df6bd2c239b54e772.json`](../../sessions/7f/7f0df6bd2c239b54e772.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Task A: westd GPU 2 回收 ✓

| 步骤 | 状态 |
|------|------|
| Kill Gemma-2 d100_s0 GSM8K (PID 503544 + 子进程 503545) | ✓ 已终止 |
| GPU 2 清空确认 | ✓ 0%, 0 MiB |
| 启动 OLMo-2 d005_s0 GSM8K on GPU 2 | ✓ PID 505062, CUDA_VISIBLE_DEVICES=2, 16696 MiB, 正在 evaluating |

**westd 当前 4 GPU 全满：**
- GPU 0: OLMo-2 d100_s0 GSM8K (PID 502704)
- GPU 1: OLMo-2 d000_s0 GSM8K (PID 500728)
- GPU 2: **OLMo-2 d005_s0 GSM8K** (PID 505062) ← 新启动
- GPU 3: Phi-4 d100_s0 GSM8K (PID 501665)

⚠️ evaluate.py 37775 bytes vs C009 reference 37591 bytes — server 内 4 个 eval 用同一文件，内部一致，但与 reference 有差异。

### Task B: cqa1 GSM8K eval 可用性

**cqa1 不适合跑 OLMo-2/Phi-4 GSM8K eval。** 原因：

- evaluate.py 存在 ✓
- **缺 OLMo-2 base model** — `/root/autodl-tmp/models/` 无 OLMo-2
- **缺 Phi-4 base model** — 无 phi-4
- **缺 OLMo-2/Phi-4 SFT checkpoints** — 全部是 Qwen / Llama / Gemma
- GPU: 单卡 RTX 4090 D (24GB)，64% 利用率（有东西在跑）
- 可用 base models: Qwen2.5-7B, Llama-3.2-3B, gemma-2-9b, Qwen2.5-14B 等
- 可用 checkpoints: Qwen (0.5B/1.5B/3B/7B/14B), Llama-3.2-3B, gemma-2-9b 各 dosage

**结论：cqa1 有丰富的 Qwen/Llama GSM8K eval 资源，但与 westd 当前需要跑的 OLMo-2/Phi-4 不匹配。传输 base model (7-14GB) 违反"不要 SCP 大文件"约束。**

---
