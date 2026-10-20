# code decoding params cli

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_decoding_params_cli_20260512T200606_result.json`
- **Structured JSON:** [`2ea3f25a4ade987bdbd4.json`](../../sessions/2e/2ea3f25a4ade987bdbd4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

### 修改概要

**run_pipeline.py — 5 处修改：**

| # | 位置 | 修改内容 |
|---|------|----------|
| 1 | L126-135 | `generate_depth_chain` 函数签名增加 `top_p`, `temperature`, `do_sample` 三个参数 |
| 2 | L162-168 | `model.generate` 调用：硬编码值 → 使用函数参数 |
| 3 | L583-592 | argparse 新增 `--top_p`, `--temperature`, `--do_sample`, `--no_sample` 四个 CLI 参数 |
| 4 | L597 | 日志输出增加 Decoding 参数信息 |
| 5 | L631 | `generate_depth_chain` 调用处传入解码参数 |

**新文件：**
- `scripts/run_exp003_ablation.sh` — 4 配置消融实验启动脚本（greedy / nuc-p0.9 / t0.7 / t1.2）

### Dry-run 结果
- **通过**，10 docs + max_depth=1 + greedy 模式完整跑完 pipeline（seed → generate → features → analysis）
- CLI 参数正确传递：日志确认 `Decoding: do_sample=False, top_p=0.95, temperature=1.0`
- greedy 模式下 transformers 自动忽略 top_p/top_k（预期行为，有 warning）
- dry-run 数据已清理

### 启动脚本路径
- 远程：`/root/autodl-tmp/gen-depth-contamination/scripts/run_exp003_ablation.sh`
- 本地：`scripts/run_exp003_ablation.sh`

### 注意
- 模型实际路径是 `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct/`（ModelScope 下载的嵌套结构），启动脚本中的 `MODEL` 变量用的是 argparse default 路径，正式运行前需确认路径或更新 default
- 备份文件在 `scripts/run_pipeline.py.bak`

---
