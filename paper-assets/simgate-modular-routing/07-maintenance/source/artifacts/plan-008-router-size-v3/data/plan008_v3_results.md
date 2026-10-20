Log files on server westb-13313:
- /root/autodl-tmp/simgate-modular-routing/logs/plan008_v3.log (0.6B + 1.7B runs)
- /root/autodl-tmp/simgate-modular-routing/logs/plan008_v3_4b.log (4B run, batch_size=2)

Checkpoints:
- /root/autodl-tmp/simgate-modular-routing/checkpoints/plan-008-v3-qwen3-0.6b/final_adapter/
- /root/autodl-tmp/simgate-modular-routing/checkpoints/plan-008-v3-qwen3-1.7b/final_adapter/
- /root/autodl-tmp/simgate-modular-routing/checkpoints/plan-008-v3-qwen3-4b/final_adapter/

Results Summary:
| Model      | train_loss | eval_loss | Runtime | batch_size | grad_accum |
|------------|-----------|-----------|---------|-----------|-----------|
| Qwen3-0.6B | 5.627     | 0.317     | 169s    | 4         | 8         |
| Qwen3-1.7B | 10.132    | 0.378     | 183s    | 4         | 8         |
| Qwen3-4B   | 17.348    | 0.308     | 378s    | 2         | 16        |

Note: 4B OOM'd with batch_size=4, required batch_size=2 + grad_accum=16.
All runs used: epochs=3, lr=2e-5, seed=42, upsample_minority, LoRA r=16/alpha=32.