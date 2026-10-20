# ssh fix vllm unicode seed456

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-vllm-unicode-seed456_20260520T103636_result.json`
- **Structured JSON:** [`7f291b9e40d5c610930d.json`](../../sessions/7f/7f291b9e40d5c610930d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

推理已正常启动，正在渲染 prompts (37648 个实例)。上一次跑完花了 ~15 分钟。

汇总:

**任务 1: Kill VLLM 服务器** — 完成。PID 194576 已终止，4 张 GPU 全部释放。

**任务 2: 修复 Unicode surrogate bug** — 完成。
- 修改文件: `/root/autodl-tmp/struct_self_consist_ie/code/sampling.py`
- 新增 `_clean_surrogates(obj)` 辅助函数 (line 664)，递归清洗 dict/list/str 中的 surrogate 字符
- `save_sampled_results()` 中 `json.dumps` 调用前应用清洗 (line 684)
- 验证通过: `json.dumps({'test': 'abc\udedadef'.encode('utf-8','replace').decode('utf-8')})` 无报错

**任务 3: 重跑 7B seed456 推理** — 已启动，后台运行中。
- PID: 197756 (nohup), EngineCore PID: 198031
- GPU: 0 (CUDA_VISIBLE_DEVICES=0)
- 命令: `python code/run_mvp_pilot.py --model_path checkpoints/qwen25-7b-fewnerd-merged --data_dir data/fewnerd --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 456 --collect_logprobs --output_dir output/fewnerd_7b/qwen25_7b_n8_seed456`
- 日志: `logs/7b_inference_seed456_rerun.log`
- 输出: `output/fewnerd_7b/qwen25_7b_n8_seed456/samples.jsonl` (预期 37648 行)
- 预计 ~15 分钟完成

---
