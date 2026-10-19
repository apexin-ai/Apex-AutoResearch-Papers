# prep v7 eval script

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_v7-eval-script_20260516T123140_result.json`
- **Structured JSON:** [`afb61e39ba5c21bd769c.json`](../../sessions/af/afb61e39ba5c21bd769c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。总结：

---

## 确认结果

| 项目 | 状态 |
|------|------|
| dtype fix (`target_dtype` + `scorer.to(dtype=...)`) | ✅ 已在 eval_acib.py:138-141 |
| conditioning_mode 从 checkpoint config 加载 | ✅ 刚加入 eval_acib.py:119 |
| `run_v7_eval.sh` | ✅ 已写入 `/root/acib/scripts/run_v7_eval.sh` |
| `run_v7_seed2.sh` | ✅ 已写入 `/root/acib/scripts/run_v7_seed2.sh` |

## 注意：eval_acib.py 的 CLI 参数

实际参数与你模板中的不同：
- `--checkpoint_dir`（不是 `--checkpoint`）
- `--base_model`（不是 `--model_id`）
- `--out_dir`（不是 `--output_dir`）

脚本已用正确参数写好。

## 启动命令（训练完成后直接执行）

**v7 eval（checkpoint-20000 就绪后）：**
```bash
tmux new-session -d -s v7_eval "bash /root/acib/scripts/run_v7_eval.sh 2>&1 | tee ~/runs/action_cond_info_bottleneck/v7_eval_ckpt20000.log"
```

**v7 seed2（Probe A < 0.8 确认后，GPU 0 空闲时）：**
```bash
tmux new-session -d -s v7_seed2 "bash /root/acib/scripts/run_v7_seed2.sh 2>&1 | tee ~/runs/action_cond_info_bottleneck/acib_v7_seed2.log"
```

---
