# Problem Space Agents (Phase 1)

## Overview

The Problem Space consists of 8 specialized agents (Agents 0, 1, 2A, 2B, 3-6) that systematically analyze customer research data to identify and document core problems, pain points, and current-state processes. This phase transforms raw interview data into strategic problem statements, actionable insights, and AI-ready visual journey maps.

## Agent Sequence

```
Agent 0 → Agent 1 → Agent 2A → Agent 2B → Agent 3 → Agent 4 → Agent 5 → Agent 6
```

## Agent Sequence & Responsibilities

### 🔍 Agent 0: Product & Service Design Specialist
**Input:** `/0-documentation/0a-projectdocs/` context files (e.g., `context.md`)  
**Output:** `/0-documentation/broad-context.md`, project scaffolding  
**Purpose:** Initial project understanding and structure setup

**Key Tasks:**
- Review `/0-documentation/0a-projectdocs/` files
- Create `/0-documentation/broad-context.md` with project scope
- Scaffold `/1-problem/` directory structure
- Hand off to Agent 1 with status summary

### 📋 Agent 1: Qualitative Research Specialist
**Input:** Interview files from `/0-documentation/0b-Interviews/`  
**Output:** Structured interview analyses  
**Purpose:** Extract insights from customer interviews

**Key Tasks:**
- Process all interview files individually
- Create `(name-or-area)-analysis.md` for each interview
- Extract people, processes, pain points, needs, opportunities
- Use interview-analysis-template.md structure

### ⚡ Agent 2A: Pain Point Granularization Specialist
**Input:** Interview analyses from Agent 1  
**Output:** `/1-problem/1b-painpoints/1b0-granular/all-painpoints-granular.md`  
**Purpose:** DECOMPOSE pain points into atomic, specific problems (30-50 pain points)

**Key Tasks:**
- Split each pain point by scenario, root cause, and process stage
- Apply atomicity tests to ensure maximum granularity
- Classify by TYPE (UX/Ops/Business/Tech)
- **Philosophy:** Divergent analysis - break everything into smallest parts

### ⚡ Agent 2B: Pain Point Clustering Specialist
**Input:** Agent 2A granular pain point list  
**Output:** Cluster files in `/1b1-painpoints-breakdown/` + consolidated `painpoint-mapping.md`  
**Purpose:** GROUP atomic pain points by relational patterns (4-6 clusters)

**Key Tasks:**
- Identify causal, contextual, and thematic relationships
- Form 4-6 meaningful clusters (6-10 pain points each)
- Classify cluster type (UX-led/Ops-led/Business-led/Tech-led/Cross)
- Generate consolidated pain point mapping
- **Philosophy:** Convergent analysis - find meaningful patterns

### 🗺️ Agent 3: As-Is Journey Mapper
**Input:** Interview analyses + pain point clusters (Agent 2B)  
**Output:** Individual As-Is journey maps  
**Purpose:** Document current-state processes and workflows

**Key Tasks:**
- Create journey maps for each source file
- Map stages: tools, pain points, needs, opportunities
- Use journey-mapping-template.md structure
- Request user confirmation before proceeding

### 🔄 Agent 4: Journey Consolidation Specialist
**Input:** Individual journey breakdowns from Agent 3  
**Output:** Unified consolidated As-Is journey  
**Purpose:** Harmonize multiple journeys into single view

**Key Tasks:**
- Analyze patterns across individual journeys
- Harmonize process stages and terminology
- Consolidate pain points and opportunities
- Create unified `/1c-asis-journey/asis-journey.md`

### 📊 Agent 5: Strategic Report Generator
**Input:** All previous analyses and consolidated journey  
**Output:** Executive-ready strategic reports (pain + problem)  
**Purpose:** Synthesize findings into actionable business reports

**Key Tasks:**
- Generate pain point report with impact analysis
- Create comprehensive problem statement report
- Provide strategic recommendations and next steps

### 🎨 Agent 6: Visual Journey Designer
**Input:** Consolidated journey + pain point mapping  
**Output:** Figma Make-ready journey visualization  
**Purpose:** Create AI-ready visual specifications for journey maps

**Key Tasks:**
- Generate structured output for Figma Make
- Implement badge system with severity/impact coding
- Create horizontal layout specifications (600px stages)
- Map pain points, needs, opportunities, and hypotheses to stages

## Workflow Dependencies

```mermaid
graph TD
    A[Agent 0: Context & Setup] --> B[Agent 1: Interview Analysis]
    B --> C[Agent 2A: Pain Point Granularization]
    C --> D[Agent 2B: Pain Point Clustering]
    B --> E[Agent 3: Journey Mapping]
    D --> E
    E --> F[Agent 4: Journey Consolidation]
    F --> G[Agent 5: Strategic Reports]
    F --> H[Agent 6: Visual Journey Designer]
```

**Note:** Agents 5 and 6 can run in parallel after Agent 4 completion.

## File Structure Created

```
1-problem/
├── 1a-interview-analysis/
│   ├── (name1)-analysis.md
│   ├── (name2)-analysis.md
│   └── ...
├── 1b-painpoints/
│   ├── 1b0-granular/
│   │   └── all-painpoints-granular.md   (Agent 2A: 30-50 atomic pain points)
│   ├── 1b1-painpoints-breakdown/
│   │   ├── (cluster1).md                (Agent 2B)
│   │   ├── (cluster2).md
│   │   └── ...
│   └── painpoint-mapping.md             (Agent 2B final mapping)
├── 1c-asis-journey/
│   ├── 1c2-asis-breakdown/
│   │   ├── (source1)-journey.md
│   │   ├── (source2)-journey.md
│   │   └── ...
│   └── asis-journey.md
└── 1d-problem-output/
    ├── pain-report.md
    ├── problem-report.md
    └── journey-output.md
```

## Pain Point Analysis: 2-Phase Process

**Why the Agent 2 split?** The original Agent 2 had conflicting goals — decompose (divergent) and cluster (convergent) — which produced over-consolidated results. The split gives each phase a clear, focused instruction set:

- **Agent 2A (Granularization):** Pure decomposition. Target 30-50 atomic pain points. Default to SPLIT when uncertain; never create umbrella pain points.
- **Agent 2B (Clustering):** Pure pattern recognition. Cluster by RELATIONSHIPS (causal, contextual, thematic), not by type. Target 4-6 meaningful clusters.

## Templates & Dependencies

### Required Templates
- `_output-structure/problem-space/interview-analysis-template.md`
- `_output-structure/problem-space/granular-painpoint-template.md` (Agent 2A)
- `_output-structure/problem-space/pain-point-analysis-template.md` (Agent 2B)
- `_output-structure/problem-space/journey-mapping-template.md`
- `_output-structure/problem-space/report-template.md`

### Supporting Files
- `_output-structure/problem-space/model-structure.md`
- `_output-structure/workflow-rules.md`

## Usage Instructions

### 1. Prerequisites
Ensure the following exist before starting:
- `/0-documentation/0a-projectdocs/` with context files
- `/0-documentation/0b-Interviews/` with interview transcripts
- All required template files in `_output-structure/`

### 2. Execution Modes
- **End-to-End:** Sequential execution without interruption
- **Step-by-Step:** Agent-by-agent with approval gates

### 3. Trigger Commands
```
start workflow
begin analysis
run agents
start process
execute workflow
```

### 4. Quality Gates
- **Agent 3 → Agent 4:** Explicit user confirmation required
- **Phase 1 → Phase 2:** Mandatory checkpoint before solution design

## Output Quality Standards

### Data Integrity Requirements
- ✅ **Source Attribution:** All findings reference original interview files
- ✅ **Conservative Language:** No invented metrics or unsubstantiated claims
- ✅ **Evidence-Based:** All conclusions supported by interview data
- ✅ **Assumption Transparency:** Clear documentation of inferences vs. facts

📋 **Guardrail Documentation:** See `/_agents/GUARDRAILS-ENFORCEMENT.md` for detailed rules on data integrity, approved language patterns, and automated validation.

### Deliverable Standards
- **Interview Analyses:** Complete coverage of all interview files
- **Granular Pain Points:** 30-50 atomic, specific problems with type classification
- **Pain Point Clusters:** 4-6 relational clusters with impact assessment
- **Journey Maps:** Stage-by-stage breakdown with touchpoints
- **Strategic Reports:** Executive-ready with actionable recommendations

## Success Metrics

### Completeness
- [ ] All interview files processed into structured analyses
- [ ] Pain points decomposed into atomic items (Agent 2A) and clustered (Agent 2B)
- [ ] Current-state journey documented comprehensively
- [ ] Strategic reports generated with clear recommendations

### Quality
- [ ] Consistent terminology across all deliverables
- [ ] Cross-references maintained for traceability
- [ ] Business impact quantified where possible
- [ ] Actionable insights identified for Phase 2

### Handoff Readiness
- [ ] Problem statement clearly articulated
- [ ] Pain point priorities established
- [ ] Current-state baseline documented
- [ ] Solution space requirements defined

## Common Issues & Solutions

### Missing Interview Files
**Issue:** No files in `/0-documentation/0b-Interviews/`  
**Solution:** Agent 1 creates placeholder noting absence for downstream agents

### Inconsistent Data Quality
**Issue:** Interview files in different formats  
**Solution:** Agent 1 extracts key information consistently using template structure

### Complex Journey Variations
**Issue:** Multiple different processes across interviews  
**Solution:** Agent 4 documents variations and creates conditional journey tracks

### Conflicting Pain Points
**Issue:** Different perspectives on same issue  
**Solution:** Document both perspectives with context in consolidation phase

## Integration Points

### Workflow Orchestrator
- Automated agent sequencing and dependency management
- Quality validation between agents
- Progress tracking and resumption capability

### Solution Phase (Phase 2)
- Problem reports feed into opportunity identification
- Pain point mapping drives solution prioritization
- Journey baseline enables future-state design

## Version History

- **v2.0.0** - Split Agent 2 into Agent 2A (Granularization) + Agent 2B (Clustering); added `1b0-granular/` structure
- **v1.1.0** - Stable version with template dependencies
- **v1.0.0** - Initial agent specification and workflow design

---

**Next Phase:** After Problem Space completion, proceed to [Solution Space Agents](../solution-space/) (Agents 6-10) for opportunity identification, experience design, solution concepts, prioritization, and product communications.
