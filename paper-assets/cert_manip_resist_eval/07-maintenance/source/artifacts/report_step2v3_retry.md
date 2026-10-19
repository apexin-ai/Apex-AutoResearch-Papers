# Step 2v3 Retry: Multi-variate Regression Analysis — 结果报告

## 基本信息
- **实验**: mvp-step2v3-retry
- **Hypothesis**: Controlling for η_max, higher K_eff → significantly lower ASR. Regression log(ASR) ~ log(K_eff) + log(η_max) should show K_eff coefficient significantly negative.
- **日期**: 2026-05-22
- **服务器**: seetacloud-rtx6000

## Conclusion: **FAILED**（运行时错误，非科学结论）

## 错误详情

脚本在 `phase1_inference()` 阶段崩溃：
- MMLU 数据集加载成功（300 samples）
- 加载第二个数据集时，HuggingFace Hub 的 `xet_get` 下载返回 **401 Unauthorized**
- 错误位置: `eval_pipeline.py:24` → `load_dataset()` → `xet_get()`

```
ConnectionError: Network error: Request error: HTTP status client error (401 Unauthorized)
domain: https://cas-server.xethub.hf.co/v2/reconstructions/...
```

## 根因

AutoDL 代理环境下 xet 协议不可用。需要设置环境变量 `HF_HUB_DISABLE_XET=1` 禁用 xet 下载，回退到标准 HTTP 下载。

这与前次 mvp-step2v3-regression 失败是**同一类问题**（运行环境配置），非代码逻辑错误。

## 回归分析数据

**无**。实验在 inference 阶段即崩溃，未产出任何回归结果。results 目录下无 step2v3 相关 JSON 文件。

## 修复建议

在启动脚本中加入：
```bash
export HF_HUB_DISABLE_XET=1
export HF_HOME=/root/autodl-tmp/.hf_cache
```

然后重新运行实验。
