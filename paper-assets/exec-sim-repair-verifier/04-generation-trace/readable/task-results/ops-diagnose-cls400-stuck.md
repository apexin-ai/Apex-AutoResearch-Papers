# ops diagnose cls400 stuck

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-cls400-stuck_20260523T193708_result.json`
- **Structured JSON:** [`6577c5693c8ceaba26e8.json`](../../sessions/65/6577c5693c8ceaba26e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### GPU 状态
| GPU | 占用 | 用途 |
|-----|------|------|
| GPU 0 | 17 GB, 46% util | CWM 8B s123 ckpt300 reeval (`eval_repo_cwm.py`) |
| GPU 1 | 17 GB, 49% util | CWM 8B s456 ckpt300 reeval (`eval_repo_cwm.py`) |
| GPU 2 | 空闲 | — |
| GPU 3 | 28 GB, 88% util | CWM 8B ckpt6100 eval (`eval_repo_cwm.py`) |

### CLS@400 训练状态
**三个 seed 全部训练完成**，best checkpoint 均已保存：
- s42: 完成于 02:16, eval_loss=0.426
- s123: 完成于 02:31, eval_loss=0.347
- s456: 完成于 02:53, eval_loss=0.516

### CLS@400 Eval 状态
- **s42 eval 已完成**：Acc=79.47%, F1=79.47%
- **s123 eval 已完成**：Acc=78.20%, F1=78.12%
- **s456 eval 未运行**：无 `/tmp/eval_ds400_s456.log`

### 关键发现
1. **没有任何 CLS@400 相关进程在运行**。当前 GPU 上跑的全是 `eval_repo_cwm.py`（CWM 实验），不是 CLS eval。
2. **Eval 结果未写入 artifacts 目录**。`artifacts/eval_cls_downsample_400_*/eval_results.json` 不存在，`find` 也搜不到任何 ds400/downsample_400 结果文件。eval 结果只打到了 `/tmp/eval_ds400_s{42,123}.log` 的 stdout 里。
3. **s456 eval 从未启动**。
4. **GPU 2 空闲**，可以立即用来跑 eval。

### 结论
Worker 卡死的原因：**eval 脚本没有写 eval_results.json 到 artifacts 目录**（或者写了但路径不对），加上 s456 eval 从未被触发。另一个 Worker 在轮询一个永远不会出现的文件。

需要：
1. 手动从 log 中提取 s42/s123 的 eval 结果写入 artifacts
2. 在 GPU 2 上启动 s456 eval
3. 确认 eval 脚本的 `--output_dir` 参数是否正确指向 artifacts 路径

---
