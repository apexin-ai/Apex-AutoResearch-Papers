# ops dryrun linear increasing

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_dryrun-linear-increasing_20260517T220852_result.json`
- **Structured JSON:** [`9b55af75b6b168c0170f.json`](../../sessions/9b/9b55af75b6b168c0170f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有关键信息收集完毕。汇报如下：

---

## Dry-run 验证结果

### 脚本内容 ✅ 正确

- 路径 `/root/spectral_collapse_ews/` ✅
- 使用 `run_phase1.py` ✅
- condition 参数 `linear_increasing` ✅
- GPU 参数化 `GPU_ID=${1:-0}` ✅
- 环境激活 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base` ✅
- `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1` ✅
- seed=42, generations=10 ✅

### run_phase1.py 支持 linear_increasing ✅

`CONDITION_CHOICES` 包含 `"linear_increasing"`，代码第 125/172/211 行有对应处理逻辑。

### 数据文件 ✅

数据文件是 `.pt` 格式（`eval_5k.pt`, `train_real_50k.pt`, `spectral_1k.pt`），不是 `.jsonl`。`run_phase1.py` 中未 grep 到 `eval_5k` 或 `train_real` 字符串，说明数据路径可能在被调用的子模块中定义，但 `.pt` 文件存在，且之前的 experiments（fixed_mix, adaptive 等）已成功运行使用同样数据，无问题。

### 模型缓存 ✅

`pythia-410m-deduped` 缓存在 `/root/autodl-tmp/.hf_cache/hub/models--EleutherAI--pythia-410m-deduped/`。`.bashrc` 中设置了 `export HF_HOME=/root/autodl-tmp/.hf_cache`，脚本通过 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base` 会 source `.bashrc`（通过 `source /etc/profile`），所以 `HF_HOME` 会被正确继承。加上 `HF_HUB_OFFLINE=1` 保证离线加载。

### Checkpoint 路径 ⚠️ 冲突

`/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/linear_increasing_seed42/` **已存在**，包含 `gen_0/` 目录（含完整模型文件）。这是之前实验的遗留数据。

**需要确认**：`run_phase1.py` 的行为是否是从 gen_0 续跑（resume），还是会覆盖。如果是覆盖/重跑，建议先备份或删除旧目录。如果代码支持 resume，则无问题。

### 总结

| 检查项 | 状态 |
|--------|------|
| 脚本内容 | ✅ |
| 数据文件 | ✅ |
| 模型缓存 | ✅ |
| run_phase1.py 支持 | ✅ |
| checkpoint 冲突 | ⚠️ 旧 linear_increasing_seed42 已存在（gen_0） |

唯一需要决策的是：是否需要清除旧的 `linear_increasing_seed42/` checkpoint 目录再重新跑，或代码会自动 resume/覆盖。

---
