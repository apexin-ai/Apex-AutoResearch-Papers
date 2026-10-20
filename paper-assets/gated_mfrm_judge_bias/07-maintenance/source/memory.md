# Memory

## 吞吐测量规范（M030 教训，2026-05-24）
**吞吐量必须用 wc -l 间隔法（≥2min，取 2 次平均）测量稳态速率。**
禁止报告 burst/瞬时速率。已因此被 Director 警告 3 次（M028, M029, M030）。
Worker 刚重启后的前几分钟数据是 burst，不代表稳态。

## D045 决策门控（2026-05-24）— 已触发，结果为 NEGATIVE
**MCMC Δτ = −0.044（方向翻转）。D045 gate FAILED。**
- joint_gmfrm τ=0.794 vs raw_average τ=0.838
- N=8 时 Δτ=+0.071, N=17 时 Δτ=−0.044
- gpt-4-turbo 是翻转主因：c=3.76 导致 θ 下修，排名 1→4
- 合成数据上方法 work (exp-018 Δτ=+0.052, p<0.001)
- **关键洞察**：Arena ELO 本身可能也被 benchmark contamination 影响（memorize benchmark 的模型在人类对话中也表现好），不是无偏 ground truth

## N=17 配置确认（2026-05-24）
- J=6 judges（排除 Mistral/opus-4.7/gpt-5.5）
- Mistral 118 行排除，Appendix 加 sensitivity
- EXCLUDE_MODELS = ["qwen3-8b"]（τ 计算排除，MCMC 保留）
- 17 matched models + 1 excluded = 18 total

## MCMC 两阶段策略（Director 最终决定，2026-05-24）
**Phase 1**：Qwen local + Qwen3 完成后，用 3 complete (LLaMA, Qwen local, Qwen3) + 3 partial (Sonnet 79%, Gemini 63%, DeepSeek ~75%) 跑 MCMC。已自动触发，PID 614592，GPU 0。
**Phase 2**：DeepSeek 完成后（已完成 18,000），重跑最终版 MCMC。
Sonnet/Gemini 已自行退出（403 地域封锁）：Sonnet 14,255 行 (79.2%)，Gemini 11,253 行 (62.5%)。

## MCMC NCP 是必须的（2026-05-25）
- Centered parameterization 在 N=17/I=500+ 下完全不收敛（R̂=2.90, ESS=4）
- NCP (b_raw ~ N(0,1), sigma_b ~ HalfNormal(1.0), b = b_raw * sigma_b) 完全解决（R̂=1.002, ESS≥1240）
- 同时对 θ_n 也做 NCP
- chain_method='vectorized' 速度最快（43 min vs 估计数小时）

## 竞品实验参考
（待填充）

## 经验教训
- TP=2 提升 vLLM generation throughput，但 collect.py 吞吐瓶颈可能在并发请求量（workers 数）而非 GPU
- KV cache 利用率低（<10%）时，应优先增加 workers 而非 GPU 数
- vLLM Blackwell (sm120) 需要 VLLM_USE_FLASHINFER_SAMPLER=0
- AutoDL 实例重启后 SSH 端口会变
- conda 环境（不是 venv）：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- Workers 完成任务后可能不退出（stuck），turn count 高 + last_text 说"任务完成"时直接 cancel
- PaperBanana 生成代码后如果公式错误，优先在生成代码中手动修改而非回退 gen_fig1.py（Director 明确禁止回退）
- DeepSeek API 吞吐瓶颈是服务端响应延迟（~3.3s/req），增加本地 workers 无法突破此限制
- OpenRouter 中国 IP 被 403 封锁 Google/Anthropic 模型："This model is not available in your region."，不可通过降速/换 key 修复
- **nohup + tqdm buffer 问题**：MCMC 脚本用 nohup 启动时，tqdm 输出被 buffer 吞掉导致日志 11h+ 无更新。下次用 `python -u script.py` (unbuffered stdout) + `tqdm(file=sys.stderr)` + `stdbuf -oL` 确保实时输出
- **AutoDL 平台级 SIGKILL**：容器编排可能在运行 7h+ 后 kill 进程，非 OOM（cgroup oom_kill=0）。长时间 MCMC 必须用增量保存（每完成一个 method 立即写盘）
- **Real-data vs Synthetic 鸿沟**：G-MFRM 在合成数据上显著 work（Δτ=+0.05-0.07），但真实数据 N=17 上 Δτ=−0.044。根因：合成 DGP 假设 ground truth ability 无污染，但 Arena ELO 可能本身被训练数据重叠影响。方法"过度修正"了真正强的高污染模型（gpt-4-turbo）。
