# ssh check 16980 gpu status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_16980_gpu_status_20260518T223946_result.json`
- **Structured JSON:** [`233d6df15cfcd4fe0bf3.json`](../../sessions/23/233d6df15cfcd4fe0bf3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**GPU 状态**
| GPU | 型号 | 显存 | GPU-Util | 功耗 |
|-----|------|------|----------|------|
| 0 | RTX PRO 6000 Blackwell (96GB) | 18277 / 97887 MiB | **90%** | 335W/600W |
| 1 | RTX PRO 6000 Blackwell (96GB) | 0 / 97887 MiB | 0% | 空闲 |

**当前活跃进程 (PID 595176, GPU 0)**
正在运行 **推理** (不是训练)：
```
python3 run_constrained_extraction.py \
  --dataset wikievents --mode unconstrained \
  --model_path .../llama_8b_lora_wikievents_merged \
  --output_path outputs/ee_llama_ft_wikievents_unconstrained.jsonl \
  --device cuda:0
```
这是 tmux 会话 `p1_llama_ee_ft`（刚创建于 06:25）中运行的 wikievents unconstrained 评估。

**tmux 会话**
- `p1_llama_ee_ft` — 当前活跃，运行上述推理
- `llama_beam` / `llama_wikievents` / `llama_wikievents_full` / `qwen_wikievents` — 旧会话

**训练日志 `/root/runs/schema_semantic_constrained_ie/p1_ee_ft_llama.log`**
这个日志是之前失败的训练，结尾是 `EXIT_CODE=1`，报错：
> `ImportError: gptqmodel requires optimum version 1.24.0 or higher`

PEFT 加载 LoRA adapter 时触发了 AWQ dispatcher 中的 gptqmodel 检查。

**结论**：训练未在跑。GPU 0 上跑的是 Llama wikievents unconstrained 模式的推理评估。GPU 1 空闲。之前的训练因 `optimum` 版本不足导致失败。

---
