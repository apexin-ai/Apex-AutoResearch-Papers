# code llama fewnerd merge prep

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_fewnerd_merge_prep_20260518T222902_result.json`
- **Structured JSON:** [`112ab9946eb7711e6397.json`](../../sessions/11/112ab9946eb7711e6397.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All scripts pass syntax validation.

---

## 训练进度

| 指标 | 值 |
|---|---|
| Step | 20900 / 24708 (84.6%) |
| Loss | 0.0183 |
| Epoch | 2.54 / 3.0 |
| Best ckpt | checkpoint-20000 (eval_loss=0.0363) |
| ETA | ~2h22m |

## 脚本和路径确认

**3 个脚本：**
1. `code/merge_llama_fewnerd.py` — LoRA merge，支持 `--base_model` / `--adapter_path` / `--output_path` 参数
2. `code/run_llama_fewnerd_inference.sh` — 全流程：merge → 3-seed 并行推理 (GPU 0/2/3, seed 42/123/456) → 分析 → 清理 merged model
3. `code/analyze_llama_fewnerd_3seed.py` — 3-seed 聚合分析：greedy/oracle F1, degeneracy, 5-signal (SJ/FK/VC/EM/LP) selection F1 + global rho, DGS

**路径确认：**
| 资源 | 路径 |
|---|---|
| Base model | `/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct` |
| LoRA adapter | `/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-fewnerd-lora/` (训练完后 best model 在根目录) |
| FewNERD test | `/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/test.json` (37648 行) |
| Merged output | `checkpoints/llama3.1-8b-fewnerd-merged/` |
| 推理输出 | `output/llama_fewnerd_s{42,123,456}/` |
| 分析汇总 | `output/llama_fewnerd_3seed_summary/aggregated.json` |

训练完成后一条命令启动：`tmux new -s llama_fewnerd_infer 'bash code/run_llama_fewnerd_inference.sh'`

---
