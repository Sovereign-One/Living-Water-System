# Distributed Water Infrastructure Architecture

## Purpose

This document describes a place-agnostic infrastructure architecture for the Living Water System.

The concept does **not** propose replacing existing centralized potable-water systems.

Conventional desalination plants, treatment facilities, modern pumps, potable-water mains, storage systems, emergency capacity, and existing utility infrastructure remain valuable and may continue operating normally.

The Living Water System instead explores whether a **second parallel water utility** can provide additional resilience and reduce the amount of high-quality potable water that must be produced and transported for uses that do not require potable quality.

The architecture therefore separates two functions:

1. production and distribution of finished potable water; and
2. distribution of lower-quality source water that can be treated closer to the point where potable quality is actually required.

## Dual-Utility Architecture

### Utility 1 — Existing Potable-Water System

The existing potable-water utility continues to provide conventionally treated water through established infrastructure.

A generalized flow is:

Source water → centralized treatment or desalination → pumping → storage → potable distribution → user

This system remains important for public health, redundancy, existing development, emergency response, and applications requiring reliable finished-water quality.

The Living Water System is intended to supplement this network rather than require its abandonment.

### Utility 2 — Tier-2 Water Backbone

The proposed second utility distributes minimally processed source water through a separate network.

Depending on local conditions, the source may include:

- seawater;
- brackish water;
- other saline water;
- other suitable non-potable water sources.

A generalized flow is:

Source water → screening / minimal pretreatment → Tier-2 backbone → local use or distributed treatment → user

The objective is to avoid performing the most energy-, process-, and quality-intensive treatment steps before long-distance distribution when those steps are not required for every use.

## Water-Quality Matching Principle

A central design principle is:

**Treat water to the quality required by the use.**

Potable water is a high-value engineered product.

Not every water demand requires potable quality.

Where appropriate, Tier-2 water could serve applications that tolerate lower-quality water directly.

Where potable water is required, final treatment can occur closer to the point of consumption.

This creates two possible paths:

Tier-2 water → appropriate non-potable use

or:

Tier-2 water → distributed final treatment → potable use

The architecture does not assume that every application, building, or community would use the same treatment pathway.

## Embedded Treatment Value

Centralized potable-water systems invest substantial treatment and energy before water enters the distribution network.

When finished potable water is lost through leakage before reaching the user, the system loses not only the source water but also the treatment, pumping, chemical, energy, and infrastructure value already invested in that water.

A Tier-2 architecture explores a different sequence:

Source water → minimal processing → distribution → final treatment near use

A leak in the Tier-2 network would still represent water loss and would still require asset-management attention.

However, the lost water would not necessarily contain the same amount of embedded final-treatment value as finished potable water.

This hypothesis should be evaluated using lifecycle energy, water-loss, cost, environmental, and reliability analysis.

## Brine Backbone

The **Brine Backbone** is the conceptual Tier-2 distribution network.

Its purpose is to move saline or otherwise lower-quality source water through the community or service area before final treatment.

The name “Brine Backbone” describes the original concept but does not require every implementation to transport highly concentrated brine.

The actual feed-water quality would depend on the available source and intended use.

The backbone may integrate:

- Gastropod composite pipe;
- conventional pipe materials where appropriate;
- gravity conveyance;
- conventional pumps;
- Desert Whale pneumatic pump stations;
- storage;
- pressure regulation;
- isolation;
- bypasses;
- flushing;
- monitoring;
- distributed treatment connections.

The architecture is intentionally compatible with hybrid systems.

Conventional pumps and electrical equipment may remain part of the network wherever they provide the best solution.

## Gastropod Pipe

The **Gastropod Pipe** is a proposed composite conveyance concept intended for aggressive saline-water environments.

The conceptual configuration combines:

- a vitrified clay or ceramic internal surface; and
- a ductile-iron structural exterior.

Its purpose within the larger architecture is to explore long-lived conveyance of saline Tier-2 water while separating corrosion resistance from structural capacity.

The manufacturing method, thermal compatibility, bonding, inspection requirements, pressure capacity, repair methods, and lifecycle performance remain open engineering questions.

## Water Elevation and Storage

Where geography and wave conditions permit, the Living Water System explores the use of environmental energy to elevate source water.

The **Water Elevator** concept uses wave-driven pressure oscillation to incrementally raise water.

Elevated water creates gravitational potential energy and provides storage that can be used later for:

- gravity distribution;
- hydraulic energy recovery;
- trompe operation;
- emergency reserve;
- local pressure support;
- other non-potable or treatment functions.

The architecture does not require every installation to use a wave elevator.

Existing terrain, conventional pumping, towers, tanks, reservoirs, or other elevation methods may perform the same infrastructure function.

## Trompe and Compressed-Air Utility

Elevated water can descend through a trompe-type hydraulic air-compression system.

The conceptual energy pathway is:

Water elevation → gravitational head → falling water → air entrainment → compressed air

The compressed air becomes a second infrastructure resource.

Potential uses include:

- operation of Desert Whale pump stations;
- pneumatic tools;
- mechanical drives;
- controls and actuators;
- air motors;
- electricity generation through suitable machinery;
- stored pneumatic energy;
- other community or industrial pneumatic loads.

This creates a conceptual parallel utility:

Compressed-air production → storage → distribution → useful pneumatic work

A compressed-air distribution network would require independent evaluation of moisture, leakage, pressure loss, pipe sizing, storage, safety, corrosion, energy efficiency, and end-use requirements.

## Desert Whale Pump Stations

The **Desert Whale** is a conceptual pneumatic water-displacement pump.

Compressed air acts on water contained within a chamber and displaces that water into the downstream conveyance network.

The concept is intended to provide water movement without requiring every pumping location to contain a conventional electrically driven rotating pump.

Desert Whale stations may coexist with conventional pumping stations.

The architecture does not assume that pneumatic pumping will always be more efficient or appropriate.

The design question is whether stored or naturally produced compressed air can provide useful pumping capability in locations where electrical supply, fuel supply, maintenance capacity, or conventional pumping infrastructure is limited.

## Distributed Final Treatment

Tier-2 water can be delivered near the location where final water quality is required.

A distributed treatment system may then produce potable water for local consumption.

The **Hibah** concept is one candidate distributed desalination method.

The architecture does not require Hibah to be the only treatment technology.

Other appropriate treatment systems may be connected to the Tier-2 backbone.

The important architectural distinction is the location of the final treatment step:

Centralized model:

Source → final treatment → long-distance distribution → user

Distributed model:

Source → minimal processing → Tier-2 distribution → final treatment near use → user

Hybrid systems may use both.

## Hibah Rooftop Desalination

The **Hibah** concept explores passive or low-energy distributed desalination using solar energy, gravity, shallow-flow geometry, evaporation, and condensation.

A generalized pathway is:

Tier-2 water → controlled distribution → evaporation surface → vapor → condensation → freshwater collection

Residual concentrate remains and must be managed appropriately.

Distributed desalination does not eliminate concentrate production.

Its recovery efficiency, water quality, maintenance requirements, salt accumulation, environmental effects, and lifecycle performance must be compared fairly with centralized alternatives.

## Non-Potable Uses

Tier-2 water may provide direct utility where potable quality is unnecessary and where the source water is compatible with the use.

Potential applications should be evaluated individually rather than assumed.

The broader principle is that high-quality potable water should not automatically be used where a lower water-quality class can safely and effectively perform the required function.

## Emergency and Resilience Water

The Tier-2 backbone may also provide an additional emergency-water resource.

Possible future configurations include:

- elevated non-potable storage;
- emergency gravity discharge;
- dedicated Tier-2 hydrants;
- hose connections;
- deluge connections;
- emergency water distribution;
- other locally appropriate fire-water or disaster-response uses.

This does not imply that existing fire-protection systems should simply be supplied with saline water.

Instead, the architecture allows new emergency-water systems to be designed around the characteristics of the Tier-2 resource.

A future concept for investigation is:

Tier-2 backbone → dedicated fire-water connection → hose / hydrant / deluge use

The value of such a system would depend on available flow, pressure, storage volume, reliability, materials compatibility, maintenance, and emergency-response requirements.

## Intentional Air Admission and Surge Management

The conveyance architecture also includes a hypothesis involving controlled air introduction.

Because liquid water has very little compressibility, intentional gas volumes may provide hydraulic cushioning during transient events.

Possible methods include:

- controlled air admission;
- microbubble generation;
- porous ceramic or clay air-admission elements;
- localized air chambers;
- other engineered gas cushions.

The objective is to investigate whether controlled air can reduce damaging pressure transients while avoiding excessive capacity loss, unstable two-phase flow, or air locking.

This concept remains an open engineering question and is tracked separately in the repository Issues.

## Operations and Maintainability

The system should be designed as infrastructure that must eventually be inspected, maintained, repaired, and replaced.

Important considerations include:

- intake screening;
- particulate removal;
- exclusion of aquatic organisms;
- biofouling;
- marine growth;
- sediment;
- flushing;
- cleanouts;
- isolation valves;
- bypasses;
- replaceable components;
- pressure monitoring;
- water-quality monitoring;
- air-system moisture management;
- corrosion;
- access for inspection;
- failure-state operation.

Maintainability is a design requirement rather than an activity to be added after construction.

## Asset Management

A distributed system may contain large numbers of pipes, tanks, treatment units, valves, pneumatic components, and local assets.

These assets should be managed over their full lifecycle.

A future asset-management framework may track:

- inventory;
- location;
- material;
- age;
- condition;
- performance;
- inspection history;
- maintenance history;
- failure modes;
- probability or likelihood of failure;
- consequence of failure;
- confidence in available information;
- remaining service life;
- lifecycle cost;
- renewal priority.

The architecture should therefore be capable of supporting both physical infrastructure and the information required to manage that infrastructure over decades.

## Hybrid Operation

The Living Water System should not be interpreted as requiring a binary choice between conventional and unconventional infrastructure.

A real implementation may include any combination of:

- centralized treatment;
- distributed treatment;
- conventional electric pumps;
- pneumatic pumps;
- gravity;
- elevated storage;
- wave-driven elevation;
- grid electricity;
- renewable electricity;
- compressed air;
- conventional pipe;
- Gastropod Pipe;
- centralized desalination;
- Hibah or other point-of-use systems.

The purpose is to expand the available infrastructure toolkit.

## Architecture Summary

The generalized system can be represented as:

Source water  
↓  
Minimal screening / pretreatment  
↓  
**Tier-2 Water Backbone**  
↓  
├── Appropriate non-potable use  
├── Emergency / resilience water  
├── Distributed treatment → potable water  
└── Storage / hydraulic-energy functions

A parallel energy pathway may operate as:

Environmental or conventional water elevation  
↓  
Gravitational potential energy  
↓  
Trompe  
↓  
Compressed air  
↓  
Storage / distribution  
↓  
Pneumatic pumping / tools / mechanical work / electricity generation

The conventional potable-water system remains available in parallel.

## Development Principle

The architecture is intended to be modular.

Individual components may succeed or fail independently.

Failure of one proposed technology does not automatically invalidate the entire dual-utility concept.

For example:

- the Tier-2 network does not require the Water Elevator;
- distributed treatment does not require Gastropod Pipe;
- Gastropod Pipe does not require Hibah;
- Desert Whale pumping does not eliminate conventional pumps;
- the compressed-air network does not require every endpoint to use pneumatic equipment.

Each component should therefore be evaluated on its own engineering merit as well as on its contribution to the larger system.

## Development Status

This document describes an open engineering architecture.

It is not a construction specification or a claim that the complete system has been validated.

Known questions are tracked through repository documentation and GitHub Issues.

The architecture should remain open to:

- testing;
- calculation;
- criticism;
- redesign;
- substitution of components;
- rejection of unsuccessful mechanisms;
- integration of better technologies.

The objective is not to preserve a particular mechanism.

The objective is to investigate whether a resilient second water utility can deliver useful lower-quality water closer to the point of need, reduce unnecessary use of finished potable water, enable distributed final treatment, and make productive use of locally available hydraulic and environmental energy.
