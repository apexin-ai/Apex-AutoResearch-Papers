# infra olmo pipeline launch

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_olmo-pipeline-launch_20260514T141126_result.json`
- **Structured JSON:** [`80ec1b0749abe3438aa4.json`](../../sessions/80/80ec1b0749abe3438aa4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部任务完成。汇总产出：

---

**OLMo-1B 模型信息**
| 项目 | 值 |
|---|---|
| Model type | `olmo` (native transformers) |
| 参数量 | 1.18B |
| 架构 | 16 layers, 16 heads, d=2048, SwiGLU, RoPE |
| Vocab | 50280 (EOS=50279, PAD=1, BOS=None) |
| LoRA target_modules | `q_proj,k_proj,v_proj` |
| 来源 | `allenai/OLMo-1B-hf` via ModelScope |
| 本地路径 | `/root/autodl-tmp/models/olmo-1b-hf/` |

**脚本修改清单**
- 新建 `scripts/run_pipeline_olmo.sh`（基于 run_pipeline.sh，使用 OLMo 路径和 target_modules）
- 新建 `data/olmo/depth_0.jsonl`（从 data/depth_0.jsonl 复制，5000 条）
- 新建目录 `data/olmo/`, `checkpoints/olmo/`
- 现有脚本无需修改（已支持 --target_modules、--model_name 参数，pad_token/bos_token 兜底已有）

**Pipeline 启动证据**
- experiment_id: `cross_model_olmo_001`
- tmux session: `cross_model_olmo_001`
- PID: 120957
- GPU 0 利用率: 94%, 12.3GB VRAM
- 训练速度: ~4.38 it/s, 939 steps/epoch × 3 epochs

---
