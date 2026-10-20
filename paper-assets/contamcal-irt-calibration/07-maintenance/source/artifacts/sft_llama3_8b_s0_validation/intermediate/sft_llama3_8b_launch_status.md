## LLaMA-3.1-8B SFT Validation (d000/d025/d100, seed=0)

Server: westd-29999
Model: /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B
Base model (not Instruct), vocab_size=128000

### Training Config
- LoRA: r=16, alpha=32, dropout=0.05
- Targets: q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj
- LR: 5e-5, epochs: 1, batch_size: 2, grad_accum: 8 (effective bs=16)
- max_seq_length: 2048, gradient_checkpointing: True, seed: 0
- No merge (adapter only, disk tight at 19GB free)

### Jobs
| Dosage | GPU | PID | Total Steps | Log | Output Dir |
|--------|-----|-----|-------------|-----|------------|
| d000 | 1 | 508650 | 3125 | /tmp/sft_llama3_d000_s0.log | /root/autodl-tmp/exp001/checkpoints/Meta-Llama-3.1-8B_d000_s0 |
| d025 | 0 | 509577 | 3384 | /tmp/sft_llama3_d025_s0.log | /root/autodl-tmp/exp001/checkpoints/Meta-Llama-3.1-8B_d025_s0 |
| d100 | 3 | 510202 | 4159 | /tmp/sft_llama3_d100_s0.log | /root/autodl-tmp/exp001/checkpoints/Meta-Llama-3.1-8B_d100_s0 |

### Memory Usage
- GPU 0 (d025): 51.0 GB / 97.9 GB
- GPU 1 (d000): 44.5 GB / 97.9 GB  
- GPU 3 (d100): 29.9 GB / 97.9 GB (still loading)

### ETA (UTC)
- d000: ~20:20
- d025: ~20:35
- d100: ~21:00

Started: 2026-05-21 ~17:58 UTC