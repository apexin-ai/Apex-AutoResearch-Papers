# ops d056 westd kill and eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d056-westd-kill-and-eval_20260514T005809_result.json`
- **Structured JSON:** [`8a4a690ab0efb566187b.json`](../../sessions/8a/8a4a690ab0efb566187b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## Kill 结果
| GPU | 实验 | PID killed | 显存释放 |
|-----|------|-----------|---------|
| 0 | CWM seed123 | 183048 | 16326 MiB → 0 |
| 1 | CWM v12 | 181202 (+父181201) | 23254 MiB → 0 |
| 2 | CLS v5-conda | 187002 | 19418 MiB → 0 |
| 3 | CLS 8B | 185438 | 25742 MiB → 0 |

## Best Checkpoints
| 实验 | Best Checkpoint | eval_loss |
|------|----------------|-----------|
| CWM v12 | checkpoint-500 | 0.3066 |
| CWM seed123 | checkpoint-500 | 0.3163 |
| CLS v5-conda | checkpoint-200 | 0.0829 |
| CLS 8B | checkpoint-200 | 0.0796 |

## Eval 启动
| GPU | tmux session | 状态 | 进度 |
|-----|-------------|------|------|
| 0 | eval_cwm_seed123 | Model loaded, inference started | — |
| 1 | eval_cwm_v12 | Model loaded, inference started | — |
| 2 | eval_cls_v5 | running | 800/9784, acc=54.9% |
| 3 | eval_cls_8b | running | 560/9784, acc=73.2% |

GPU 使用: 0→13GB, 1→13GB, 2→18GB, 3→21GB

**Bug 修复**: `eval_repo_cwm.py` 第 97 行 tokenizer 从 `checkpoint_dir` 加载改为 `base_model_name`（CLS 版本已是正确的），否则 LoRA checkpoint 无 model_type 导致 ValueError。

---
