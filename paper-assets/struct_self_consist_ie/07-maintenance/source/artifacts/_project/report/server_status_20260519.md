# Server Status Check — 2026-05-19 21:15 UTC

## ⚡ 72B FewNERD (Server B — autodl-5090-b) — RUNNING (Greedy Phase)

- 进程状态: PID 59040 存活，已运行 5h13m
- 脚本: `zeroshot_inference_72b.py --datasets scierc conll2003 fewnerd`
- 阶段进度:
  - scierc: ✅ 完成 (529 instances × 8 samples)
  - conll2003: ✅ 完成 (2756 instances × 8 samples)
  - fewnerd: Stochastic ✅ 完成 (耗时 16194s ≈ 4.5h)，**Greedy 🔄 进行中** — 9909/37648 (26%)
- Greedy 速度: ~9.7 prompts/s
- Greedy ETA: ~48 min → **~22:00 UTC May 19**
- 信号报告: scierc + conll2003 的 full_signal_report.json 已生成，fewnerd 待 greedy 完成后生成

### scierc 结果摘要 (72B zero-shot)
| Method | F1 | 95% CI |
|--------|-----|--------|
| Greedy | 0.399 | [0.375, 0.425] |
| Majority Vote | 0.413 | [0.387, 0.439] |
| Oracle | 0.549 | [0.524, 0.574] |
| Best signal (VC) | ρ=0.277 | — |

### conll2003 结果摘要 (72B zero-shot)
| Method | F1 | 95% CI |
|--------|-----|--------|
| Greedy | 0.712 | [0.697, 0.727] |
| Majority Vote | 0.703 | [0.689, 0.718] |
| Oracle | 0.765 | [0.751, 0.779] |
| Best signal (SJ) | ρ=0.304 | — |

## Server A (autodl-5090) — 32B Training
- 实验: exp_qwen25_32b_fewnerd (seed=42)
- Step: 4000/41180 (9.7%), Epoch 0.49
- Loss: 0.0627 (step 4000), grad_norm: 0.126
- LR: 1.94e-4
- Speed: ~2.5 s/step
- 当前状态: 评估中 (1238/2353 eval samples, 52%)
- ETA: ~27-28h → **~01:00 UTC May 21**

## Server C (autodl-5090-c) — 14B + 7B Training

### 14B (cuda:0,1, PID 56773)
- 实验: exp_qwen25_14b_fewnerd (seed=42)
- Step: 7196/41180 (17.5%), Epoch 0.87
- Loss: 0.0573 (step 7150), grad_norm: 0.600
- Speed: ~2.2 s/step
- 最近 checkpoint: checkpoint-6000 (saved at 4h22m)
- ETA: ~21h → **~18:00 UTC May 20**

### 7B (cuda:2,3, PID 71837)
- 实验: exp_qwen25_7b_fewnerd (seed=42)
- Step: 2467/20590 (12.0%), Epoch 0.59
- Loss: 0.0628 (step 2450), grad_norm: 0.395
- Speed: ~2.3 s/step
- 最近 checkpoint: checkpoint-2000 (saved at 1h25m)
- ETA: ~11.5h → **~09:00 UTC May 20**

## GPU Utilization

### Server B (4× RTX 5090)
| GPU | Util | VRAM | Temp | Power |
|-----|------|------|------|-------|
| 0 | 100% | 31.9/32.6 GB | 68°C | 381W |
| 1 | 100% | 31.9/32.6 GB | 64°C | 385W |
| 2 | 100% | 31.9/32.6 GB | 64°C | 379W |
| 3 | 100% | 31.9/32.6 GB | 66°C | 370W |
进程: VLLM TP=4 workers

### Server A (4× RTX 5090)
| GPU | Util | VRAM | Temp | Power |
|-----|------|------|------|-------|
| 0 | 93% | 29.8/32.6 GB | 76°C | 449W |
| 1 | 100% | 29.8/32.6 GB | 78°C | 454W |
| 2 | 100% | 29.9/32.6 GB | 73°C | 463W |
| 3 | 100% | 28.6/32.6 GB | 76°C | 476W |

### Server C (4× RTX 5090)
| GPU | 任务 | Util | VRAM | Temp | Power |
|-----|------|------|------|------|-------|
| 0 | 14B | 100% | 25.9/32.6 GB | 57°C | 295W |
| 1 | 14B | 97% | 25.5/32.6 GB | 73°C | 513W |
| 2 | 7B | 68% | 16.7/32.6 GB | 67°C | 504W |
| 3 | 7B | 78% | 17.7/32.6 GB | 65°C | 459W |
