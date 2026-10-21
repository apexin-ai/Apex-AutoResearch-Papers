# 诊断报告：eval_mbpp_sft_rasp_20 失败

**日期**: 2026-05-20
**服务器**: westb-23072
**运行时长**: 37 秒
**退出码**: 1

## 错误信息

```
OSError: Repo id must be in the form 'repo_name' or 'namespace/repo_name': '/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20'. Use `repo_type` argument if needed.
```

崩溃点：`eval_mbpp.py:98` → `AutoTokenizer.from_pretrained(args.model_path)`

## 根因

**模型路径不存在。** 命令指定 `--model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20`，但该目录不存在。

westb-23072 上实际可用的 SFT RASP 20% 模型：

| 路径 | 说明 |
|------|------|
| `sft_rasp_20_1p5b` | SFT RASP 20% (1.5B) ← **应该用这个** |
| `sft_rasp_25` | SFT RASP 25% |
| `sft_rasp_rlvr_20` | SFT RASP RLVR 20% |

同类成功实验 `eval_humaneval_sft_rasp_20` 使用的路径正是 `sft_rasp_20_1p5b`。

Transformers 发现本地路径不存在后，尝试将路径当作 HuggingFace repo id 解析，触发 `HFValidationError`（绝对路径不是合法 repo id），最终抛出 `OSError`。

## 修复

重新提交实验，将模型路径改为正确路径：

```bash
CUDA_VISIBLE_DEVICES=0 python src/eval_mbpp.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b \
  --max_new_tokens 2048 \
  --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_rasp_20.json
```

---

# MATH-500 SFT eval 速度基准（2026-05-23 实测）

| 模型 | avg s/it | 预计总时长(500题) | avg_response_len | truncated_rate |
|------|---------|-----------------|-----------------|---------------|
| sft_cka_only_20 | 27s | 3.7h | 673 tokens | 23.2% |
| sft_rasp_alpha1p0_20 | 14.6s | 2h | 930 tokens | ~36% |
| sft_standard_20 | ~77s | ~10.7h | 撞 max_new_tokens=2048 上限 | 极高 |
| sft_random_20 | ~70s | ~9.8h | 撞 max_new_tokens=2048 上限 | 极高 |

**关键发现（C2 evidence）**：Standard/Random 剪枝的 SFT 模型生成极其缓慢，因为模型退化导致无法正常生成 EOS，大量 sample 撞到 max_new_tokens 上限。RASP 和 CKA-only 模型保留了更好的生成质量，输出更短更精确。这是剪枝方法质量的直接证据。

**注意**：之前报告的 213s/it 是 GPU 竞争导致的假象（两个模型同时加载同一 GPU），实际无竞争速度 ~70s/it。

---

# [失败模式] GPU 竞争导致进程 OOM 崩溃

**日期**: 2026-05-23
**实验**: eval_math500_sft_rasp_alpha0p5_20_fixed (PID 170326)
**服务器**: westd-32935 GPU 3

两个 eval 同时运行在 GPU 3 上（grpo_cka_only_25_fixed PID 168451 + sft_rasp_alpha0p5 PID 170326），各占 ~16.8GB VRAM（总 33.5GB / 48GB RTX PRO 6000）。SFT RASP 进程因 VRAM 竞争被 SIGTERM (EXIT_CODE=143) 杀死，GRPO 进程存活。

**教训**：两个 7B 模型 eval 同时上一张 48GB GPU 不一定 OOM，但竞争会导致其中一个被杀或严重减速。必须严格执行一 GPU 一进程。

---

# 诊断报告：eval_mbpp_sft_standard_20 失败

**日期**: 2026-05-20
**服务器**: westd-29022
**运行时长**: ~2h15m（02:08→04:23 UTC+8）
**退出码**: 143 (SIGTERM)

## 进度

完成 189/374（50.5%）。最后一次 checkpoint log 在 180/374，Pass@1=0.1278。

Pass@1 趋势：
| 进度 | Pass@1 | 正确数 |
|------|--------|--------|
| 20/374 | 0.2500 | 5 |
| 40/374 | 0.2250 | 9 |
| 140/374 | 0.1286 | 18 |
| 160/374 | 0.1313 | 21 |
| 180/374 | 0.1278 | 23 |

## SIGTERM 来源

**外部 kill（非 OOM、非 timeout wrapper）。**

排除项：
- ❌ OOM killer：OOM 发送 SIGKILL (EXIT_CODE=137)，不是 SIGTERM (143)；且无 kern.log/syslog 记录
- ❌ `timeout` wrapper：timeout 命令返回 EXIT_CODE=124（如 eval_mbpp_grpo_standard_20 所示），而非 143
- ❌ 进程自身崩溃：日志无 traceback，只有 `Terminated`

最可能原因：被 `kill_job` 工具或其他 Worker 发送 `kill <pid>` 终止。时间线吻合——04:00 左右新的 MBPP eval (sft_rasp_20, grpo_standard_20) 在同服务器启动，可能需要释放 GPU 资源。

## Partial Results

**无。** `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_standard_20.json` 不存在。脚本只在全部完成后才写结果文件。

## 速度分析

平均 ~40s/it，部分问题 60-80s/it。按此速度完成 374 题需 ~4.5h。对比 sft_rasp_20 在同服务器仅 ~10s/it，sft_standard_20 慢 4x，可能因为模型生成更长的无效代码（max_new_tokens=2048）。

## 建议

需要重提交。考虑增加 `--timeout_per_task` 或降低 `--max_new_tokens` 来加速，避免再次超时被 kill。

---

# CKA Scoring Stability 验证结论

**日期**: 2026-05-19
**实验**: cka_scoring_stability_ablation (plan_014)

CKA scoring 对 calibration size (256/512/1024) 高度稳定：min combined ρ = 0.964, mean = 0.979。所有 pair 均 > 0.95 阈值。这意味着 reviewer 关于 "scoring 对样本量敏感" 的潜在质疑可以直接用数据回应：即使 calibration 减半（512→256），排名几乎不变。

---

# westd-29022 网络离线约束

**日期**: 2026-05-19 确认
westd-29022 网络不通。所有在 westd 上的实验命令必须包含 `HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1`，否则 HuggingFace datasets 库即使有本地缓存也会先发 HEAD 请求导致崩溃。eval_mbpp_sft_standard_20_clean 因缺少此标志而失败（第5次 Standard MBPP eval 失败）。

---

# Checkpoint 存在性扫描（2026-05-23 westd-32935 / westb-23072）

| Checkpoint | westd-32935 | westb-23072 |
|-----------|:-----------:|:-----------:|
| sft_rasp_alpha0p5_20 | ✓ (12.3GB) | ✗ |
| grpo_rasp_alpha0p5_20 | ✗ | ✓ |
| grpo_rasp_alpha2p0_20 | ✓ | — |
| grpo_rasp_alpha4p0_20 | ✗ (grpo_alpha4_20 有, 已确认是 RASP) | — |
| grpo_random_20 | ✗ (用 retrain) | ✗ (用 retrain) |
| grpo_unpruned | ✗ | — |
| sft_alpha4_20 | ✓ (westd, SFT RASP α=4.0) | — |

**注意**: grpo_alpha4_20 是 RASP α=4.0 的 GRPO（命名不含 rasp_ 前缀，已通过 config.json 确认）。sft_alpha4_20 同理。

---

# [失败模式] Cron 误判：eval 实验正常完成但被标记为 failed

**日期**: 2026-05-22
**实验**: eval_gsm8k_grpo_alpha4_20_v3

Cron 监控报 "process dead 5× with no sentinel/W&B — auto-resolved as failed"，但日志显示实验完整跑完 1319/1319 samples，sentinel 文件 `.done` 已正确写入，results JSON 也已保存。实际 accuracy = 62.77%。

**原因**: Eval 实验不使用 W&B，cron 依赖 W&B metrics 或 sentinel 检测。进程正常退出后 cron 多次检测未找到有效信号，自动标记 failed。可能是 sentinel 路径不匹配或检测时序问题。

**修复**: 收到此类 "process dead with no sentinel/W&B" 失败时，**先 tail 日志确认是否实际完成**，再决定是否重跑。v3 验证了 `--max_new_tokens 2048` 修复方案有效：总耗时从 v1 的 2h28min（774/1319 未完成）降至 1h33min（1319/1319 完成）。

---

### grpo_random_20_retrain 失败诊断 (2026-05-23)
- 原因：提交命令包含 `--save_only_model True`，但 `train_grpo_v5.py` 不支持该参数，argparse 报错 `unrecognized arguments: --save_only_model True`，EXIT_CODE=2
- 其他检查：SFT checkpoint 存在 ✅、磁盘充足（根 22G / 数据盘 43G）✅、脚本存在 ✅、依赖已装（vLLM 版本警告非阻塞）✅
- 修复建议：去掉 `--save_only_model True` 参数重跑即可，其余参数无问题