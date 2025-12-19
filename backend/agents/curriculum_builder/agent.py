def run(roadmap_data):
    roadmap = roadmap_data["roadmap"]

    units = []
    unit_id = 1

    for phase in roadmap:
        prev_unit_id = None

        for concept in phase["concepts"]:
            unit = {
                "unit_id": unit_id,
                "phase": phase["phase"],
                "title": concept,
                "depends_on": prev_unit_id
            }

            units.append(unit)
            prev_unit_id = unit_id
            unit_id += 1

    return {
        "current_unit": units[0],
        "all_units": units
    }
