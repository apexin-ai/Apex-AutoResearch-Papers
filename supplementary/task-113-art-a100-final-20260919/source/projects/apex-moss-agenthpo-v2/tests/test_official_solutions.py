from __future__ import annotations

import hashlib
import json
from dataclasses import replace
from pathlib import Path

import pytest

from optimization_lab.harness_builder.official_solutions import (
    ALEBenchCodeCodec,
    EdgeBenchBundleCodec,
    OfficialSolutionArchive,
)
from optimization_lab.harness_builder.contract_compatibility import (
    ContractCapabilityCard,
)
from optimization_lab.harness_builder.solutions import SolutionContractError


def _edge_response(*files: dict[str, str], **extra: object) -> str:
    return json.dumps(
        {"schema_version": 1, "files": list(files), **extra},
        ensure_ascii=False,
    )


def _file(path: str, content: str, *, file_type: str = "file") -> dict[str, str]:
    return {"path": path, "type": file_type, "content": content}


def _summary_signature(summary: dict[str, object]) -> str:
    encoded = (
        json.dumps(summary, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode()
    return hashlib.sha256(encoded).hexdigest()


def test_edge_codec_round_trip_is_canonical_and_deterministic() -> None:
    codec = EdgeBenchBundleCodec(required_submit_path="solution.py")
    first = codec.parse(
        _edge_response(
            _file("z/helper.txt", "helper\r\ntext\r\n"),
            _file("solution.py", "print('ok')\r\n"),
        )
    )
    second = codec.parse(
        '{"files":['
        '{"type":"file","content":"print(\'ok\')\\n","path":"solution.py"},'
        '{"content":"helper\\ntext\\n","path":"z/helper.txt","type":"file"}'
        '],"schema_version":1}'
    )

    expected = (
        '{"files":['
        '{"content":"print(\'ok\')\\n","path":"solution.py","type":"file"},'
        '{"content":"helper\\ntext\\n","path":"z/helper.txt","type":"file"}'
        '],"schema_version":1}\n'
    )
    assert first.text == expected
    assert second.text == expected
    assert (
        first.sha256
        == second.sha256
        == hashlib.sha256(expected.encode()).hexdigest()
    )
    assert first.structural_signature == second.structural_signature
    assert first.extension == ".json"
    assert first.artifact_kind == "edgebench_file_bundle_v1"

    reparsed = codec.parse(first.text)
    assert (reparsed.text, reparsed.sha256, reparsed.compatibility_trace) == (
        first.text,
        first.sha256,
        first.compatibility_trace,
    )


def test_edge_and_ale_codecs_expose_explicit_contract_skills() -> None:
    edge_skill = EdgeBenchBundleCodec().capability_card
    ale_skill = ALEBenchCodeCodec().capability_card

    assert isinstance(edge_skill, ContractCapabilityCard)
    assert edge_skill.policy_id == "edgebench-file-bundle-v1"
    assert edge_skill.response_boundary == "one complete JSON object and no prose"
    assert "solution.py" in edge_skill.literal_template
    assert "markdown_fence" in edge_skill.forbidden_transformations
    assert len(edge_skill.skill_sha256()) == 64

    assert isinstance(ale_skill, ContractCapabilityCard)
    assert ale_skill.policy_id == "alebench-fenced-source-v1"
    assert ale_skill.response_boundary == "one complete fenced source file and no prose"
    assert "language label" in ale_skill.literal_template
    assert "extra_prose" in ale_skill.forbidden_transformations
    assert len(ale_skill.skill_sha256()) == 64


def test_edge_codec_summary_contains_structure_but_not_source() -> None:
    secret = "[REDACTED]"
    artifact = EdgeBenchBundleCodec().parse(
        _edge_response(_file("solution.py", f"print('{secret}')\n"))
    )

    summary = artifact.compatibility_trace
    assert summary == {
        "schema_version": 1,
        "file_count": 1,
        "paths": ["solution.py"],
        "extensions": [".py"],
        "byte_lengths": [35],
        "content_sha256s": [
            hashlib.sha256(f"print('{secret}')\n".encode()).hexdigest()
        ],
    }
    assert secret not in json.dumps(summary, sort_keys=True)


@pytest.mark.parametrize(
    "path",
    [
        "",
        "/solution.py",
        "C:/solution.py",
        "C:\\solution.py",
        "//server/share/solution.py",
        "\\\\server\\share\\solution.py",
        ".",
        "..",
        "dir/./solution.py",
        "dir/../solution.py",
        "dir//solution.py",
        "dir/solution.py/",
        "dir\\solution.py",
    ],
)
def test_edge_codec_rejects_unsafe_paths(path: str) -> None:
    with pytest.raises(SolutionContractError, match="path"):
        EdgeBenchBundleCodec().parse(
            _edge_response(
                _file("solution.py", "pass\n"),
                _file(path, "bad\n"),
            )
        )


def test_edge_codec_rejects_duplicate_and_conflicting_paths() -> None:
    codec = EdgeBenchBundleCodec()
    with pytest.raises(SolutionContractError, match="duplicate"):
        codec.parse(
            _edge_response(
                _file("solution.py", "pass\n"),
                _file("solution.py", "different\n"),
            )
        )
    with pytest.raises(SolutionContractError, match="conflict"):
        codec.parse(
            _edge_response(
                _file("solution.py", "pass\n"),
                _file("pkg", "file\n"),
                _file("pkg/module.py", "pass\n"),
            )
        )


@pytest.mark.parametrize("schema_version", [True, 1.0])
def test_edge_codec_requires_an_integer_schema_version(
    schema_version: object,
) -> None:
    response = json.dumps(
        {
            "schema_version": schema_version,
            "files": [_file("solution.py", "pass\n")],
        }
    )
    with pytest.raises(SolutionContractError, match="schema version"):
        EdgeBenchBundleCodec().parse(response)


@pytest.mark.parametrize(
    "files",
    [
        (
            _file("solution.py", "pass\n"),
            _file("SOLUTION.PY", "different\n"),
        ),
        (
            _file("solution.py", "pass\n"),
            _file("Pkg", "file\n"),
            _file("pkg/module.py", "pass\n"),
        ),
        (
            _file("solution.py", "pass\n"),
            _file("pkg", "file\n"),
            _file("pkg-extra", "sibling\n"),
            _file("pkg/module.py", "pass\n"),
        ),
    ],
)
def test_edge_codec_rejects_casefolded_path_conflicts(
    files: tuple[dict[str, str], ...],
) -> None:
    with pytest.raises(SolutionContractError, match="conflict"):
        EdgeBenchBundleCodec().parse(_edge_response(*files))


def test_edge_codec_rejects_symlinks_extra_fields_and_duplicate_json_keys() -> None:
    codec = EdgeBenchBundleCodec()
    with pytest.raises(SolutionContractError, match="file type"):
        codec.parse(
            _edge_response(
                _file("solution.py", "pass\n"),
                _file("link.py", "solution.py", file_type="symlink"),
            )
        )
    with pytest.raises(SolutionContractError, match="fields"):
        codec.parse(_edge_response(_file("solution.py", "pass\n"), note="no"))
    with pytest.raises(SolutionContractError, match="fields"):
        codec.parse(
            _edge_response(
                {
                    **_file("solution.py", "pass\n"),
                    "mode": "executable",
                }
            )
        )
    with pytest.raises(SolutionContractError, match="duplicate JSON key"):
        codec.parse(
            '{"schema_version":1,"schema_version":1,'
            '"files":[{"path":"solution.py","type":"file","content":"pass\\n"}]}'
        )


def test_edge_codec_rejects_missing_submit_path_and_size_limits() -> None:
    with pytest.raises(SolutionContractError, match="required submit path"):
        EdgeBenchBundleCodec(required_submit_path="solution.py").parse(
            _edge_response(_file("main.py", "pass\n"))
        )
    with pytest.raises(SolutionContractError, match="file size"):
        EdgeBenchBundleCodec(max_file_bytes=4, max_total_bytes=20).parse(
            _edge_response(_file("solution.py", "12345"))
        )
    with pytest.raises(SolutionContractError, match="total size"):
        EdgeBenchBundleCodec(max_file_bytes=10, max_total_bytes=7).parse(
            _edge_response(
                _file("solution.py", "1234"),
                _file("other.txt", "5678"),
            )
        )


def test_edge_parse_never_materializes_files(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.chdir(tmp_path)
    before = list(tmp_path.iterdir())
    EdgeBenchBundleCodec().parse(
        _edge_response(
            _file("solution.py", "pass\n"),
            _file("pkg/helper.py", "VALUE = 1\n"),
        )
    )
    assert list(tmp_path.iterdir()) == before


@pytest.mark.parametrize(
    ("label", "canonical_language", "extension"),
    [
        ("cpp", "cpp", ".cpp"),
        ("cpp17", "cpp17", ".cpp"),
        ("cpp20", "cpp20", ".cpp"),
        ("cpp23", "cpp23", ".cpp"),
        ("python", "python", ".py"),
        ("py", "python", ".py"),
        ("rust", "rust", ".rs"),
    ],
)
def test_ale_codec_accepts_allowlisted_single_fences(
    label: str, canonical_language: str, extension: str
) -> None:
    secret = "[REDACTED]"
    artifact = ALEBenchCodeCodec().parse(
        f"```{label}\r\nprint('{secret}')\r\n\r\n```\r\n"
    )

    assert artifact.text == f"print('{secret}')\n"
    assert artifact.extension == extension
    assert artifact.artifact_kind == f"alebench_source_{canonical_language}"
    assert artifact.compatibility_trace == {
        "schema_version": 1,
        "language": canonical_language,
        "byte_length": len(artifact.text.encode()),
        "source_sha256": artifact.sha256,
    }
    assert secret not in json.dumps(artifact.compatibility_trace, sort_keys=True)


def test_ale_codec_canonicalization_is_deterministic() -> None:
    codec = ALEBenchCodeCodec()
    first = codec.parse("```py\r\nprint('ok')\r\n\r\n```")
    second = codec.parse("```python\nprint('ok')\n```")
    assert first.text == second.text == "print('ok')\n"
    assert first.sha256 == second.sha256
    assert first.structural_signature == second.structural_signature


@pytest.mark.parametrize(
    "response",
    [
        "print('no fence')\n",
        "Here is the answer:\n```python\npass\n```",
        "```python\npass\n```\nextra prose",
        "```python\npass\n```\n```python\npass\n```",
        "```javascript\nconsole.log(1)\n```",
        "```CPP\nint main() {}\n```",
        "```\npass\n```",
        "```python pass\n```",
    ],
)
def test_ale_codec_rejects_non_single_or_unsupported_fences(response: str) -> None:
    with pytest.raises(SolutionContractError):
        ALEBenchCodeCodec().parse(response)


def test_ale_codec_rejects_oversized_source() -> None:
    with pytest.raises(SolutionContractError, match="source size"):
        ALEBenchCodeCodec(max_source_bytes=4).parse("```python\n12345\n```")


def test_official_archive_is_content_addressed_idempotent_and_secret_free(
    tmp_path: Path,
) -> None:
    secret = "[REDACTED]"
    edge = EdgeBenchBundleCodec().parse(
        _edge_response(_file("solution.py", f"print('{secret}')\n"))
    )
    ale = ALEBenchCodeCodec().parse("```python\nprint('different')\n```")
    archive = OfficialSolutionArchive(tmp_path / "official")

    stored = archive.store(edge)
    assert archive.store(edge) == stored
    assert stored.artifact_sha256 == edge.sha256
    assert stored.artifact_path.name == f"{edge.sha256}.json"
    assert stored.artifact_path.read_text(encoding="utf-8") == edge.text
    receipt_text = stored.receipt_path.read_text(encoding="utf-8")
    assert secret not in receipt_text
    assert json.loads(receipt_text)["structural_summary"] == edge.compatibility_trace

    other = archive.store(ale)
    assert other.artifact_path != stored.artifact_path
    assert stored.artifact_path.read_text(encoding="utf-8") == edge.text


def test_official_archive_idempotence_depends_on_canonical_content(
    tmp_path: Path,
) -> None:
    codec = ALEBenchCodeCodec()
    first = codec.parse("```py\r\nprint('same')\r\n\r\n```\r\n")
    second = codec.parse("```python\nprint('same')\n```")
    assert first.sha256 == second.sha256
    archive = OfficialSolutionArchive(tmp_path / "official")

    assert archive.store(first) == archive.store(second)


def test_official_archive_revalidates_artifact_with_its_codec(
    tmp_path: Path,
) -> None:
    edge = EdgeBenchBundleCodec().parse(
        _edge_response(_file("solution.py", "pass\n"))
    )
    noncanonical_text = json.dumps(json.loads(edge.text), indent=2) + "\n"
    noncanonical_edge = replace(
        edge,
        raw_response=noncanonical_text,
        text=noncanonical_text,
        sha256=hashlib.sha256(noncanonical_text.encode()).hexdigest(),
    )
    archive = OfficialSolutionArchive(tmp_path / "official")
    with pytest.raises(ValueError, match="canonical"):
        archive.store(noncanonical_edge)

    ale = ALEBenchCodeCodec().parse("```python\nprint('one')\n```")
    mismatched_ale = replace(
        ale,
        raw_response="```python\nprint('two')\n```",
    )
    with pytest.raises(ValueError, match="binding"):
        archive.store(mismatched_ale)


def test_official_archive_rejects_leaky_structural_summary(
    tmp_path: Path,
) -> None:
    secret = "[REDACTED]"
    artifact = ALEBenchCodeCodec().parse(f"```python\nprint('{secret}')\n```")
    leaky_summary = {**artifact.compatibility_trace, "source_text": secret}
    forged = replace(
        artifact,
        compatibility_trace=leaky_summary,
        structural_signature=_summary_signature(leaky_summary),
    )

    with pytest.raises(ValueError, match="summary"):
        OfficialSolutionArchive(tmp_path / "official").store(forged)


def test_official_archive_refuses_content_address_collision(tmp_path: Path) -> None:
    artifact = ALEBenchCodeCodec().parse("```rust\nfn main() {}\n```")
    archive = OfficialSolutionArchive(tmp_path / "official")
    collision = (
        tmp_path
        / "official"
        / "artifacts"
        / f"{artifact.sha256}{artifact.extension}"
    )
    collision.parent.mkdir(parents=True)
    collision.write_bytes(b"different content\n")

    with pytest.raises(ValueError, match="content-address collision"):
        archive.store(artifact)
    assert collision.read_bytes() == b"different content\n"


def test_edge_archive_materializes_only_into_a_fresh_attempt_root(
    tmp_path: Path,
) -> None:
    artifact = EdgeBenchBundleCodec().parse(
        _edge_response(
            _file("solution.py", "print('ok')\n"),
            _file("pkg/helper.py", "VALUE = 1\n"),
        )
    )
    archive = OfficialSolutionArchive(tmp_path / "official")
    stored = archive.store(artifact)
    attempt_root = tmp_path / "attempt-v001"

    assert (
        archive.materialize_edge_bundle(stored.artifact_sha256, attempt_root)
        == attempt_root
    )
    assert (attempt_root / "solution.py").read_text(encoding="utf-8") == "print('ok')\n"
    assert (attempt_root / "pkg" / "helper.py").read_text(
        encoding="utf-8"
    ) == "VALUE = 1\n"

    (attempt_root / "sentinel.txt").write_text("keep", encoding="utf-8")
    with pytest.raises(ValueError, match="already exists"):
        archive.materialize_edge_bundle(stored.artifact_sha256, attempt_root)
    assert (attempt_root / "sentinel.txt").read_text(encoding="utf-8") == "keep"


def test_edge_archive_rejects_any_preexisting_attempt_root(tmp_path: Path) -> None:
    artifact = EdgeBenchBundleCodec().parse(
        _edge_response(_file("solution.py", "pass\n"))
    )
    archive = OfficialSolutionArchive(tmp_path / "official")
    stored = archive.store(artifact)
    empty_root = tmp_path / "existing-empty"
    empty_root.mkdir()

    with pytest.raises(ValueError, match="already exists"):
        archive.materialize_edge_bundle(stored.artifact_sha256, empty_root)
    assert list(empty_root.iterdir()) == []


def test_edge_archive_cleans_failed_staging_and_can_retry(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    artifact = EdgeBenchBundleCodec().parse(
        _edge_response(
            _file("solution.py", "print('first')\n"),
            _file("z/helper.py", "VALUE = 1\n"),
        )
    )
    archive = OfficialSolutionArchive(tmp_path / "official")
    stored = archive.store(artifact)
    attempt_root = tmp_path / "attempt-v002"
    staging_roots: set[Path] = set()
    original_open = Path.open

    def fail_second_file(
        path: Path,
        mode: str = "r",
        *args: object,
        **kwargs: object,
    ) -> object:
        if mode == "xb":
            relative = path.relative_to(attempt_root.parent)
            staging_roots.add(attempt_root.parent / relative.parts[0])
            if path.name == "helper.py":
                raise OSError("injected materialization failure")
        return original_open(path, mode, *args, **kwargs)

    with monkeypatch.context() as patch:
        patch.setattr(Path, "open", fail_second_file)
        with pytest.raises(OSError, match="injected materialization failure"):
            archive.materialize_edge_bundle(stored.artifact_sha256, attempt_root)

    assert staging_roots
    assert attempt_root not in staging_roots
    assert not attempt_root.exists()
    assert all(not staging_root.exists() for staging_root in staging_roots)

    assert (
        archive.materialize_edge_bundle(stored.artifact_sha256, attempt_root)
        == attempt_root
    )
    assert (attempt_root / "solution.py").read_text(
        encoding="utf-8"
    ) == "print('first')\n"
    assert (attempt_root / "z" / "helper.py").read_text(
        encoding="utf-8"
    ) == "VALUE = 1\n"
