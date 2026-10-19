# infra fix wandb restart 41718

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix_wandb_restart_41718_20260518T002520_result.json`
- **Structured JSON:** [`096e23883a7570a61007.json`](../../sessions/09/096e23883a7570a61007.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修复完成。总结报告：

## 诊断结果

**任务描述的错误原因（wandb 缺失）并非实际失败根因。**

**实际失败原因**：westd-41718 无法访问 huggingface.co（`[Errno 101] Network is unreachable`），且本地无 wikitext 数据集缓存。

**失败细节**：
- `multiseed_kl50.sh` (cuda:0)：seed=123 训练 1000 步完成并保存了 checkpoint，但 eval 阶段加载 wikitext-2 数据时网络不通而 crash。`set -e` 导致脚本停止，seed=456 未执行。
- `multiseed_kl30_fixed.sh` (cuda:1)：同样模式，seed=123 训练完成但 eval crash。
- Checkpoints `kl_50pct_s123` 和 `kl_30pct_s123` 已不存在（被后续操作清理），需要完全重跑。

## 已完成的修复

1. **wandb 0.27.0 已安装**（pip install 成功）
2. **wikitext-103 已下载**到 `/root/autodl-tmp/data/wikitext103/`（522MB，1,801,350 examples）
3. **wikitext-2 test 已下载**到 `/root/autodl-tmp/data/wikitext2/test/`（1.3MB，4,358 examples）
4. **WANDB_MODE=offline** 已写入 `/root/.bashrc`
5. 数据通过 `HF_ENDPOINT=https://hf-mirror.com` 下载（huggingface.co 不通但 hf-mirror.com 可用）

## GPU 状态

两张 RTX PRO 6000 Blackwell 97GB 均空闲（0% util, 0MiB）。

## 需要重启的命令

**cuda:0** — KL 50% multiseed（脚本已存在）：
```bash
nohup bash /root/distill_sparse_swiglu/scripts/multiseed_kl50.sh > /root/distill_sparse_swiglu/logs/multiseed_kl50_v2.log 2>&1 &
```

**cuda:1** — KL 30% multiseed（脚本已存在）：
```bash
nohup bash /root/distill_sparse_swiglu/scripts/multiseed_kl30_fixed.sh > /root/distill_sparse_swiglu/logs/multiseed_kl30_fixed_v2.log 2>&1 &
```

注意：脚本中 `WANDB_MODE=disabled`，而 .bashrc 设为 `offline`。脚本内的设置会覆盖，无影响。两个脚本各跑 2 个 seed（123+456）的 train+eval，预计每个脚本约 2-3 小时。

---
