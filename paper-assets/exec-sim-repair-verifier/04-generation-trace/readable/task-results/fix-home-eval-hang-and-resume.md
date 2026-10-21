# fix home eval hang and resume

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_home-eval-hang-and-resume_20260514T172705_result.json`
- **Structured JSON:** [`c9c255b4f684f2aa8546.json`](../../sessions/c9/c9c255b4f684f2aa8546.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

8B eval 正常运行中，批次 0-8 已完成（~30s），每批 1-5s。无挂起。

**执行汇总：**

| 步骤 | 状态 | 说明 |
|------|------|------|
| Kill PID 3145070 | ✅ | SIGTERM 成功，GPU 已释放 |
| 修复 eval_repo_cls.py (home) | ✅ | L201: `max_new_tokens=8` → `512` |
| eval_repo_cwm.py | ✅ 无需修改 | 已有 `--max_new_tokens=1024` CLI 参数 |
| 同步修复到 westd | ✅ | `/root/exec-sim-repair-verifier/eval_repo_cls.py` L144: `8` → `512` |
| 8B ckpt-3000 val@5120 重跑 | 🔄 运行中 | tmux `eval_8b_val5120_fix`，~9335 样本 |
| 4B seed123 ckpt-400/600/800 | ⏳ 排队 | 8B 完成后自动开始 |
| 4B v5 ckpt-600/4000/4400/4600 | ⏳ 排队 | seed123 完成后自动开始 |

**注意事项：**
- 已有 6664 行部分结果无 resume 支持，全量重跑（脚本 overwrite）
- 4B 模型用 HF hub `Qwen/Qwen3-4B`（本地已缓存）
- 8B 模型路径 `/home/sonny/projects/verifier-tts-struct-ie/models/Qwen3-8B`
- 项目非 git repo，westd 修复通过直接 sed 完成
- 8B batch_size 降至 8（8B 模型 + 5120 seq_length VRAM 更紧张）
- 估计 8B ~60min，每个 4B ~15min，全部 ~2.5h

---
