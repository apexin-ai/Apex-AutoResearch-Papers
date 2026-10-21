# infra gpu utilization diag

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu_utilization_diag_20260513T185110_result.json`
- **Structured JSON:** [`c970dcb5b85b7bef663e.json`](../../sessions/c9/c970dcb5b85b7bef663e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已采集完毕，下面是诊断结果。

---

## GPU 利用率诊断报告

### 1. 实时状态

| GPU | 实验 | 状态 | GPU Util | 显存占用 | 温度 |
|-----|------|------|----------|----------|------|
| 0 | SciERC | **已完成** (551/551, EXIT_CODE=0) | 0% | 0 MiB / 97887 MiB | 28°C |
| 1 | DocRED | 运行中 (149/998) | 87% | 16943 MiB / 97887 MiB | 53°C |

**"43.5% 平均利用率"的真相**：(0% + 87%) / 2 = 43.5%。SciERC 已跑完退出，GPU 0 完全空闲拉低了平均值。GPU 1 实际利用率 87%，并不算差。

### 2. 推理方式分析

两个脚本都用 **transformers 后端 + 逐条顺序推理**：

**`run_extraction.py` (SciERC)**：
- 有 `--batch_size` 参数（default=32），但 transformers 路径完全忽略它——循环里是 `for i, sample in enumerate(samples)` 逐条 `model.generate()`
- batch_size 只在 vLLM 路径生效，而 vLLM 不支持 Qwen3，所以实际跑的是 transformers 逐条推理
- 已完成，38分47秒处理551条，平均 4.22s/sample

**`run_extraction_docred.py` (DocRED)**：
- **没有 batch_size 参数**
- 纯逐条推理：每个 doc → tokenize → `model.generate()` → decode → 写文件
- 每条耗时 3-36 秒不等（取决于文档长度），均值约 18.5s/doc
- 输出文件用 `"w"` 模式打开，**无断点续跑支持**

### 3. 瓶颈诊断

| 指标 | 数值 | 判断 |
|------|------|------|
| GPU Util | 87% | 合理——13% gap 来自 generate() 间的 CPU 开销（tokenize/decode/IO/Python） |
| 显存利用率 | 16.9GB / 97.9GB = **17.3%** | 严重浪费 |
| 推理方式 | 逐条串行 | **主瓶颈**——batch=1 让 GPU 大部分时间在等单条 sequence 的 autoregressive decoding |
| I/O bound? | 否 | GPU util 稳定 87%，不是高低波动模式；瓶颈在 autoregressive decoding 本身是串行的 |

**核心问题**：94GB 显存的卡只装了 16GB 模型 + 单条推理的 KV cache，剩下 80GB 完全闲置。应该用 batch 推理同时处理多条。

### 4. DocRED 预计完成时间

- 已处理：149/998（14.9%）
- 启动时间：02:05 UTC，已跑 46 分钟
- 平均速度：149 / 46 = 3.24 doc/min
- 剩余：849 docs ÷ 3.24 = **~262 分钟 ≈ 4.4 小时**
- 预计完成：**~07:15 UTC（北京时间 15:15）**

### 5. 优化建议

#### A. 当前实验（不停机）
- **无法优化**。DocRED 正在跑且无 batch 接口，改代码需要停掉重启。
- GPU 0 空闲，如果有其他任务可以跑起来。

#### B. 重启 DocRED（需停机，推荐）

代价：需停止当前进程并重跑全部 998 条（因为输出文件是 `"w"` 模式，无续跑）。但如果优化后速度提升 3-4x，总时间反而更短。

| 优化项 | 预期提升 | 改动量 |
|--------|----------|--------|
| **加 batch 推理** (batch_size=4-8) | 2-4x | 改 ~30 行代码 |
| **双 GPU 数据并行** (GPU0 跑前 499 条，GPU1 跑后 499 条) | 2x | 启动两个进程 |
| **batch + 双 GPU** | 4-8x | 上述两项组合 |
| **加续跑支持** (`"a"` 模式 + skip processed) | 避免重跑已完成部分 | 改 ~15 行 |

**最优方案**：batch=4 + 双 GPU 并行 → 998 条预计 ~30-60 分钟完成（vs 当前剩余 4.4 小时）。

#### C. 未来实验通用优化

| 方案 | 说明 |
|------|------|
| **SGLang** | vLLM 替代品，Qwen3 支持更好，continuous batching + RadixAttention |
| **vLLM 更新** | 检查 vLLM ≥ 0.19 是否已支持 Qwen3 |
| **torch.compile** | `model = torch.compile(model)` 可加速 ~10-20%，无侵入 |
| **flash_attention_2** | Qwen3 默认应该已启用，可用 `model.config._attn_implementation` 确认 |

---

**结论**：43.5% 是假象（一块 GPU 已空闲），实际瓶颈是逐条推理浪费 83% 显存。建议停掉当前 DocRED 进程，加 batch 推理 + 双 GPU 并行重跑，预计总时间从 4.4 小时降到 30-60 分钟。是否需要我修改 `run_extraction_docred.py` 加上 batch 推理和续跑支持？

---
