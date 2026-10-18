# code prepare olmo temp09 submission

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_olmo_temp09_submission_20260514T203347_result.json`
- **Structured JSON:** [`c0a0d74849fd770bca17.json`](../../sessions/c0/c0a0d74849fd770bca17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇总如下：

---

**Registry entry: `olmo_temp09_001`** — PREPARING
- hypothesis: OLMo-1B temp-only τ=0.9 递归深度信号与 nucleus p=0.95 一致
- parent: `cross_model_olmo_002`
- plan_id: `plan_002b`

**脚本确认: `scripts/run_pipeline_olmo_temp09.sh`**
- 模型: `/root/autodl-tmp/models/olmo-1b-hf`
- 解码: `temp_only`, temperature=0.9
- 数据: `data/olmo_temp09/depth_{1,2,3}.jsonl`
- Checkpoint: `checkpoints/olmo_temp09/lora_depth_{0,1,2}`
- depth-0 adapter 复用 nucleus 版本 (symlink)
- LoRA target: `q_proj,k_proj,v_proj`

**启动命令:**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recursive_gen_depth_est && bash scripts/run_pipeline_olmo_temp09.sh"
```

**`allocate_and_submit` 参数:**
| 参数 | 值 |
|------|-----|
| exp_id | `olmo_temp09_001` |
| server | `gpu-6000pro-2` |
| gpu | `1` (待 gpt2xl_temp09_001 完成释放 cuda:1) |
| command | 上述启动命令 |
| data_path | `data/olmo_temp09/` |
| model_name | `olmo-1b-hf` |
| seed | 42 |

---
