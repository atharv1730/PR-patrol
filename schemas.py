from dataclasses import dataclass, field
from enum import Enum


class Severity(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class FindingCategory(str, Enum):
    BUG = "bug"
    SECURITY = "security"
    STYLE = "style"
    PERFORMANCE = "performance"
    STRUCTURE = "structure"


@dataclass
class Finding:
    file: str
    line: int | None
    severity: Severity
    category: FindingCategory
    title: str
    description: str
    suggestion: str | None = None


@dataclass
class AgentReport:
    agent_name: str
    findings: list[Finding] = field(default_factory=list)
    summary: str = ""


@dataclass
class PRContext:
    repo: str
    pr_number: int
    title: str
    description: str
    diff: str
    changed_files: list[str]
    skills: dict[str, str]
