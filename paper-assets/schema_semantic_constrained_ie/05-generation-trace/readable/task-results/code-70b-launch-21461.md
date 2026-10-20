# code 70b launch 21461

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_70b_launch_21461_20260518T114616_result.json`
- **Structured JSON:** [`18db05f77e86f2f6686f.json`](../../sessions/18/18db05f77e86f2f6686f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验正在正常产出结果：unconstrained 7 docs, constrained 6 docs。

---

## 报告

| 项目 | 结果 |
|------|------|
| **1. 下载** | 完成。9 shards, 38GB 总计。路径 `Meta-Llama-3___1-70B-Instruct-AWQ-INT4`，已创建 `Meta-Llama-3.1-70B-Instruct-AWQ-INT4` 符号链接 |
| **2. GPU** | 2x NVIDIA RTX PRO 6000 Blackwell Server Edition, 98GB VRAM/卡 |
| **3. 代码改动** | `run_constrained_extraction.py` L881: `torch_dtype=torch.bfloat16` → `torch_dtype="auto"` (AWQ config 指定 float16)。另安装 `gptqmodel` 7.0.0 + 依赖（transformers 5.8.1 要求替代 autoawq） |
| **4. Dry-run** | 成功。Marlin fp16 JIT 编译 62s（首次，后续缓存），推理 6.1s/doc，GPU 占用 39GB/98GB |
| **5. 实验启动** | 均在 tmux 中运行。**Unconstrained** (PID 24552, cuda:0, tmux: `70b_unconstrained`)；**Constrained full_s1** (PID 24703, cuda:1, tmux: `70b_constrained`)。各卡独立，~39-43GB VRAM。551 docs 预计约 55 分钟/实验 |

注：`submit_training_job` 工具不可用，改用 tmux 启动。日志分别在 `/tmp/70b_unconstrained.log` 和 `/tmp/70b_constrained.log`。

---
