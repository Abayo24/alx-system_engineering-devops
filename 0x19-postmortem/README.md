# Post Mortem: Major API Collapse June 2024

## Issue Summary

**Duration:**
- **Start:** June 22, 2024, 5:00 EAT
- **End:** June 22, 2024, 7:30 EAT

**Impact:**
- The API service took an unexpected nap.
- 4,444 users were exposed to 500 Internal Server Error responses.
- Approximately 80% of users were affected, primarily those relying on real-time data.

**Root Cause:**
- A misconfiguration of load balancer routing rules after deployment sent traffic to a black hole. Oops!

## Timeline

- **17:00 EAT** – **Attention!** Our monitoring system detected a sudden increase in 500 errors. API is out of control.
- **17:05 EAT** – Technician on duty took a sip of coffee, choked a bit, and started the inspection.
- **17:10 EAT** – Focused on recent API changes and database performance, like checking the fridge during a power outage.
- **17:20 EAT** – Scanned databases and API server logs. Nothing. The mystery just kept getting bigger.
- **17:35 EAT** – **False Lead:** Suspected a problem with the database connection (nope, false lead).
- **17:45 EAT** – The digital cavalry was called in, a.k.a. the network engineering team.
- **18:00 EAT** – The network team discovered an error in our load balancing configuration. Aargh!
- **18:15 EAT** – Reset the load balancer routing rules. Partially recovered, but still some issues.
- **18:30 EAT** – Ran a full audit of load balancing and deployment protocols. Inspector Gadget mode: ON.
- **19:00 EAT** – Root cause found: Incorrect redirect to a non-existent server pool. Bingo!
- **19:30 EAT** – Correct routing rules re-applied. API is back! *Cue celebration music.*

## Root Cause and Solution

**Root Cause:**
- During a routine deployment, an intentional but erroneous configuration change in the load balancer settings sent all traffic to a non-existent server pool. The result? API traffic jams going nowhere.

**Solution:**
- The fix involved rolling back to the previous configuration and then carefully reapplying the correct routing rules. We also performed a thorough audit to ensure that all routing paths were pointing to actual live servers.

## Corrective and Preventive Actions

**Improvements/Fixes:**
- The deployment process should be hardened with automatic configuration checks.
- With increased monitoring, these errors should be detected in real time.
- A robust review process for any critical infrastructure changes is a must.

**Tasks:**

1. **Automate Configuration Validation:**
   - Create and integrate scripts to validate load balancer configurations before each deployment. Think of it as a pre-flight checklist.

2. **Improve Monitoring:**
   - Set up alerts for unusual traffic patterns or routing errors on your load balancers.
   - Implement end-to-end API request tracking to identify issues faster than a speeding ticket.

3. **Reviews and Training:**
   - Host training on configuration management best practices. Maybe with pizza.
   - Update your deployment and configuration management SOPs. Make them foolproof (or at least fool-resistant).

4. **Redundancy Checks:**
   - Add a mandatory peer review step for load balancer changes. Two heads are better than one.
   - Schedule regular checks of critical configurations to ensure everything is healthy.

Taking these measures will not only put out fires but also make your house fireproof. Cheers to a more resilient API service!

![API Meltdown](https://example.com/funny-api-meltdown.png)
