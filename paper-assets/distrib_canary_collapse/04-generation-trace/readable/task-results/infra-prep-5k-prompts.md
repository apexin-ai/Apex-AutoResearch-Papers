# infra prep 5k prompts

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_prep-5k-prompts_20260514T053849_result.json`
- **Structured JSON:** [`9768f0dec060de38046f.json`](../../sessions/97/9768f0dec060de38046f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完毕。脚本只写入 `--output_dir` 指定的目录，我的命令没有覆盖旧数据。旧数据 `data/wikitext103/prompts` 本来就是 5000 条（脚本默认 `n_prompts=5000`），并非预期的 1000。

汇报如下：

---

**新数据集 `data/wikitext103_5k/`** — 已生成并验证通过：
- Train: 716,506 examples
- Eval: 1,564 examples
- Prompts: 5,000 ✓

**旧数据 `data/wikitext103/`** — 未被本次操作修改（我的命令仅写入 `wikitext103_5k/`），但旧数据 prompts 数量是 **5000**，不是 1000。`prepare_data.py` 的默认值就是 `n_prompts=5000`，所以旧数据大概率当初也是按默认值生成的。如果 rep42/rep43 确实使用了 1000 prompts，可能是在训练脚本侧做的截断，而非数据集本身只有 1000 条。

**rep42/rep43 运行状态** — **未在运行**：
- GPU 无计算进程（`nvidia-smi` 返回空）
- 日志文件 `mvp_rep42.log` / `mvp_rep43.log` 为空
- Results 目录 `results/mvp/rep_42/` 和 `rep_43/` 不存在

---
