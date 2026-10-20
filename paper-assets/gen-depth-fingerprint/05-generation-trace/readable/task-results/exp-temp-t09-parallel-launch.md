# exp temp t09 parallel launch

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_temp-t09-parallel-launch_20260518T165526_result.json`
- **Structured JSON:** [`bb1749589c509cddfd0f.json`](../../sessions/bb/bb1749589c509cddfd0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. t=0.9 generation 成功启动

| tmux session | GPU | 模型 | 进度 | 速度 | 预计总时长 |
|---|---|---|---|---|---|
| `temp_olmo_t09` | GPU 2 | OLMo-2-1B t=0.9 | 27/995 | ~8.67s/it | ~2.4h |
| `temp_qwen06_t09` | GPU 3 | Qwen3-0.6B t=0.9 | 20/996 | ~11.28s/it | ~3.1h |

### 2. 使用的完整命令

**OLMo t=0.9 (GPU 2):**
```bash
tmux new-session -d -s temp_olmo_t09 "source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint && python generate_chain.py --model-name olmo-2-1b-t09 --model-path /root/autodl-tmp/models/olmo-2-1b-hf/allenai/OLMo-2-0425-1B --temperature 0.9 --top-p 0.9 --output-dir data/ --device cuda:2 ..."
```

**Qwen3-0.6B t=0.9 (GPU 3):**
```bash
tmux new-session -d -s temp_qwen06_t09 "source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint && python generate_chain.py --model-name qwen3-0.6b-t09 --model-path /root/autodl-tmp/models/Qwen/Qwen3-0___6B-Base --temperature 0.9 --top-p 0.9 --output-dir data/ --device cuda:3 ..."
```

### 3. GPU 使用情况 — 4 张全部在用

| GPU | 显存占用 | 任务 |
|---|---|---|
| 0 | 3625/32607 MiB | OLMo t=0.5 (901/995) |
| 1 | 1827/32607 MiB | Qwen t=0.5 (604/996) |
| 2 | 3625/32607 MiB | OLMo t=0.9 (27/995) |
| 3 | 1825/32607 MiB | Qwen t=0.9 (20/996) |

### 4. Monitor 脚本 — 不需要修改

- 32GB RTX 5090 显存充裕，extraction（~2GB）与 generation（~3.6GB）共用同一 GPU 不会 OOM
- `can_start` 排序逻辑（t=0.5 pipeline 完成后才跑 t=0.9 pipeline）在当前场景仍然合理
- 原脚本 t=0.5 完成后会在 GPU 0/1 尝试跑 t=0.9，与 GPU 2/3 并发写同一文件。`generate_chain.py` 的 crash recovery + append 模式保证安全（最坏情况少量重复记录，可去重）

---
