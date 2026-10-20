"""Optimized driver: clone each project repo once, reuse for instances."""
import json
import logging
import os
import subprocess
import sys
import time
import traceback

sys.path.insert(0, "/root/trace_distill_repair")

from bugsinpy_setup import BugsInPySetup
from trace_collector import TraceCollector
from structural_segmenter import StructuralSegmenter
from line_segmenter import LineSegmenter
from dtd_types import serialize_segment

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
                    handlers=[logging.StreamHandler(sys.stdout)])
logger = logging.getLogger(__name__)
# Force flush
sys.stdout.reconfigure(line_buffering=True)

WORKSPACE = "/root/trace_distill_repair/bugsinpy_workspace"
OUTPUT_DIR = "/root/trace_distill_repair/pipeline_output"
REPO_POOL = os.path.join(WORKSPACE, "repo_pool")
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(REPO_POOL, exist_ok=True)

setup = BugsInPySetup(workspace_dir=WORKSPACE)
setup._ensure_repo()

# Build project -> github_url mapping
project_urls = {}
for project, bug_id, _ in setup.CANDIDATE_BUGS:
    if project in project_urls:
        continue
    bug_dir = os.path.join(setup.repo_dir, "projects", project, "bugs", str(bug_id))
    bug_info = setup._read_bug_info(bug_dir)
    repo_url = bug_info.get("github_url", "")
    if not repo_url:
        pinfo = os.path.join(setup.repo_dir, "projects", project, "project.info")
        if os.path.isfile(pinfo):
            with open(pinfo) as f:
                for line in f:
                    if "github_url" in line.lower():
                        _, _, url = line.partition("=")
                        repo_url = url.strip().strip('"')
                        break
    if repo_url:
        project_urls[project] = repo_url
        logger.info("Project %s -> %s", project, repo_url)

# Phase 1: Clone each project repo once
logger.info("=== PRE-CLONE: %d unique project repos ===", len(project_urls))
for project, url in project_urls.items():
    pool_dir = os.path.join(REPO_POOL, project)
    if os.path.isfile(os.path.join(pool_dir, "HEAD")):
        logger.info("SKIP clone %s (exists)", project)
        continue
    logger.info("Cloning %s from %s ...", project, url)
    try:
        subprocess.run(["git", "clone", "--bare", url, pool_dir],
                       check=True, capture_output=True, timeout=120)
        logger.info("OK clone %s", project)
    except Exception as e:
        logger.error("FAIL clone %s: %s", project, e)

# Phase 1b: Setup instances using local clones
instances = []
setup_results = {"success": [], "failed": []}

logger.info("=== PHASE 1: Setting up %d BugsInPy instances ===", len(setup.CANDIDATE_BUGS))
for project, bug_id, desc in setup.CANDIDATE_BUGS:
    key = f"{project}_{bug_id}"
    work_dir = os.path.join(WORKSPACE, "instances", key)
    buggy_dir = os.path.join(work_dir, "buggy")

    if os.path.isdir(buggy_dir) and os.path.isdir(os.path.join(buggy_dir, ".git")):
        logger.info("SKIP setup %s (exists)", key)
        bug_dir = os.path.join(setup.repo_dir, "projects", project, "bugs", str(bug_id))
        bug_info = setup._read_bug_info(bug_dir)
        test_cmd = bug_info.get("test_command", "python -m pytest")
        instances.append({
            "project": project,
            "bug_id": bug_id,
            "buggy_dir": buggy_dir,
            "test_command": test_cmd,
            "bug_info": bug_info,
        })
        setup_results["success"].append(key)
        continue

    os.makedirs(work_dir, exist_ok=True)
    pool_dir = os.path.join(REPO_POOL, project)
    bug_dir = os.path.join(setup.repo_dir, "projects", project, "bugs", str(bug_id))

    try:
        bug_info = setup._read_bug_info(bug_dir)
        commit_id = bug_info.get("buggy_commit_id", "")
        test_cmd = bug_info.get("test_command", "python -m pytest")

        if not commit_id:
            raise ValueError(f"No buggy commit ID for {key}")

        if os.path.isfile(os.path.join(pool_dir, "HEAD")):
            # Clone from local bare repo (very fast)
            subprocess.run(["git", "clone", pool_dir, buggy_dir],
                           check=True, capture_output=True, timeout=120)
        else:
            # Fallback to remote clone
            repo_url = project_urls.get(project, "")
            if not repo_url:
                raise ValueError(f"No URL for {project}")
            subprocess.run(["git", "clone", repo_url, buggy_dir],
                           check=True, capture_output=True, timeout=120)

        subprocess.run(["git", "checkout", commit_id],
                       check=True, capture_output=True, cwd=buggy_dir)

        instances.append({
            "project": project,
            "bug_id": bug_id,
            "buggy_dir": buggy_dir,
            "test_command": test_cmd,
            "bug_info": bug_info,
        })
        setup_results["success"].append(key)
        logger.info("OK: %s", key)
    except Exception as e:
        setup_results["failed"].append({"key": key, "error": str(e)})
        logger.error("FAIL: %s -> %s", key, e)

logger.info("Phase 1 done: %d/%d success", len(setup_results["success"]), len(setup.CANDIDATE_BUGS))

# Phase 2: Trace collection
collector = TraceCollector(max_events=50000, max_depth=30)
trace_results = {"success": [], "failed": [], "traces": {}}

logger.info("=== PHASE 2: Collecting traces for %d instances ===", len(instances))
for inst in instances:
    key = f"{inst['project']}_{inst['bug_id']}"
    try:
        buggy_dir = inst["buggy_dir"]
        test_cmd = inst.get("test_command", "python -m pytest")

        main_py = None
        for root, dirs, files in os.walk(buggy_dir):
            dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", ".tox", "venv", "node_modules", ".eggs")]
            for f in sorted(files):
                if f.endswith(".py") and not f.startswith("test_") and f != "setup.py":
                    main_py = os.path.join(root, f)
                    break
            if main_py:
                break

        if not main_py:
            trace_results["failed"].append({"key": key, "error": "No Python file found"})
            logger.error("FAIL trace %s: no Python file", key)
            continue

        events = collector.collect(main_py, test_cmd, timeout=120)

        if events:
            trace_results["success"].append(key)
            trace_results["traces"][key] = events
            trace_file = os.path.join(OUTPUT_DIR, f"{key}_trace.json")
            with open(trace_file, "w") as f:
                json.dump([{
                    "event_type": e.event_type,
                    "function_name": e.function_name,
                    "filename": e.filename,
                    "lineno": e.lineno,
                    "call_depth": e.call_depth,
                } for e in events], f)
            logger.info("OK trace %s: %d events", key, len(events))
        else:
            trace_results["failed"].append({"key": key, "error": "No events collected"})
            logger.warning("FAIL trace %s: 0 events", key)
    except Exception as e:
        trace_results["failed"].append({"key": key, "error": str(e)[:200]})
        logger.error("FAIL trace %s: %s", key, str(e)[:200])

logger.info("Phase 2 done: %d/%d success", len(trace_results["success"]), len(instances))

# Phase 3: Segmentation
struct_seg = StructuralSegmenter()
line_seg = LineSegmenter(window_size=5, stride=5)
seg_results = {"structural": {}, "line": {}}

logger.info("=== PHASE 3: Segmenting traces ===")
for key, events in trace_results["traces"].items():
    try:
        s_segs = struct_seg.segment(events)
        l_segs = line_seg.segment(events)

        seg_results["structural"][key] = {
            "num_segments": len(s_segs),
            "types": {},
        }
        for s in s_segs:
            t = s.segment_type
            seg_results["structural"][key]["types"][t] = seg_results["structural"][key]["types"].get(t, 0) + 1

        seg_results["line"][key] = {"num_segments": len(l_segs)}

        s_file = os.path.join(OUTPUT_DIR, f"{key}_structural_segments.json")
        l_file = os.path.join(OUTPUT_DIR, f"{key}_line_segments.json")
        with open(s_file, "w") as f:
            json.dump([serialize_segment(s) for s in s_segs], f)
        with open(l_file, "w") as f:
            json.dump([serialize_segment(s) for s in l_segs], f)

        logger.info("OK seg %s: structural=%d, line=%d", key, len(s_segs), len(l_segs))
    except Exception as e:
        logger.error("FAIL seg %s: %s", key, e)

# Summary
summary = {
    "phase1_setup": {
        "total": len(setup.CANDIDATE_BUGS),
        "success": len(setup_results["success"]),
        "failed": len(setup_results["failed"]),
        "failed_list": setup_results["failed"],
    },
    "phase2_traces": {
        "total": len(instances),
        "success": len(trace_results["success"]),
        "failed": len(trace_results["failed"]),
        "failed_list": trace_results["failed"],
        "event_counts": {k: len(v) for k, v in trace_results["traces"].items()},
    },
    "phase3_segmentation": seg_results,
    "output_dir": OUTPUT_DIR,
}

with open(os.path.join(OUTPUT_DIR, "summary.json"), "w") as f:
    json.dump(summary, f, indent=2)

logger.info("=== FINAL SUMMARY ===")
logger.info("Phase 1: %d/%d", summary["phase1_setup"]["success"], summary["phase1_setup"]["total"])
logger.info("Phase 2: %d/%d", summary["phase2_traces"]["success"], summary["phase2_traces"]["total"])
if trace_results["traces"]:
    avg_events = sum(len(v) for v in trace_results["traces"].values()) / len(trace_results["traces"])
    logger.info("Avg trace events: %.0f", avg_events)
logger.info("Phase 3: %d structural, %d line", len(seg_results["structural"]), len(seg_results["line"]))
logger.info("Output: %s", OUTPUT_DIR)
