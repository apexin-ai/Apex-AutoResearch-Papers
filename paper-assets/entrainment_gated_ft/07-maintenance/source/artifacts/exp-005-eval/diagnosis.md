# exp-005-eval 诊断报告

## 失败原因

实验经历了 4 次下载尝试，均未完成全部模型下载，因此评估阶段从未执行。

### 尝试时间线

| 尝试 | 日志文件 | 方式 | 结果 |
|------|---------|------|------|
| v1 (20:31) | priority1.log | HuggingFace 直连 | GLA model.safetensors 下载超时 (read operation timed out) |
| v2 (20:46) | priority1_v2.log | HuggingFace + xet | xet_get 返回 **401 Unauthorized** (AutoDL 代理已知问题) |
| v3 (20:53) | priority1_v3.log | ModelScope | GLA 下载成功 (58 min)，DeltaNet 下载到 59% 时被中断 |
| run_all (22:22) | run_all.log / exp-005-eval.log | `hf` CLI | CLI 语法错误，打印 help 后 EXIT_CODE=1 |

### CRON 捕获的最终错误

`run_all.log` 脚本使用了错误的 `hf` CLI 命令（输出为 `hf models ls --search "gemma"` 等帮助文本），未能实际下载任何模型，直接 EXIT_CODE=1 退出。

### 关键错误行

```
# v1 - HF 超时
Error while downloading from https://huggingface.co/m-a-p/340M-20B-GLA-hybrid-3-1/.../model.safetensors: The read operation timed out

# v2 - xet 401
ConnectionError: Network error: ... CAS Client Error: HTTP status client error (401 Unauthorized)
domain: https://cas-server.xethub.hf.co/...

# v3 - 下载中断（进程被 kill 或超时）
Downloading [model.safetensors]: 59%|█████▉| 752M/1.24G [33:42<23:01, 394kB/s]  (日志在此截断)

# run_all - CLI 语法错误
EXIT_CODE=1
```

## 部分产出

| 模型 | 状态 |
|------|------|
| 340M-20B-GLA-hybrid-3-1 | **已下载** (1.24GB model.safetensors, v3 第 58 分钟完成) |
| 340M-20B-DeltaNet-hybrid-3-1 | **未下载** (目录不存在，v3 下载到 59% 被中断) |
| 340M-20B-HGRN-hybrid-3-1 | **未下载** (空目录) |
| RetNet/HGRN2/GatedDeltaNet 系列 | 已存在 (5/18 由 exp-005 下载) |

**无评估结果产出。** 结果目录中无任何 eval JSON 或 metrics 文件。

## 建议

**直接关闭，不需要重试。** 理由：

1. 父实验 exp-005 已被 kill，原因是 "Wang et al. zoo 仅含 GDN/RetNet/HGRN2，无法扩展 n>3"——这个结论仍然成立
2. GLA/DeltaNet/HGRN 三个模型的下载在 AutoDL 上极慢 (~400kB/s, 每个模型需 ~1 小时)，且网络不稳定
3. 即使下载成功，这些额外架构对核心论点（entrainment gating 的泛化性）的贡献有限，因为原始 zoo 已有 3 种架构 (GDN/RetNet/HGRN2) 的完整比较数据
4. GLA 已下载的模型可保留备用，但不值得为此重启实验
