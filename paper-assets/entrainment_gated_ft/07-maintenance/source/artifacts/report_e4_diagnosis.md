# E4 Pythia Seed Calibration — 失败诊断报告

**日期**: 2026-05-22
**服务器**: westb-48145

## 失败根因

aria2 批量下载 Pythia 410M seed 权重时被中断（"Emergency shutdown"），9 个 seed 的 `pytorch_model.bin`（各 869MB）均未下载完成。Eval 阶段在损坏的模型文件上运行，`config.json` 缺少 `model_type` 字段导致全部 9 个 seed 的 lm_eval 失败。

## 关键错误日志

### 下载阶段 (download_final.log)
```
05/22 19:05:23 [NOTICE] Emergency shutdown sequence commencing...
05/22 19:05:23 [NOTICE] Download GID#0966c9d7ab720d49 not complete: /root/autodl-tmp/pythia_weights/seed1/pytorch_model.bin
...
seed1: 911449213 bytes - CORRUPT
seed2: 911449213 bytes - CORRUPT
seed3: 911449213 bytes - CORRUPT
seed4: 911449213 bytes - CORRUPT
seed5: 911449213 bytes - CORRUPT
seed6: MISSING
seed7: MISSING
seed8: MISSING
seed9: MISSING
```

下载速度仅 ~100-500 KB/s，3 分钟内（19:02:10→19:05:23）每个 seed 仅完成 1-5%。aria2 并行下载 5 个 869MB 文件时触发 Emergency shutdown（可能是超时或 OOM）。seed6-9 排队未开始。

### 评估阶段 (eval_all.log)
```
ValueError: Unrecognized model in /root/autodl-tmp/pythia_weights/seed1.
Should have a `model_type` key in its config.json.
```
seed1-5 全部报同样错误。seed6-9 直接跳过（"SKIP seed6 (no model)"）。

## 部分结果状态

- **完成的 seed**: 0 / 9
- **results 目录**: 仅 `seed1/` 存在但为空目录
- **e4_analysis.json**: 空 `{}`
- **模型文件**: `/root/autodl-tmp/pythia_weights/` 目录已不存在（被清理）

## 环境状态（正常）

- 磁盘: 30G 用了 16G (53%) — 非磁盘满
- GPU: RTX PRO 6000 96GB，空闲，正常
- 无残留进程

## 修复建议

**问题核心**: aria2 直接下载 HF 权重文件的方式不可靠（被 xet CDN 重定向、带宽差、无断点续传保护）。

**方案**: 改用 `run_eval.sh`（已存在），让 lm_eval 通过 HuggingFace transformers 自动下载模型：

```bash
# 1. 先验证 Pythia seed 模型名称是否正确存在
#    EleutherAI/pythia-410m 是默认 seed
#    seed variants 可能命名为 pythia-410m-seed2, pythia-410m-seed3 等
#    需确认 HF 上实际的 repo 命名

# 2. 清理残留
rm -rf /root/entrainment_gated_ft/results/e4_pythia_seed/seed*/
rm -f /root/entrainment_gated_ft/results/e4_pythia_seed/e4_analysis.json

# 3. 用 run_eval.sh 重跑（已配置 HF_HUB_DISABLE_XET=1 避免 xet 问题）
cd /root/entrainment_gated_ft/results/e4_pythia_seed
nohup bash run_eval.sh > /tmp/e4_eval_rerun.log 2>&1 &

# 4. 监控
tail -f /tmp/e4_eval_rerun.log
```

**注意事项**:
- `run_eval.sh` 已设置 `HF_HUB_DISABLE_XET=1`，会走普通 HF CDN 而非 xet
- 单 seed 下载 ~869MB，9 个约 7.8GB，根分区剩余 15GB 可能不够——确保 `HF_HOME=/root/autodl-tmp/.hf_cache` 生效，缓存写到数据盘
- 每个 seed 逐个运行（脚本已是串行），避免并发下载竞争带宽
- 建议用 `nohup` 运行，避免 SSH 断连导致进程终止
