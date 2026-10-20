# ops gpu readiness and exp002 verify

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_readiness_and_exp002_verify_20260514T041700_result.json`
- **Structured JSON:** [`d7bd17c5577ff8055335.json`](../../sessions/d7/d7bd17c5577ff8055335.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集。汇报如下。

---

## 1. GPU / Eval 进度

| GPU | PID | 任务 | 显存 | 当前进度 | 预计完成 |
|-----|-----|------|------|----------|----------|
| 0 | 251924 | 其他 | 10.0/24.0 GB | — | — |
| 1 | 249294+255322 | 其他 | 12.6/24.0 GB | — | — |
| 2 | 266521+266790 | 其他 | 7.3/24.0 GB | — | — |
| **3** | **242591** | **eval_3B_d000_s123** | 13.5/24.0 GB | HumanEval 123/164 (75%), ~28s/it | **~12:37 UTC (~20min)** |
| 4 | 271921 | 其他 | 18.5/24.0 GB | — | — |
| **5** | **250610** | **eval_1.5B_d000_s123** | 10.4/24.0 GB | HumanEval 103/164 (63%), ~24s/it | **~12:42 UTC (~25min)** |

两个 eval 都在跑最后一个 benchmark（HumanEval），mmlu/gsm8k/arc_challenge 已完成。均无报错（`libnvJitLink.so.13` warning 不影响运行）。

**注意**：cuda:5 跑的是 **Qwen2.5-1.5B**（非 15B），job 名 `eval_15B` 是命名偏差。

---

## 2. exp-002 代码完整性

| 文件 | 大小 | 状态 |
|------|------|------|
| compute_signals.py | 8.7KB | ✓ |
| signal_embedding.py | 7.8KB | ✓ |
| signal_minkpp.py | 8.6KB | ✓ |
| signal_constat.py | 4.1KB | ✓ |
| signal_selfcritique.py | 8.2KB | ✓ |
| aggregate_rrf.py | 7.7KB | ✓ |

**依赖**: sentence_transformers ✓ / faiss_cpu 1.13.2 ✓（已安装在 conda base）

**代码就绪**，可执行。

---

## 3. 3B d100 SFT 提交命令草案

参考 3B_d000_s42 的超参（batch=1, grad_accum=16, lr=2e-4, epochs=1, max_seq=2048）：

```bash
cd /root/contamcal-irt-calibration/exp001 && \
python train_sft.py \
  --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B \
  --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl \
  --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42 \
  --seed 42 \
  --gpu 3 \
  --batch-size 1 \
  --grad-accum 16 \
  --lr 2e-4 \
  --max-seq-length 2048 \
  --epochs 1
```

**提交前须遵守 C001**：先 `nvidia-smi` 确认 cuda:3 已无进程，再提交。

**已有 checkpoint 矩阵**：

| 模型 | d000_s42 | d000_s123 | d005_s42 | d100_s42 |
|------|----------|-----------|----------|----------|
| 0.5B | ✓ | ✓ | ✓ | ✓ |
| 1.5B | ✓ | ✓ | ✓ | ✓ |
| 3B | ✓ | ✓ | ✗ | **← 下一个** |

3B 缺 d005 和 d100。cuda:3 释放后先提交 d100（P1），后续再安排 d005。

---
