# check server full probe

**solver trace ablation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_server_full_probe_20260513T085746_result.json`
- **Structured JSON:** [`22d0b10b203232aa89c6.json`](../../sessions/22/22d0b10b203232aa89c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 探测结果汇总

### 1. GPU 状态
| GPU | 型号 | 显存占用 | 总显存 | 利用率 |
|-----|------|---------|--------|--------|
| GPU 0 | NVIDIA RTX PRO 6000 Blackwell Server Edition | 79,003 MiB | 97,887 MiB | 49% |
| GPU 1 | NVIDIA RTX PRO 6000 Blackwell Server Edition | 82,991 MiB | 97,887 MiB | 0% |

**GPU 进程**: PID 10532 (`python phase0_orthogonality.py`) 占用双卡（78,992 + 82,980 MiB）

### 2. Phase 0 v2 状态：**运行中**
- tmux session `phase0_ortho_v2`，14:28 启动，已运行 ~2.5 小时
- **当前进度**: Step 2 生成阶段，已生成 **4704/5000** samples（~94%）
- 最后日志时间: 16:58，每 ~100 samples 约 2.5-3 分钟
- **无错误**，预计 ~10 分钟内完成 Step 2 生成
- Step 1 (Fine-tuning) 已完成，checkpoint 已保存

### 3. correlation_matrix.json
**不存在**。尚未生成——当前仍在 Step 2 生成阶段，correlation matrix 应在后续步骤产出。

### 4. 日志关键行
```
14:28:10 - 加载数据完成 (train 8000, val 1000, test 1000)
14:28:10 - [Step 1] Fine-tuning on 8000 samples
         - trainable params: 4,358,144 / 1,548,072,448 (0.28%)
14:51   - checkpoint 保存完成
         - [Step 2] 开始生成 5000 samples
16:58:04 - [Step 2] Generated 4704/5000 samples  ← 最新
```

### 5. Python 环境
- Python 3.12.3 (conda base)
- **torch 2.10.0+cu128**, accelerate 1.13.0
- transformers 4.57.6, peft 0.19.0, trl 1.1.0
- datasets 4.8.4, sentence-transformers 5.4.1
- sacrebleu 2.6.0, scipy 1.17.1, matplotlib 3.10.5

### 6. 已下载模型
- **Qwen2.5-1.5B** (`/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B/config.json`)

### 7. 数据文件
| 文件 | 行数 |
|------|------|
| train.jsonl | 8,000 |
| val.jsonl | 1,000 |
| test.jsonl | 1,000 |
| **合计** | **10,000** |

### 8. Phase 0 输出目录
- `outputs/phase0/checkpoint/` — LoRA adapter 已保存（adapter_model.safetensors 17MB）
- `outputs/phase0/run.log` — 71KB 运行日志
- `scored_samples.jsonl` — **尚未生成**

---
