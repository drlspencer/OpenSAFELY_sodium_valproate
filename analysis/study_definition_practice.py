from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv  # NOQA

teratogenic_drug_codes = codelist_from_csv(
    "codelists/opensafely-teratogenic-medicines.csv", system="ctv3", column="CTV3ID"
)

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
    teratogenic_drug_codes,
    between=["2019-03-01", "2020-02-29"],
    ignore_days_where_these_clinical_codes_occur=copd_reviews,
    returning="number_of_episodes",
    episode_defined_as="series of events each <= 28 days apart",
    return_expectations={
        "int": {"distribution": "normal", "mean": 2, "stddev": 1},
        "incidence": 0.2,
    },


    example=with_these_medications(
        teratogenic_drug_codes, 
        return_expectations={
            "int": {"distribution": "normal", "mean": 2, "stddev": 1},
            "incidence": 0.2,
        },
        on_or_before=None, 
        on_or_after=None, 
        between=None, 
        find_first_match_in_period=None, 
        find_last_match_in_period=None, 
        returning='binary_flag', 
        include_date_of_match=False, 
        date_format=None, 
        ignore_days_where_these_clinical_codes_occur=None, 
        episode_defined_as=None, 
        return_binary_flag=None, 
        return_number_of_matches_in_period=False, 
        return_first_date_in_period=False, 
        return_last_date_in_period=False, 
        include_month=False, 
        include_day=False)

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