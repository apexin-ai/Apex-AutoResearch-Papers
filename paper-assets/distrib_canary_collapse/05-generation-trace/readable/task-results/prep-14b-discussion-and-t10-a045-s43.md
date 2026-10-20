# prep 14b discussion and t10 a045 s43

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_14b_discussion_and_t10_a045_s43_20260522T232435_result.json`
- **Structured JSON:** [`b5e4f1dc955490e362c2.json`](../../sessions/b5/b5e4f1dc955490e362c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**Part 1 — 部署命令已写入 memory.md "待部署实验" 段：**

```bash
cd /root/autodl-tmp/distrib_canary_collapse && \
tmux new-session -d -s 14b_t10_a045_s43 && \
tmux send-keys -t 14b_t10_a045_s43 'export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && CUDA_VISIBLE_DEVICES=4 python -u iterative_train.py --model_name /root/autodl-tmp/.ms_cache/EleutherAI/pythia-1.4b-deduped --data_dir data/wikitext103_5k --synthetic_ratio 0.45 --num_generations 10 --steps_per_gen 5000 --output_dir results/phase_diagram/t10_a045_s43_fp32_14b --seed 43 --batch_size 4 --max_length 512 --lr 5e-5 --gen_max_new_tokens 256 --gen_batch_size 8 --top_p 0.95 --optim adamw_torch --gradient_checkpointing 2>&1 | tee logs/scale_14b_t10_a045_s43_fp32.log' Enter
```

变更点 vs s42: `--seed 43`, `--output_dir .../t10_a045_s43_fp32_14b`, tmux session name `14b_t10_a045_s43`, log file `scale_14b_t10_a045_s43_fp32.log`。其余参数完全一致。

**Part 2 — Discussion 模板已保存并注册：**
- 文件: `artifacts/discussion_14b_template.md` (art_20260522_2e300e)
- 结构: Opening → Sync-dip Disappearance → PermG Attenuation → ECE Robustness → Implications
- 7 个 PLACEHOLDER 标记待填: cross-seed s43 (×3 α), T=15 results, ECE analysis, mechanism hypothesis, α_c shift confirmation

---
