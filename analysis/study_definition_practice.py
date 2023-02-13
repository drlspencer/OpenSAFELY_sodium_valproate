from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv  # NOQA

study = StudyDefinition(
    # define default dummy data behaviour
    default_expectations={
        "date": {"earliest": "1970-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.2,
    },

    # define the study index date
    index_date="2020-01-01",

    # define the study population
    population=patients.all(),

    valproate_count=patients.with_these_medications(
    oral_steroid_med_codes,
    between=["2019-03-01", "2020-02-29"],
    ignore_days_where_these_clinical_codes_occur=copd_reviews,
    returning="number_of_episodes",
    episode_defined_as="series of events each <= 28 days apart",
    return_expectations={
        "int": {"distribution": "normal", "mean": 2, "stddev": 1},
        "incidence": 0.2,
    },
)

    # define the study variables
    age=patients.age_as_of("index_date")

    sex=patients.sex(
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"M": 0.49, "F": 0.51}},
        }
    ),
)