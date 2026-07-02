# Delivery Space Rules

## Overview

This folder contains Cursor rules for **Delivery Space Agents** (Agents 11-12), the final phase of the product discovery workflow that transforms all analysis and planning into executable documentation and project structures.

## Available Agents

### Agent 11: Confluence Documentation Specialist
**File:** `agent-11-confluence-documentation-specialist.mdc`

**Purpose:** Structure and format all project documentation for Confluence with navigable hierarchy

**Triggers:**
- "create confluence documentation"
- "generate confluence structure"
- "convert to confluence"
- "prepare confluence pages"
- "run agent 11"

**Outputs:** 
- Complete Confluence page hierarchy in `/3-delivery/confluence/`
- Structure map and import guide
- Formatted, linked, navigable documentation

**Key Features:**
- Converts all markdown to Confluence format
- Establishes page hierarchy and navigation
- Applies Confluence macros and formatting
- Creates import guide

---

### Agent 12: Jira Project Setup Specialist
**File:** `agent-12-jira-project-setup-specialist.mdc`

**Purpose:** Create Jira Initiative, Epics and Stories structure ready for sprint execution

**Triggers:**
- "create jira structure"
- "generate jira project"
- "convert to jira"
- "prepare jira stories"
- "run agent 12"

**Outputs:**
- Initiative with strategic context in `/3-delivery/jira/`
- Epics organized by concept/theme
- Stories with acceptance criteria
- Sprint allocation and import guide

**Key Features:**
- Converts features to user stories
- Maps priorities and story points
- Establishes Epic Links and dependencies
- Creates CSV import template

---

## Workflow Integration

### Complete Agent Sequence

```
PROBLEM SPACE
├── Agent 0: Product/Service Specialist
├── Agent 1: Qualitative Research Specialist
├── Agent 2a: Painpoint Granularization Specialist
├── Agent 2b: Painpoint Clustering Specialist
├── Agent 3: As-Is Journey Mapper
├── Agent 4: Journey Consolidation Specialist
├── Agent 5: Strategic Report Generator
└── Agent 6: Visual Journey Designer

SOLUTION SPACE
├── Agent 6: Solution Ideation Specialist
├── Agent 7: Experience Design Specialist
├── Agent 8: Communication Specialist
├── Agent 9: Product Prioritization Specialist
└── Agent 10: Product Communication Specialist

DELIVERY SPACE ⭐
├── Agent 11: Confluence Documentation Specialist
└── Agent 12: Jira Project Setup Specialist
```

### When to Use Delivery Agents

**After completing:**
- All Problem Space analysis (Agents 0-6)
- All Solution Space planning (Agents 6-10)
- Product brief and roadmap finalized

**Before:**
- Project kickoff
- Team onboarding
- Stakeholder alignment
- Sprint planning

**Purpose:**
- Create centralized knowledge base (Confluence)
- Enable execution tracking (Jira)
- Bridge strategy to implementation

---

## Input Requirements

### Agent 11 Inputs (Confluence)
**From Problem Space:**
- Interview analysis
- Pain point clusters
- As-Is journeys
- Problem reports

**From Solution Space:**
- Product brief
- Opportunities
- Future journeys
- Solution concepts
- MVP scope and features
- Product roadmap

**From Context:**
- Broad context
- Project documentation

### Agent 12 Inputs (Jira)
**From Solution Space:**
- MVP scope (Agent 9)
- MVP features with priorities (Agent 9)
- Stage 2 scope (Agent 9)
- Product brief (Agent 10)
- Product roadmap (Agent 10)
- Solution concepts (Agent 8)

**From Context:**
- Problem report
- Validation plan

---

## Output Structure

### Confluence Outputs (`/3-delivery/confluence/`)

```
confluence/
├── _structure-map.md          # Complete hierarchy
├── _import-guide.md            # Import instructions
├── 00-home.md                  # Navigable home page
├── 01-project-context/         # Project documentation
├── 01-problem-space/           # Problem analysis
│   ├── research/               # Interview analysis
│   ├── pain-points/            # Pain clusters
│   ├── journeys/               # As-Is journeys
│   └── reports/                # Consolidated reports
├── 02-solution-space/          # Solution planning
│   ├── product-brief.md        # ⭐ Key page
│   ├── opportunities/          # Strategic opportunities
│   ├── future-experience/      # To-Be journeys
│   ├── concepts/               # Solution concepts
│   ├── mvp/                    # MVP scope & features
│   └── roadmap/                # Product roadmap
└── 03-delivery/                # Execution guidance
```

### Jira Outputs (`/3-delivery/jira/`)

```
jira/
├── _project-summary.md         # Overview & statistics
├── _import-guide.md            # Import instructions
├── _dependency-map.md          # Relationships visual
├── sprint-allocation.md        # Sprint planning
├── import-template.csv         # CSV for import
├── initiative.md               # Strategic context
├── epics/                      # Epics by theme
│   ├── epic-001.md
│   ├── epic-002.md
│   └── ...
└── stories/                    # Detailed stories
    ├── story-001.md
    ├── story-002.md
    └── ...
```

---

## Usage Examples

### Running Agent 11 (Confluence)

```
User: "Create Confluence documentation structure"
or
User: "Run Agent 11"
```

**Agent Will:**
1. Analyze all Problem/Solution Space outputs
2. Create hierarchical page structure
3. Convert all markdown to Confluence format
4. Establish internal navigation and links
5. Apply Confluence formatting and macros
6. Generate structure map and import guide

**Result:** Complete Confluence documentation in `/3-delivery/confluence/`

---

### Running Agent 12 (Jira)

```
User: "Create Jira project structure"
or
User: "Run Agent 12"
```

**Agent Will:**
1. Extract MVP scope and features from Agent 9
2. Create Initiative with strategic context
3. Decompose concepts into Epics
4. Convert features to Stories with acceptance criteria
5. Map priorities and story points
6. Establish relationships and dependencies
7. Generate CSV import template and guide

**Result:** Complete Jira structure in `/3-delivery/jira/`

---

### Running Both Agents

```
User: "Run Delivery Space agents"
or
User: "Prepare project for execution"
```

**Result:** 
- Confluence documentation ready for team
- Jira backlog ready for sprint planning
- Project ready for kickoff

---

## Key Transformations

### Agent 11 Transformations (Markdown → Confluence)

| Source | Target | Notes |
|--------|--------|-------|
| Markdown files | Confluence pages | Hierarchical structure |
| `## Headers` | Confluence headers | With anchors |
| `[Link](file.md)` | `[Page Title]` | Internal page links |
| Markdown tables | Confluence tables | Enhanced formatting |
| Code blocks | Confluence code macros | Syntax highlighting |
| Lists | Confluence lists | Proper formatting |

**Plus:**
- Breadcrumbs navigation
- Table of contents macros
- Info/warning/success panels
- Status indicators
- Children displays
- Page trees

---

### Agent 12 Transformations (Features → Jira)

| Source | Target | Notes |
|--------|--------|-------|
| Product brief | Initiative | Strategic context |
| Solution concepts | Epics | Thematic grouping |
| MVP features | Stories | User story format |
| Impact/Effort scores | Story points | Fibonacci scale |
| P0/P1/P2/P3 | Highest/High/Med/Low | Jira priorities |
| Feature dependencies | Issue links | Blocks, Blocked By |
| MVP/Stage 2 phases | Sprint allocation | 2-week sprints |
| Acceptance criteria | Story AC | Testable criteria |

**Plus:**
- Epic Links (Story → Epic → Initiative)
- Labels (MVP, Frontend/Backend, etc)
- Sprint suggestions
- CSV import template

---

## Templates Used

### Confluence Templates
- `confluence-page-template.md` - Standard page structure
  - Headers, navigation, macros
  - Overview, detail, and report patterns
  - Confluence-specific formatting

### Jira Templates
- `jira-initiative-template.md` - Initiative structure
  - Strategic context, metrics, phases
  - Epic links and resources
  
- `jira-epic-template.md` - Epic structure
  - Epic description, goal, AC
  - Story list, dependencies, metrics
  
- `jira-story-template.md` - Story structure
  - User story format (As a... I want... So that...)
  - Detailed acceptance criteria
  - Story points, dependencies

### Import Templates
- `import-guide-template.md` - Import instructions
  - Confluence import methods
  - Jira import methods
  - Post-import checklists

---

## Success Criteria

### Agent 11 Success (Confluence)
- [ ] Complete hierarchical structure created
- [ ] All documents converted to Confluence format
- [ ] Internal links functional
- [ ] Navigation intuitive (breadcrumbs, TOC, page trees)
- [ ] Confluence macros applied appropriately
- [ ] Import guide complete and usable
- [ ] Ready for direct Confluence import

### Agent 12 Success (Jira)
- [ ] 1 Initiative with complete context
- [ ] All concepts converted to Epics
- [ ] All P0/P1 features converted to Stories
- [ ] User story format correct
- [ ] Acceptance criteria complete (3-5 per story)
- [ ] Story points estimated
- [ ] Epic Links and dependencies configured
- [ ] CSV import template created
- [ ] Import guide complete
- [ ] Ready for direct Jira import

---

## Best Practices

### For Confluence (Agent 11)

**DO:**
- ✅ Preserve all content (don't summarize)
- ✅ Create shallow hierarchy (max 3-4 levels)
- ✅ Link extensively between related pages
- ✅ Use Confluence macros for enhancement
- ✅ Make navigation intuitive
- ✅ Test links after conversion

**DON'T:**
- ❌ Skip any source documents
- ❌ Create deep hierarchy (>4 levels)
- ❌ Leave broken links
- ❌ Use markdown syntax in Confluence
- ❌ Forget breadcrumbs and TOC

### For Jira (Agent 12)

**DO:**
- ✅ Use proper user story format
- ✅ Include 3-5 acceptance criteria per story
- ✅ Map priorities correctly (P0→Highest)
- ✅ Estimate story points from Effort scores
- ✅ Establish all relationships
- ✅ Create realistic sprint allocation

**DON'T:**
- ❌ Skip features from Agent 9
- ❌ Use generic user stories
- ❌ Leave out acceptance criteria
- ❌ Assign arbitrary story points
- ❌ Forget Epic Links
- ❌ Overload sprints

---

## Completion Indicators

### Agent 11 Complete When:
```
[Agent11] ✅ Confluence documentation structure complete!

Created:
- Structure map with [X] pages
- Navigable home page
- [Y] Problem Space pages
- [Z] Solution Space pages
- Complete import guide

Location: /3-delivery/confluence/
Ready for Confluence import!
```

### Agent 12 Complete When:
```
[Agent12] ✅ Jira project structure complete!

Created:
- 1 Initiative with strategic context
- [X] Epics (MVP: [Y], Stage 2: [Z])
- [W] Stories ([A] P0, [B] P1, [C] P2+)
- Total story points: [XXX]
- Sprint plan: [N] sprints
- CSV import template

Location: /3-delivery/jira/
Ready for Jira import!

🎉 DELIVERY SPACE COMPLETE!
```

---

## Final Workflow State

After both agents complete:

**✅ Problem Space** - What we discovered
- Research analyzed
- Pain points identified
- Current journeys mapped
- Problem defined

**✅ Solution Space** - What we're building
- Opportunities identified
- Future experience designed
- Solutions conceptualized
- MVP prioritized
- Roadmap created

**✅ Delivery Space** - How to execute ⭐
- **Documentation ready** (Confluence)
- **Backlog ready** (Jira)
- **Team ready** (Complete context)
- **Execution ready** (Sprint planning enabled)

**Result:** Project ready for kickoff! 🚀

---

## Related Documentation

**Full Agent Documentation:**
- `/_agents/delivery-space/README.md` - Delivery Space overview
- `/_agents/delivery-space/agent-11-confluence-documentation-specialist.md`
- `/_agents/delivery-space/agent-12-jira-project-setup-specialist.md`

**Templates:**
- `/_output-structure/delivery-space/confluence-page-template.md`
- `/_output-structure/delivery-space/jira-initiative-template.md`
- `/_output-structure/delivery-space/jira-epic-template.md`
- `/_output-structure/delivery-space/jira-story-template.md`
- `/_output-structure/delivery-space/import-guide-template.md`

**Upstream Rules:**
- Problem Space agents: `.cursor/rules/problem-space/`
- Solution Space agents: `.cursor/rules/solution-space/`

---

**These agents complete the full product discovery to delivery workflow, enabling teams to move from research insights to sprint execution with complete documentation and structured backlog.**

