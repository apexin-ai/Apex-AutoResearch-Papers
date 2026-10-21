# LongBench 在 benchmark_eval.py 中的集成方式 — 代码分析报告

> 数据来源：本地代码仓库无 `src/benchmark_eval.py`（仅存在于 westd-34887 远程）。本报告基于 2026-05-16 期间多个 worker 通过 `ssh_read_only cat /root/distill_sparse_swiglu/src/benchmark_eval.py` 抓取的文件内容、`worker_code_longbench-support` / `worker_ops_fix-longbench-*` 系列日志的 patch 记录，以及 `checkpoints/longbench_*_v6_DONE_*.json` 中固化的最终配置重建得出。本会话因无 SSH 工具，无法直接核对当前线上版本。

## 1. 总览

LongBench 评测**没有独立脚本**。它通过 `src/benchmark_eval.py` 走 `lm-evaluation-harness` 的 `simple_evaluate`，与 ARC/MMLU/GSM8K 等任务共用同一入口。LongBench 的特殊性（32k-token 文档、生成式评测、单卡放不下）全部在外层 wrapper（`--multi_gpu` 开关 + 命令行环境变量）中处理，**核心 `run_lm_eval_tasks` 函数对 LongBench 无任何特殊路径**。

## 2. 关键代码定位

| 位置 | 内容 |
|------|------|
| `src/benchmark_eval.py:50` | `LM_EVAL_DEFAULTS` dict — task 白名单 + few-shot 数 |
| `src/benchmark_eval.py:114` | `--batch_size` arg，默认 8 |
| `src/benchmark_eval.py:128` | `load_model_and_tokenizer(model_path, device, multi_gpu=False)` |
| `src/benchmark_eval.py:238` | `run_lm_eval_tasks(model, tokenizer, tasks, batch_size, device)` |
| `src/benchmark_eval.py:241-243` | `from lm_eval.models.huggingface import HFLM` + `lm_obj = HFLM(pretrained=model, tokenizer=tokenizer, batch_size=batch_size)` |
| `src/benchmark_eval.py:258` | `lm_eval.simple_evaluate(model=lm_obj, tasks=task_group, num_fewshot=num_fewshot, batch_size=batch_size)` |
| `src/benchmark_eval.py:291` | `lm_eval_tasks = [t for t in tasks if t in LM_EVAL_DEFAULTS]` — 白名单过滤 |
| `src/benchmark_eval.py:294` | `unknown = [t for t in tasks if t != "wikitext2" and t not in LM_EVAL_DEFAULTS]` — 报告未识别 task |

## 3. LongBench 在 LM_EVAL_DEFAULTS 中的注册（2026-05-16 patch）

`worker_code_longbench-support_20260516T124754` 在 ARC/MMLU 之前插入了 9 条 longbench 入口：

```python
LM_EVAL_DEFAULTS = {
    # LongBench tasks (generation-based, 0-shot)
    "longbench": {"num_fewshot": 0},
    "longbench_single": {"num_fewshot": 0},
    "longbench_multi": {"num_fewshot": 0},
    "longbench_summarization": {"num_fewshot": 0},
    "longbench_fewshot": {"num_fewshot": 0},
    "longbench_narrativeqa": {"num_fewshot": 0},
    "longbench_qasper": {"num_fewshot": 0},
    "longbench_gov_report": {"num_fewshot": 0},
    "longbench_multi_news": {"num_fewshot": 0},
    "arc_challenge": {"num_fewshot": 25},
    "winogrande": {"num_fewshot": 5},
    "mmlu": {"num_fewshot": 5},
    "gsm8k": {"num_fewshot": 8},
}
```

**注意**：这个 dict 是项目自己的白名单 + few-shot 元数据，**不是 lm-eval-harness 的 task 注册表**。`task_group` 最终是直接传给 `lm_eval.simple_evaluate(tasks=...)`，由 lm-eval-harness 内部用同名 YAML 配置匹配，所以 task 名必须与 lm-eval-harness 的注册名一致。

## 4. 数据加载方式

- **不是自定义加载**：`get_eval_dataset` 只服务于 `wikitext2`（perplexity 路径）。
- LongBench 走 **lm-eval-harness 内部**通过 datasets 库加载。
- v6 成功跑通时数据集是 `Xnhyacinth/LongBench`（parquet 格式的 LongBench 镜像），并已预缓存到 `/root/autodl-tmp/.hf_cache/datasets/Xnhyacinth___long_bench/`。`HF_DATASETS_OFFLINE=1 / HF_HUB_OFFLINE=1` 下从本地缓存读取，每个子任务（narrativeqa / qasper / gov_report / multi_news）一个 config。
- **原始 `THUDM/LongBench` 不可用**：HF datasets ≥ 3.x 已禁用 `trust_remote_code`，而 `THUDM/LongBench` 是基于 `LongBench.py` loading script 的，导致 `ERROR: Dataset scripts are no longer supported, but found LongBench.py`。

## 5. 序列长度处理

- `--seq_len` 参数（默认 2048）**只用于 wikitext2**。
- LongBench 的 truncation / max_length 由 lm-eval-harness 的 task YAML 配置控制（每个子任务有独立 `max_length`、`max_gen_toks`、`generation_kwargs`）。`benchmark_eval.py` 不传 `max_length` / `gen_kwargs` 给 `simple_evaluate`，全部走 lm-eval 默认。
- 32k token 上下文带来的内存压力**没有在代码层缓解**，仅靠：
  - `--multi_gpu` → `device_map="auto"`（双卡切层）
  - `--batch_size 1`
  - 环境变量 `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`

## 6. 生成 / 评分方式

- LongBench 子任务在 lm-eval-harness 中全部是 `output_type: generate_until` 的生成式任务（narrativeqa/qasper → QA F1，gov_report/multi_news → ROUGE）。
- `run_lm_eval_tasks` 用 `HFLM(pretrained=model, ...)` 包装已加载好的模型，由 lm-eval-harness 自行决定调用 `generate_until` 还是 `loglikelihood`。
- HFLM 在接到已实例化 model 时会打印警告：`pretrained model kwarg is not of type str. Many other model arguments may be ignored. Please do not launch via accelerate or use parallelize=True if passing an existing model this way.` — 这意味着 **HFLM 自带的多卡/parallelize 参数被忽略**，2 GPU 拆分必须依赖外层 `device_map="auto"` 在 `from_pretrained` 时完成。

## 7. 多卡支持的 patch（v4，`worker_ops_fix-longbench-tp-resubmit`）

新增 `--multi_gpu` 标志：

```python
def load_model_and_tokenizer(model_path, device, multi_gpu=False):
    ...
    load_kwargs = dict(torch_dtype=torch.bfloat16, attn_implementation=_best_attn_impl())
    if multi_gpu:
        load_kwargs["device_map"] = "auto"
    else:
        load_kwargs["device_map"] = {"": device}
    model = AutoModelForCausalLM.from_pretrained(model_path, **load_kwargs)
```

同时把 `apply_static_masks` 里 `mask.to(device=device, ...)` 改为 `mask.to(device=layer.mlp.gate_proj.weight.device, ...)`，以匹配 `device_map="auto"` 后各层散落在不同 GPU 上的事实。

## 8. 5 次失败的根因总结

| 版本 | 失败模式 | 根因 | 修复 |
|------|---------|------|------|
| v0 | task 被静默过滤 | `longbench_*` 不在 `LM_EVAL_DEFAULTS` → 第 291 行过滤后为空 | 加入 9 条 longbench 条目 |
| v1 | 数据集 load 失败 | `THUDM/LongBench` 用 loading script，HF datasets ≥3 禁用 | 改用 `Xnhyacinth/LongBench` 镜像并预缓存 |
| v2 | OOM | 两进程抢同一 GPU + 未启用 flash-attn | 固定 GPU 分配 + `_best_attn_impl()` |
| v3 | OOM | 单卡放不下 32k token 上下文（8B + KV cache） | 加 `--multi_gpu`（`device_map="auto"`）拆 2 卡 |
| v4–v6 | 通过 | `--multi_gpu --batch_size 1`，预缓存 Xnhyacinth 数据 | v6 双任务（dense + kl30）全部 DONE |

成功命令模板（来自 `checkpoints/longbench_dense_v6_DONE_*.json`）：

```bash
python -u src/benchmark_eval.py \
  --exp_id longbench_dense_v6 \
  --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b \
  --dense --multi_gpu --batch_size 1 \
  --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news \
  --gpu 0
```

环境变量：`HF_HOME=/root/autodl-tmp/.hf_cache`、`PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`、`HF_DATASETS_OFFLINE=1`、`HF_HUB_OFFLINE=1`、`TRANSFORMERS_OFFLINE=1`、`WANDB_MODE=offline`。GPU 分配：cuda:0 + cuda:1，wall clock ~77 min（dense）/ ~107 min（kl30）。

## 9. lm-eval-harness 版本要求

- 顶部 docstring 写的是 `lm-eval >= 0.4.0`。
- LongBench 子任务（`longbench_narrativeqa` 等）在 lm-eval-harness **v0.4.0+** 才被纳入官方 task 库（位于 `lm_eval/tasks/longbench/`）。
- 本地 `R-Sparse/lm_eval/tasks/` 目录列出的是 R-Sparse 自带的旧版 lm-eval fork（没有 longbench/scrolls 之外的长文档任务），不是 benchmark_eval.py 实际使用的版本——后者用的是 `pip install lm_eval` 装在 conda base 的现代版本。
- 本地没有 `requirements.txt` / `pyproject.toml` 锁定 lm-eval 版本（仅 docstring 注释），版本只能从服务器 `pip show lm_eval` 验证。

## 10. 潜在问题点

1. **5 条聚合 task 名可能无效**：`longbench`、`longbench_single`、`longbench_multi`、`longbench_summarization`、`longbench_fewshot` 这 5 个聚合名在 lm-eval-harness 的 task 注册表里**不一定存在**（v0.4.x 通常只注册各子任务 + `longbench` group）。如果传给 `simple_evaluate` 会报 `Task X not found`。**建议只使用已验证 OK 的 4 个具体子任务**：`longbench_narrativeqa, longbench_qasper, longbench_gov_report, longbench_multi_news`。
2. **`--seq_len` 完全不影响 LongBench**：很多 worker 误以为可以通过这个参数控制 LongBench 截断，实际上它只走 wikitext2。LongBench 截断由 lm-eval-harness 的 task YAML 决定，要改 max_length 需要在 lm-eval 的 task config 里改。
3. **`HFLM(pretrained=model, ...)` 路径不支持 `parallelize=True`**：HFLM 警告明确说 "Many other model arguments may be ignored"。多 GPU 必须靠 `from_pretrained(device_map="auto")` 在外层完成，否则单卡 OOM。
4. **batch_size 默认 8 对 LongBench 是致命的**：CLI 默认值 8 必须显式覆写为 1，否则即使双卡也会 OOM。这个默认值对其他基准是合理的，但 LongBench 没有单独的 batch_size 默认。
5. **`Xnhyacinth/LongBench` 是非官方镜像**：依赖该 repo 持续可用。如果该 repo 被撤回，需要回退到从官方 HF（已被 datasets ≥3 弃用）或者改用 `pip install datasets<3` 才能加载 THUDM/LongBench。
6. **结果指标可能噪声大**：`longbench_kl30_uniform_v6` 的 `multi_news=18.01` 比 dense baseline `2.5` 高 7×，这种异常说明 dense baseline 本身（仅 200 例 narrativeqa + 4 子任务 800 例）的样本量不足以稳定 ROUGE 指标，需谨慎用作论文证据。
7. **`_best_attn_impl()` 行为不透明**：来自 `evaluate.py`，需核对它是否在 multi_gpu 路径下能正确返回 `flash_attention_2`。如果返回 `sdpa` 或 `eager`，32k 序列会显著放大内存。

## 11. 修改建议（按优先级）

**P0（必做）**：
- 在 `LM_EVAL_DEFAULTS` 里删除 5 个未验证存在的聚合名（`longbench`/`longbench_single`/`longbench_multi`/`longbench_summarization`/`longbench_fewshot`），只保留 4 个已 v6 跑通的具体子任务。可选：先 `python -c "from lm_eval.tasks import TaskManager; print([t for t in TaskManager().all_tasks if 'longbench' in t])"` 列出实际可用任务名再决定。
- LongBench 任务 group 在 `parse_args` 里强制 `args.batch_size = min(args.batch_size, 1)` 并自动启用 `args.multi_gpu = True`，避免每次都靠人工传参。

**P1（强化稳定性）**：
- `run_lm_eval_tasks` 中检测到 task 名以 `longbench_` 开头时，传入更显式的 `gen_kwargs`（如 `max_gen_toks` 与 LongBench 原始论文一致：narrativeqa=128, qasper=128, gov_report=512, multi_news=512）。当前完全依赖 lm-eval 默认值，可能与官方 leaderboard 不可比。
- 在 `lm_eval.simple_evaluate` 调用处加 `apply_chat_template=False`（Llama-3.1-8B base 不是 instruct，可能被 lm-eval 误判）。
- 在脚本启动时 `assert os.environ.get("PYTORCH_CUDA_ALLOC_CONF", "").find("expandable_segments") >= 0`，防止漏设环境变量再次 OOM。

**P2（写作 / 复现）**：
- 在文件顶部 docstring 的 `--tasks` 示例里加 longbench 用法，并说明 LongBench 必须配合 `--multi_gpu --batch_size 1`。
- 把 v6 成功命令固化为 `scripts/eval_longbench.sh`，避免每次 ops worker 手敲长命令。
- 把 `Xnhyacinth/LongBench` 缓存目录写进 `decisions.yaml`，避免下次清理 `/root/autodl-tmp` 时被误删。

## 12. 信息缺口

- 服务器上 lm-eval 实际版本未知（本地无 requirements.txt / pyproject.toml 锁定）。需要：`ssh westd-34887 "/root/miniconda3/bin/pip show lm_eval"`。
- `_best_attn_impl()` 在 multi_gpu 时实际返回的实现未验证。需要：在 v6 日志里 grep `attn_implementation` 或加一行 print 验证。
- LongBench 的 lm-eval task YAML 里 `max_length`/`max_gen_toks` 默认值未核对，需要：`ssh westd-34887 "find /root/miniconda3/lib/python*/site-packages/lm_eval/tasks/longbench -name '*.yaml' | xargs head -50"`。
