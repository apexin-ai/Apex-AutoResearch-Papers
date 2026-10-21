# ops p1 westd16980 status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p1_westd16980_status_20260520T094351_result.json`
- **Structured JSON:** [`f7531ce61c3c4e61a2bd.json`](../../sessions/f7/f7531ce61c3c4e61a2bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态报告

### GPU

| GPU | 使用率 | 显存占用 | 总显存 |
|-----|--------|----------|--------|
| GPU0 | 90% | 68,143 MiB | 97,887 MiB (69.6%) |
| GPU1 | 0% | 0 MiB | 97,887 MiB (空闲) |

### 正在运行的 Python 进程

| PID | CPU | 启动时间 | 命令 |
|-----|-----|----------|------|
| 738751 | 100% | 17:02 (运行约42分钟) | `run_constrained_extraction.py --mode unconstrained --dataset docred --model_path qwen_lora_docred_merged --decoding_strategy beam --num_beams 8 --max_docs 200` |
| 349350 | 0% | May16 | http.server :18888 (checkpoint 文件服务) |
| 451275 | 0% | May17 | download_wiki.py |
| 485171 | 0% | May18 | http.server :18080 |
| 492102 | 0% | May18 | http.server :38980 |

系统进程: jupyter-lab, tensorboard (自启动，忽略)

### d065 Llama 进程

**无 d065 相关进程在跑。** 只匹配到 tmux session `llama_beam` 的壳进程。

### d066 Beam Sweep 进程

**正在跑。** `d066_qwen_beam_sweep.sh` 脚本活跃中：
- PID 712981/712982: bash 脚本（启动于 10:56）
- PID 712984: tee 日志写入
- PID 738751: 当前执行的是 **qwen_docred_200_beam8_unconstrained**（GPU0，100% CPU）
  - 输出: `/root/autodl-tmp/schema_outputs/d066_beam_sweep/qwen_docred_200_beam8_unconstrained.jsonl`

### outputs 目录最近文件

今天 (May 20) 生成了 16 个 d066 结果 JSON（10:01-10:02），涵盖：
- d066_scierc_zs_{s1,semantic,grammar,unc}.json
- d066_docred_zs_{s1,semantic,grammar,unc}.json
- d066_{llama,qwen}_{scierc,docred}_lora_{s1,unc}.json
- d068_guided_beam/ 目录 (May 20 00:27)

### tmux Sessions

| Session | 创建时间 |
|---------|----------|
| llama_beam | May 17 10:56 |
| llama_wikievents | May 18 00:42 |
| llama_wikievents_full | May 18 01:47 |
| qwen_wikievents | May 18 00:42 |

### nohup 输出

无 nohup.out 文件。

---

**总结**: GPU0 被 d066 beam sweep 占用（qwen_docred beam8 unconstrained 正在跑），GPU1 完全空闲。d065 无活跃进程。

---
