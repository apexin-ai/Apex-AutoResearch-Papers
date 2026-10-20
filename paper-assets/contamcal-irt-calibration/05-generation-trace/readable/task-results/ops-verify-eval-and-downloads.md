# ops verify eval and downloads

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-eval-and-downloads_20260518T132730_result.json`
- **Structured JSON:** [`aba4014d42143184cd9d.json`](../../sessions/ab/aba4014d42143184cd9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 任务 1：evaluate.py batch generation 改造验证

**结果：改造正确，全部通过。**

| 检查项 | 状态 |
|--------|------|
| 语法检查 | OK |
| `evaluate_gsm8k` batch generation | OK — `for i in range(0, len(prompts), batch_size)` 循环，left padding，批量 `model.generate` |
| `evaluate_humaneval` batch generation | OK — 同上结构，批量生成 + 逐样本后处理 |
| `padding_side = "left"` 设置 | OK — 两个函数都有，且退出前恢复原值 |
| `--batch-size` CLI 参数 | OK — argparse 定义（默认 8），传递到所有 evaluate 函数 |
| `batch_compute_choice_logprobs` | 未出现（choice-based benchmarks 未改造，符合预期） |

另外注意：有一个 eval 进程正在运行（PID 25320），在 cuda:1 上跑 `Qwen2.5-7B_d000_s42` 的 gsm8k 评测。

---

### 任务 2：模型下载进度

| 模型 | 路径 | safetensors | 大小 | incomplete | 进度 | 状态 |
|------|------|-------------|------|------------|------|------|
| **Phi-4** | `/root/autodl-tmp/models/phi-4/` | 2 | 20G | 4 | 12/21 files (57%) | 下载中 |
| **OLMo-2-1124-7B** | `/root/autodl-tmp/models/OLMo-2-1124-7B/` | 4 | 25G | 2 | 7/16 files (44%) | 下载中（遇到 timeout，自动重试中） |
| **Gemma-2-9b** | `/root/autodl-tmp/models/gemma-2-9b/` | 5 | 32G | 3 | 6/18 files (33%) | 下载中（较慢，~75min/file） |

补充发现：还有一个 **Qwen2.5-14B** 在通过 `snapshot_download` 下载到 HF 缓存（PID 28640）。

### 活跃下载进程

| PID | 模型 | 方式 |
|-----|------|------|
| 6380 | gemma-2-9b | `hf download` → local-dir |
| 19571 | OLMo-2-1124-7B | `hf download` → local-dir |
| 19608 | phi-4 | `hf download` → local-dir |
| 28640 | Qwen2.5-14B | `snapshot_download` → HF cache |

OLMo-2 的 xet bridge 下载出现过 timeout 错误但在自动重试，Gemma-2 下载速度最慢（每文件约 75 分钟）。三个模型都还需数小时才能完成。

---
