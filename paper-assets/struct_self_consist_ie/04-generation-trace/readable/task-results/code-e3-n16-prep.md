# code e3 n16 prep

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_e3_n16_prep_20260514T092556_result.json`
- **Structured JSON:** [`96e395e2de4b741f797a.json`](../../sessions/96/96e395e2de4b741f797a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完毕。汇报结果：

## E3 代码就绪报告：**Yes，无需代码修改**

### N=16 支持确认

| 检查项 | 结果 |
|--------|------|
| `--n_samples` 参数 | `type=int`，无上限校验，直接传递给 vLLM `n=` 参数 |
| `sampling.py` | `n_samples` 作为函数参数透传，无硬编码限制 |
| `consistency.py` Fleiss' Kappa | 通用实现，N 仅影响 rating matrix 行数 |
| `consistency.py` Soft Jaccard | `combinations(range(n), 2)` → C(16,2)=120 对，每对做 Hungarian matching，轻量 CPU 计算 |
| 报告/verdict 逻辑 | 全部通用，无 N=8 硬编码 |

### 资源估算

| 指标 | N=8 (E2 实际) | N=16 (E3 预估) |
|------|---------------|----------------|
| 推理时间 | ~2-3h | ~4-6h |
| Consistency 计算 | 28 pairs/inst | 120 pairs/inst (~4.3x，但 CPU 耗时可忽略) |
| 显存 | RTX 5090 32GB 够用 | 不变（vLLM batch 大小无关 N） |
| 实例数 | 551 | 551 |

### 完整启动命令

```bash
cd /root/autodl-tmp/struct_self_consist_ie && \
CUDA_VISIBLE_DEVICES=0 nohup python3 code/run_mvp_pilot.py \
  --model_path checkpoints/qwen3-8b-scierc-merged-v2 \
  --data_dir data/scierc/processed_data \
  --dataset scierc \
  --subtask joint \
  --n_samples 16 \
  --temperature 0.7 \
  --max_tokens 1024 \
  --output_dir output/e3_ner_n16 \
  --num_test 551 \
  --seed 42 \
  --tensor_parallel 1 \
> output/e3_ner_n16.log 2>&1 &
```

注意：温度用 **0.7** 而非 1.0，与 E2 (mvp_pilot_005) 保持一致。E2 在 T=0.7 下 RE 子任务已有 42% 的 sample F1=0 率，T=1.0 会更糟。

---
