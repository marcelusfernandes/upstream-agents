# Problem Space Agents

## Overview
Agents responsible for analyzing the current state, identifying pain points, and mapping user journeys in the problem space.

## Agent Sequence

```
Agent 0 → Agent 1 → Agent 2A → Agent 2B → Agent 3 → Agent 4 → Agent 5 → Agent 6
```

## Agent Descriptions

### Agent 0: Product Service Specialist
**Input:** Raw project data, business context  
**Job:** Understand product/service, set up documentation structure  
**Output:** `/0-documentation/broad-context.md`

### Agent 1: Qualitative Research Specialist  
**Input:** Raw interviews  
**Job:** Deep interview analysis, extract pain points, user behaviors  
**Output:** `/1-problem/1a-interview-analysis/(interview-name).md`

### Agent 2A: Pain Point Granularization Specialist ⚡ NEW
**Input:** Agent 1 interview analyses  
**Job:** **DECOMPOSE** pain points into atomic, specific problems (30-50 pain points)  
**Output:** `/1-problem/1b-painpoints/1b0-granular/all-painpoints-granular.md`  
**Philosophy:** Divergent analysis - break everything into smallest parts  
**Mindset:** "How many different problems are hiding inside this one?"

### Agent 2B: Pain Point Clustering Specialist ⚡ NEW  
**Input:** Agent 2A granular pain point list  
**Job:** **GROUP** atomic pain points by relational patterns (4-6 clusters)  
**Output:**  
- `/1-problem/1b-painpoints/1b1-painpoints-breakdown/(cluster-name).md`
- `/1-problem/1b-painpoints/painpoint-mapping.md`

**Philosophy:** Convergent analysis - find meaningful patterns  
**Mindset:** "What connects these pain points? Why do they belong together?"

### Agent 3: As-Is Journey Mapper
**Input:** Agent 2B pain point clusters  
**Job:** Map current user journey with pain points  
**Output:** `/1-problem/1c-asis-journey/` files

### Agent 4: Journey Consolidation Specialist  
**Input:** Agent 3 journey maps  
**Job:** Consolidate multiple journey maps  
**Output:** Unified journey documentation

### Agent 5: Strategic Report Generator
**Input:** All problem space analyses  
**Job:** Generate executive problem reports  
**Output:** `/1-problem/1d-problem-output/` reports

### Agent 6: Visual Journey Designer
**Input:** Agent 5 reports  
**Job:** Create Figma-ready visual journey specifications  
**Output:** Visual journey specs

## Pain Point Analysis: 2-Phase Process

### Why Split Agent 2?

**Original Problem:**
- Agent 2 had conflicting goals: decompose (divergent) + cluster (convergent)
- Results were over-consolidated (16 pain points instead of 40)
- Instructions pulled in opposite directions

**Solution:**
- **Agent 2A:** Pure decomposition (30-50 atomic pain points)
- **Agent 2B:** Pure clustering (4-6 thematic clusters)
- Clear, focused instructions for each
- Better output quality and consistency

### Phase 1: Granularization (Agent 2A)

**Goal:** Maximum granularity - atomic pain points

**Process:**
1. Read Agent 1 analysis
2. For each pain point:
   - Split by scenario
   - Split by root cause
   - Split by process stage
3. Test atomicity (4 tests)
4. Classify by TYPE (UX/Ops/Business/Tech)
5. Document in granular list

**Output:** 30-50 specific, actionable pain points

**Example:**
```
Input: "No social features"
Output: 
  PP1: Cannot create leagues
  PP2: No rankings visible
  PP3: No friend comparison
  PP4: No social sharing
  PP5: No achievement badges
  PP6: No challenges/missions
  PP7: No streak tracking
  PP8: No rivalry features
  PP9: No geo-competition
  PP10: No match-day engagement
```

### Phase 2: Clustering (Agent 2B)

**Goal:** Find relational patterns - meaningful clusters

**Process:**
1. Read Agent 2A granular list
2. Identify patterns:
   - Causal relationships
   - Shared root causes
   - Common contexts
   - Thematic coherence
   - Impact correlation
3. Form 4-6 clusters (6-10 pain points each)
4. Classify cluster type (UX-led/Ops-led/Business-led/Tech-led/Cross)
5. Document relationships
6. Create consolidated mapping

**Output:** 
- 4-6 cluster files
- 1 consolidated mapping

**Example:**
```
From 40 atomic pain points → 5 clusters:
- Transparency & Tracking (6 PPs) - Cross-dimensional
- Social & Gamification (10 PPs) - UX-led
- Rewards & Recognition (8 PPs) - Business-led
- Onboarding & Education (8 PPs) - UX-led
- Feature Gaps (8 PPs) - Cross-dimensional
```

## Output Structure

```
/1-problem/
  /1a-interview-analysis/
    luiz-henrique-analysis.md (Agent 1)
    
  /1b-painpoints/
    /1b0-granular/ (Agent 2A) ⚡ NEW
      all-painpoints-granular.md (30-50 atomic pain points)
      
    /1b1-painpoints-breakdown/ (Agent 2B)
      transparency-tracking.md (Cluster 1)
      social-gamification.md (Cluster 2)
      rewards-recognition.md (Cluster 3)
      onboarding-education.md (Cluster 4)
      feature-gaps.md (Cluster 5)
      
    painpoint-mapping.md (Agent 2B final mapping)
```

## Key Principles

### Agent 2A Principles
✅ **DO:**
- Break down into smallest parts
- Each distinct issue = separate pain point
- Default to SPLIT when uncertain
- Target 30-50 atomic pain points

❌ **DON'T:**
- Group related issues together
- Create umbrella pain points
- Think about clustering yet

### Agent 2B Principles
✅ **DO:**
- Cluster by RELATIONSHIPS (not type)
- Any dimension can lead a cluster
- Show type distribution within clusters
- Target 4-6 meaningful clusters

❌ **DON'T:**
- Cluster all UX together just because they're UX
- Force type-based groupings
- Ignore cross-dimensional patterns

## Version History

- **v2.0.0 (2025-10-16):** Split Agent 2 into Agent 2A + 2B
- **v1.0.0 (2025-08-19):** Original single Agent 2

## Related Documents

- Agent 2A: `agent-2a-painpoint-granularization-specialist.md`
- Agent 2B: `agent-2b-painpoint-clustering-specialist.md`
- Agent 2 (deprecated): `agent-2-painpoint-analysis-specialist.md.backup`
- Template (granular): `/_output-structure/problem-space/granular-painpoint-template.md`
- Template (cluster): `/_output-structure/problem-space/pain-point-analysis-template.md`
- Workflow: `/_output-structure/workflow-rules.md`
