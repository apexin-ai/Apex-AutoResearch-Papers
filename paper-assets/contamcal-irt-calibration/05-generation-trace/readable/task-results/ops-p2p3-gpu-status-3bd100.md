# ops p2p3 gpu status 3Bd100

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p2p3_gpu_status_3Bd100_20260514T184618_result.json`
- **Structured JSON:** [`410017e1ba8615e2c5fd.json`](../../sessions/41/410017e1ba8615e2c5fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 418705 is dead. Here's the full picture:

## GPU Status

| GPU | Status | PID | Process | VRAM |
|-----|--------|-----|---------|------|
| 0 | **IDLE** | — | — | 0 MiB |
| 1 | **IDLE** | — | — | 0 MiB |
| 2 | **BUSY** (38%) | 422138 (wrapper: 422128) | `compute_signals.py` — exp-002 0.5B d025 signals (embedding, minkpp, selfcritique) | 20,377 MiB |
| 3 | **BUSY** (44%) | 420195 | `train_sft.py` — **3B d100 SFT** | 13,325 MiB |
| 4 | **BUSY** (53%) | 420910 (wrapper: 420905) | `evaluate.py` — 1.5B d025 eval (aligned) | 5,857 MiB |
| 5 | **BUSY** (46%) | 405520 (wrapper: 405515) | `train_sft.py` — 3B d000 v2 SFT | 18,661 MiB |

对比 Director 关注的点：
- **cuda:0** — 已释放，空闲 ✓
- **cuda:2** — exp-002 d025 signals 在跑（PID 422138，非原来的 422128，422128 是 wrapper）
- **cuda:3** — PID 418705 (exp_006 GSM8K Stan) **已死**，当前占用者是 3B d100 SFT (PID 420195)
- **cuda:4** — 1.5B d025 eval 仍在跑 (PID 420910)
- **cuda:5** — 3B d000 v2 SFT 仍在跑 (PID 405520)

## 3B d100 SFT

- **PID 420195: ALIVE**，运行在 GPU 3
- **超参: `lr=5e-5, alpha=16`** — 这是 D020 校准后的正确超参
- 完整命令: `train_sft.py --model-name Qwen2.5-3B --data-path sft_dosage_100.jsonl --output-dir Qwen2.5-3B_d100_s42 --gpu 3 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 16`
- **Recommendation: CONTINUE** — 超参正确，无需 kill 重训

---
