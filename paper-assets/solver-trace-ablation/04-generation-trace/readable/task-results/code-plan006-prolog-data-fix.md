# code plan006 prolog data fix

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan006-prolog-data-fix_20260514T110325_result.json`
- **Structured JSON:** [`fb2da6cab1fd5e2299b9.json`](../../sessions/fb/fb2da6cab1fd5e2299b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结论

**问题不存在。** plan006-prolog-exec-s42 当前正在正常运行，已到 step ~361/500。

具体发现：

1. **运行中进程**（PID 506020，GPU 0，从 17:49 开始）：
   ```
   python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s42
   ```

2. **数据路径**：所有 Prolog config（`grpo_prolog_exec_only.yaml`、`grpo_prolog_exec_sta.yaml`、`grpo_prolog_exec_only_k16_warmup.yaml`）都使用 `data_path: data/train_500_seed42.jsonl`，即 FOL 数据文件（符合 C001 约束）。

3. **`data/prolog/` 目录确实不存在**，但没有任何 config 或代码引用这个路径。`train_grpo.py` 第 390 行直接 `load_jsonl(args.data_path)` 不做路径改写。

4. **`data/prolog/train_500_seed42.jsonl` 这个路径在服务器上无任何引用**——不在 config 中，不在代码中，不在日志中。

**根因推测**：报错 `FileNotFoundError: data/prolog/train_500_seed42.jsonl` 来自之前的失败尝试，当时 config 或启动命令中 data_path 被错误设为 `data/prolog/train_500_seed42.jsonl`。之后 config 已修正为 `data/train_500_seed42.jsonl`，第三次启动成功。

**无需修复。** 训练正常运行中，预计还需约 30 分钟完成。

---
