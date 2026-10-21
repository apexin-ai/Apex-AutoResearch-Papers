# westd-38929 Silent Crash Diagnosis Report (2026-05-23)

## 1. 存活 vs 崩溃命令 Diff

**存活实验 (GPU 0, PID 209581)** — `eval_random_k09_long_s43`:
```
CUDA_VISIBLE_DEVICES=0
TRANSFORMERS_OFFLINE=1      ← 关键
HF_HUB_OFFLINE=1            ← 关键
HF_HOME=/root/autodl-tmp/.hf_cache  ← 关键
python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.9 ...
```

**崩溃实验 (GPU 1/2/3)** — 部署命令示例:
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=3 python -u eval_pi05_pruning_libero.py ..."
```
**缺少 `TRANSFORMERS_OFFLINE=1`, `HF_HUB_OFFLINE=1`, `HF_HOME=/root/autodl-tmp/.hf_cache`**

## 2. 系统日志

- `dmesg`: 容器环境无权限（Operation not permitted）
- `journalctl`: 无 OOM/kill/error/segfault 记录
- 结论：非 OOM kill，非内核崩溃

## 3. 崩溃日志

`eval_pi05_random_k03_long_seed43.log` 和 v2 均显示相同错误：
```
httpx.ConnectError: [Errno 101] Network is unreachable
ValueError: Failed to instantiate processor step 'tokenizer_processor' 
  with config: {'tokenizer_name': 'google/paligemma-3b-pt-224'}
  Error: [Errno 101] Network is unreachable
EXIT_CODE=1
```

`eval_pi05_l2norm_k05_long_seed43.log` 同样错误模式。
l2norm_k07 和 l2norm_k085 无日志文件（可能部署时未正确设置 log tee）。

## 4. 崩溃根因

**缺少 HuggingFace 离线模式环境变量。**

脚本在 `make_pre_post_processors()` 中需要加载 `google/paligemma-3b-pt-224` tokenizer。
- tokenizer 已缓存在 `/root/autodl-tmp/.hf_cache/hub/models--google--paligemma-3b-pt-224`
- 但崩溃实验缺少 `HF_HOME=/root/autodl-tmp/.hf_cache`，HF 默认查找 `~/.cache/huggingface`（不存在）
- 同时缺少 `TRANSFORMERS_OFFLINE=1`，HF 尝试从网络下载
- AutoDL 容器网络不可达 → `[Errno 101] Network is unreachable` → 脚本 exit(1)
- tmux session 在进程退出后销毁

存活实验由之前的 worker 部署，该 worker 正确设置了这 3 个环境变量。

## 5. 修复方案

在部署命令中添加 3 个环境变量：
```bash
TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache
```

手动测试（GPU 1, l2norm k=0.7, 2 episodes）验证成功，通过 tokenizer 步骤并完成 8/10 tasks。

## 6. 重部署结果

| GPU | Exp ID | PID | tmux session | 验证 |
|-----|--------|-----|-------------|------|
| 1 | eval_pi05_l2norm_k07_long_seed43_v2 | 289572 | eval_l2norm_k07_long_s43_v2 | ✓ PRUNE-DIAG l2norm n_keep=179/256 |
| 2 | eval_pi05_random_k03_long_seed43_v3 | 289643 | eval_random_k03_long_s43_v3 | ✓ PRUNE-DIAG random n_keep=76/256 |
| 3 | eval_pi05_l2norm_k085_long_seed43_v2 | 289780 | eval_l2norm_k085_long_s43_v2 | ✓ PRUNE-DIAG l2norm n_keep=217/256 |

全部 3 个实验已通过 tokenizer 关键步骤，正在正常评估中。GPU 内存占用 9.7-10.7 GB。
