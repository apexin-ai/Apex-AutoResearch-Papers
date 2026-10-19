# ApexTune AIF360 trajectory: aif360-integration-gpt56sol-r1-datasetfix-20260909

- Code version: `code-v2`
- Experiment round: `1`
- Search strategy: `patch-manifest-hpo-heavy`
- Strategy meaning: Each LLM request produced one patch/knob-manifest structure; most structures expanded locally into a default validation plus HPO variants.
- Model: `OpenAI/gpt-5.6-sol`
- Protocol: `diagnostic`; comparable=`false`; leaderboard eligible=`false`
- LLM structure requests: `29`
- Reserved requests without a durable terminal record: `0`
- Validated structures: `29`
- Generation-failed structures: `0`
- Full validation steps: `100`
- Default structure validations: `29`
- HPO variant validations: `71`
- Stall batch decisions / cooldown batches: `0` / `0`
- Restart draws: `{}`
- Pool parent draws / pooled steps: `0` / `0`
- Final normalized score: `0.21880897422530848`
- Final absolute AOD: `0.021053621638746994`
- Final accuracy: `0.6257889990982868`

`APEXTUNE_STRUCTURE_INDEX.jsonl` has one row for every logical LLM request, including failed generation requests. `APEXTUNE_VALIDATION_TRAJECTORY.jsonl` has one row for every full validation. Rows sharing an `apextune_structure_id` belong to the same LLM-proposed code structure; `variant_kind=hpo_variant` marks local parameter variants of that structure. On `code-v4` rows, `admission_kind` labels the archive outcome (new_cell / displaced_elite / pooled / rejected) and `pooled=true` marks near-best variants retained by the epsilon-band elite pool. Requests reserved before a process interruption but lacking a durable terminal record are retained with `status=missing` and are not counted as successful or failed generations.
