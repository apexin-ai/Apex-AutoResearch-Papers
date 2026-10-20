"""DTD MVP end-to-end pipeline.

Runs the full Diagnostic Trace Distillation pipeline:
1. Collect trace from buggy code
2. Segment (structural + line baseline)
3. Teacher scoring and filtering
4. Generate repair under 4 conditions (no_trace, full_trace, structural_filtered, line_filtered)
5. Evaluate repair against ground truth

Dependencies: openai, pandas (optional).
"""
from __future__ import annotations

import json
import logging
import os
import shlex
import subprocess
import time
from typing import Any, Dict, List, Optional

from dtd_types import TraceEvent, TraceSegment, ScoredSegment, estimate_tokens, serialize_event
from trace_collector import TraceCollector
from structural_segmenter import StructuralSegmenter
from line_segmenter import LineSegmenter
from teacher_scorer import TeacherScorer

logger = logging.getLogger(__name__)

try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False
    logger.warning("pandas not installed, DataFrame output unavailable")

REPAIR_PROMPT_TEMPLATE = """\
You are an expert software engineer. Fix the bug described below.

## Bug Report
{issue_description}

## Buggy Code
```python
{buggy_code}
```
{trace_section}
## Task
Provide the corrected code. Output ONLY the fixed Python code, no explanations.
"""

TRACE_SECTION_TEMPLATE = """
## Execution Trace ({condition})
The following trace information was collected during test execution:
```
{trace_context}
```
"""


class MVPPipeline:
    CONDITIONS = ["no_trace", "full_trace", "structural_filtered", "line_filtered"]

    def __init__(
        self,
        teacher_api_key: [REDACTED] = None,
        repair_api_key: [REDACTED] = None,
        repair_model: str = "deepseek-chat",
        output_dir: str = "./mvp_results",
    ):
        self.collector = TraceCollector(max_events=50000, max_depth=30)
        self.structural_segmenter = StructuralSegmenter()
        self.line_segmenter = LineSegmenter(window_size=5, stride=5)
        self.teacher = TeacherScorer(api_key=[REDACTED]
        self.repair_api_key = [REDACTED] or os.environ.get("DEEPSEEK_API_KEY", "")
        self.repair_model = repair_model
        self.output_dir = os.path.abspath(output_dir)
        os.makedirs(self.output_dir, exist_ok=True)
        self._repair_client = None

    def _get_repair_client(self):
        if self._repair_client is None:
            from openai import OpenAI
            self._repair_client = OpenAI(
                api_key=[REDACTED],
                base_url="https://api.deepseek.com/v1",
            )
        return self._repair_client

    def run_single(self, instance: dict, buggy_code: str, fixed_code: str) -> dict:
        instance_id = f"{instance['project']}_{instance['bug_id']}"
        logger.info("Running pipeline for %s", instance_id)

        # 1. Collect trace
        events = self.collector.collect(
            instance.get("buggy_dir", ""),
            instance.get("test_command", ""),
            timeout=120,
        )
        logger.info("Collected %d trace events for %s", len(events), instance_id)

        # 2. Segment
        structural_segments = self.structural_segmenter.segment(events) if events else []
        line_segments = self.line_segmenter.segment(events) if events else []

        # 3. Teacher scoring
        issue = instance.get("issue_description", "")
        structural_scored = (
            self.teacher.score_batch(issue, buggy_code, structural_segments)
            if structural_segments else []
        )
        line_scored = (
            self.teacher.score_batch(issue, buggy_code, line_segments)
            if line_segments else []
        )
        structural_filtered = self.teacher.filter_segments(structural_scored)
        line_filtered = self.teacher.filter_segments(line_scored)

        # 4. Build repair prompts for each condition
        full_trace_text, truncation_info = self._format_full_trace(events, max_tokens=8000)
        structural_trace_text = self._format_filtered_trace(structural_filtered)
        line_trace_text = self._format_filtered_trace(line_filtered)

        conditions = {
            "no_trace": "",
            "full_trace": full_trace_text,
            "structural_filtered": structural_trace_text,
            "line_filtered": line_trace_text,
        }

        # 5. Call repair LLM for each condition
        buggy_file_relpath = instance.get("bug_info", {}).get("buggy_file", "")

        results = {"instance_id": instance_id, "trace_events_count": len(events)}
        results["full_trace_truncation"] = truncation_info
        for condition, trace_ctx in conditions.items():
            prompt = self._build_repair_prompt(issue, buggy_code, trace_ctx, condition)
            tokens_used = estimate_tokens(prompt)

            try:
                generated_fix = self._call_repair_llm(prompt)
            except Exception as e:
                logger.error("Repair LLM failed for %s/%s: %s", instance_id, condition, e)
                generated_fix = ""

            # 6. Evaluate
            eval_result = self._evaluate_repair(
                generated_fix, fixed_code,
                instance.get("test_command", ""),
                instance.get("buggy_dir", ""),
                buggy_file_relpath=buggy_file_relpath,
            )

            results[condition] = {
                "repair_success": eval_result["pass"],
                "eval_method": eval_result.get("method", "none"),
                "line_overlap": eval_result.get("line_overlap", 0.0),
                "tokens_used": tokens_used,
                "generated_fix_length": len(generated_fix),
            }
            logger.info("%s/%s: success=%s (method=%s), tokens=%d",
                        instance_id, condition, eval_result["pass"],
                        eval_result.get("method", "none"), tokens_used)

        results["segments_structural"] = len(structural_segments)
        results["segments_line"] = len(line_segments)
        results["filtered_structural"] = len(structural_filtered)
        results["filtered_line"] = len(line_filtered)

        if structural_segments:
            total_tokens = sum(s.segment.token_estimate for s in structural_scored)
            filtered_tokens = sum(s.segment.token_estimate for s in structural_filtered)
            results["compression_ratio"] = filtered_tokens / max(total_tokens, 1)
        else:
            results["compression_ratio"] = 1.0

        return results

    def run_batch(
        self,
        instances: Optional[List[dict]] = None,
        workspace: str = "./bugsinpy_workspace",
        bug_list: Optional[List[tuple]] = None,
    ) -> Any:
        from bugsinpy_setup import BugsInPySetup
        setup = BugsInPySetup(workspace)

        if instances is None:
            if bug_list is None:
                bug_list = [(p, bid) for p, bid, _ in BugsInPySetup.CANDIDATE_BUGS]
            instances = []
            for project, bug_id in bug_list:
                try:
                    instances.append(setup.setup_instance(project, bug_id))
                except Exception as e:
                    logger.error("Failed to setup %s#%d: %s", project, bug_id, e)

        rows = []
        for inst in instances:
            if "buggy_dir" not in inst:
                try:
                    inst = setup.setup_instance(inst["project"], inst["bug_id"])
                except Exception as e:
                    logger.error("Failed to setup %s#%d: %s", inst.get("project"), inst.get("bug_id"), e)
                    continue

            buggy_code = setup.get_buggy_code(inst)
            fixed_code = setup.get_fixed_code(inst)

            result = self.run_single(inst, buggy_code, fixed_code)

            for condition in self.CONDITIONS:
                cond_result = result.get(condition, {})
                rows.append({
                    "instance_id": result["instance_id"],
                    "condition": condition,
                    "repair_success": cond_result.get("repair_success", False),
                    "tokens_used": cond_result.get("tokens_used", 0),
                    "compression_ratio": result.get("compression_ratio", 1.0),
                    "trace_events_count": result.get("trace_events_count", 0),
                    "segments_count": result.get(
                        "segments_structural" if "structural" in condition else "segments_line", 0
                    ),
                })

        if HAS_PANDAS:
            return pd.DataFrame(rows)
        return rows

    def _build_repair_prompt(self, issue: str, code: str, trace_context: str, condition: str) -> str:
        trace_section = ""
        if trace_context:
            trace_section = TRACE_SECTION_TEMPLATE.format(
                condition=condition, trace_context=trace_context,
            )
        return REPAIR_PROMPT_TEMPLATE.format(
            issue_description=issue,
            buggy_code=code,
            trace_section=trace_section,
        )

    def _call_repair_llm(self, prompt: str) -> str:
        client = self._get_repair_client()
        response = client.chat.completions.create(
            model=self.repair_model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=4096,
        )
        raw_content = response.choices[0].message.content
        content = raw_content.strip() if raw_content else ""
        if not content:
            return ""
        if content.startswith("```"):
            lines = content.split("\n")
            if lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].strip() == "```":
                lines = lines[:-1]
            content = "\n".join(lines)
        return content

    def _evaluate_repair(
        self, generated_fix: str, fixed_code: str,
        test_command: str = "", buggy_dir: str = "",
        buggy_file_relpath: str = "",
    ) -> dict:
        result = {"pass": False, "method": "none"}
        if not generated_fix:
            return result

        gen_lines = generated_fix.strip().splitlines()
        fix_lines = fixed_code.strip().splitlines()
        if gen_lines == fix_lines:
            result["pass"] = True
            result["method"] = "exact_match"
            result["line_overlap"] = 1.0
            return result

        gen_set = set(gen_lines)
        fix_set = set(fix_lines)
        overlap = len(gen_set & fix_set)
        total = max(len(fix_set), 1)
        result["line_overlap"] = overlap / total

        if test_command and buggy_dir and buggy_file_relpath:
            test_result = self._run_test_evaluation(
                generated_fix, test_command, buggy_dir, buggy_file_relpath
            )
            result.update(test_result)
        else:
            result["method"] = "line_overlap_fallback"
            if result["line_overlap"] > 0.9:
                result["pass"] = True

        return result

    def _run_test_evaluation(
        self, generated_fix: str, test_command: str,
        buggy_dir: str, buggy_file_relpath: str,
    ) -> dict:
        buggy_file_path = os.path.join(buggy_dir, buggy_file_relpath)
        if not os.path.isfile(buggy_file_path):
            logger.warning("Buggy file not found: %s", buggy_file_path)
            return {"method": "test_skipped", "reason": "buggy_file_not_found"}

        with open(buggy_file_path, "r") as f:
            original_content = f.read()

        try:
            with open(buggy_file_path, "w") as f:
                f.write(generated_fix)

            try:
                proc = subprocess.run(
                    shlex.split(test_command),
                    capture_output=True,
                    text=True,
                    timeout=120,
                    cwd=buggy_dir,
                )
                return {
                    "pass": proc.returncode == 0,
                    "method": "test_execution",
                    "returncode": proc.returncode,
                    "stderr_snippet": proc.stderr[:500] if proc.stderr else "",
                }
            except subprocess.TimeoutExpired:
                return {"pass": False, "method": "test_execution", "reason": "timeout"}
            except Exception as e:
                logger.warning("Test execution failed: %s", e)
                return {"pass": False, "method": "test_execution", "reason": str(e)[:200]}
        finally:
            with open(buggy_file_path, "w") as f:
                f.write(original_content)

    def _format_full_trace(self, events: List[TraceEvent], max_tokens: int = 8000) -> tuple:
        lines = []
        truncated = False
        for idx, ev in enumerate(events):
            line = f"[{ev.event_type:9s}] {ev.function_name}:{ev.lineno} depth={ev.call_depth}"
            key_locals = {k: v for k, v in list(ev.locals_snapshot.items())[:3]}
            if key_locals:
                line += f" {key_locals}"
            if ev.return_value is not None:
                line += f" -> {repr(ev.return_value)[:80]}"
            if ev.exception_info:
                line += f" EXCEPTION: {ev.exception_info[0]}: {ev.exception_info[1]}"
            lines.append(line)
            if estimate_tokens("\n".join(lines)) > max_tokens:
                remaining = len(events) - idx - 1
                lines.append(f"... ({remaining} more events truncated)")
                truncated = True
                break

        text = "\n".join(lines)
        events_included = len(lines) - (1 if truncated else 0)
        truncation_info = {
            "truncated": truncated,
            "events_included": events_included,
            "events_total": len(events),
            "truncation_ratio": (len(events) - events_included) / max(len(events), 1) if truncated else 0.0,
        }
        return text, truncation_info

    def _format_filtered_trace(self, scored_segments: List[ScoredSegment]) -> str:
        if not scored_segments:
            return "(no relevant trace segments found)"
        lines = []
        for ss in scored_segments:
            seg = ss.segment
            lines.append(f"--- {seg.segment_type} ---")
            for ev in seg.events[:30]:
                line = f"  [{ev.event_type:9s}] {ev.function_name}:{ev.lineno}"
                key_locals = {k: v for k, v in list(ev.locals_snapshot.items())[:3]}
                if key_locals:
                    line += f" {key_locals}"
                lines.append(line)
            if len(seg.events) > 30:
                lines.append(f"  ... ({len(seg.events) - 30} more events)")
        return "\n".join(lines)

    def save_results(self, df: Any, path: Optional[str] = None):
        if path is None:
            path = os.path.join(self.output_dir, "mvp_results.csv")
        if HAS_PANDAS and hasattr(df, "to_csv"):
            df.to_csv(path, index=False)
        else:
            import csv
            with open(path, "w", newline="") as f:
                if df:
                    writer = csv.DictWriter(f, fieldnames=df[0].keys())
                    writer.writeheader()
                    writer.writerows(df)
        logger.info("Results saved to %s", path)

    def print_summary(self, df: Any):
        if HAS_PANDAS and hasattr(df, "groupby"):
            summary = df.groupby("condition").agg({
                "repair_success": ["sum", "count", "mean"],
                "tokens_used": "mean",
                "compression_ratio": "mean",
            })
            print("\n=== MVP Results Summary ===")
            print(summary.to_string())
        else:
            print("\n=== MVP Results Summary ===")
            from collections import defaultdict
            by_cond = defaultdict(list)
            for row in df:
                by_cond[row["condition"]].append(row)
            for cond, rows in by_cond.items():
                n = len(rows)
                successes = sum(1 for r in rows if r["repair_success"])
                avg_tokens = sum(r["tokens_used"] for r in rows) / max(n, 1)
                print(f"  {cond}: {successes}/{n} success, avg_tokens={avg_tokens:.0f}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="DTD MVP Pipeline - Diagnostic Trace Distillation")
    parser.add_argument("--workspace", default="./bugsinpy_workspace", help="BugsInPy workspace directory")
    parser.add_argument("--output-dir", default="./mvp_results", help="Output directory for results")
    parser.add_argument("--repair-model", default="deepseek-chat", help="Repair LLM model name")
    parser.add_argument("--single", action="store_true", help="Run single instance mode")
    parser.add_argument("--project", type=str, help="Project name (for --single mode)")
    parser.add_argument("--bug-id", type=int, help="Bug ID (for --single mode)")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(name)s %(levelname)s: %(message)s")

    api_key = [REDACTED]"DEEPSEEK_API_KEY", "")
    if not api_key:
        logger.warning("DEEPSEEK_API_KEY not set; repair LLM calls will fail")

    pipeline = MVPPipeline(repair_api_key=[REDACTED], repair_model=args.repair_model, output_dir=args.output_dir)

    if args.single:
        if not args.project or args.bug_id is None:
            parser.error("--single requires --project and --bug-id")
        from bugsinpy_setup import BugsInPySetup
        setup = BugsInPySetup(args.workspace)
        instance = setup.setup_instance(args.project, args.bug_id)
        buggy_code = setup.get_buggy_code(instance)
        fixed_code = setup.get_fixed_code(instance)
        result = pipeline.run_single(instance, buggy_code, fixed_code)
        print(json.dumps(result, indent=2, default=str))
    else:
        df = pipeline.run_batch(workspace=args.workspace)
        pipeline.save_results(df)
        pipeline.print_summary(df)
