# ssh check 5090c status

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_5090c_status_20260521T182044_result.json`
- **Structured JSON:** [`f516e79ba5ef0342e4a9.json`](../../sessions/f5/f516e79ba5ef0342e4a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### GPU 使用

| GPU | 状态 | 显存 |
|-----|------|------|
| cuda:0 | **空闲** | 0 / 32607 MiB |
| cuda:1 | **空闲** | 0 / 32607 MiB |
| cuda:2 | **运行中** (82%) | 30233 / 32607 MiB |
| cuda:3 | **运行中** (77%) | 30295 / 32607 MiB |

### 实验逐项

**1. exp_e2_pretrained_fewnerd_s456 (cuda:2)**
- 状态：**RUNNING** — 正在推理，刚启动不久
- 进度：`Processed prompts: 3% | 8168/301184`（301184 = 37648 × 8 samples）
- 速度：~3120 toks/s input, ~4632 toks/s output
- ETA：~4-5 小时（log 显示已跑 ~8 分钟）
- samples.jsonl 尚未生成（推理过程中不写文件）

**2. exp_e2_pretrained_fewnerd_s42 (cuda:3)**
- 状态：**RUNNING** — 正在推理
- 进度：`Processed prompts: 2% | 7464/301184`
- 速度：~3029 toks/s input, ~4534 toks/s output
- ETA：~4-5 小时
- ⚠️ **注意**：输出目录是 `e2_pretrained_fewnerd_s42`（不是 `s42_v2`），目录还是空的
- tmux session 名是 `e2_fewnerd_s42`（从 ps 可见）

**3. exp_e2_pretrained_fewnerd_s123**
- 状态：**已完成** ✅
- samples.jsonl: **37648 行**（FewNERD full，完整）
- report.json 已生成，verdict = **PASS**
- 关键指标：greedy_f1=0.512, oracle_f1=0.619, headroom=0.107, fleiss_kappa=0.443, soft_jaccard=0.687
- structural_beats_surface=true, rho_advantage=0.047

**4. 5-epoch s456 模型 (cuda:0)**
- 状态：**SCP 传输中** — 模型正从另一台 AutoDL (端口 21071) 拷贝过来
- 已传输文件：model-00001 (4.9GB), model-00002 (4.9GB), model-00003 (3.5GB, 正在写入中)
- 还缺 model-00004 和其他文件（tokenizer 等）
- 推理尚未开始，cuda:0 空闲

---
