Remote file: /home/sonny/exec-sim-repair-verifier/p2p_regression_analysis.md on home-1x5090

Key findings:
- P2P regression rate: 1.04% mean, 0% median
- 77.4% of incorrect patches break zero P2P tests
- 22.6% break at least 1 P2P test (median 1 test, mean 1.9)
- Aggregated: 45 failures / 19,940 P2P test executions = 0.226%
- Data: CoderForge Qwen3-32B on SWE-bench Verified, 106 unresolved patches
- Conclusion: <5% zone, per-test P2P advantage not significant. Main value in F2P dimension.