# ops exp002 signal dryrun

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp002-signal-dryrun_20260514T084100_result.json`
- **Structured JSON:** [`f105d716db835a9c75ef.json`](../../sessions/f1/f105d716db835a9c75ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇报：

## 验证结果：**脚本就绪，可立即运行**

### 1. 脚本
- `run_signals_05B.sh` ✓ — 完整，3sig 模式跑 embedding/minkpp/selfcritique，遍历 d000/d005/d100 × mmlu/gsm8k/arc_challenge
- `compute_signals.py` ✓ — 支持 `--dry-run`
- `aggregate_rrf.py` ✓

### 2. Python 依赖
- `torch`, `faiss`, `sentence_transformers` ✓ — 均已安装在 `/root/miniconda3/lib/python3.12/site-packages/`
- sentence-transformers 模型 `all-MiniLM-L6-v2` 和 `all-mpnet-base-v2` 已缓存

### 3. 数据文件
| 资源 | 状态 |
|------|------|
| Base model `Qwen2.5-0.5B` | ✓ 已缓存 |
| LoRA d000_s42 | ✓ `adapter_model.safetensors` 存在 |
| LoRA d005_s42 | ✓ |
| LoRA d100_s42 | ✓ |
| SFT data (000/005/100) | ✓ 50000/50826/66533 行 |
| Benchmark: mmlu | ✓ 已缓存 |
| Benchmark: gsm8k | ✓ 已缓存 |
| Benchmark: arc_challenge | ✓ 已缓存 |

### 4. 运行命令
```bash
CUDA_VISIBLE_DEVICES=1 bash /root/contamcal-irt-calibration/exp002/run_signals_05B.sh 3sig
```

### 5. 预计运行时间
3 dosage × 3 benchmark × 3 signal = 27 个信号计算任务。0.5B 模型较小，单 GPU 估计 **1.5–3 小时**（取决于 selfcritique 的生成量和 embedding 编码速度）。

### 6. 注意事项
- 运行前需按 C001 约束执行 `nvidia-smi` 确认 cuda:1 无同类进程
- 脚本首行 `source /etc/network_turbo` 已配置（benchmark 数据虽已缓存，但 HF datasets 仍可能检查更新）

---
